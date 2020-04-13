# This program displays all instructions, then a search array of 5 distractors and 1 target, then 
# an orange and black rectangle. It runs for 10 practice trials and 180 experimental trials 
# (10 of each condition (3) x search array position (6)). Only experimental trials are written to the log_file.

from psychopy import visual, event, core, misc
from psychopy.hardware import keyboard
import psychtoolbox as ptb
import numpy as np
import random

# The variable win is set equal to None.
win = None
# The variable task_start_time is set equal to None.
task_start_time = None
# The variable kb is set equal to None.
kb = None
# The variable mouse is set equal to None.
mouse = None
# The variable log_file is set equal to None.
log_file = None
# The variable box1 is set equal to None.
box1 = None
# The variable box2 is set equal to None.
box2 = None
# The variable im is set equal to an empty list.
im = []
# The variable im1 is set equal to an empty list.
im1 = []
# The variable im2 is set equal to an empty list.
im2 = []
# The variable im3 is set equal to an empty list.
im3 = []
# The variable im4 is set equal to an empty list.
im4 = []
# The variable im5 is set equal to an empty list.
im5 = []
# The variable imKeys is set equal to an empty list.
imKeys = []
# The variable im_positions is set equal to None.
im_positions = None
# The variable t_name is set equal to an empty list.
t_name = []
# The variable numberoftrials is set equal to an empty list.
numberoftrials = []
# The variable array_entry is set equal to an empty list.
array_entry = []
# The variable response_entry is set equal to an empty list.
response_entry = []
# The variable color_entry is set equal to an empty list.
color_entry = []

