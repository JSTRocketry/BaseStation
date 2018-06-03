from tkinter import filedialog
from tkinter import *
import serial
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

RocketDataType = ['GYRO','ACCEL','ORIENTATION','PRESSURE_HEIGHT']

class rocketData:
    type
    values = []
    timeStamp = 0

FlightData = []
gyroSyntax = ["GX:","GY:","GZ:","TS:"]
accelSyntax = ["AX:","AY:","AZ:","TS:"]

matplotlib.use('TkAgg')
window = Tk()

class UserInterface:
    mode = IntVar()
    def __init__(self, master):
        self.master = master
        self.master.title("BaseStation")
        self.master.geometry('800x800')
        self.addModeButtons()
        self.createGraph()

    def plotGraph(self):
        self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")
        self.canvas.show()
    def createGraph(self):

        self.frame = Frame(self.master)
        self.f = Figure( figsize=(10, 9), dpi=80 )
        self.ax0 = self.f.add_axes( (0.05, .05, .90, .90), axisbg=(.75,.75,.75), frameon=False)
        self.ax0.set_xlabel( 'Time (s)' )
        self.ax0.set_ylabel( 'Frequency (Hz)' )
        #self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")
        self.frame = Frame( self.master )
        self.frame.grid(column=0,row=1,columnspan=3)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.show()
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame )
        #self.toolbar.grid(column = 0, row = 2, columnspan=2)
        self.toolbar.update()

    def addModeButtons(self):
        self.openFileRadioButton = Radiobutton(self.master, text='Open File', value=1, variable=self.mode)
        self.radioRadioButton = Radiobutton(self.master, text='Radio', value=2, variable=self.mode)
        self.openFileRadioButton.grid(column=0,row=0)
        self.radioRadioButton.grid(column=1,row=0)
        self.openButton = Button(self.master, text='Open', command=self.handleOpen)
        self.openButton.grid(column=2,row=0)


    def openAndParseFile(self,fileName):
        f = open(fileName,'r')
        for line in f:
            #parse the line
            #add to the block
            self.parse(line)
        f.close()

    def handleOpen(self):
        if(self.mode.get() == 1):
            print("Openning File!")
            #self.filename = filedialog.askopenfilename(initialdir = "./",title = "Select file")
            self.filename = "/home/jeremy/programming/github/BaseStation/FDAT1.TXT"
            self.openAndParseFile(self.filename)
            print (self.filename)
        elif(self.mode.get() == 2):
            print("Using Radio")
        self.plotGraph()
        print("Plotted")

    def parseForList(self, line, syntaxList):
        #look through line for each member of syntaxList and return
        print()

    def parse(self,line):
        tempData = rocketData
        syntaxToLookFor = []
        if(line.find("GX")):
            tempData.type = RocketDataType[0]
            members = self.parseForList(line, gyroSyntax)
            print("Gyro Line")
        #print("Parsing!")

def main():
    gui = UserInterface(window)
    window.mainloop()


if __name__ == "__main__":
    main()
