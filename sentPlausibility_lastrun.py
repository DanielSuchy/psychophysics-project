#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on prosinec 01, 2021, at 12:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'sentPlausibility'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\materialy\\psychophysics\\psychophysics-project\\sentPlausibility_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr = visual.ImageStim(
    win=win,
    name='instr', 
    image='instuctions.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
confirm = keyboard.Keyboard()

# Initialize components for Routine "native"
nativeClock = core.Clock()
isNative = visual.TextStim(win=win, name='isNative',
    text="Do you consider yourself to be a native speaker of English? \n\nPress 'y' for yes, 'n' for no.",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
isNativeResp = keyboard.Keyboard()

# Initialize components for Routine "readProb"
readProbClock = core.Clock()
hasReadProb = visual.TextStim(win=win, name='hasReadProb',
    text="Do you experience any problems with reading?\n\nPress 'y' for yes, 'n' for no.",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
hasReadProbResp = keyboard.Keyboard()

# Initialize components for Routine "practiceInfo"
practiceInfoClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Now you will be presented with a practice trial.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice1"
practice1Clock = core.Clock()
practice1Cross = visual.TextStim(win=win, name='practice1Cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice1Text = visual.TextStim(win=win, name='practice1Text',
    text='The driver crashed the car.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice1Resp = keyboard.Keyboard()
message1 = "empty message"
message2 = "empty message"

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()
feedback1Text = visual.TextStim(win=win, name='feedback1Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedback1Blank = visual.TextStim(win=win, name='feedback1Blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice2"
practice2Clock = core.Clock()
practice2Cross = visual.TextStim(win=win, name='practice2Cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice2Text = visual.TextStim(win=win, name='practice2Text',
    text='The car drives the airplane.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice2Resp = keyboard.Keyboard()

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()
feedback2Text = visual.TextStim(win=win, name='feedback2Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedback2Blank = visual.TextStim(win=win, name='feedback2Blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "showSentence"
showSentenceClock = core.Clock()
sentence = visual.TextStim(win=win, name='sentence',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fixationCross = visual.TextStim(win=win, name='fixationCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sentenceResp = keyboard.Keyboard()

# Initialize components for Routine "debrief"
debriefClock = core.Clock()
debriefText = visual.TextStim(win=win, name='debriefText',
    text='The experiment is over now. It will close in a few seconds.\n\nThanks for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
confirm.keys = []
confirm.rt = []
_confirm_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr, confirm]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
    # *confirm* updates
    waitOnFlip = False
    if confirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confirm.frameNStart = frameN  # exact frame index
        confirm.tStart = t  # local t and not account for scr refresh
        confirm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confirm, 'tStartRefresh')  # time at next scr refresh
        confirm.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(confirm.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(confirm.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if confirm.status == STARTED and not waitOnFlip:
        theseKeys = confirm.getKeys(keyList=['y'], waitRelease=False)
        _confirm_allKeys.extend(theseKeys)
        if len(_confirm_allKeys):
            confirm.keys = _confirm_allKeys[-1].name  # just the last key pressed
            confirm.rt = _confirm_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# check responses
if confirm.keys in ['', [], None]:  # No response was made
    confirm.keys = None
thisExp.addData('confirm.keys',confirm.keys)
if confirm.keys != None:  # we had a response
    thisExp.addData('confirm.rt', confirm.rt)
thisExp.addData('confirm.started', confirm.tStartRefresh)
thisExp.addData('confirm.stopped', confirm.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "native"-------
continueRoutine = True
# update component parameters for each repeat
isNativeResp.keys = []
isNativeResp.rt = []
_isNativeResp_allKeys = []
# keep track of which components have finished
nativeComponents = [isNative, isNativeResp]
for thisComponent in nativeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nativeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "native"-------
while continueRoutine:
    # get current time
    t = nativeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nativeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *isNative* updates
    if isNative.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isNative.frameNStart = frameN  # exact frame index
        isNative.tStart = t  # local t and not account for scr refresh
        isNative.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isNative, 'tStartRefresh')  # time at next scr refresh
        isNative.setAutoDraw(True)
    
    # *isNativeResp* updates
    waitOnFlip = False
    if isNativeResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isNativeResp.frameNStart = frameN  # exact frame index
        isNativeResp.tStart = t  # local t and not account for scr refresh
        isNativeResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isNativeResp, 'tStartRefresh')  # time at next scr refresh
        isNativeResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(isNativeResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(isNativeResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if isNativeResp.status == STARTED and not waitOnFlip:
        theseKeys = isNativeResp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _isNativeResp_allKeys.extend(theseKeys)
        if len(_isNativeResp_allKeys):
            isNativeResp.keys = _isNativeResp_allKeys[-1].name  # just the last key pressed
            isNativeResp.rt = _isNativeResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nativeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "native"-------
for thisComponent in nativeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('isNative.started', isNative.tStartRefresh)
thisExp.addData('isNative.stopped', isNative.tStopRefresh)
# check responses
if isNativeResp.keys in ['', [], None]:  # No response was made
    isNativeResp.keys = None
thisExp.addData('isNativeResp.keys',isNativeResp.keys)
if isNativeResp.keys != None:  # we had a response
    thisExp.addData('isNativeResp.rt', isNativeResp.rt)
thisExp.addData('isNativeResp.started', isNativeResp.tStartRefresh)
thisExp.addData('isNativeResp.stopped', isNativeResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "native" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "readProb"-------
continueRoutine = True
# update component parameters for each repeat
hasReadProbResp.keys = []
hasReadProbResp.rt = []
_hasReadProbResp_allKeys = []
# keep track of which components have finished
readProbComponents = [hasReadProb, hasReadProbResp]
for thisComponent in readProbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
readProbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "readProb"-------
while continueRoutine:
    # get current time
    t = readProbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=readProbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hasReadProb* updates
    if hasReadProb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hasReadProb.frameNStart = frameN  # exact frame index
        hasReadProb.tStart = t  # local t and not account for scr refresh
        hasReadProb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hasReadProb, 'tStartRefresh')  # time at next scr refresh
        hasReadProb.setAutoDraw(True)
    
    # *hasReadProbResp* updates
    waitOnFlip = False
    if hasReadProbResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hasReadProbResp.frameNStart = frameN  # exact frame index
        hasReadProbResp.tStart = t  # local t and not account for scr refresh
        hasReadProbResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hasReadProbResp, 'tStartRefresh')  # time at next scr refresh
        hasReadProbResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(hasReadProbResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(hasReadProbResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if hasReadProbResp.status == STARTED and not waitOnFlip:
        theseKeys = hasReadProbResp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _hasReadProbResp_allKeys.extend(theseKeys)
        if len(_hasReadProbResp_allKeys):
            hasReadProbResp.keys = _hasReadProbResp_allKeys[-1].name  # just the last key pressed
            hasReadProbResp.rt = _hasReadProbResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readProbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "readProb"-------
for thisComponent in readProbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hasReadProb.started', hasReadProb.tStartRefresh)
thisExp.addData('hasReadProb.stopped', hasReadProb.tStopRefresh)
# check responses
if hasReadProbResp.keys in ['', [], None]:  # No response was made
    hasReadProbResp.keys = None
thisExp.addData('hasReadProbResp.keys',hasReadProbResp.keys)
if hasReadProbResp.keys != None:  # we had a response
    thisExp.addData('hasReadProbResp.rt', hasReadProbResp.rt)
thisExp.addData('hasReadProbResp.started', hasReadProbResp.tStartRefresh)
thisExp.addData('hasReadProbResp.stopped', hasReadProbResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "readProb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceInfo"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
# keep track of which components have finished
practiceInfoComponents = [text, text_2]
for thisComponent in practiceInfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceInfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceInfo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practiceInfoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceInfoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceInfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceInfo"-------
for thisComponent in practiceInfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "practice1"-------
continueRoutine = True
routineTimer.add(11.000000)
# update component parameters for each repeat
practice1Resp.keys = []
practice1Resp.rt = []
_practice1Resp_allKeys = []
# keep track of which components have finished
practice1Components = [practice1Cross, practice1Text, practice1Resp]
for thisComponent in practice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice1Cross* updates
    if practice1Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice1Cross.frameNStart = frameN  # exact frame index
        practice1Cross.tStart = t  # local t and not account for scr refresh
        practice1Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1Cross, 'tStartRefresh')  # time at next scr refresh
        practice1Cross.setAutoDraw(True)
    if practice1Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice1Cross.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            practice1Cross.tStop = t  # not accounting for scr refresh
            practice1Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice1Cross, 'tStopRefresh')  # time at next scr refresh
            practice1Cross.setAutoDraw(False)
    
    # *practice1Text* updates
    if practice1Text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        practice1Text.frameNStart = frameN  # exact frame index
        practice1Text.tStart = t  # local t and not account for scr refresh
        practice1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1Text, 'tStartRefresh')  # time at next scr refresh
        practice1Text.setAutoDraw(True)
    if practice1Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice1Text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            practice1Text.tStop = t  # not accounting for scr refresh
            practice1Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice1Text, 'tStopRefresh')  # time at next scr refresh
            practice1Text.setAutoDraw(False)
    
    # *practice1Resp* updates
    waitOnFlip = False
    if practice1Resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        practice1Resp.frameNStart = frameN  # exact frame index
        practice1Resp.tStart = t  # local t and not account for scr refresh
        practice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1Resp, 'tStartRefresh')  # time at next scr refresh
        practice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice1Resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice1Resp.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            practice1Resp.tStop = t  # not accounting for scr refresh
            practice1Resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice1Resp, 'tStopRefresh')  # time at next scr refresh
            practice1Resp.status = FINISHED
    if practice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = practice1Resp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _practice1Resp_allKeys.extend(theseKeys)
        if len(_practice1Resp_allKeys):
            practice1Resp.keys = _practice1Resp_allKeys[-1].name  # just the last key pressed
            practice1Resp.rt = _practice1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice1"-------
for thisComponent in practice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice1Cross.started', practice1Cross.tStartRefresh)
thisExp.addData('practice1Cross.stopped', practice1Cross.tStopRefresh)
thisExp.addData('practice1Text.started', practice1Text.tStartRefresh)
thisExp.addData('practice1Text.stopped', practice1Text.tStopRefresh)
# check responses
if practice1Resp.keys in ['', [], None]:  # No response was made
    practice1Resp.keys = None
thisExp.addData('practice1Resp.keys',practice1Resp.keys)
if practice1Resp.keys != None:  # we had a response
    thisExp.addData('practice1Resp.rt', practice1Resp.rt)
thisExp.addData('practice1Resp.started', practice1Resp.tStartRefresh)
thisExp.addData('practice1Resp.stopped', practice1Resp.tStopRefresh)
thisExp.nextEntry()
if practice1Resp.keys == 'y':
    message1 = "Your response was: 'yes'. Now let's try one more round."
else:
    message1 = "Your answer was incorrect. Please talk to Dan about the instructions."

# ------Prepare to start Routine "feedback1"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
feedback1Text.setText(message1)
# keep track of which components have finished
feedback1Components = [feedback1Text, feedback1Blank]
for thisComponent in feedback1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedback1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedback1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedback1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback1Text* updates
    if feedback1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback1Text.frameNStart = frameN  # exact frame index
        feedback1Text.tStart = t  # local t and not account for scr refresh
        feedback1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback1Text, 'tStartRefresh')  # time at next scr refresh
        feedback1Text.setAutoDraw(True)
    if feedback1Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback1Text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback1Text.tStop = t  # not accounting for scr refresh
            feedback1Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedback1Text, 'tStopRefresh')  # time at next scr refresh
            feedback1Text.setAutoDraw(False)
    
    # *feedback1Blank* updates
    if feedback1Blank.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        feedback1Blank.frameNStart = frameN  # exact frame index
        feedback1Blank.tStart = t  # local t and not account for scr refresh
        feedback1Blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback1Blank, 'tStartRefresh')  # time at next scr refresh
        feedback1Blank.setAutoDraw(True)
    if feedback1Blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback1Blank.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            feedback1Blank.tStop = t  # not accounting for scr refresh
            feedback1Blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedback1Blank, 'tStopRefresh')  # time at next scr refresh
            feedback1Blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback1"-------
for thisComponent in feedback1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('feedback1Text.started', feedback1Text.tStartRefresh)
thisExp.addData('feedback1Text.stopped', feedback1Text.tStopRefresh)
thisExp.addData('feedback1Blank.started', feedback1Blank.tStartRefresh)
thisExp.addData('feedback1Blank.stopped', feedback1Blank.tStopRefresh)

# ------Prepare to start Routine "practice2"-------
continueRoutine = True
routineTimer.add(11.000000)
# update component parameters for each repeat
practice2Resp.keys = []
practice2Resp.rt = []
_practice2Resp_allKeys = []
# keep track of which components have finished
practice2Components = [practice2Cross, practice2Text, practice2Resp]
for thisComponent in practice2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice2Cross* updates
    if practice2Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice2Cross.frameNStart = frameN  # exact frame index
        practice2Cross.tStart = t  # local t and not account for scr refresh
        practice2Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice2Cross, 'tStartRefresh')  # time at next scr refresh
        practice2Cross.setAutoDraw(True)
    if practice2Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice2Cross.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            practice2Cross.tStop = t  # not accounting for scr refresh
            practice2Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice2Cross, 'tStopRefresh')  # time at next scr refresh
            practice2Cross.setAutoDraw(False)
    
    # *practice2Text* updates
    if practice2Text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        practice2Text.frameNStart = frameN  # exact frame index
        practice2Text.tStart = t  # local t and not account for scr refresh
        practice2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice2Text, 'tStartRefresh')  # time at next scr refresh
        practice2Text.setAutoDraw(True)
    if practice2Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice2Text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            practice2Text.tStop = t  # not accounting for scr refresh
            practice2Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice2Text, 'tStopRefresh')  # time at next scr refresh
            practice2Text.setAutoDraw(False)
    
    # *practice2Resp* updates
    waitOnFlip = False
    if practice2Resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        practice2Resp.frameNStart = frameN  # exact frame index
        practice2Resp.tStart = t  # local t and not account for scr refresh
        practice2Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice2Resp, 'tStartRefresh')  # time at next scr refresh
        practice2Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice2Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice2Resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice2Resp.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            practice2Resp.tStop = t  # not accounting for scr refresh
            practice2Resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice2Resp, 'tStopRefresh')  # time at next scr refresh
            practice2Resp.status = FINISHED
    if practice2Resp.status == STARTED and not waitOnFlip:
        theseKeys = practice2Resp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _practice2Resp_allKeys.extend(theseKeys)
        if len(_practice2Resp_allKeys):
            practice2Resp.keys = _practice2Resp_allKeys[-1].name  # just the last key pressed
            practice2Resp.rt = _practice2Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice2"-------