# The function MakeSearchArray() takes no input arguments. It returns an ouput of a search array for each trial. Its purpose is to randomize distractor images, target images, and positions on each trial, creating a search array.
def MakeSearchArray():
    # Make the following variables global: t_name, im, im1, im2, im3, im4, im5, imKeys, im_positions.
    global t_name
    global im
    global im1
    global im2
    global im3
    global im4
    global im5
    global imKeys
    global im_positions
    
    # The variable path defines where these images are located on my computer.
    path = '/Users/ariel/OneDrive - University of Iowa/Spring 2020/Programming/Cat Task'
    # The variable d_name is a list of all of the distractors.
    d_name = ['Dis_1_1.bmp','Dis_1_2.bmp','Dis_1_3.bmp','Dis_1_4.bmp','Dis_1_5.bmp','Dis_1_6.bmp','Dis_1_7.bmp','Dis_1_8.bmp','Dis_1_9.bmp','Dis_1_10.bmp',
    'Dis_1_11.bmp','Dis_1_12.bmp','Dis_1_13.bmp','Dis_1_14.bmp','Dis_1_15.bmp','Dis_1_16.bmp','Dis_1_17.bmp','Dis_1_18.bmp','Dis_1_19.bmp','Dis_1_20.bmp',
    'Dis_1_21.bmp','Dis_1_22.bmp','Dis_1_23.bmp','Dis_1_24.bmp','Dis_1_25.bmp','Dis_1_26.bmp','Dis_1_27.bmp','Dis_1_28.bmp','Dis_1_29.bmp','Dis_1_30.bmp',
    'Dis_1_31.bmp','Dis_1_32.bmp','Dis_1_33.bmp','Dis_1_34.bmp','Dis_1_35.bmp','Dis_1_36.bmp','Dis_1_37.bmp','Dis_1_38.bmp','Dis_1_39.bmp','Dis_1_40.bmp',
    'Dis_1_41.bmp','Dis_1_42.bmp','Dis_1_43.bmp','Dis_1_44.bmp','Dis_1_45.bmp','Dis_1_46.bmp','Dis_1_47.bmp','Dis_1_48.bmp','Dis_1_49.bmp','Dis_1_50.bmp',
    'Dis_1_51.bmp','Dis_1_52.bmp','Dis_1_53.bmp','Dis_1_54.bmp','Dis_1_55.bmp','Dis_1_56.bmp','Dis_1_57.bmp','Dis_1_58.bmp','Dis_1_59.bmp','Dis_1_60.bmp',
    'Dis_1_61.bmp','Dis_1_62.bmp','Dis_1_63.bmp','Dis_1_64.bmp','Dis_1_65.bmp','Dis_1_66.bmp','Dis_1_67.bmp','Dis_1_68.bmp','Dis_1_69.bmp','Dis_1_70.bmp',
    'Dis_1_71.bmp','Dis_1_72.bmp','Dis_1_73.bmp','Dis_1_74.bmp','Dis_1_75.bmp',
    'Dis_2_1.bmp','Dis_2_2.bmp','Dis_2_3.bmp','Dis_2_4.bmp','Dis_2_5.bmp','Dis_2_6.bmp','Dis_2_7.bmp','Dis_2_8.bmp','Dis_2_9.bmp','Dis_2_10.bmp',
    'Dis_2_11.bmp','Dis_2_12.bmp','Dis_2_13.bmp','Dis_2_14.bmp','Dis_2_15.bmp','Dis_2_16.bmp','Dis_2_17.bmp','Dis_2_18.bmp','Dis_2_19.bmp','Dis_2_20.bmp',
    'Dis_2_21.bmp','Dis_2_22.bmp','Dis_2_23.bmp','Dis_2_24.bmp','Dis_2_25.bmp','Dis_2_26.bmp','Dis_2_27.bmp','Dis_2_28.bmp','Dis_2_29.bmp','Dis_2_30.bmp',
    'Dis_2_31.bmp','Dis_2_32.bmp','Dis_2_33.bmp','Dis_2_34.bmp','Dis_2_35.bmp','Dis_2_36.bmp','Dis_2_37.bmp','Dis_2_38.bmp','Dis_2_39.bmp','Dis_2_40.bmp',
    'Dis_2_41.bmp','Dis_2_42.bmp','Dis_2_43.bmp','Dis_2_44.bmp','Dis_2_45.bmp','Dis_2_46.bmp','Dis_2_47.bmp','Dis_2_48.bmp','Dis_2_49.bmp','Dis_2_50.bmp',
    'Dis_2_51.bmp','Dis_2_52.bmp','Dis_2_53.bmp','Dis_2_54.bmp','Dis_2_55.bmp','Dis_2_56.bmp','Dis_2_57.bmp','Dis_2_58.bmp','Dis_2_59.bmp','Dis_2_60.bmp',
    'Dis_2_61.bmp','Dis_2_62.bmp','Dis_2_63.bmp','Dis_2_64.bmp','Dis_2_65.bmp','Dis_2_66.bmp','Dis_2_67.bmp','Dis_2_68.bmp','Dis_2_69.bmp','Dis_2_70.bmp',
    'Dis_2_71.bmp','Dis_2_72.bmp','Dis_2_73.bmp','Dis_2_74.bmp','Dis_2_75.bmp']
    # This randomly shuffles the list of distractors.
    np.random.shuffle(d_name)
    
    # The variable t_name is a list of all of the targets.
    t_name = ['Cat_1_1.bmp','Cat_1_2.bmp','Cat_1_3.bmp','Cat_2_1.bmp','Cat_2_2.bmp','Cat_2_3.bmp']
    # This randomly shuffles the list of targets. 
    np.random.shuffle(t_name)
    
    # This area selects images for the search array on each trial.
    # The variable im randomly chooses 1 target on each trial.
    im = visual.ImageStim(win, image=t_name[0])
    # The variable im1 randomly chooses 1 distractor for this position on each trial, without replacement.
    im1 = visual.ImageStim(win, image=d_name[0])
    # The variable im2 randomly chooses 1 distractor for this position on each trial, without replacement.
    im2 = visual.ImageStim(win, image=d_name[1])
    # The variable im3 randomly chooses 1 distractor for this position on each trial, without replacement.
    im3 = visual.ImageStim(win, image=d_name[2])
    # The variable im4 randomly chooses 1 distractor for this position on each trial, without replacement.
    im4 = visual.ImageStim(win, image=d_name[3])
    # The variable im5 randomly chooses 1 distractor for this position on each trial, without replacement.
    im5 = visual.ImageStim(win, image=d_name[4])
    
    # The variable im_positions creates a list of position keys for each of the 5 images. The positions are in inches and are indexed by 0-5.
    im_positions = {0: (-5, -5),
                    1: (5, 5),
                    2: (-5, 5),
                    3: (5, -5),
                    4: (-7.5, 0),
                    5: (7.5, 0)}
    # The variable imKeys takes the list of im_positions and shuffles them each trial.
    imKeys = np.array(list(im_positions.keys()))
    
    # This section sets each image position before each trial.
    # This randomly shuffles the imKeys.
    np.random.shuffle(imKeys)
    # The variable im.pos takes the value of the first of the im_positions and is shuffled.
    im.pos=(im_positions[imKeys[0]])
    # The variable im1.pos takes the value of the second of the im_positions and is shuffled.
    im1.pos=(im_positions[imKeys[1]])
    # The variable im2.pos takes the value of the third of the im_positions and is shuffled.
    im2.pos=(im_positions[imKeys[2]])
    # The variable im3.pos takes the value of the fourth of the im_positions and is shuffled.
    im3.pos=(im_positions[imKeys[3]])
    # The variable im4.pos takes the value of the fifth of the im_positions and is shuffled.
    im4.pos=(im_positions[imKeys[4]])
    # The variable im5.pos takes the value of the sixth of the im_positions and is shuffled.
    im5.pos=(im_positions[imKeys[5]])

