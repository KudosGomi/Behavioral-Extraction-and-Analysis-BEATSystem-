from tkinter import *
from Page import Page

BUTTON_FONT = 'Helvetica 18 bold'
LARGE_FONT = 'Helvetica 14 bold'
NORM_BOLD_FONT = 'Helvetica 12 bold'
NORM_FONT = 'Helvetica 12'
SMALL_FONT = 'Helvetica 8 bold'

class PluginManagementPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        container = Frame(self, bg="white")
        container.pack(fill=BOTH, expand=TRUE)

        pluginViewFrame = Frame(container, bd=2, relief=RIDGE)
        pluginViewFrame.pack(side=LEFT, fill=Y, expand=FALSE, padx=2)

        pluginsFrame = Frame(pluginViewFrame)
        pluginsFrame.pack(fill=Y)
        newPluginBtnFrame = Frame(pluginViewFrame)
        newPluginBtnFrame.pack(side=BOTTOM, fill=Y, pady=2)

        pvLabel = Label(pluginsFrame, text="Plugin View", bg="SteelBlue1", font=LARGE_FONT)
        pvLabel.grid(row=0, column=0, sticky=NSEW)

        searchPluginEntryText = StringVar()
        searchPluginEntryText.set("Search Plugin")
        # This method clears the text inside search box, uses the above 2 variables ^^^
        #        def searchEntryClicked(event):
        #
        #            event.widget.delete(0, END)

        searchPluginEntry = Entry(pluginsFrame, textvariable=searchPluginEntryText, fg="gray60", justify="center",
                                  bd=2, relief="ridge")
        # searchProjectEntry.bind("<Button-1>", searchEntryClicked)
        # mag = PhotoImage(file = "mag.jpg")
        # searchPluginEntry.image = PhotoImage(image = mag)
        searchPluginEntry.grid(row=1, padx=5, pady=4, sticky=W)
        # imgLbl = Label(pluginsFrame, image=mag)
        # imgLbl.grid(row=1, column=1, sticky=E)

        projectALabel = Button(pluginsFrame, text="Plugin A", bd=0)
        projectALabel.grid(row=2, column=0, padx=15, sticky=NSEW)
        projectBLabel = Button(pluginsFrame, text="Plugin B", bd=0)
        projectBLabel.grid(row=3, column=0, padx=15, sticky=NSEW)
        projectCLabel = Button(pluginsFrame, text="Plugin C", bd=0)
        projectCLabel.grid(row=4, column=0, padx=15, sticky=NSEW)
        projectDotLabel = Button(pluginsFrame, text="...", bd=0)
        projectDotLabel.grid(row=5, column=0, padx=15, sticky=NSEW)
        projectXLabel = Button(pluginsFrame, text="Plugin X", bd=0)
        projectXLabel.grid(row=6, column=0, padx=15, sticky=NSEW)

        newPluginBtn = Button(newPluginBtnFrame, text="New Plugin +", width=11, bg="white", fg="Black")
        newPluginBtn.grid(sticky=SE)
        # ----------- END OF PLUGINS VIEW FRAME -----------

        # ----------- DETAILED PLUGIN VIEW FRAME -----------
        detailedPluginViewFrame = Frame(container, bd=2, relief=RIDGE)
        detailedPluginViewFrame.pack(fill=BOTH, expand=TRUE, padx=2)

        titleFrame = Frame(detailedPluginViewFrame)
        titleFrame.pack(side=TOP, fill=X)

        dpvLabel = Label(detailedPluginViewFrame, text="Detailed Plugin View", bg="SteelBlue1", font=LARGE_FONT)
        dpvLabel.pack(fill=X)

        middleFrame = Frame(detailedPluginViewFrame)
        middleFrame.pack(fill=BOTH, pady=5)

        middleFrame.grid_columnconfigure(0, weight=0)
        middleFrame.grid_columnconfigure(1, weight=1)
        middleFrame.grid_columnconfigure(2, weight=0)

        pluginStructureLabel = Label(middleFrame, text="Plugin Structure:", font=NORM_FONT)
        pluginStructureLabel.grid(row=0, sticky=E, padx=10)

        pluginStructureEntry = Entry(middleFrame, fg="gray60", bd=3, relief="raised", justify="center")
        pluginStructureEntry.grid(row=0, column=1, sticky=NSEW)

        pluginStructureBrowseBtn = Button(middleFrame, text="Browse..", width=8, bg="white", fg="Black")
        pluginStructureBrowseBtn.grid(row=0, column=3, padx=10)

        pluginDataSetLabel = Label(middleFrame, text="Plugin Predefined Data Set:", font='Helvetica 12')
        pluginDataSetLabel.grid(row=1, sticky=E, padx=10)

        pluginDataSetLabel = Entry(middleFrame, fg="gray60", bd=3, relief="raised", justify="center")
        pluginDataSetLabel.grid(row=1, column=1, sticky=NSEW)

        pluginStructureBrowseBtn = Button(middleFrame, text="Browse..", width=8, bg="white", fg="Black")
        pluginStructureBrowseBtn.grid(row=1, column=3, padx=10)

        pluginName = Label(middleFrame, text="Plugin Name:", font='Helvetica 12')
        pluginName.grid(row=2, sticky=E, padx=10)

        pluginName = Entry(middleFrame, fg="gray60", bd=3, relief="raised", justify="center")
        pluginName.grid(row=2, column=1, sticky=NSEW)

        pluginDescrpLabel = Label(middleFrame, text="Plugin Description:", font='Helvetica 12')
        pluginDescrpLabel.grid(row=3, sticky=E)

        pluginDescrpText = Text(middleFrame, height=7, relief=RAISED, borderwidth=2)
        pluginDescrpText.grid(row=3, column=1, sticky=NSEW)

        plugintkvar = StringVar(self)
        choices = {""}

        pluginMenu = OptionMenu(middleFrame, plugintkvar, *choices)
        Label(middleFrame, text="Default Output Field: ", font='Helvetica 12').grid(row=4, sticky=E)
        pluginMenu.grid(row=4, column=1, sticky=NSEW)

        pointsOfInterestLabel = Label(middleFrame, text="Points of Interest:", font='Helvetica 12')
        pointsOfInterestLabel.grid(row=5, sticky=E)

        pointsOfInterestText = Text(middleFrame, height=7, relief=RAISED, borderwidth=2)
        pointsOfInterestText.grid(row=5, column=1, sticky=NSEW)

        deleteBtn = Button(middleFrame, text="Delete", width=10, bg="white", fg="Black")
        deleteBtn.grid(row=6, column=0, padx=10)

        saveBtn = Button(middleFrame, text="Save", width=10, bg="white", fg="Black")
        saveBtn.grid(row=6, column=3, padx=10)