for thisComponent in practice2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice2Cross.started', practice2Cross.tStartRefresh)
thisExp.addData('practice2Cross.stopped', practice2Cross.tStopRefresh)
thisExp.addData('practice2Text.started', practice2Text.tStartRefresh)
thisExp.addData('practice2Text.stopped', practice2Text.tStopRefresh)
# check responses
if practice2Resp.keys in ['', [], None]:  # No response was made
    practice2Resp.keys = None
thisExp.addData('practice2Resp.keys',practice2Resp.keys)
if practice2Resp.keys != None:  # we had a response
    thisExp.addData('practice2Resp.rt', practice2Resp.rt)
thisExp.addData('practice2Resp.started', practice2Resp.tStartRefresh)
thisExp.addData('practice2Resp.stopped', practice2Resp.tStopRefresh)
thisExp.nextEntry()
if practice2Resp.keys == 'n':
    message2 = "Your response was: 'no', which is correct. The experiment will begin now."
else:
    message2 = "Your answer was incorrect. Please talk to Dan about the instructions."

# ------Prepare to start Routine "feedback2"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
feedback2Text.setText(message2)
# keep track of which components have finished
feedback2Components = [feedback2Text, feedback2Blank]
for thisComponent in feedback2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedback2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedback2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedback2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback2Text* updates
    if feedback2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback2Text.frameNStart = frameN  # exact frame index
        feedback2Text.tStart = t  # local t and not account for scr refresh
        feedback2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback2Text, 'tStartRefresh')  # time at next scr refresh
        feedback2Text.setAutoDraw(True)
    if feedback2Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback2Text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback2Text.tStop = t  # not accounting for scr refresh
            feedback2Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedback2Text, 'tStopRefresh')  # time at next scr refresh
            feedback2Text.setAutoDraw(False)
    
    # *feedback2Blank* updates
    if feedback2Blank.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        feedback2Blank.frameNStart = frameN  # exact frame index
        feedback2Blank.tStart = t  # local t and not account for scr refresh
        feedback2Blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback2Blank, 'tStartRefresh')  # time at next scr refresh
        feedback2Blank.setAutoDraw(True)
    if feedback2Blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback2Blank.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            feedback2Blank.tStop = t  # not accounting for scr refresh
            feedback2Blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedback2Blank, 'tStopRefresh')  # time at next scr refresh
            feedback2Blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback2"-------