# The function Initialize() initializes multiple variables for later use in the experiment. It takes no input arguments and has no output arguments. 
def Initialize():
    # Make the following variables global: win, task_start_time, kb, mouse, log_file, box1, box2.
    global win
    global task_start_time
    global kb
    global mouse
    global log_file
    global box1
    global box2
    
    # The variable task_start_time calculates the start time of the task. 
    task_start_time = core.getTime()
    
    # The variable win defines the window for the experiment.
    win = visual.Window(fullscr=True, monitor = "testMonitor", units = "deg",
        screen=1, color = 'white')
    
    # The variable box1 creates an orange rectangle.
    box1 = visual.Rect(win, width = 200, height = 200, units = "pix", pos = (300, 0), lineColor = None, 
        fillColor = 'orange')
    # The variable box2 creates a black rectangle.
    box2 = visual.Rect(win, width = 200, height = 200, units = "pix", pos = (-300, 0), lineColor = None, 
        fillColor = 'black')
    
    # This calls the function MakeSearchArray().
    MakeSearchArray()
    
    # This initializes the mouse as mouse.
    mouse = event.Mouse()
    
    # This initializes the keyboard as kb.
    kb = keyboard.Keyboard()
    
    # This adds the information collected in the experiment to the log_file by appending it.
    log_file = open('CatData.csv', 'a')

# The function ShowInstructions() displays the experimental instructions. It takes no input or output arguments.
def ShowInstructions():
    # Make the variable win global.
    global win
    
    # The variable ins creates the instructions for the first screen.
    ins = visual.TextStim(win, height = 0.5, wrapWidth = 15, color = 'black',
        pos = (0, 0), text = 'On each trial, you will be asked to find a cat and report its position on the screen. \nPress j for left and k for right. \
    \n \nThen, you will be asked to identify the color of the cat. \nUsing the mouse, click on the box corresponding to the color. \n \n \nPress spacebar for more instructions.')
    
    # This loop continues to draw the first screen instructions until a key is pressed.
    while not event.getKeys():
        ins.draw()
        
        win.flip()
    
    # The variable black_cat chooses the primary target for the experiment for the second screen.
    # The variable cat_ins creates the instructions for the second screen.
    black_cat =  visual.ImageStim(win, image='Cat_1_1.bmp')
    cat_ins = visual.TextStim(win, height = 0.5, wrapWidth = 15, color = 'black',
        pos = (0, 5), text = 'This is your primary target. Always look for this exact cat first. \nIf this cat is not present in the search array, search for another cat. \
    \n \nWhen you find the cat, report the side of the screen its on and its color. \n \n \nPress spacebar to begin.')
    
    # This loop continues to draw the second screen instructions and primary target until a key is pressed.
    while not event.getKeys():
        black_cat.draw()
        cat_ins.draw()
        
        win.flip()

# The function RunTrial() draws the search array, the responses boxes, and collects information from each trial. It takes no 
# input arguments. Its output arguments are side_entry, response_entry, and color_entry.
def RunTrial():
    # Make the following variables global: win, kb, mouse, box1, box2, im, im1, im2, im3, im4, im5, imKeys, t_name, im_positions
    # array_entry, response_entry, color_entry.
    global win
    global kb
    global mouse
    global box1
    global box2
    global im
    global im1
    global im2
    global im3
    global im4
    global im5
    global imKeys
    global t_name
    global im_positions
    global array_entry
    global response_entry
    global color_entry
    
    # This resets the clock for the keypress.
    kb.clock.reset()
    # This clears all keypress events up until now.
    event.clearEvents()
    
    # This loop draws the images for the array while there is no keypress.
    while not event.getKeys():
        im.draw()
        im1.draw()
        im2.draw()
        im3.draw()
        im4.draw()
        im5.draw()
        
        win.flip()
    
    # This section tracks where the target appeared in the search array.
    # The variable im.pos takes the target position from the search array.
    im.pos = (im_positions[imKeys[0]])
    # The variable x takes the first target chosen for each trial.
    x = im.pos[0]
    # This loop tracks the side of the screen that the target appeared on. If it appeared on the positive side of the screen, 
    # the side_entry is right.
    if x > 0:
        side_entry = 'right'
    # Or, if the target appeared on the negative side of the screen, the side_entry is left.
    elif x < 0:
        side_entry = 'left'
    # Or, if something weird happens and no target appears, the side_entry is none.
    else:
        side_entry = 'none'
    
    # The variable array_entry takes a string of the target name for each trial and the side that the target appeared on for each trial.
    array_entry = str(t_name[0]) + "," + side_entry
    
    # The variable ptbKeys takes two input arguments: a list of acceptable keys and turns waitRelease to false so that the reaction time doesn't wait for the key to be released. 
    ptbKeys = kb.getKeys(keyList = ['j', 'k'], waitRelease = False)
    
    # The variable response_entry takes the name of the first keypress and a string of the keypress reaction time.
    response_entry = ptbKeys[0].name + ',' + str(ptbKeys[0].rt)
    
    # The variable mouse_clicked checks for a mouse click and is initialized as false.
    mouse_clicked = False
    
    # This loop draws the black and orange response boxes until a button is pressed.
    while mouse_clicked == False:
        # The variable mouse_pos tracks the position of the mouse.
        mouse_pos = mouse.getPos()
        # The variable x takes the position of the first mouse click.
        x = mouse_pos[0]
        
        # This draws both response boxes, then flips the window.
        box1.draw()
        box2.draw()
        
        win.flip()
        
        # The variable buttons waits for the mouse to be pressed.
        buttons = mouse.getPressed()
        # The variable mouse_clicked waits for the first left click of the mouse.
        mouse_clicked = buttons[0]
    
    # This loop tracks where the mouse was pressed. If the mouse was pressed on the positive (right) side of the screen,
    # the color_entry is orange.
    if x > 0:
        color_entry = 'orange'
    # Or, if the mouse was pressed on the negative (left) side of the screen, the color_entry is orange.
    elif x < 0:
        color_entry = 'black'
    # Or, if nothing was pressed, the color_entry is none.
    else:
        color_entry = 'none'

