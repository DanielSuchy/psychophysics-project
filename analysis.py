import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from statistics import mean
from statsmodels.stats.anova import AnovaRM
from scipy.stats import ttest_ind
from scipy.stats import norm

dataPath = "data/"
csvFiles = [dataPath + file for file in listdir(dataPath) if ".csv" in file]

#apply read_csv to every file and concatenate their contents
allData = pd.concat(map(pd.read_csv, csvFiles)) 

#select rows that say if a particiapnt is native
nativeInfo = allData[allData["isNativeResp.keys"].isnull() == False]
nativeInfo = nativeInfo["isNativeResp.keys"] # -> 3 non-native and 2 native speakers

#select responses to experiment trials
responses = allData[allData["sentenceID"].isnull() == False]
# -> I have acquired 320 responses, 64 per participant

#select only relevant columns
responses = responses[["sentenceID", "isConcordant", "isPlausible", "sentenceType", "sentenceContent", "participant", "sentenceResp.keys", "sentenceResp.rt"]]
#rename auto-generated columns
responses = responses.rename(columns={"sentenceResp.keys": "response", "sentenceResp.rt": "reactionTime"})

#put native info into every judgement
# participants 1,2,3 non-native, others native
#add boolean value to the column "native" based on participant ID
responses["native"] = None
responses.loc[responses["participant"] <= 3, "native"] = False
responses.loc[responses["participant"] > 3, "native"] = True

#get timeout responses
timeouts = responses[responses["response"] == "None"]
#there are 10 sentences that led to timeout
#all by a single participant
#7 intransitive 3 transitive
# not associated with any specific verb

#delete timeout responses
responses = responses[responses["response"] != "None"]

# get response types by plausibility
correct = responses[(responses["response"] == "y") & (responses["isPlausible"] == True) | (responses["response"] == "n") & (responses["isPlausible"] == False )] #244
incorrect = responses[(responses["response"] == "y") & (responses["isPlausible"] == False) | (responses["response"] == "n") & (responses["isPlausible"] == True )] #66
correctPlausible = responses[(responses["response"] == "y") & (responses["isPlausible"] == True)] #135
correctInplausible = responses[(responses["response"] == "n") & (responses["isPlausible"] == False)] #109
incorrectPlausible = responses[(responses["response"] == "n") & (responses["isPlausible"] == True)] #19
incorrectInplausible = responses[(responses["response"] == "y") & (responses["isPlausible"] == False)] #47

# reaction times by plausibility
print("Correct mean RT:", mean(correct["reactionTime"]))
print("Incorrect mean RT:", mean(incorrect["reactionTime"]))
print("Correct plausible mean RT:", mean(correctPlausible["reactionTime"]))
print("Correct inplausible mean RT:", mean(correctInplausible["reactionTime"]))
print("Incorrect plausible mean RT:", mean(incorrectPlausible["reactionTime"]))
print("Incorrect inplausible mean RT:", mean(incorrectInplausible["reactionTime"]))

print("Correct:Incorrect t-test:", ttest_ind(correct["reactionTime"], incorrect["reactionTime"]))

fig, ax = plt.subplots()
box = ax.boxplot([correctPlausible["reactionTime"], correctInplausible["reactionTime"], incorrectPlausible["reactionTime"], incorrectInplausible["reactionTime"]])
ax.set_ylabel("RT (s)")
ax.set_xticklabels(["CorrPlau", "CorrInplau", "IncorrPlau", "IncorrInplau"])
plt.show()


# get response types by verb bias
matchingBias = responses[responses["isConcordant"] == True] #156 (after removed timeouts)
mismatchingBias = responses[responses["isConcordant"] == False] #154 (after removed timeouts)

correctMatchingBias = matchingBias[(matchingBias["response"] == "y") & (matchingBias["isPlausible"] == True) | (matchingBias["response"]  == "n") & (matchingBias["isPlausible"] == False )] #131
incorrectMatchingBias = matchingBias[(matchingBias["response"] == "n") & (matchingBias["isPlausible"] == True) | (matchingBias["response"]  == "y") & (matchingBias["isPlausible"] == False )] #25
correctMismatchingBias = mismatchingBias[(mismatchingBias["response"] == "y") & (mismatchingBias["isPlausible"] == True) | (mismatchingBias["response"]  == "n") & (mismatchingBias["isPlausible"] == False )] #113
incorrectMismatchingBias = mismatchingBias[(mismatchingBias["response"] == "n") & (mismatchingBias["isPlausible"] == True) | (mismatchingBias["response"]  == "y") & (mismatchingBias["isPlausible"] == False )] #41

#reaction times by verb bias
print("Matching bias mean RT:", mean(matchingBias["reactionTime"]))
print("Mismatching bias mean RT:", mean(mismatchingBias["reactionTime"]))

print("Correct Matching bias mean RT:", mean(correctMatchingBias["reactionTime"]))
print("Incorrect Matching bias mean RT:", mean(incorrectMatchingBias["reactionTime"]))
print("Correct Mismatching bias mean RT:", mean(correctMismatchingBias["reactionTime"]))
print("Incorrect Mismatching bias mean RT:", mean(incorrectMismatchingBias["reactionTime"]))

print("Matching:mismatching t-test:", ttest_ind(matchingBias["reactionTime"], mismatchingBias["reactionTime"]))

