import tkinter as tk
from PIL import ImageTk, Image
import time
import os

f = open('log.txt', 'a')
f.write("\nNew Session: \n" + str(time.localtime()) + "\n\n")
f.close()

log = []

root = tk.Tk()

width_set=300
height_set=300

foward=False
backward=False
left=False
right=False

#canvas = tk.Canvas(root, height=664, width=1176, bg="#5A5A5A")
canvas = tk.Canvas(root, height=height_set, width=height_set, bg="#5A5A5A")
canvas.grid(row=1,column=0)
canvas.pack()

rd_x1=0
rd_y1=0
rd_x2=300
rd_y2=300

#canvas.create_oval(100, 100, 250, 250, fill="grey")
canvas.create_oval(rd_x1, rd_y1, rd_x2, rd_y2, fill="grey")

dot_rad=(rd_x2-rd_x1)/30
middle_place = rd_x2/2 + rd_x1
top_left_place = rd_y2/4 + rd_y1
bot_right_place = (rd_y2*3)/4 + rd_y1

"""
front_dot = canvas.create_oval(170, 125, 180, 135, fill="red")
back_dot = canvas.create_oval(170, 210, 180, 220, fill="red")
left_dot = canvas.create_oval(125, 170, 135, 180, fill="red")
right_dot = canvas.create_oval(210, 170, 220, 180, fill="red")
"""
# front_dot = canvas.create_oval("")
# back_dot
# left_dot
# right_dot
"""
front_dot = canvas.create_oval(middle_place-dot_rad, top_left_place-dot_rad, middle_place+dot_rad, top_left_place+dot_rad, fill="red")
back_dot = canvas.create_oval(middle_place-dot_rad, bot_right_place-dot_rad, middle_place+dot_rad, bot_right_place+dot_rad, fill="red")
left_dot = canvas.create_oval(top_left_place-dot_rad, middle_place-dot_rad, top_left_place+dot_rad, middle_place+dot_rad, fill="red")
right_dot = canvas.create_oval(bot_right_place-dot_rad, middle_place-dot_rad, bot_right_place+dot_rad, middle_place+dot_rad, fill="red")
"""
front = False
back = False
left = False
right = False

def blitFront():
    global front_dot
    global front
    if(not front):
        # print("front")
        log.append("Front Detected: " + str(time.localtime()))
        front=True
        front_dot = canvas.create_oval(middle_place-dot_rad, top_left_place-dot_rad, middle_place+dot_rad, top_left_place+dot_rad, fill="red")
def blitBack():
    global back_dot
    global back
    if(not back):
        # print("back")
        log.append("Back Detected: " + str(time.localtime()))
        back=True
        back_dot = canvas.create_oval(middle_place-dot_rad, bot_right_place-dot_rad, middle_place+dot_rad, bot_right_place+dot_rad, fill="red")
def blitLeft():
    global left_dot
    global left
    if(not left):
        # print("left")
        log.append("Left Detected: " + str(time.localtime()))
        left=True
        left_dot = canvas.create_oval(top_left_place-dot_rad, middle_place-dot_rad, top_left_place+dot_rad, middle_place+dot_rad, fill="red")
def blitRight():
    global right_dot
    global right
    if(not right):
        # print("right")
        log.append("Right Detected: " + str(time.localtime()))
        right=True
        right_dot = canvas.create_oval(bot_right_place-dot_rad, middle_place-dot_rad, bot_right_place+dot_rad, middle_place+dot_rad, fill="red")

def delFront():
    global front
    global front_dot
    # print("deleted front")
    front=False
    canvas.delete(front_dot)

def delBack():
    global back
    global back_dot
    # print("deleted back")
    back=False
    canvas.delete(back_dot)

def delLeft():
    global left
    global left_dot
    # print("deleted left")
    left=False
    canvas.delete(left_dot)

def delRight():
    global right
    global right_dot
    # print("deleted right")
    right=False
    canvas.delete(right_dot)

def keyPress(e):
    # print(e.char)
    if(e.char == 'w'):
        blitFront()
    if(e.char == 'a'):
        blitLeft()
    if(e.char == 's'):
        blitBack()
    if(e.char == 'd'):
        blitRight()

def keyRelease(e):
    # print(e.char)
    if(e.char == 'w'):
        delFront()
    if(e.char == 'a'):
        delLeft()
    if(e.char == 's'):
        delBack()
    if(e.char == 'd'):
        delRight()



canvas.bind("<KeyPress>", keyPress)
canvas.bind("<KeyRelease>", keyRelease)
canvas.focus_set()#keys affact canvas

root.mainloop()



with open('log.txt', 'a') as f:
    for detection in log:
        f.write(detection + ',\n')
f.close()