for thisComponent in feedback2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('feedback2Text.started', feedback2Text.tStartRefresh)
thisExp.addData('feedback2Text.stopped', feedback2Text.tStopRefresh)
thisExp.addData('feedback2Blank.started', feedback2Blank.tStartRefresh)
thisExp.addData('feedback2Blank.stopped', feedback2Blank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
sentenceLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliFiltered.xlsx'),
    seed=None, name='sentenceLoop')
thisExp.addLoop(sentenceLoop)  # add the loop to the experiment
thisSentenceLoop = sentenceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSentenceLoop.rgb)
if thisSentenceLoop != None:
    for paramName in thisSentenceLoop:
        exec('{} = thisSentenceLoop[paramName]'.format(paramName))

for thisSentenceLoop in sentenceLoop:
    currentLoop = sentenceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSentenceLoop.rgb)
    if thisSentenceLoop != None:
        for paramName in thisSentenceLoop:
            exec('{} = thisSentenceLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "showSentence"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    sentence.setText(sentenceContent)
    sentenceResp.keys = []
    sentenceResp.rt = []
    _sentenceResp_allKeys = []
    # keep track of which components have finished
    showSentenceComponents = [sentence, fixationCross, sentenceResp]
    for thisComponent in showSentenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    showSentenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "showSentence"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = showSentenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=showSentenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentence* updates
        if sentence.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sentence.frameNStart = frameN  # exact frame index
            sentence.tStart = t  # local t and not account for scr refresh
            sentence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentence, 'tStartRefresh')  # time at next scr refresh
            sentence.setAutoDraw(True)
        if sentence.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sentence.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                sentence.tStop = t  # not accounting for scr refresh
                sentence.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sentence, 'tStopRefresh')  # time at next scr refresh
                sentence.setAutoDraw(False)
        
        # *fixationCross* updates
        if fixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationCross.frameNStart = frameN  # exact frame index
            fixationCross.tStart = t  # local t and not account for scr refresh
            fixationCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationCross, 'tStartRefresh')  # time at next scr refresh
            fixationCross.setAutoDraw(True)
        if fixationCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationCross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationCross.tStop = t  # not accounting for scr refresh
                fixationCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationCross, 'tStopRefresh')  # time at next scr refresh
                fixationCross.setAutoDraw(False)
        
        # *sentenceResp* updates
        waitOnFlip = False
        if sentenceResp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sentenceResp.frameNStart = frameN  # exact frame index
            sentenceResp.tStart = t  # local t and not account for scr refresh
            sentenceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentenceResp, 'tStartRefresh')  # time at next scr refresh
            sentenceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sentenceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sentenceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sentenceResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sentenceResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                sentenceResp.tStop = t  # not accounting for scr refresh
                sentenceResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sentenceResp, 'tStopRefresh')  # time at next scr refresh
                sentenceResp.status = FINISHED
        if sentenceResp.status == STARTED and not waitOnFlip:
            theseKeys = sentenceResp.getKeys(keyList=['y', 'n'], waitRelease=False)
            _sentenceResp_allKeys.extend(theseKeys)
            if len(_sentenceResp_allKeys):
                sentenceResp.keys = _sentenceResp_allKeys[-1].name  # just the last key pressed
                sentenceResp.rt = _sentenceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in showSentenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "showSentence"-------
    for thisComponent in showSentenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sentenceLoop.addData('sentence.started', sentence.tStartRefresh)
    sentenceLoop.addData('sentence.stopped', sentence.tStopRefresh)
    sentenceLoop.addData('fixationCross.started', fixationCross.tStartRefresh)
    sentenceLoop.addData('fixationCross.stopped', fixationCross.tStopRefresh)
    # check responses
    if sentenceResp.keys in ['', [], None]:  # No response was made
        sentenceResp.keys = None
    sentenceLoop.addData('sentenceResp.keys',sentenceResp.keys)
    if sentenceResp.keys != None:  # we had a response
        sentenceLoop.addData('sentenceResp.rt', sentenceResp.rt)
    sentenceLoop.addData('sentenceResp.started', sentenceResp.tStartRefresh)
    sentenceLoop.addData('sentenceResp.stopped', sentenceResp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'sentenceLoop'


# ------Prepare to start Routine "debrief"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
debriefComponents = [debriefText]
for thisComponent in debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debriefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = debriefClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debriefClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefText* updates
    if debriefText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefText.frameNStart = frameN  # exact frame index
        debriefText.tStart = t  # local t and not account for scr refresh
        debriefText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefText, 'tStartRefresh')  # time at next scr refresh
        debriefText.setAutoDraw(True)
    if debriefText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > debriefText.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            debriefText.tStop = t  # not accounting for scr refresh
            debriefText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(debriefText, 'tStopRefresh')  # time at next scr refresh
            debriefText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief"-------
for thisComponent in debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debriefText.started', debriefText.tStartRefresh)
thisExp.addData('debriefText.stopped', debriefText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
