#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Sat Sep 10 15:26:15 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound
from psychopy import gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from start_code
from psychopy.hardware import keyboard
from psychopy import core


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'SID_fMRI'  # from the Builder filename that created this script
expInfo = {
    'participant ID': '',
    'condition (A/NA)':'',
    'run (1/2)': '',
    'start target duration (s)': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant ID'], expInfo['condition (A/NA)'], expInfo['run (1/2)'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/uscpsyc/Downloads/SID fMRI FINAL/SID_fMRI.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')
defaultKeyboard.keys = []
defaultKeyboard.rt = []
_default_kb_allKeys = []

# --- Initialize components for Routine "Instructions" ---
welcome = visual.TextStim(win=win, name='welcome',
    text='The experiment will begin shortly.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from start_code
response = ['']
mri_trigger = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
ITI_txt = visual.TextStim(win=win, name='ITI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from ITI_start
k = 0

# --- Initialize components for Routine "cue" ---
cueimage = visual.ImageStim(
    win=win,
    name='cueimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ant" ---
ant_cross = visual.TextStim(win=win, name='ant_cross',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "target" ---
squaretarget = visual.ImageStim(
    win=win,
    name='squaretarget', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
targ_key = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback" ---
fb_img = visual.ImageStim(
    win=win,
    name='fb_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "end_round" ---
text = visual.TextStim(win=win, name='text',
    text='END OF ROUND\n\nPLEASE WAIT FOR EXPERIMENTER',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 


# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from start_code
l = 0
trigger_time = []
mri_trigger.rt = []
_mri_trigger_allKeys = []
# keep track of which components have finished
InstructionsComponents = [welcome, mri_trigger]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome.started')
        welcome.setAutoDraw(True)
    
    # *mri_trigger* updates
    waitOnFlip = False
    if mri_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mri_trigger.frameNStart = frameN  # exact frame index
        mri_trigger.tStart = t  # local t and not account for scr refresh
        mri_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mri_trigger, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'mri_trigger.started')
        mri_trigger.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mri_trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mri_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mri_trigger.status == STARTED and not waitOnFlip:
        theseKeys = mri_trigger.getKeys(keyList=['5'], waitRelease=False)
        _mri_trigger_allKeys.extend(theseKeys)
        if len(_mri_trigger_allKeys):
            trigger_time = _mri_trigger_allKeys[0].tDown  # just the first key pressed
            mri_trigger.rt = _mri_trigger_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
            
    # Run 'Each Frame' code from start_code
    if len(defaultKeyboard.keys) > l:
        response.append(defaultKeyboard.keys[-1])
        l = len(defaultKeyboard.keys)
    if len(response) > 0:
        print('Button pressed: ' + str(response))
        del response[0]
    # check for keys
    if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
        allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
        _default_kb_allKeys.extend(allKeys)
        if len(_default_kb_allKeys):
            defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
            defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
            
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from start_code
thisExp.addData('scan start', trigger_time)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=25.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    

    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ITI_start
    k+=1
    print('The current trial is ' + str(k) + '   Trial type: ' + str(trial_type))
    # reset start values
    if (k == 1): 
        tar_dur = float(expInfo['start target duration (s)'])
    jitter = np.random.choice(np.arange(0, 0.5, .001))
    ITI_dur = 1.5 - jitter - (tar_dur - 0.2)
    thisExp.addData('jitter', jitter)
    # keep track of which components have finished
    ITIComponents = [ITI_txt]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_txt* updates
        if ITI_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_txt.frameNStart = frameN  # exact frame index
            ITI_txt.tStart = t  # local t and not account for scr refresh
            ITI_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_txt.started')
            ITI_txt.setAutoDraw(True)
        if ITI_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_txt.tStartRefresh + ITI_dur-frameTolerance:
                # keep track of stop time/frame for later
                ITI_txt.tStop = t  # not accounting for scr refresh
                ITI_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_txt.stopped')
                ITI_txt.setAutoDraw(False)
        if ITI_txt.status == STARTED:  # only update if drawing
            ITI_txt.setText('+', log=False)
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
                
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "cue" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cueimage.setImage(cue_image)
    # keep track of which components have finished
    cueComponents = [cueimage]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "cue" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cueimage* updates
        if cueimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cueimage.frameNStart = frameN  # exact frame index
            cueimage.tStart = t  # local t and not account for scr refresh
            cueimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cueimage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cueimage.started')
            cueimage.setAutoDraw(True)
        if cueimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cueimage.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                cueimage.tStop = t  # not accounting for scr refresh
                cueimage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cueimage.stopped')
                cueimage.setAutoDraw(False)
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "cue" ---
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # --- Prepare to start Routine "ant" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from antvar
    ant_var = jitter + 2
    thisExp.addData("ant duration", ant_var)
    # keep track of which components have finished
    antComponents = [ant_cross]
    for thisComponent in antComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ant" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ant_cross* updates
        if ant_cross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ant_cross.frameNStart = frameN  # exact frame index
            ant_cross.tStart = t  # local t and not account for scr refresh
            ant_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ant_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ant_cross.started')
            ant_cross.setAutoDraw(True)
        if ant_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ant_cross.tStartRefresh + ant_var-frameTolerance:
                # keep track of stop time/frame for later
                ant_cross.tStop = t  # not accounting for scr refresh
                ant_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ant_cross.stopped')
                ant_cross.setAutoDraw(False)
        if ant_cross.status == STARTED:  # only update if drawing
            ant_cross.setText('+', log=False)
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in antComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ant" ---
    for thisComponent in antComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ant" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    targ_key.keys = []
    targ_key.time = []
    targ_key.rt = []
    _targ_key_allKeys = []
    # keep track of which components have finished
    targetComponents = [squaretarget, targ_key]
    for thisComponent in targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "target" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *squaretarget* updates
        if squaretarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            squaretarget.frameNStart = frameN  # exact frame index
            squaretarget.tStart = t  # local t and not account for scr refresh
            squaretarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(squaretarget, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'squaretarget.started')
            squaretarget.setAutoDraw(True)
        if squaretarget.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > squaretarget.tStartRefresh + tar_dur-frameTolerance:
                # keep track of stop time/frame for later
                squaretarget.tStop = t  # not accounting for scr refresh
                squaretarget.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'squaretarget.stopped')
                squaretarget.setAutoDraw(False)
        if squaretarget.status == STARTED:  # only update if drawing
            squaretarget.setImage('SID_images/target.png', log=False)
            
        # check for cutoff time
        if t >= tar_dur:
            continueRoutine = False
        
        # *targ_key* updates
        waitOnFlip = False
        if targ_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targ_key.frameNStart = frameN  # exact frame index
            targ_key.tStart = t  # local t and not account for scr refresh
            targ_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targ_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'targ_key.started')
            targ_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(targ_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(targ_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if targ_key.status == STARTED and not waitOnFlip:
            theseKeys = targ_key.getKeys(keyList=['1','2','3','4'])
            _targ_key_allKeys.extend(theseKeys)
            if len(_targ_key_allKeys):
                targ_key.keys = _targ_key_allKeys[0].name  # just the first key pressed
                targ_key.rt = _targ_key_allKeys[0].rt
                targ_key.time = _targ_key_allKeys[0].tDown
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "target" ---
    for thisComponent in targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from adjustment
    print('target duration: ' + str(tar_dur))
    thisExp.addData("target dur", tar_dur)
    # store current trial RT and target duration
    if not targ_key.keys:
        prev_RT = tar_dur + 0.01
        print('no button press')
        thisExp.addData("reaction time", 'NA')
    else:
        prev_RT = targ_key.rt
        print('reaction time (s): ' + str(prev_RT))
        thisExp.addData("target button", targ_key.keys)
        thisExp.addData("time pressed", targ_key.time)
        thisExp.addData("reaction time", prev_RT)

    # the Routine "target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fix_start
    # set current trial feedback and adjust target duration for next trial
    if trial_type == "incentive": 
        if prev_RT < tar_dur:
            feedback_image = "SID_images/thumbsup.png"
            status = 1
            tar_dur = tar_dur - .01
        else:
            feedback_image = "SID_images/equalsign.png"
            status = 0
            tar_dur = tar_dur + .01
    else:
        if prev_RT < tar_dur:
            feedback_image = "SID_images/equalsign.png"
            status = 1
            tar_dur = tar_dur - .01
        else:
            feedback_image = "SID_images/equalsign.png"
            status = 0
            tar_dur = tar_dur + .01
    
    thisExp.addData("status", status)
    # keep track of which components have finished
    fixationComponents = [fixcross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixcross.started')
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 1.3-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.stopped')
                fixcross.setAutoDraw(False)
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.300000)
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    fb_img.setImage(feedback_image)
    # keep track of which components have finished
    feedbackComponents = [fb_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fb_img* updates
        if fb_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fb_img.frameNStart = frameN  # exact frame index
            fb_img.tStart = t  # local t and not account for scr refresh
            fb_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fb_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fb_img.started')
            fb_img.setAutoDraw(True)
        if fb_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fb_img.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fb_img.tStop = t  # not accounting for scr refresh
                fb_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fb_img.stopped')
                fb_img.setAutoDraw(False)
        # check for keys
        if defaultKeyboard.getKeys(keyList=["1","2","3","4"]):
            allKeys = defaultKeyboard.getKeys(keyList=["1","2","3","4"], waitRelease=False)
            _default_kb_allKeys.extend(allKeys)
            if len(_default_kb_allKeys):
                defaultKeyboard.keys = [key.name for key in _default_kb_allKeys]  # storing all keys
                defaultKeyboard.rt = [key.tDown for key in _default_kb_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Store Button Presses This Trial
    thisExp.addData("all buttons", defaultKeyboard.keys)
    thisExp.addData("all buttons time", defaultKeyboard.rt)
    _default_kb_allKeys = []
    defaultKeyboard.keys = []
    defaultKeyboard.rt = []
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()

# completed 25.0 repeats of 'trials'

# --- Prepare to start Routine "end_round" ---
continueRoutine = True
routineForceEnded = False
if expInfo['run (1/2)'] == '1':
    print('NEXT RUN START TARGET DURATION: ' + str(tar_dur))
    thisExp.addData('NEXT TARGET DURATION', tar_dur)
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
end_roundComponents = [text, mouse]
for thisComponent in end_roundComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_round" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_roundComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
