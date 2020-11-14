"""  
Menu Update

How to change menu1 to menu2 and vice versa without creating a second window?

Intially menu1 is loaded, its mode is Neutral, to change to Play mode, we
press Mode->Play which would bring us to menu2. Press Mode->Neutral to bring
us to initial Neutral mode again.

"""  

import PySimpleGUI as sg

# Constants
menu1 = [
        ['File', ['Quit']],
        ['Mode', ['Play']],
        ['Engine', ['Setting']]
]

menu2 = [
        ['File', ['Quit']],
        ['Mode', ['Neutral']],
        ['Help', ['How to Play']]
]

# Create variables for our elements. We will use this for updates.
menu_elem = sg.Menu(menu1)
txt_elem = sg.Text('Layout, mode = Neutral')

# Create layout for our elements
layout = [
        [menu_elem],
        [txt_elem],
]

w = sg.Window('Menu Update', layout)

while True:
    e, v = w.Read(timeout=100)
    
    # If Quit menu entry is pressed or X is pressed
    if e == 'Quit' or e is None:
        break
    
    # Change to Play mode, load menu2
    if e == 'Play':
        print('Hits Play')
        menu_elem.Update(menu2)
        txt_elem.Update('Layout, mode = Play')
        continue
        
    # Change to Neutral mode, load menu1
    if e == 'Neutral':
        print('Hits Neutral')
        menu_elem.Update(menu1)
        txt_elem.Update('Layout, mode = Neutral')

w.Close()