# The function RunPrac() displays practice instructions, runs 10 practice trials by calling RunTrial() and MakeSearchArray(),
# and displays experiment start instructions. It takes no input arguments and has no output arguments.
def RunPrac():
    # Make the following variables global: win, numberoftrials.
    global win
    global numberoftrials
    
    # The variable prac_ins creates the instructions for the screen before practice.
    prac_ins = visual.TextStim(win, height = 0.5, wrapWidth = 15, color = 'black',
        pos = (0, 0), text = 'Press any key to begin the practice.')
    
    # This loop continues to draw the screen before practice until a key is pressed.
    while not event.getKeys():
        prac_ins.draw()
        
        win.flip()
    
    # The variable numberoftrials is set to 10 to run 10 practice trials.
    numberoftrials = 10
    # This loop runs a practice trial 10 times.
    for i in range(numberoftrials):
        # This calls the function RunTrial().
        RunTrial()
        # This calls the function MakeSearchArray().
        MakeSearchArray()
    
    # The variable start_ins creates the instructions for the screen before the experiment.
    start_ins = visual.TextStim(win, height = 0.5, wrapWidth = 15, color = 'black',
        pos = (0, 0), text = 'Press any key to begin the experiment.')
    
    # This loop continues to draw the screen before the experiment until a key is pressed.
    while not event.getKeys():
        start_ins.draw()
        
        win.flip()

# The function RunTask() runs 180 experimental trials by calling RunTrial(), MakeSearchArray(), and writing to the log_file. 
# It takes no input arguments but outputs to the log_file.
def RunTask():
    # Make the following variables global: numberoftrials, array_entry, response_entry, color_entry.
    global numberoftrials
    global array_entry
    global response_entry
    global color_entry
    
    # The variable numberoftrials is set to 180 to run 180 experimental trials.
    numberoftrials = 180
    # This loop runs an experimental trial 180 times.
    for i in range(numberoftrials):
        # This calls the function RunTrial().
        RunTrial()
        # This calls the function MakeSearchArray().
        MakeSearchArray()
        # This writes down all of the information collected in RunTrial(), then starts a new line.
        log_file.write(array_entry + "," + response_entry + "," + color_entry + "\n")

# The function ShowThanks() takes no input or output arguments. Its purpose is to display final instructions until a key is pressed.
def ShowThanks():
    # Make the variable win global.
    global win
    
    # The variable thanks_ins creates the thank you instructions for the final screen.
    thanks_ins = visual.TextStim(win, height = 0.5, wrapWidth = 15, color = 'black',
        pos = (0, 0), text = 'Thanks for participating in this experiment!')
    
    # This loop continues to draw the final screen instructions until a key is pressed.
    while not event.getKeys():
        thanks_ins.draw()
        
        win.flip()

# The function TerminateTask() takes no input arguments. Its purpose is to close to log_file and the window, and quit the experiment.
def TerminateTask():
    # Make the following variables global: win, log_file.
    global win
    global log_file
    
    # Close the log_file.
    log_file.close()
    # Close the window.
    win.close()
    # Quit the experiment.
    core.quit()

# This area calls each function in the correct order of the experiment: Initialize(), ShowInstrctions(), RunPrac(), RunTask(), ShowThanks(), TerminateTask().
Initialize()
ShowInstructions()
RunPrac()
RunTask()
ShowThanks()
TerminateTask()