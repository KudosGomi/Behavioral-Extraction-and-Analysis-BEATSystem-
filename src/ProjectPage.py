from tkinter import *
from tkinter import filedialog
from Page import Page
import Fonts
import r2pipe


def addNewProjectLabel(projectName):
    label = Label(savedProjectsFrame, text=projectName)
    label.pack()


def newProjectFrame(root):
    npF = Toplevel(root)
    npF.grab_set()
    npF.lift(aboveThis=root)
    # npF.wm_attributes("-topmost", 1)
    npF.wm_title("New Project")

    width = 410
    height = 124
    x = (root.winfo_screenwidth() / 2) - (width / 2)
    y = (root.winfo_screenheight() / 2) - (height / 2)
    npF.geometry("%dx%d+%d+%d" % (width, height, x, y))
    npF.resizable(FALSE, FALSE)

    npF.grid_rowconfigure(2, weight=1)

    prjNameLbl = Label(npF, text="Project Name: ", font=Fonts.NORM_FONT)
    prjNameLbl.grid(row=0, column=0, padx=5, sticky=E)

    nameEntry = Entry(npF)
    nameEntry.grid(row=0, column=1)

    binaryFilePathLbl = Label(npF, text="x86 Binary File: ", font=Fonts.NORM_FONT)
    binaryFilePathLbl.grid(row=1, column=0, padx=5)

    filename = StringVar()
    binaryFileEntry = Entry(npF, textvariable=filename)
    binaryFileEntry.grid(row=1, column=1)

    def browse_file():
        file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=((("Executables", "/*"), ("ALL FILES", ".*"))))
        filename.set(file)

    browseBtn = Button(npF, text="Browse...", font=Fonts.BUTTON_FONT, command=browse_file)
    browseBtn.grid(row=1, column=2)

    def createNewProject(projectName, binaryPathFile):
        npF.destroy()
        # temp = viewImports(binaryPathFile, "network")
        # str = StringVar()
        # for a in temp:
        #     # str = StringVar()
        #     str.set(a + " ")
        # print(temp)
        prjName.set(projectName)
        setBinaryPath.set(binaryPathFile)
        # binaryFilePropertiesText.insert(INSERT, temp)

    def p(event):
        print("ok")

    createBtn = Button(npF, text="Create", font=Fonts.BUTTON_BOLD_FONT, highlightcolor="blue",
                       command=lambda: createNewProject(nameEntry.get(), binaryFileEntry.get()))
    createBtn.grid(row=2, column=2, pady=10, sticky=S)
    npF.update_idletasks()
    npF.bind("<Return>", lambda event: createNewProject(nameEntry.get(), binaryFileEntry.get()))


    cancelBtn = Button(npF, text="Cancel", font=Fonts.BUTTON_BOLD_FONT, command=npF.destroy)
    cancelBtn.grid(row=2, column=1, pady=10, sticky=SE)


def viewImports(file, plugin=None):
    r2 = r2pipe.open(file)
    return r2.cmd("pd")
    # global rlocal
    # r2 = r2pipe.open("/bin/./ping")
    # r2 = r2pipe.open('./ping') # Open ping in Radare2
    # r2 = r2pipe.open('./ping', flags=['-2'])
    # r2.cmd('doo; db main; dc')
    # print(r2.cmd("doo"))
    # print(r2.cmd("db main"))
    # print(r2.cmd("dc"))
    # reg = r2.cmdj("drj")["rax"]
    # print(reg)
    # print(r2.cmd("dr eax"))
    # print(r2.cmd('aa'))
    # print(r2.cmd("afl"))
    # print(r2.cmdj("aflj"))
    # print(r2.cmd("aaa"))
    # return r2.cmd("pd")
    # return r2.cmd("pdf")
    # r2.cmd(".aab")
    # r2.cmd("aaa")
    # functions = r2.cmd("aflj")
    # if functions:
    #     functionList = json_out.loads(functions)
    # else:
    #     functionList = []
    # return functionList
    # strs = r2.cmd("iij") # Grab all imports used by binary in json format and returns an object
    # if plugin == None: #If no plugin specified, output all imports
    #     return strs
    # else:
    #     temp = []
    #     pluginMap = pluginRead(plugin)
    #     for a in strs:
    #         if a['name'] in pluginMap.keys():
    #             temp.append(a)
    #     return temp


class ProjectPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(fill=BOTH, expand=TRUE, padx=7, pady=5)

        # ----------- LEFT-SIDE PROJECTS VIEW FRAME -----------
        projectViewFrame = Frame(container, height=1, bd=2, relief=RIDGE)
        projectViewFrame.pack(side=LEFT, fill=Y, padx=1, expand=FALSE)

        global savedProjectsFrame
        savedProjectsFrame = Frame(projectViewFrame)
        savedProjectsFrame.pack(fill=X)

        newBtnFrame = Frame(projectViewFrame)
        newBtnFrame.pack(side=BOTTOM, fill=Y)

        pV_Title = Label(savedProjectsFrame, text="Project View", fg="white", bg="RoyalBlue4", font=Fonts.LARGE_FONT)
        pV_Title.pack(fill=X)

        newProjectBtn = Button(newBtnFrame, text="New Project +", width=11, font=Fonts.BUTTON_FONT,
                               command=lambda: newProjectFrame(container))
        newProjectBtn.pack(side=BOTTOM, padx=5, pady=5)
        # ----------- END OF LEFT-SIDE PROJECTS VIEW FRAME -----------

        # ----------- DETAILED PROJECT VIEW FRAME -----------
        detailedProjectViewFrame = Frame(container, bd=2, relief=RIDGE)
        detailedProjectViewFrame.pack(fill=BOTH, expand=TRUE, padx=1)

        dPV_Title = Label(detailedProjectViewFrame, text="Detailed Project View", fg="white", bg="RoyalBlue4",
                          font=Fonts.LARGE_FONT)
        dPV_Title.pack(side=TOP, fill=X)

        mainFrame = Frame(detailedProjectViewFrame)
        mainFrame.pack(fill=BOTH, padx=10, pady=5, expand=TRUE)
        mainFrame.grid_columnconfigure(0, weight=0)
        mainFrame.grid_columnconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(2, weight=1)

        projectNameLabel = Label(mainFrame, text="Project Name:", font=Fonts.NORM_FONT)
        projectNameLabel.grid(row=0, sticky=E)

        global prjName
        prjName = StringVar()
        projectNameEntry = Entry(mainFrame, text=prjName, fg="gray40", bd=3, selectbackground="white", relief=RIDGE,
                                 justify="center", font=Fonts.NORM_BOLD_FONT)
        projectNameEntry.grid(row=0, column=1, sticky=NSEW)
        projectNameEntry.bind("<Key>", "ignore")

        binaryPathLabel = Label(mainFrame, text="Binary File Path:", font=Fonts.NORM_FONT)
        binaryPathLabel.grid(row=1, sticky=E)

        global setBinaryPath
        setBinaryPath = StringVar()
        binaryPathEntry = Entry(mainFrame, text=setBinaryPath, fg="gray40", bd=3, relief=RAISED, justify="center",
                                font=Fonts.NORM_BOLD_FONT)
        binaryPathEntry.grid(row=1, column=1, sticky=NSEW)
        binaryPathEntry.bind("<Key>", "ignore")

        projectDescrpLabel = Label(mainFrame, text="Project Description:", font=Fonts.NORM_FONT)
        projectDescrpLabel.grid(row=2, sticky=E)

        def selectAll(event):
            # event.widget.select_range(0, 'end')
            # event.widget.icursor('end')
            projectDescrpText.tag_add(SEL, "1.0", END)
            projectDescrpText.mark_set(INSERT, "1.0")
            projectDescrpText.see(INSERT)
            return 'break'

        global projectDescrpText
        projectDescrpText = Text(mainFrame, height=10, font=Fonts.NORM_BOLD_FONT, fg="grey40", relief=RAISED, bd=3)
        projectDescrpText.grid(row=2, column=1, sticky=NSEW)
        projectDescrpText.bind("<Control-KeyRelease-a>", selectAll)

        # global binaryBrowseBtn
        # binaryBrowseBtn = Button(mainFrame, text="Browse...", width=8, bg="white", fg="Black", font=Fonts.BUTTON_FONT)
        # binaryBrowseBtn.grid(row=2, column=3, padx=10)

        binaryFileProperties = Label(mainFrame, text="Binary File Properties:", font=Fonts.NORM_FONT)
        binaryFileProperties.grid(row=3, sticky=E)

        global binaryFilePropertiesText
        binaryFilePropertiesText = Text(mainFrame, font=Fonts.NORM_BOLD_FONT, fg="grey40", height=10, relief=RAISED,
                                        borderwidth=2)
        binaryFilePropertiesText.grid(row=3, column=1, sticky=NSEW)
        binaryFilePropertiesText.bind("<Key>", "ignore")

        btnsFrame = Frame(detailedProjectViewFrame)
        btnsFrame.pack(side=BOTTOM, fill=BOTH, pady=10, expand=FALSE)
        btnsFrame.grid_columnconfigure(0, weight=3)

        deleteBtn = Button(btnsFrame, text="Delete", width=10, bg="white", font=Fonts.BUTTON_FONT)
        deleteBtn.grid(row=4, column=3, sticky=E, padx=10)

        def saveProject():
            addNewProjectLabel(prjName.get())

        saveBtn = Button(btnsFrame, text="Save", width=10, bg="white", highlightcolor="blue", font=Fonts.BUTTON_FONT, command=saveProject)
        saveBtn.grid(row=5, column=3, sticky=E, padx=10)
        # ----------- END OF DETAILED PROJECT VIEW FRAME -----------