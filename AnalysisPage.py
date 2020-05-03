from tkinter import *
from Page import Page
import Fonts
import r2pipe


def controlsFrame(dPOIViewFrame):
    cframe = Frame(dPOIViewFrame)
    cframe.pack(fill=X, padx=10, pady=10, expand=FALSE)

    pluginLbl = Label(cframe, text="Plugin: ")
    pluginLbl.grid(row=1, column=0, sticky=E)

    pluginValue = StringVar()
    pluginValue.set("")

    pluginChoices = {"Network", "Encryption"}

    pluginMenu = OptionMenu(cframe, pluginValue, *pluginChoices)
    pluginMenu.grid(row=1, column=1)
    pluginMenu.configure(width=10)

    poiTypeLbl = Label(cframe, text="Point of Interest Type: ")
    poiTypeLbl.grid(row=2, column=0)

    poiValue = StringVar()
    poiValue.set("")

    networkChoices = {"Variable", "String", "DLL", "Function", "Packet Protocol", "Data Structure"}

    poiTypeMenu = OptionMenu(cframe, poiValue, *networkChoices)
    poiTypeMenu.grid(row=2, column=1)
    poiTypeMenu.configure(width=10)


def runStaticAnalysis():
    temp = viewImports("bin/./ping", "network")
    poiText.insert(INSERT, temp)


def viewImports(file, plugin=None):
    r2 = r2pipe.open(file)
    return r2.cmd("pd")


class AnalysisPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(fill=BOTH, expand=TRUE, padx=7, pady=5)

        controlsFrame(container)

        # ----------- LEFT-SIDE POINTS OF INTEREST VIEW FRAME -----------
        poiViewFrame = Frame(container, height=1, bd=2, relief=RIDGE)
        poiViewFrame.pack(side=LEFT, fill=Y, padx=1)

        projectsFrame = Frame(poiViewFrame)
        projectsFrame.pack(side=TOP, fill=Y)

        titleLabel = Label(projectsFrame, text="Point of Interest View", fg="white", bg="RoyalBlue4", font=Fonts.LARGE_FONT)
        titleLabel.grid(row=0, column=0, sticky=NSEW)

        # The following adds checkboxes for selecting points of interest
        poi1 = IntVar()
        Checkbutton(projectsFrame, text="Point of Interest A", variable=poi1).grid(row=2, column=0, sticky=NSEW)
        # ----------- END OF POINTS OF INTEREST VIEW FRAME -----------

        # ----------- DETAILED POINTS OF INTEREST VIEW FRAME -----------
        detailedPOIFrame = Frame(container, bd=2, relief=RIDGE)
        detailedPOIFrame.pack(fill=BOTH, expand=TRUE, padx=1)

        dPV_Title = Label(detailedPOIFrame, text="Detailed Points Of Interest View", fg="white", bg="RoyalBlue4",
                          font=Fonts.LARGE_FONT)
        dPV_Title.pack(side=TOP, fill=X)

        mainFrame = Frame(detailedPOIFrame, bd=2)
        mainFrame.pack(fill=BOTH, expand=TRUE)

        # bottomFrame = Frame(detailedPOIFrame, bd=2, relief=RIDGE)
        # bottomFrame.pack(side=BOTTOM, fill=X)

        # middleFrame.grid_columnconfigure(0, weight=3)

        global poiText
        poiText = Text(mainFrame)
        poiText.pack(fill=BOTH, expand=TRUE)
        # poiText.grid(row=0)
        poiText.bind("<Key>", "ignore")

        # analysisText = Tk()
        # scrollBar = Scrollbar(analysisText)
        # pageText = Text(analysisText, height=4, width=50)
        # S.pack(side=tk.RIGHT, fill=tk.Y)
        # T.pack(side=tk.LEFT, fill=tk.Y)
        # S.config(command=T.yview)
        # T.config(yscrollcommand=S.set)

        # pageText.insert(END, text)

        # bottomFrame.grid_columnconfigure(0, weight=3)

        # bottomLabel = Label(bottomFrame, text="Point of Interest Area")
        # bottomLabel.grid(row=0)
        # ----------- END OF DETAILED POINTS OF INTEREST VIEW FRAME -----------