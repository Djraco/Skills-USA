#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5e
#  in conjunction with Tcl version 8.6
#    May 28, 2022 07:37:33 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import customwidgetdemo_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#d9d9d9' # X11 color: 'gray85'
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
    style.configure('.',font='-family {DejaVu Sans} -size 12')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'black':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class formCustomDemo:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("529x522+296+123")
        top.minsize(1, 1)
        top.maxsize(1265, 770)
        top.resizable(1,  1)
        top.title("Custom Widget Demo")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        _style_code()
        self.TSizegrip1 = ttk.Sizegrip(self.top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.038, rely=0.029, relheight=0.121
                , relwidth=0.928)
        self.Message1.configure(font="-family {DejaVu Sans Mono} -size 10")
        self.Message1.configure(highlightbackground="wheat")
        self.Message1.configure(relief="sunken")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=491)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.057, rely=0.211, relheight=0.718
                , relwidth=0.501)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(highlightbackground="wheat")

        self.Custom1 = customwidgetdemo_support.Custom(self.Frame1)
        self.Custom1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.btnGetChecks = tk.Button(self.top)
        self.btnGetChecks.place(relx=0.681, rely=0.335, height=30, width=110)
        self.btnGetChecks.configure(activebackground="#d9d9d9")
        self.btnGetChecks.configure(command=customwidgetdemo_support.on_btnGetChecks)
        self.btnGetChecks.configure(disabledforeground="#b8a786")
        self.btnGetChecks.configure(font="-family {DejaVu Sans Mono} -size 10")
        self.btnGetChecks.configure(highlightbackground="wheat")
        self.btnGetChecks.configure(text='''Get Checks''')

        self.btnClearChecks = tk.Button(self.top)
        self.btnClearChecks.place(relx=0.681, rely=0.527, height=30, width=110)
        self.btnClearChecks.configure(activebackground="#d9d9d9")
        self.btnClearChecks.configure(command=customwidgetdemo_support.on_btnClearChecks)
        self.btnClearChecks.configure(disabledforeground="#b8a786")
        self.btnClearChecks.configure(font="-family {DejaVu Sans Mono} -size 10")
        self.btnClearChecks.configure(highlightbackground="wheat")
        self.btnClearChecks.configure(state='active')
        self.btnClearChecks.configure(text='''Clear Checks''')

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(relx=0.681, rely=0.718, height=30, width=110)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(command=customwidgetdemo_support.on_btnExit)
        self.btnExit.configure(disabledforeground="#b8a786")
        self.btnExit.configure(font="-family {DejaVu Sans Mono} -size 10")
        self.btnExit.configure(highlightbackground="wheat")
        self.btnExit.configure(text='''Exit''')

def start_up():
    customwidgetdemo_support.main()

if __name__ == '__main__':
    customwidgetdemo_support.main()



