

from tkinter import*
def _window(var, title, geometry):
    
    var.title(title)
    var.geometry(geometry)
def _title(var, title):
    var.title(title)
def _geometry(var, geometry):
    var.geometry(geometry)
def _buttonCommand(var, displayText, function, x, y):
    Button(var, text=displayText, command=function).place(x=x,y=y)
def _button(var, displayText, x, y):
    Button(var, text=displayText).place(x=x, y=y)
def _background(var, color):
    var.config(background=color)
def _create(root, name, place_x, place_y, bg, command):
    create = Checkbutton(root, text=name, command=command)
    create.config(background= bg)
    create.place(x=place_x, y=place_y)

def _checkbox_disable(root, name, place_x, place_y, bg, command):
    create = Checkbutton(root, text=name, command=command, state="disabled")
    create.config(background=bg)
    create.place(x=place_x, y=place_y)
def _checkbox(root, name, place_x, place_y, bg):
    create = Checkbutton(root, text=name)
    create.config(background=bg)
    create.place(x=place_x, y=place_y)
def _entry(root, x, y, state):
    Entry(root, state=state).place(x=x, y=y)
def _title(root, title):
    root.title(title)

