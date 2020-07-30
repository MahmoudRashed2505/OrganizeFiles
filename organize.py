import time
import os
from tkinter import Button, Tk, filedialog, messagebox
from tkinter.filedialog import askdirectory
import shutil

#Creating a Function that Classify the Files
def classify(extention):
    Videos = "avi mpg mpe mpeg asf wmv mov qt rm mp4 flv m4v webm ogv ogg mkv ts tsv".split()
    Audio = "mp3 wav wma mpa ram ra aac aif m4a tsa".split()
    Compressed = "zip rar r0* r1* arj gz sit sitx sea ace bz2 7z iso".split()
    Software = "exe msi".split()
    Documents = "doc pdf ppt pps docx pptx csv xlsx".split()
    Photos = "JPG PNG TIF JPEG GIF TIFF PSD EPS AI".lower().split()
    categories = {'Videos':Videos,'Audio':Audio,'Compressed':Compressed,"Software":Software,'Documents':Documents,'Photos':Photos}
    for cat,ext in categories.items():
        if extention in ext:
            return cat
    return "UnCategorized"

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
    folders = list()
    for file in files:
        if os.path.isdir(file) == True:
            folders.append(str(file))
    checkFolders(folders)
    categoryFolders = ['Videos','Music','Documents','Compressed','Software','UnCategorized']
    for file in files:
        if os.path.isfile(file) == True:
            filename = str(file)
            ext = filename.split('.')
            ext = ext[-1]
            cat = classify(ext)
            shutil.move(file,os.path.join(os.getcwd(),cat))
        if os.path.isdir(file) == True:
            if str(file) not in categoryFolders:
                shutil.move(file,os.path.join(os.getcwd(),'Folders'))
    popup()


def checkFolders(folders):
    if 'Folders' not in folders:
        os.mkdir('Folders')
    if 'Videos' not in folders:
        os.mkdir('Videos')
    if 'Music' not in folders:
        os.mkdir('Music')
    if 'Documents' not in folders:
        os.mkdir('Documents')
    if 'Software' not in folders:
        os.mkdir("Software")
    if 'Compressed' not in folders:
        os.mkdir('Compressed')
    if 'UnCategorized' not in folders:
        os.mkdir('UnCategorized')
    if 'Photos' not in folders:
        os.mkdir('Photos')

#Popup MSG Box after Complete organizing
def popup():
    messagebox.showinfo("Organizing Completed Successfuly !","Successfuly !")

#Creating new Form From Tkinter GUI
root = Tk()
root.title("Organize Your Files")

#Creating The Main and only Btn
organizeButton = Button(root, text="Choose a Folder To Organize !", padx=200,pady=200, command =getDirectory)
organizeButton.pack()

root.mainloop()


