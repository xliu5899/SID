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
expName = 'prac_SID'  # from the Builder filename that created this script
expInfo = {
    'participant ID':'',
    'modality (fMRI/EEG)':'',
    'condition (A/NA)':'',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant ID'], expInfo['modality (fMRI/EEG)'], expInfo['condition (A/NA)'])

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

# --- Initialize components for Routine "pretask" ---
start_prac = keyboard.Keyboard()
pretask_text = visual.TextStim(win=win, name='pretask_text',
    text='Press SPACEBAR to begin',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);


# --- Initialize components for Routine "p_ITI" ---
p_ITI_txt = visual.TextStim(win=win, name='p_ITI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from p_ITI_start
prev_pRT = 0
prac_tar_dur = 0.3
p = 0
status = []

# --- Initialize components for Routine "prac_cue" ---
p_cue = visual.ImageStim(
    win=win,
    name='p_cue', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_ant" ---
prac_ant_txt = visual.TextStim(win=win, name='prac_ant_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from p_antvar
prac_ant_var = ''

# --- Initialize components for Routine "pract_targ" ---
prac_target = visual.ImageStim(
    win=win,
    name='prac_target', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
prac_key = keyboard.Keyboard()

# --- Initialize components for Routine "pfixation" ---
p_fixcross = visual.TextStim(win=win, name='p_fixcross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "prac_feedback" ---
prac_feed = visual.ImageStim(
    win=win,
    name='prac_feed', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
    
# --- Initialize components for Routine "end_prac" ---
text = visual.TextStim(win=win, name='text',
    text='END OF PRACTICE ROUND\n\nPLEASE WAIT FOR EXPERIMENTER',
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

# --- Prepare to start Routine "pretask" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_prac.keys = []
start_prac.rt = []
_start_prac_allKeys = []
# keep track of which components have finished
pretaskComponents = [start_prac, pretask_text]
for thisComponent in pretaskComponents:
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

# --- Run Routine "pretask" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_prac* updates
    waitOnFlip = False
    if start_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_prac.frameNStart = frameN  # exact frame index
        start_prac.tStart = t  # local t and not account for scr refresh
        start_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_prac, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_prac.started')
        start_prac.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_prac.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_prac.status == STARTED and not waitOnFlip:
        theseKeys = start_prac.getKeys(keyList=['space'], waitRelease=False)
        _start_prac_allKeys.extend(theseKeys)
        if len(_start_prac_allKeys):
            start_prac.keys = _start_prac_allKeys[-1].name  # just the last key pressed
            start_prac.rt = _start_prac_allKeys[-1].tDown
            # a response ends the routine
            continueRoutine = False
    
    # *pretask_text* updates
    if pretask_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pretask_text.frameNStart = frameN  # exact frame index
        pretask_text.tStart = t  # local t and not account for scr refresh
        pretask_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pretask_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pretask_text.started')
        pretask_text.setAutoDraw(True)
    
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
    for thisComponent in pretaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pretask" ---
for thisComponent in pretaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_prac.keys in ['', [], None]:  # No response was made
    start_prac.keys = None
thisExp.addData('start_prac.keys',start_prac.keys)
if start_prac.keys != None:  # we had a response
    thisExp.addData('start_prac.rt', start_prac.rt)
thisExp.nextEntry()
# the Routine "pretask" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('prac_cond.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "p_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from p_ITI_start
    p += 1
    print('Practice trial: ' + str(p) + '   Trial type: ' + str(prac_trialtype))
    jitter = np.random.choice(np.arange(0, 0.5, .001))
    p_ITI_dur = 1.5 - jitter - (prac_tar_dur - 0.3)
    thisExp.addData('jitter', jitter)
    # keep track of which components have finished
    p_ITIComponents = [p_ITI_txt]
    for thisComponent in p_ITIComponents:
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
    
    # --- Run Routine "p_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_ITI_txt* updates
        if p_ITI_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_ITI_txt.frameNStart = frameN  # exact frame index
            p_ITI_txt.tStart = t  # local t and not account for scr refresh
            p_ITI_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_ITI_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_txt.started')
            p_ITI_txt.setAutoDraw(True)
        if p_ITI_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_ITI_txt.tStartRefresh + p_ITI_dur-frameTolerance:
                # keep track of stop time/frame for later
                p_ITI_txt.tStop = t  # not accounting for scr refresh
                p_ITI_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_txt.stopped')
                p_ITI_txt.setAutoDraw(False)
        if p_ITI_txt.status == STARTED:  # only update if drawing
            p_ITI_txt.setText('+', log=False)
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in p_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "p_ITI" ---
    for thisComponent in p_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "p_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_cue" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    p_cue.setImage(prac_cueimage)
    # keep track of which components have finished
    prac_cueComponents = [p_cue]
    for thisComponent in prac_cueComponents:
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
    
    # --- Run Routine "prac_cue" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_cue* updates
        if p_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_cue.frameNStart = frameN  # exact frame index
            p_cue.tStart = t  # local t and not account for scr refresh
            p_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue.started')
            p_cue.setAutoDraw(True)
        if p_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_cue.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                p_cue.tStop = t  # not accounting for scr refresh
                p_cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue.stopped')
                p_cue.setAutoDraw(False)
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in prac_cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_cue" ---
    for thisComponent in prac_cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # --- Prepare to start Routine "prac_ant" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from p_antvar
    prac_ant_var=jitter + 2
    thisExp.addData('ant dur', prac_ant_var)
    # keep track of which components have finished
    prac_antComponents = [prac_ant_txt]
    for thisComponent in prac_antComponents:
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
    
    # --- Run Routine "prac_ant" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_ant_txt* updates
        if prac_ant_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_ant_txt.frameNStart = frameN  # exact frame index
            prac_ant_txt.tStart = t  # local t and not account for scr refresh
            prac_ant_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_ant_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ant_txt.started')
            prac_ant_txt.setAutoDraw(True)
        if prac_ant_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_ant_txt.tStartRefresh + prac_ant_var-frameTolerance:
                # keep track of stop time/frame for later
                prac_ant_txt.tStop = t  # not accounting for scr refresh
                prac_ant_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ant_txt.stopped')
                prac_ant_txt.setAutoDraw(False)
        if prac_ant_txt.status == STARTED:  # only update if drawing
            prac_ant_txt.setText('+', log=False)
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in prac_antComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_ant" ---
    for thisComponent in prac_antComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_ant" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pract_targ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_target.setImage('SID_images/target.png')
    prac_key.keys = []
    prac_key.time = []
    prac_key.rt = []
    _prac_key_allKeys = []
    # keep track of which components have finished
    pract_targComponents = [prac_target, prac_key]
    for thisComponent in pract_targComponents:
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
    
    # --- Run Routine "pract_targ" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_target* updates
        if prac_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_target.frameNStart = frameN  # exact frame index
            prac_target.tStart = t  # local t and not account for scr refresh
            prac_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target.started')
            prac_target.setAutoDraw(True)
        if prac_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_target.tStartRefresh + prac_tar_dur-frameTolerance:
                # keep track of stop time/frame for later
                prac_target.tStop = t  # not accounting for scr refresh
                prac_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target.stopped')
                prac_target.setAutoDraw(False)
        # check for cutoff time
        if t >= prac_tar_dur:
            continueRoutine = False
        
        # *prac_key* updates
        waitOnFlip = False
        if prac_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_key.frameNStart = frameN  # exact frame index
            prac_key.tStart = t  # local t and not account for scr refresh
            prac_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_key.started')
            prac_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_key.status == STARTED and not waitOnFlip:
            theseKeys = prac_key.getKeys(keyList=['space'])
            _prac_key_allKeys.extend(theseKeys)
            if len(_prac_key_allKeys):
                prac_key.keys = [key.name for key in _prac_key_allKeys]  # storing all keys
                prac_key.time = [key.tDown for key in _prac_key_allKeys]
                prac_key.rt = [key.rt for key in _prac_key_allKeys]
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in pract_targComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pract_targ" ---
    for thisComponent in pract_targComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from p_adjust
    # store current trial RT and target duration
    print('target duration: ' + str(prac_tar_dur))
    thisExp.addData("target dur", prac_tar_dur)
    if not prac_key.keys:
        prev_pRT = prac_tar_dur + 0.01
        print('no button press')
        thisExp.addData("reaction time", 'NA')
    else:
        prev_pRT = prac_key.rt[0]
        print('reaction time (s): ' + str(prev_pRT))
        thisExp.addData("reaction time", prev_pRT)
        
    # the Routine "pract_targ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pfixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pfix_start
    # set current trial feedback and adjust target duration for next trial
    if prac_trialtype == "incentive": 
        if prev_pRT < prac_tar_dur:
            feedback_image = "SID_images/thumbsup.png"
            prac_tar_dur = prac_tar_dur - .01
        else:
            feedback_image = "SID_images/equalsign.png"
            prac_tar_dur = prac_tar_dur + .01
    else:
        feedback_image = "SID_images/equalsign.png"
        if prev_pRT < prac_tar_dur:
            prac_tar_dur = prac_tar_dur - .01
        else:
            prac_tar_dur = prac_tar_dur + .01

    # keep track of which components have finished
    pfixationComponents = [p_fixcross]
    for thisComponent in pfixationComponents:
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
    
    # --- Run Routine "pfixation" ---
    while continueRoutine and routineTimer.getTime() < 1.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_fixcross* updates
        if p_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_fixcross.frameNStart = frameN  # exact frame index
            p_fixcross.tStart = t  # local t and not account for scr refresh
            p_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_fixcross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixcross.started')
            p_fixcross.setAutoDraw(True)
        if p_fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_fixcross.tStartRefresh + 1.3-frameTolerance:
                # keep track of stop time/frame for later
                p_fixcross.tStop = t  # not accounting for scr refresh
                p_fixcross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.stopped')
                p_fixcross.setAutoDraw(False)
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in pfixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pfixation" ---
    for thisComponent in pfixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.300000)
    
    # --- Prepare to start Routine "prac_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_feed.setImage(feedback_image)
    # keep track of which components have finished
    prac_feedbackComponents = [prac_feed]
    for thisComponent in prac_feedbackComponents:
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
    
    # --- Run Routine "prac_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_feed* updates
        if prac_feed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_feed.frameNStart = frameN  # exact frame index
            prac_feed.tStart = t  # local t and not account for scr refresh
            prac_feed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_feed, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fb.started')
            prac_feed.setAutoDraw(True)
        if prac_feed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_feed.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                prac_feed.tStop = t  # not accounting for scr refresh
                prac_feed.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fb.stopped')
                prac_feed.setAutoDraw(False)
        
        # check for keys
        if defaultKeyboard.getKeys():
            allKeys = defaultKeyboard.getKeys(waitRelease=False)
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
        for thisComponent in prac_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_feedback" ---
    for thisComponent in prac_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Store Button Presses This Trial
    thisExp.addData("all keys", defaultKeyboard.keys)
    thisExp.addData("time pressed", defaultKeyboard.rt)
    _default_kb_allKeys = []
    defaultKeyboard.keys = []
    defaultKeyboard.rt = []
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'prac_trials'

# --- Prepare to start Routine "end_prac" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
thisExp.addData('START TARGET DURATION', prac_tar_dur)
print('START TARGET DURATION: ' + str(prac_tar_dur))
# keep track of which components have finished
end_pracComponents = [text, mouse]
for thisComponent in end_pracComponents:
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

# --- Run Routine "end_prac" ---
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
    for thisComponent in end_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_prac" ---
for thisComponent in end_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
