from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import json
import os

Window = Tk()
Window.title("PvzModder V0.2")
Window.geometry('420x420')

def edit_byte_in_exe(file_path, address, new_value):
    # Convert hexadecimal address string to an integer
    address = int(address, 16)

    with open(file_path, 'rb') as file:
        # Read the entire file into a bytearray
        exe_data = bytearray(file.read())
        
    # Modify the byte at the specified address
    exe_data[address] = new_value

    with open(file_path, 'wb') as file:
        # Write the modified data back to the file
        file.write(exe_data)

JSONFile = 'Plants.Json'

def PlantsProps():
 global JSONFile
 script_dir = os.path.dirname(os.path.abspath(__file__))
 PlantsJSON = os.path.join(script_dir,JSONFile)
 ReadedJSON = open(PlantsJSON,'r')
 PlantsPropertys = json.load(ReadedJSON)
 return PlantsPropertys
 #for i in PlantsPropertys['peashooter']:
 # print(PlantsPropertys['peashooter'][i])
def Set(*args):
  global propsDrop
  global ValueEntery
  global plant
  global DoneButton
  global plantsDrop
  
  propsDrop.pack_forget()
  DoneButton.pack_forget()
  ValueEntery.pack_forget()
  
  newVal = int(ValueEntery.get())
  address = str(propsDrop.get())
  # Example usage without explicitly using 0x for new_value
  exe_file_path = PVZPath
  edit_byte_in_exe(exe_file_path, PlantsProps()[plant][address],newVal)
  print(newVal,address,PlantsProps()[plant][address])

advanced = False

def changeMode(*args):
 global JSONFile
 global propsDrop
 global plant
 global plantsDrop
 global plants
 if JSONFile == 'Plants.Json':
   JSONFile = 'Adv.Json'
 else:
   JSONFile = 'Plants.Json'
  
 print(JSONFile)
 plant = plantsDrop.get()
 props = []
 for i in PlantsProps()[plant]:
   props.append(i)
 propsDrop.values = props
 
 plants = []
 for i in PlantsProps():
  plants.append(i)
 plantsDrop.config(values=plants)
 plantsDrop
 print(plants)
 
def ShowPropsSetValue(event):
 global plant
 global plantsDrop
 global props
 global propsDrop
 global ValueEntery
 global DoneButton
 try:
     ValueEntery.pack_forget()
 except NameError:
   print('firstTime')
 try:
     DoneButton.pack_forget()
 except NameError:
   print('firstTime')
 ValueEntery = ttk.Entry(Window)
 ValueEntery.focus()
 ValueEntery.pack()
 DoneButton = ttk.Button(text='Set',master=Window,command=Set)
 DoneButton.pack()

def ShowProps(event):
 global plant
 global plantsDrop
 global props
 global propsDrop
 global JSONFile
 global advB
 try:
     propsDrop.pack_forget()
 except NameError:
   print('firstTime')
 try:
     advB.pack_forget()
 except NameError:
   print('firstTime')
   
 advB = ttk.Checkbutton(Window, text='Advanced',variable=JSONFile, onvalue='Adv.Json', offvalue='Plants.Json', command=changeMode)
 advB.pack()

 plant = plantsDrop.get()
 props = []
 for i in PlantsProps()[plant]:
   props.append(i)
  
 propsDrop = ttk.Combobox(values=props,master=Window)
 propsDrop.pack()

 propsDrop.bind("<<ComboboxSelected>>", ShowPropsSetValue)

PVZPath = ''

plants = []
for i in PlantsProps():
 plants.append(i)

plant = ''


def ChoosePlant():
  global plantsDrop
  global Plantclicked
  Plantclicked = StringVar()
  Plantclicked.set(plants[0])
  try:
     plantsDrop.pack_forget()
  except NameError:
   print('firstTime')

  plantsDrop = ttk.Combobox(values=plants,master=Window) 
  plantsDrop.pack()
  plantsDrop.bind("<<ComboboxSelected>>", ShowProps)

#propsDrop = OptionMenu(Window,plant,*plants) 
#propsDrop.pack() 

def select_file():
    global PVZPath
    filetypes = (
        ('Plants Vs Zombies', '*.exe'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    PVZPath = filename
    ChoosePlant()
   



# open button
open_button = ttk.Button(
    Window,
    text='Open a File',
    command=select_file
)
open_button.pack()



Window.mainloop()