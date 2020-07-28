import time
import os
from tkinter import Button, Tk, filedialog, messagebox
from tkinter.filedialog import askdirectory
import shutil

#Creating a Function that Classify the Files
def classify(file):
    pass

path = None
#Creating Btn Function
def getDirectory():
    global path
    path = askdirectory(title = 'Select Folder')
    organize(path)

#Create Function to Organize the files
def organize(path):
    os.chdir(path)
    files = os.listdir()

#Popup MSG Box after Complete organizing
def popup():
    messagebox.showinfo("Organizing Completed Successfuly !")

#Creating new Form From Tkinter GUI
root = Tk()
root.title("Organize Your Files")
#Creating The Main and only Btn
organizeButton = Button(root, text="Choose a Folder To Organize !", padx=200,pady=200, command =getDirectory)
organizeButton.pack()

root.mainloop()


