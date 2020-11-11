#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

df_xlsx = None
t1 = None
t2 = None

def long_function_thread( window ):
    global df_xlsx
    df_xlsx = pandas.ExcelFile( values[ "-FILE-" ] )
    window.write_event_value( '-THREAD DONE-', '' )

def long_function_thread2( window ):
    i = 0
    window[ '-PROG-' ].update_bar( 0, 0 )
    while ( t1.is_alive() ):
        window[ '-PROG-' ].update_bar( i, 100 )
        i = i + 1
        print ( i )
        if ( i == 99 ):
            i = 0
            window[ '-PROG-' ].update_bar( 0, 0 )
    window[ '-PROG-' ].update_bar( 100, 100 )

def long_function():
    global t1
    t1 = threading.Thread(target=long_function_thread, args=(window,), daemon=True)
    t1.name = 't1'
    t1.start()

def long_function2():
    global t2 
    t2 = threading.Thread(target=long_function_thread2, args=(window,), daemon=True)
    t2.name = 't2'
    t2.start()

layout = [
          [ sg.Output( size=( 60, 10 ) ) ],
          [ sg.Button( 'Go' ), sg.Button( 'Nothing' ), sg.Button( 'Exit' ) ],
          [ sg.Text( 'Browse to a file' ) ],
          [ sg.Input( key='-FILE-', visible=False, enable_events=True ), sg.FileBrowse() ],
          [ sg.Text( 'Work progress' ), sg.ProgressBar( 100, size=( 20, 20 ), orientation='h', key='-PROG-' ) ]
         ]

window = sg.Window( 'Window Title', layout )

while True:             # Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        print('About to go to call my long function')
        long_function()
        long_function2()
        print('Long function has returned from starting')

    elif event == '-THREAD DONE-':
        print('Your long operation completed')
        print ( df_xlsx.sheet_names )

    else:
        print(event, values)

window.close()