fig, ax = plt.subplots()
box = ax.boxplot([correctMatchingBias["reactionTime"], incorrectMatchingBias["reactionTime"], correctMismatchingBias["reactionTime"], incorrectMismatchingBias["reactionTime"]])
ax.set_ylabel("RT (s)")
ax.set_xticklabels(["CorrMatch", "IncorrMatch", "CorrMismatch", "IncorrMismatch"])
plt.show()

#ANOVA on RTs
independentVariables = ["participant", "isConcordant", "isPlausible"]
meanRTs = responses.groupby(by=independentVariables)["reactionTime"].mean().reset_index()
model = AnovaRM(data = meanRTs, depvar = "reactionTime",
subject = "participant", within = ["isConcordant", "isPlausible"]).fit()
print(model)

#add isCorrectColumn to responses
def getResponseType(isPlausible, response):
    if (isPlausible == True and response == "y"):
        return "hit"
    elif (isPlausible == True and response == "n"):
        return "falseAlarm"
    elif (isPlausible == False and response == "n"):
        return "correctRejection"
    elif (isPlausible == False and response == "y"):
        return "miss"
    else:
        return None

responses['responseType'] = responses.apply(lambda x: getResponseType(x['isPlausible'], x['response']), axis=1)

# SDT by verb bias
accuracy = pd.DataFrame({"matchesBias" : [True, False],
"hits" : [0,0], "misses" : [0,0], "CRs" : [0,0], "FAs" :
[0,0]})
    
for index, row in responses.iterrows():
    if row["isConcordant"] == True:
        rowInd = 0
        if row["responseType"] == "hit":
            accuracy.loc[rowInd,"hits"] += 1   
        elif row["responseType"] == "falseAlarm":
            accuracy.loc[rowInd,"FAs"] += 1   
        elif row["responseType"] == "miss":
            accuracy.loc[rowInd,"misses"] += 1
        elif row["responseType"] == "correctRejection":
            accuracy.loc[rowInd,"CRs"] += 1        
    else:
        rowInd = 1
        if row["responseType"] == "hit":
            accuracy.loc[rowInd,"hits"] += 1   
        elif row["responseType"] == "falseAlarm":
            accuracy.loc[rowInd,"FAs"] += 1   
        elif row["responseType"] == "miss":
            accuracy.loc[rowInd,"misses"] += 1
        elif row["responseType"] == "correctRejection":
            accuracy.loc[rowInd,"CRs"] += 1 
            
#d' function
def dPrime(hitRate, FArate):
    stat = norm.ppf(hitRate) - norm.ppf(FArate)
    return stat
#criterion function
def criterion(hitRate, FArate):
    stat = -.5*(norm.ppf(hitRate) + norm.ppf(FArate))
    return stat

hitRateMatchesBias = accuracy.loc[0,"hits"]/88
FArateMatchesBias = accuracy.loc[0,"FAs"]/88
hitRateMismatchesBias = accuracy.loc[1,"hits"]/94
FArateMismatchesBias = accuracy.loc[1,"FAs"]/94

print("dPrime matches bias:", dPrime(hitRateMatchesBias, FArateMatchesBias))
print("dPrime mismatches bias:", dPrime(hitRateMismatchesBias, FArateMismatchesBias))

print("criterion matches bias:", criterion(hitRateMatchesBias, FArateMatchesBias))
print("criterion mismatches bias:", criterion(hitRateMismatchesBias, FArateMismatchesBias))

#SDT by sentenceType
accuracySentenceType = pd.DataFrame({"sentenceType" : ["transitive", "intransitive"],
"hits" : [0,0], "misses" : [0,0], "CRs" : [0,0], "FAs" :
[0,0]})
    
for index, row in responses.iterrows():
    if row["sentenceType"] == "transitive":
        rowInd = 0
        if row["responseType"] == "hit":
            accuracySentenceType.loc[rowInd,"hits"] += 1   
        elif row["responseType"] == "falseAlarm":
            accuracySentenceType.loc[rowInd,"FAs"] += 1   
        elif row["responseType"] == "miss":
            accuracySentenceType.loc[rowInd,"misses"] += 1
        elif row["responseType"] == "correctRejection":
            accuracySentenceType.loc[rowInd,"CRs"] += 1        
    else:
        rowInd = 1
        if row["responseType"] == "hit":
            accuracySentenceType.loc[rowInd,"hits"] += 1   
        elif row["responseType"] == "falseAlarm":
            accuracySentenceType.loc[rowInd,"FAs"] += 1   
        elif row["responseType"] == "miss":
            accuracySentenceType.loc[rowInd,"misses"] += 1
        elif row["responseType"] == "correctRejection":
            accuracySentenceType.loc[rowInd,"CRs"] += 1 
            
hitRateTransitive = accuracy.loc[0,"hits"]/86
FArateTransitive = accuracy.loc[0,"FAs"]/86
hitRateIntransitive = accuracy.loc[1,"hits"]/76
FArateIntransitive = accuracy.loc[1,"FAs"]/76

print("dPrime transitive:", dPrime(hitRateTransitive, FArateTransitive))
print("dPrime intransitive:", dPrime(hitRateIntransitive, FArateIntransitive))

print("criterion transitive:", criterion(hitRateTransitive, FArateTransitive))
print("criterion intransitive:", criterion(hitRateIntransitive, FArateIntransitive ))