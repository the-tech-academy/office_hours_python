
#Importing different modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import webbrowser

#Creating class for GUI
class webGen( Frame ):
    def __init__( self ):
        #Creating GUI Design including labels, a text input, and a submission button
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Web Generator")
        self.top = Label(self, text = "Enter the desired HTML body below")
        self.top.grid(column = 2, row = 0)
        self.button1 = Button( self, text = "Generate Web Page", width = 15,
                               command = self.Generate)
        self.button1.grid( row = 2, column = 2, columnspan = 1, pady=(5,5))
    
        self.T1 = Text(self, height=20, width=60)
        self.T1.grid( row = 1, column = 1, columnspan = 3, padx=(10,10),pady=(10,10))
        self.scroll = tk.Scrollbar(self)
        self.T1.configure(yscrollcommand = self.scroll.set)
  
        self.scroll.config(command = self.T1.yview)
        self.scroll.grid(column=4, row=1, rowspan=2,  sticky=N+S+W)

        #Creating the function for the Submission button that creates/overwrites an "index.html" file and then opens it in the computers default browser
    def Generate(self):
        #Takes the input from the text widget
        Body = input = self.T1.get("1.0",END)
        f = open("index.html", "w")
        #Overwrites the HTML file altering the "Body" with the text input
        f.write('<!doctype html>\n<html lang="en">\n<head>\n    <meta charset="utf-8">\n    <title>Auto-Generated Web Page</title>\n   <meta name="description" content=">Auto-Generated Web Page">\n\
                <meta name="Josh" content="SitePoint">\n   </head>\n<body>\n' + Body + '\n</body>\n</html>')
        f.close()
        #Opens the generated html file in the default browser
        webbrowser.open("index.html", new=0, autoraise=True)
def main(): 
    webGen().mainloop()
if __name__ == '__main__':
    main()
