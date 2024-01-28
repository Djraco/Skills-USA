#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0Q
#  in conjunction with Tcl version 8.6
#    Dec 26, 2023 06:15:44 AM CST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import PAGE80Demo_support

_bgcolor = 'cornsilk4'
_fgcolor = 'black'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: PAGE80Demo_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'cornsilk-dark.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('cornsilk-dark')
    style.configure('.', font = "-family {DejaVu Sans} -size 11 -weight bold")
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1002x750+746+225")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("Toplevel 0")
        top.configure(background="cornsilk4")
        top.configure(highlightbackground="cornsilk4")
        top.configure(highlightcolor="black")

        self.top = top
        self.SpinData = tk.StringVar()
        self.SpinData.set('20')
        self.comboThemes = tk.StringVar()
        self.tch47 = tk.IntVar()
        self.selectedButton = tk.IntVar()
        self.VProg = tk.IntVar()
        self.HProg = tk.IntVar()
        self.VScale = tk.DoubleVar()
        self.HScale = tk.DoubleVar()
        self.WrapOption = tk.IntVar()

        _style_code()
        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(x=10, y=10, height=70, width=70)
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='left')
        photo_location = os.path.join(_location,"./graphics/ChubbyOwlLogo60.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.TLabel1.configure(image=_img0)
        self.TLabel1.configure(compound='none')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(x=130, y=31, height=24, width=201)
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='e')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Available Themes:''')
        self.TLabel2.configure(compound='left')

        self.btnExit = ttk.Button(self.top)
        self.btnExit.place(x=840, y=20, height=40, width=97)
        self.btnExit.configure(command=PAGE80Demo_support.on_btnExit)
        self.btnExit.configure(text='''Exit''')
        photo_location = os.path.join(_location,"./graphics/system-log-out.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btnExit.configure(image=_img1)
        self.btnExit.configure(compound='left')
        self.btnExit.configure(style='Toolbutton')

        self.chkApplyBkgnd = ttk.Checkbutton(self.top)
        self.chkApplyBkgnd.place(x=150, y=70, width=415, height=36)
        self.chkApplyBkgnd.configure(variable=self.tch47)
        self.chkApplyBkgnd.configure(command=PAGE80Demo_support.on_ChkApplyBkgnd)
        self.chkApplyBkgnd.configure(text='''Apply Background to Notebook Pages''')
        self.chkApplyBkgnd.configure(compound='left')

        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(x=30, y=130, height=524, width=924)
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Page 1''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t1.configure(background="cornsilk4")
        self.TNotebook1_t1.configure(highlightbackground="cornsilk4")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Page 2''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2.configure(background="cornsilk4")
        self.TNotebook1_t2.configure(highlightbackground="cornsilk4")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Page 3''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3.configure(background="cornsilk4")
        self.TNotebook1_t3.configure(highlightbackground="cornsilk4")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Page 4''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t4.configure(background="cornsilk4")
        self.TNotebook1_t4.configure(highlightbackground="cornsilk4")

        self.Scrolledtreeview1 = ScrolledTreeView(self.TNotebook1_t1)
        self.Scrolledtreeview1.place(x=170, y=60, height=382, width=580)
        self.Scrolledtreeview1.configure(columns="Col1")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",text="Tree")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="281")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Col1")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="281")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")

        self.TPanedwindow1 = ttk.Panedwindow(self.TNotebook1_t2
                , orient="horizontal")
        self.TPanedwindow1.place(x=20, y=40, height=440, width=858)
        self.TPanedwindow1_p1 = ttk.Labelframe(self.TPanedwindow1, width=225
                , text='Pane 1')
        self.TPanedwindow1.add(self.TPanedwindow1_p1, weight=0)
        self.TPanedwindow1_p1.configure(text='''Pane 1''')
        self.TPanedwindow1_p2 = ttk.Labelframe(self.TPanedwindow1, text='Pane 2')

        self.TPanedwindow1.add(self.TPanedwindow1_p2, weight=0)
        self.TPanedwindow1_p2.configure(text='''Pane 2''')
        self.__funcid0 = self.TPanedwindow1.bind('<Map>', self.__adjust_sash0)

        self.Scrolledlistbox1 = ScrolledListBox(self.TPanedwindow1_p1)
        self.Scrolledlistbox1.place(x=5, y=40, height=391, width=198
                , bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(disabledforeground="#68665a")
        self.Scrolledlistbox1.configure(exportselection="0")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightbackground="cornsilk4")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#d9d9d9")

        self.TPanedwindow2 = ttk.Panedwindow(self.TPanedwindow1_p2
                , orient="vertical")
        self.TPanedwindow2.place(x=20, y=40, height=388, width=580
                , bordermode='ignore')
        self.TPanedwindow2_p1 = ttk.Labelframe(self.TPanedwindow2, height=125
                , text='Pane 1')
        self.TPanedwindow2.add(self.TPanedwindow2_p1, weight=0)
        self.TPanedwindow2_p1.configure(text='''Pane 1''')
        self.TPanedwindow2_p2 = ttk.Labelframe(self.TPanedwindow2, text='Pane 2')

        self.TPanedwindow2.add(self.TPanedwindow2_p2, weight=0)
        self.TPanedwindow2_p2.configure(text='''Pane 2''')
        self.__funcid1 = self.TPanedwindow2.bind('<Map>', self.__adjust_sash1)

        self.TRadiobutton2 = ttk.Radiobutton(self.TPanedwindow2_p1)
        self.TRadiobutton2.place(x=177, y=48, width=91, height=28
                , bordermode='ignore')
        self.TRadiobutton2.configure(variable=self.selectedButton)
        self.TRadiobutton2.configure(value='2')
        self.TRadiobutton2.configure(text='''TRadio 2''')
        self.TRadiobutton2.configure(compound='left')
        self.TRadiobutton2.configure(style='Toolbutton')

        self.TRadiobutton3 = ttk.Radiobutton(self.TPanedwindow2_p1)
        self.TRadiobutton3.place(x=311, y=48, width=91, height=28
                , bordermode='ignore')
        self.TRadiobutton3.configure(variable=self.selectedButton)
        self.TRadiobutton3.configure(value='3')
        self.TRadiobutton3.configure(text='''TRadio 3''')
        self.TRadiobutton3.configure(compound='left')
        self.TRadiobutton3.configure(style='Toolbutton')

        self.TRadiobutton4 = ttk.Radiobutton(self.TPanedwindow2_p1)
        self.TRadiobutton4.place(x=445, y=48, width=91, height=28
                , bordermode='ignore')
        self.TRadiobutton4.configure(variable=self.selectedButton)
        self.TRadiobutton4.configure(value='4')
        self.TRadiobutton4.configure(text='''TRadio 4''')
        self.TRadiobutton4.configure(compound='left')
        self.TRadiobutton4.configure(style='Toolbutton')

        self.TRadiobutton1 = ttk.Radiobutton(self.TPanedwindow2_p1)
        self.TRadiobutton1.place(x=43, y=48, width=91, height=28
                , bordermode='ignore')
        self.TRadiobutton1.configure(variable=self.selectedButton)
        self.TRadiobutton1.configure(text='''TRadio 1''')
        self.TRadiobutton1.configure(compound='left')
        self.TRadiobutton1.configure(style='Toolbutton')

        self.TProgressbar1 = ttk.Progressbar(self.TPanedwindow2_p2)
        self.TProgressbar1.place(x=210, y=50, width=18, height=100
                , bordermode='ignore')
        self.TProgressbar1.configure(orient="vertical")
        self.TProgressbar1.configure(mode="indeterminate")
        self.TProgressbar1.configure(variable=self.VProg)

        self.TProgressbar2 = ttk.Progressbar(self.TPanedwindow2_p2)
        self.TProgressbar2.place(x=250, y=50, width=100, height=18
                , bordermode='ignore')
        self.TProgressbar2.configure(mode="indeterminate")
        self.TProgressbar2.configure(variable=self.HProg)

        self.TScale1 = ttk.Scale(self.TPanedwindow2_p2, from_=1, to=100)
        self.TScale1.place(x=30, y=50, height=100, width=14)
        self.TScale1.configure(variable=self.VScale)
        self.TScale1.configure(orient="vertical")
        self.VScale.set(1)

        self.TScale2 = ttk.Scale(self.TPanedwindow2_p2, from_=1, to=100)
        self.TScale2.place(x=70, y=50, height=14, width=100)
        self.TScale2.configure(variable=self.HScale)
        self.HScale.set(1)

        self.btnAnimate = ttk.Button(self.TPanedwindow2_p2)
        self.btnAnimate.place(x=290, y=150, height=30, width=222
                , bordermode='ignore')
        self.btnAnimate.configure(command=PAGE80Demo_support.on_btnAnimate)
        self.btnAnimate.configure(text='''Start Automation''')
        self.btnAnimate.configure(compound='left')

        self.TLabel4 = ttk.Label(self.TPanedwindow2_p2)
        self.TLabel4.place(x=410, y=60, height=24, width=101
                , bordermode='ignore')
        self.TLabel4.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='center')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Speed''')
        self.TLabel4.configure(compound='left')

        self.TSpinbox1 = ttk.Spinbox(self.TPanedwindow2_p2, from_=20, to=60)
        self.TSpinbox1.place(x=420, y=90, height=24, width=85
                , bordermode='ignore')
        self.TSpinbox1.configure(command=PAGE80Demo_support.on_Spin)
        self.TSpinbox1.configure(exportselection="0")
        self.TSpinbox1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TSpinbox1.configure(textvariable=self.SpinData)
        self.SpinData.set('''SpinData''')
        self.TSpinbox1.configure(background="white")

        self.TFrame1 = ttk.Frame(self.TNotebook1_t3)
        self.TFrame1.place(x=20, y=20, height=445, width=895)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TFrame2 = ttk.Frame(self.TFrame1)
        self.TFrame2.place(x=10, y=10, height=425, width=875)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")

        self.TFrame3 = ttk.Frame(self.TFrame2)
        self.TFrame3.place(x=690, y=3, height=405, width=185)
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief="groove")

        self.Label2 = tk.Label(self.TFrame3)
        self.Label2.place(x=10, y=10, height=32, width=164)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(background="peachpuff2")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#68665a")
        self.Label2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label2.configure(highlightbackground="cornsilk4")
        self.Label2.configure(text='''Wrap Settings''')

        self.TRadiobutton6 = ttk.Radiobutton(self.TFrame3)
        self.TRadiobutton6.place(x=25, y=100, width=130, height=32)
        self.TRadiobutton6.configure(variable=self.WrapOption)
        self.TRadiobutton6.configure(value='2')
        self.TRadiobutton6.configure(command=PAGE80Demo_support.on_WrapSettings)
        self.TRadiobutton6.configure(text='''Char''')
        self.TRadiobutton6.configure(compound='left')
        self.TRadiobutton6.configure(style='Toolbutton')

        self.TRadiobutton7 = ttk.Radiobutton(self.TFrame3)
        self.TRadiobutton7.place(x=25, y=140, width=130, height=32)
        self.TRadiobutton7.configure(variable=self.WrapOption)
        self.TRadiobutton7.configure(value='3')
        self.TRadiobutton7.configure(command=PAGE80Demo_support.on_WrapSettings)
        self.TRadiobutton7.configure(text='''Word''')
        self.TRadiobutton7.configure(compound='left')
        self.TRadiobutton7.configure(style='Toolbutton')

        self.TRadiobutton5 = ttk.Radiobutton(self.TFrame3)
        self.TRadiobutton5.place(x=25, y=60, width=130, height=32)
        self.TRadiobutton5.configure(variable=self.WrapOption)
        self.TRadiobutton5.configure(command=PAGE80Demo_support.on_WrapSettings)
        self.TRadiobutton5.configure(text='''None''')
        self.TRadiobutton5.configure(compound='left')
        self.TRadiobutton5.configure(style='Toolbutton')

        self.Label1 = tk.Label(self.TFrame2)
        self.Label1.place(x=10, y=10, height=32, width=674)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(background="peachpuff2")
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#68665a")
        self.Label1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label1.configure(highlightbackground="cornsilk4")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''ScrolledText widget''')

        self.Scrolledtext1 = ScrolledText(self.TFrame2)
        self.Scrolledtext1.place(x=10, y=50, height=370, width=674)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(exportselection="0")
        self.Scrolledtext1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Scrolledtext1.configure(highlightbackground="cornsilk4")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#d9d9d9")
        self.Scrolledtext1.configure(wrap="none")

        self.TLabel5 = ttk.Label(self.TNotebook1_t4)
        self.TLabel5.place(x=20, y=20, height=59, width=64)
        self.TLabel5.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        photo_location = os.path.join(_location,"./graphics/ChubbyOwlLogo60.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.TLabel5.configure(image=_img2)
        self.TLabel5.configure(compound='none')

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t4)
        self.TSeparator1.place(x=120, y=71, width=780)

        self.TLabel3 = ttk.Label(self.TNotebook1_t4)
        self.TLabel3.place(x=349, y=16, height=44, width=221)
        self.TLabel3.configure(font="-family {DejaVu Sans} -size 16 -weight bold -slant italic")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='center')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''ABOUT''')
        self.TLabel3.configure(compound='left')

        self.Message1 = tk.Message(self.TNotebook1_t4)
        self.Message1.place(x=20, y=100, height=364, width=885)
        self.Message1.configure(anchor='n')
        self.Message1.configure(background="cornsilk4")
        self.Message1.configure(borderwidth="3")
        self.Message1.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.Message1.configure(highlightbackground="cornsilk4")
        self.Message1.configure(justify='center')
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(relief="ridge")
        self.Message1.configure(text='''This program was written by Gregory Walters.

Copyright © 2023, 2024 by Gregory Walters

This program is licensed under the MIT license (see license.txt)''')
        self.Message1.configure(width=885)

        self.TComboThemes = ttk.Combobox(self.top)
        self.TComboThemes.place(x=336, y=32, height=24, width=200)
        self.TComboThemes.configure(exportselection="0")
        self.TComboThemes.configure(font="-family {DejaVu Sans} -size 10")
        self.TComboThemes.configure(textvariable=self.comboThemes)

    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [225, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

    def __adjust_sash1(self, event):
        paned = event.widget
        pos = [125, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid1)
        del self.__funcid1

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    PAGE80Demo_support.main()

if __name__ == '__main__':
    PAGE80Demo_support.main()



