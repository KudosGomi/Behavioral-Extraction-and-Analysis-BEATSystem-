from tkinter import *
from Page import Page

BUTTON_FONT = 'Helvetica 18 bold'
LARGE_FONT = 'Helvetica 14 bold'
NORM_BOLD_FONT = 'Helvetica 12 bold'
NORM_FONT = 'Helvetica 12'
SMALL_FONT = 'Helvetica 8 bold'

class DocumentationPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # ----------- OPTIONS-TOP FRAME -----------
        optsBar = Frame(self, relief=RIDGE)
        optsBar.pack(side=TOP, fill=X, padx=2, pady=2)

        plugintkvar = StringVar(self)

        # Dictionary with options
        choices = {'Network'}

        # on change dropdown value
        #    def change_plugin_dropdown(*args):
        #        print(plugintkvar.get())

        # link function to change dropdown
        #        plugintkvar.trace('w', change_plugin_dropdown)

        whitSpcLabel = Label(optsBar, text="       ")
        whitSpcLabel.grid(row=2, column=3, sticky=NSEW)

        poitypetkvar = StringVar(self)

        # on change dropdown value
        #    def change_poi_dropdown(*args):
        #        print(poitypetkvar.get())

        # link function to change dropdown
        #        plugintkvar.trace('w', change_poi_dropdown)
        # ----------- END OF OPTIONS-TOP FRAME -----------

        # ----------- LEFT-SIDE POINTS OF INTEREST VIEW FRAME -----------

        # Main Frame for the left-hand side
        poiViewFrame = Frame(self, height=1, bd=2, relief=RIDGE)

        # Both of these frames below go within the poiViewFrame
        projectsFrame = Frame(poiViewFrame)

        titleLabel = Label(projectsFrame, text="Detailed Documented View", bg="SteelBlue1")
        titleLabel.grid(row=0, column=0, sticky=NSEW)

        searchPOIEntryText = StringVar()
        searchPOIEntryText.set("Search Document..")
        # This method clears the text inside search box, uses the above 2 variables ^^^
        #    def searchEntryClicked(event):
        #
        #        event.widget.delete(0, END)

        searchPOIEntry = Entry(projectsFrame, textvariable=searchPOIEntryText, fg="gray60", justify="center", bd=2,
                               relief="ridge")
        #        searchPOIEntry.bind("<Button-1>", searchEntryClicked)
        searchPOIEntry.grid(row=1, sticky=NSEW)

        projectDotLabel = Label(projectsFrame, text="BEAT Documentation")
        projectDotLabel.grid(row=2, column=0, sticky=NSEW)

        projectDotLabel2 = Label(projectsFrame, text="Plugin Structure")
        projectDotLabel2.grid(row=3, column=0, sticky=NSEW)

        projectsFrame.pack(side=TOP, fill=Y)
        poiViewFrame.pack(side=LEFT, fill=Y, padx=10, pady=5)
        # ----------- END OF POINTS OF INTEREST VIEW FRAME -----------

        # ----------- DETAILED POINTS OF INTEREST VIEW FRAME -----------
        # Made 3 panles/frames
        detailedProjectViewFrame = Frame(self, bd=2, relief=RIDGE)
        titleFrame = Frame(detailedProjectViewFrame)
        middleFrame = Frame(detailedProjectViewFrame, height=200, bd=2, relief=RIDGE)

        dPV_Title = Label(titleFrame, text="Detailed Documented View", bg="SteelBlue1", )
        dPV_Title.pack(fill=X)

        # Add weight/more space to columns for the grid layout
        middleFrame.grid_columnconfigure(0, weight=3)

        middleLabel = Label(middleFrame, text="Documented View")
        middleLabel.grid(row=0)

        # ----------- END OF DETAILED POINTS OF INTEREST VIEW FRAME -----------

        titleFrame.pack(side=TOP, fill=X)
        middleFrame.pack(fill=X)
        detailedProjectViewFrame.pack(fill=BOTH, expand=TRUE, padx=2, pady=2)