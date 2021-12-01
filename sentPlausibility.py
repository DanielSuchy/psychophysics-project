#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on listopad 23, 2021, at 08:58
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
    originPath='F:\\materialy\\psychophysics\\psychophysics-project\\sentPlausibility.py',
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
practiceCross = visual.TextStim(win=win, name='practiceCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='The driver crashed the car.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyResp1 = keyboard.Keyboard()
message1 = "empty message"

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()
feedback1Text = visual.TextStim(win=win, name='feedback1Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
key_resp = keyboard.Keyboard()

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
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
practice1Components = [practiceCross, text_3, keyResp1]
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
    
    # *practiceCross* updates
    if practiceCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceCross.frameNStart = frameN  # exact frame index
        practiceCross.tStart = t  # local t and not account for scr refresh
        practiceCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceCross, 'tStartRefresh')  # time at next scr refresh
        practiceCross.setAutoDraw(True)
    if practiceCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practiceCross.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            practiceCross.tStop = t  # not accounting for scr refresh
            practiceCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practiceCross, 'tStopRefresh')  # time at next scr refresh
            practiceCross.setAutoDraw(False)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyResp1.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            keyResp1.tStop = t  # not accounting for scr refresh
            keyResp1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(keyResp1, 'tStopRefresh')  # time at next scr refresh
            keyResp1.status = FINISHED
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['y', 'n'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
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
thisExp.addData('practiceCross.started', practiceCross.tStartRefresh)
thisExp.addData('practiceCross.stopped', practiceCross.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
if keyResp1.keys == 'y':
    message1 = 'You response was: yes. Now let\'s try one more round.'
else:
    message1 = 'You answer was incorrect. Please talk to Dan about the instructions.'

# ------Prepare to start Routine "feedback1"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
feedback1Text.setText(message1)
# keep track of which components have finished
feedback1Components = [feedback1Text]
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

# set up handler to look after randomisation of conditions etc
sentenceLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli.xlsx'),
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
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    showSentenceComponents = [sentence, fixationCross, key_resp]
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
            if tThisFlipGlobal > sentence.tStartRefresh + 2-frameTolerance:
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
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
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
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    sentenceLoop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        sentenceLoop.addData('key_resp.rt', key_resp.rt)
    sentenceLoop.addData('key_resp.started', key_resp.tStartRefresh)
    sentenceLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'sentenceLoop'


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
