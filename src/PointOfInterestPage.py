from tkinter import *
import Fonts
from Page import Page


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


class PointOfInterestPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(fill=BOTH, expand=TRUE, padx=7, pady=5)

        # ----------- LEFT-SIDE POINTS OF INTEREST VIEW FRAME -----------
        poiViewFrame = Frame(container, height=1, bd=2, relief=RIDGE)
        poiViewFrame.pack(side=LEFT, fill=Y, padx=1, expand=FALSE)

        poisFrame = Frame(poiViewFrame)
        poisFrame.pack(fill=X)

        newBtnFrame = Frame(poiViewFrame)
        newBtnFrame.pack(side=BOTTOM, fill=Y)

        poiV_Title = Label(poisFrame, text="Point of Interest View", font=Fonts.LARGE_FONT, fg="white", bg="RoyalBlue4")
        poiV_Title.pack(fill=X)

        # poi1 = IntVar()
        # Checkbutton(poisFrame, text="Point of Interest A", variable=poi1).grid(row=2, column=0, sticky=NSEW)
        # poi2 = IntVar()
        # Checkbutton(poisFrame, text="Point of Interest B", variable=poi2).grid(row=3, column=0, sticky=NSEW)
        # poi3 = IntVar()
        # Checkbutton(poisFrame, text="Point of Interest C", variable=poi3).grid(row=4, column=0, sticky=NSEW)
        # projectDotLabel = Label(poisFrame, text="...")
        # projectDotLabel.grid(row=5, column=0, sticky=NSEW)
        # poix = IntVar()
        # Checkbutton(poisFrame, text="Point of Interest X", variable=poix).grid(row=9, column=0, sticky=NSEW)
        # newPluginBtn = Button(newBtnFrame, text="New PoI", width=11, bg="white", fg="Black")
        # newPluginBtn.grid(sticky=SE)
        # ----------- END OF LEFT-SIDE POINTS OF INTEREST VIEW FRAME -----------

        # ----------- DETAILED POINTS OF INTEREST VIEW FRAME -----------
        detailedPOIViewFrame = Frame(container, bd=2, relief=RIDGE)
        detailedPOIViewFrame.pack(fill=BOTH, expand=TRUE, padx=1)

        dPOI_Titlte = Label(detailedPOIViewFrame, text="Detailed Point of Interest View", fg="white", bg="RoyalBlue4",
                            font=Fonts.LARGE_FONT)
        dPOI_Titlte.pack(side=TOP, fill=X)

        controlsFrame(detailedPOIViewFrame)

        poiXMLFrame = Frame(detailedPOIViewFrame, relief=RIDGE, bd=2)
        poiXMLFrame.pack(fill=BOTH, padx=10, pady=5, expand=TRUE)

        global poiXMLArea
        poiXMLText = Text(poiXMLFrame, height=10, font=Fonts.NORM_FONT, fg="grey40")
        poiXMLText.pack(fill=BOTH, expand=TRUE)
        poiXMLText.bind("<Key>", "ignore")

        btnsFrame = Frame(detailedPOIViewFrame)
        btnsFrame.pack(side=BOTTOM, fill=BOTH, pady=10, expand=FALSE)
        btnsFrame.grid_columnconfigure(0, weight=2)

        deleteBtn = Button(btnsFrame, text="Delete", width=10, bg="white", font=Fonts.BUTTON_FONT)
        deleteBtn.grid(row=1, column=3, padx=10)

        saveBtn = Button(btnsFrame, text="Save", width=10, bg="white", highlightcolor="blue", font=Fonts.BUTTON_FONT)
        saveBtn.grid(row=2, column=3, padx=10)
        # ----------- END OF DETAILED POINTS OF INTEREST VIEW FRAME -----------