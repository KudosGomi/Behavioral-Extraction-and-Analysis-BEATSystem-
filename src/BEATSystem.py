from tkinter import *
import Fonts
from ProjectPage import ProjectPage
from AnalysisPage import AnalysisPage
from PluginManagementPage import PluginManagementPage
from PointOfInterestPage import PointOfInterestPage
from DocumentationPage import DocumentationPage


class Toolbar(Frame):
    def __init__(self, master):
        frame = Frame(master, bg="DarkOrange1")
        frame.pack(side=TOP, fill=X)

        projectBtn = Button(frame, text="Project", width=10, height=2, bg="white", fg="Black", bd=3,
                            relief=RAISED, font=Fonts.BUTTON_BOLD_FONT, command=p1.lift)
        projectBtn.pack(side=LEFT, padx=10, pady=10)

        pluginManagementBtn = Button(frame, text="Plugin Management", width=17, height=2, bg="white", fg="Black",
                                     bd=3,relief=RAISED, font=Fonts.BUTTON_BOLD_FONT, command=p2.lift)
        pluginManagementBtn.pack(side=LEFT, pady=10)

        poiBtn = Button(frame, text="Points of Interest", width=16, height=2, bg="white", fg="Black", bd=3,
                        relief=RAISED, font=Fonts.BUTTON_BOLD_FONT, command=p3.lift)
        poiBtn.pack(side=LEFT,  padx=10, pady=10)

        analysisBtn = Button(frame, text="Analysis", width=10, height=2, bg="white", fg="Black", bd=3, relief=RAISED,
                             font=Fonts.BUTTON_BOLD_FONT, command=p4.lift)
        analysisBtn.pack(side=LEFT, pady=10)

        documentBtn = Button(frame, text="Documentation", width=14, height=2, bg="white", fg="Black", bd=3,
                             relief=RAISED, font=Fonts.BUTTON_BOLD_FONT, command=p5.lift)
        documentBtn.pack(side=LEFT, padx=10, pady=10)


class MainView(Frame):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=TRUE)

        container = Frame(frame, bd=2, relief=RIDGE)
        container.pack(side=TOP, fill=BOTH, expand=TRUE, pady=0)

        label = Label(container, text="Select a Page to view", font=Fonts.NORM_BOLD_FONT, bd=4, relief=GROOVE)
        label.pack(fill=BOTH, expand=TRUE, padx=50, pady=50, anchor=CENTER)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


class TerminalCommand(Frame):
    def __init__(self, master):
        frame = Frame(master, bg="DarkOrange1")
        frame.pack(side=BOTTOM, fill=X, expand=FALSE)

        commandLineFrame = Frame(frame)
        commandLineFrame.pack(side=TOP, fill=X)

        terminalFrameLEFT = Frame(commandLineFrame, relief=SUNKEN)
        terminalFrameLEFT.pack(side=LEFT)

        pathFileText = Label(terminalFrameLEFT, text="BEAT:~ R2$")
        pathFileText.pack(padx=3)

        terminalFrameRIGHT = Frame(commandLineFrame)
        terminalFrameRIGHT.pack(fill=X, expand=FALSE)

        def executeCommand(event):
            commandLine.delete(0, END)

        def selectAll(event):
            event.widget.select_range(0, 'end')
            event.widget.icursor('end')

        commandLine = Entry(terminalFrameRIGHT)
        commandLine.pack(fill=X, expand=FALSE)
        commandLine.bind("<Return>", executeCommand)
        commandLine.bind("<Control-KeyRelease-a>", selectAll)

        messageTextFrame = Frame(frame)
        messageTextFrame.pack(side=BOTTOM, fill=X, expand=FALSE)

        displayText = Text(messageTextFrame, relief=RIDGE, bd=2, height=2, wrap=WORD, fg="green", bg="black")
        displayText.pack(fill=X)
        displayText.insert(INSERT, "COMMAND LINE: Messages or errors will be displayed here referring to the commands entered above.")
        displayText.configure(state=DISABLED)


root = Tk()
root.title("Behavior Extraction and Analysis Tool")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.minsize(824, 550)

p1 = ProjectPage(root)
p2 = PluginManagementPage(root)
p3 = PointOfInterestPage(root)
p4 = AnalysisPage(root)
p5 = DocumentationPage(root)

toolbar = Toolbar(root)
main = MainView(root)
terminal = TerminalCommand(root)

root.mainloop()
