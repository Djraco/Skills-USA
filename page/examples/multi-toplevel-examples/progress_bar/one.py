#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5e
#  in conjunction with Tcl version 8.6
#    May 28, 2022 07:27:09 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import one_support

_bgcolor = 'wheat'  # X11 color: #f5deb3
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
_ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
_ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='-family {DejaVu Sans Mono} -size 14')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'black':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+779+229")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top
        self.prog_var = tk.IntVar()

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.42, rely=0.733, height=39, width=96)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(command=one_support.quit)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Quit''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.1, rely=0.102, height=99, width=494)
        self.Label1.configure(activebackground="#ffffcd")
        self.Label1.configure(background="wheat")
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Label1.configure(highlightbackground="wheat")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Example of Using a Progress bar.
Hit the Advance button below repeatedly.
Wait after progress bar fills until it 
dissapears.''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.267, rely=0.513, height=39, width=276)
        self.Button2.configure(activebackground="#f4bcb2")
        self.Button2.configure(background="wheat")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(command=one_support.advance)
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(text='''Advance Progress Bar''')

        _style_code()
        self.TProgressbar1 = ttk.Progressbar(self.top)
        self.TProgressbar1.place(relx=0.333, rely=0.378, relwidth=0.333
                , relheight=0.0, height=19)
        self.TProgressbar1.configure(variable=self.prog_var)

def start_up():
    one_support.main()

if __name__ == '__main__':
    one_support.main()



