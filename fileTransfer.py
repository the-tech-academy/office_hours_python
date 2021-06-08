#Importing different modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import shutil
import os

#Creating class for GUI
class fileTransfer( Frame ):
    def __init__( self ):
        self.root = Tk()
        #Creating GUI Design including labels, "Browse" buttons to locate files, entry widgets to store file paths, and a "Check Files" button that transfers the files
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("File Transfer")
        self.top = Label(self, text = "Locate the files source")
        self.top.grid(column = 2, row = 0, sticky=W)
        self.top = Label(self, text = "Locate the files Destination")
        self.top.grid(column = 2, row = 2, sticky=W)
        self.button1 = Button( self, text = "Browse", width = 15,
                               command = self.LocateSource)
        self.button1.grid( row = 1, column = 0, columnspan = 1, pady=(5,5), padx=(5,0))
        self.button2 = Button( self, text = "Browse", width = 15,
                               command = self.LocateDestination)
        self.button2.grid( row = 3, column = 0, columnspan = 1, pady=(5,5), padx=(5,0))
        self.button3 = Button( self, text = "Check for Files", width = 15, height = 3,
                               command = self.CheckFiles)
        self.button3.grid( row = 4, column = 0, columnspan = 1, pady=(5,5), padx=(5,0))
        self.button4 = Button( self, text = "Quit", width = 15, height = 3,
                               command = self.root.destroy)
        self.button4.grid( row = 4, column = 3, columnspan = 1, pady=(5,5), padx=(5,0))
    
        self.E1 = Entry(self, width=50)
        self.E1.grid( row = 1, column = 1, columnspan = 3, padx=(10,10),pady=(10,10))
        self.E2 = Entry(self, width=50)
        self.E2.grid( row = 3, column = 1, columnspan = 3, padx=(10,10),pady=(10,10))

        #Creating the function for each "Browse" button to set the entry widgets with the selected file directory
    def LocateSource(self):
        source = tkinter.filedialog.askdirectory()
        self.E1.insert(0, source)
        pass
    def LocateDestination(self):
        dest= tkinter.filedialog.askdirectory()
        self.E2.insert(0, dest)
        pass

        #Move all files in the selected source to the selected directory
    def CheckFiles(self):
        source = self.E1.get()
        dest = self.E2.get()
        files = os.listdir(source)
        for i in files:
            shutil.move(source+i,dest)

        pass
def main():
    fileTransfer().mainloop()
if __name__ == '__main__':
    main()
