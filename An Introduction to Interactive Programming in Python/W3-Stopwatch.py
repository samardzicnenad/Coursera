'''
Created on May 10, 2013
@author: Nenad

This mini-project focuses on combining text drawing in the canvas with timers to build a simple digital stopwatch 
that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons. 

http://www.codeskulptor.org/#user12_OOoDSHZV9G_0.py
'''
# template for "Stopwatch: The Game"
import simplegui

# define global variables
nCounter, nTotal, nGood = 0, 0, 0
sTimer, sScore = "", ""
bRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def tFormat(t):
    ndSec, t = t%10, t//10
    nSec2, t = t%10, t//10
    nSec1, nMin = t%6, t//6
    #print "%1d:%1d%1d.%1d" % (nMin, nSec1, nSec2, ndSec)
    return str(nMin)+":"+str(nSec1)+str(nSec2)+"."+str(ndSec)

def Score():
    return str(nGood) + "/" + str(nTotal)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global bRunning
    timer.start()
    bRunning = True

def stop():
    global bRunning, nTotal, nGood
    timer.stop()
    if bRunning:
        nTotal += 1
        if nCounter%10 == 0:
            nGood += 1
    bRunning = False

def reset():
    global bRunning, nCounter, nTotal, nGood
    timer.stop()
    nCounter, nTotal, nGood = 0, 0, 0
    bRunning = False

# define event handler for timer with 0.1 sec interval
def tick():
    global nCounter
    nCounter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(tFormat(nCounter), [60, 85], 36, "White")
    canvas.draw_text(Score(), [155, 25], 26, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()