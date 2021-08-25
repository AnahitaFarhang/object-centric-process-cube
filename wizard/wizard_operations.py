from tkinter import *
from tkinter import ttk
from wizard.wizard_UI import wizard_UI
from wizard.wizard_UI_single_dimension import wizard_UI_single_dimension
from output.eventlog import eventlog
from output.MVP_frequency import MVP_frequency
from output.MVP_performance import MVP_performance
from output.object_centric_petrinet import object_centric_petrinet

class wizard_operations():
    def __init__(self, root, cubeview_frame, cubeview_frame2, result_frame, result_frame2, result_canvas, result_canvas2,
                 cubesdic,df,obj_df):
        #overviewframe1
        self.dfccbx=[]; self.dfccbx2=[]
        self.root=root;self.result_canvas=result_canvas;
        self.cubeview_frame=cubeview_frame;self.df=df;self.obj_df=obj_df
        self.result_frame=result_frame
        for widget in self.cubeview_frame.winfo_children():
            widget.destroy()
        label = Label(self.cubeview_frame, text=""); label.grid(row=0,column=0)

        self.cubeaddress = Frame(self.cubeview_frame,
                                width=1000, height=100, bd=0)
        self.cubeaddress.grid(sticky=NW)

        labelcubes = Label(self.cubeaddress, text="Name:",font=('Helvetica', 8, 'bold')); labelcubes.grid(row=1,column=1)
        cubenames=list(cubesdic.keys());self.cubesdic=cubesdic

        self.combocubes = ttk.Combobox(self.cubeaddress, width=20, values=cubenames)
        self.combocubes.grid(row=1,column=2);
        self.combocubes.current(0)
        self.combocubes.bind("<<ComboboxSelected>>", self.callback)
        self.matlabel = Label(self.cubeaddress, text="Materialization:", font=('Helvetica', 8, 'bold'));
        self.matlabel.grid(row=1,column=3)
        self.combomat = ttk.Combobox(self.cubeaddress, width=20, values=['Existence', 'All'])
        self.combomat.grid(row=1, column=4)
        self.combomat.current(0)
        self.combomat.bind("<<ComboboxSelected>>", self.matcallback)
        self.keycube=self.combocubes.get()
        alldimensions=list((self.cubesdic[self.combocubes.get()][self.combomat.get()].keys()))

        dimensions=[]
        for dim in alldimensions:
            if len(dim)>2:
                if 'event' in dim or 'object' in dim:
                    dimensions.append(dim)
        labelrow = Label(self.cubeaddress, text="Dimension1:", font=('Helvetica', 8, 'bold')); labelrow.grid(row=2,column=1)
        self.comborow = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
        self.comborow.grid(row=2,column=2);
        self.comborow.bind("<<ComboboxSelected>>", self.rowcallback)
        labelcolumn = Label(self.cubeaddress, text="Dimension2:", font=('Helvetica', 8, 'bold')); labelcolumn.grid(row=2,column=3)
        self.combocolumn = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
        self.combocolumn.grid(row=2,column=4);
        labelrow = Label(self.cubeaddress, text=""); labelrow.grid(row=2,column=7)
        labelrow = Label(self.cubeaddress, text=""); labelrow.grid(row=3, column=0)

        self.combocolumn.bind("<<ComboboxSelected>>", self.columncallback)

        self.firstlistwidg = self.cubeview_frame.winfo_children()

        for item in self.firstlistwidg:
            if item.winfo_children():
                self.firstlistwidg.extend(item.winfo_children())

        self.result_canvas2=result_canvas2
        self.cubeview_frame2=cubeview_frame2;self.df=df;self.obj_df=obj_df
        self.result_frame2=result_frame2
        for widget in self.cubeview_frame2.winfo_children():
            widget.destroy()
        label2 = Label(self.cubeview_frame2, text=""); label2.grid(row=0,column=0)

        self.cubeaddress2 = Frame(self.cubeview_frame2,
                                width=1000, height=100, bd=0)
        self.cubeaddress2.grid(sticky=NW)

        labelcubes2 = Label(self.cubeaddress2, text="Name:",font=('Helvetica', 8, 'bold')); labelcubes2.grid(row=1,column=1)
        cubenames2=list(cubesdic.keys());self.cubesdic2=cubesdic
        self.combocubes2 = ttk.Combobox(self.cubeaddress2, width=20, values=cubenames2)
        self.combocubes2.grid(row=1,column=2);
        self.combocubes2.current(0)
        self.combocubes2.bind("<<ComboboxSelected>>", self.callback)
        self.matlabel2 = Label(self.cubeaddress2, text="Materialization:", font=('Helvetica', 8, 'bold'));
        self.matlabel2.grid(row=1,column=3)
        self.combomat2 = ttk.Combobox(self.cubeaddress2, width=20, values=["Existence", "All"])
        self.combomat2.grid(row=1, column=4)
        self.combomat2.current(0)
        self.combomat2.bind("<<ComboboxSelected>>", self.matcallback2)

        self.keycube2=self.combocubes2.get()
        alldimensions2=list((self.cubesdic[self.combocubes2.get()][self.combomat2.get()].keys()))
        dimensions2=[]
        for dim in alldimensions2:
            if len(dim)>2:
                if 'event' in dim or 'object' in dim:
                    dimensions2.append(dim)
        labelrow2 = Label(self.cubeaddress2, text="Dimension1:", font=('Helvetica', 8, 'bold')); labelrow2.grid(row=2,column=1)
        self.comborow2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
        self.comborow2.grid(row=2,column=2);
        self.comborow2.bind("<<ComboboxSelected>>", self.rowcallback2)

        labelcolumn2 = Label(self.cubeaddress2, text="Dimension2:", font=('Helvetica', 8, 'bold')); labelcolumn2.grid(row=2,column=3)
        self.combocolumn2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
        self.combocolumn2.grid(row=2,column=4);
        label = Label(self.cubeaddress2, text=""); label.grid(row=2,column=7)
        label = Label(self.cubeaddress2, text=""); label.grid(row=3, column=0)

        self.combocolumn2.bind("<<ComboboxSelected>>", self.columncallback2)
        self.firstlistwidg2 = self.cubeview_frame2.winfo_children()

        for item in self.firstlistwidg2:
            if item.winfo_children():
                self.firstlistwidg2.extend(item.winfo_children())

        showthemodeleventlog = Button(self.root, text="Compare the Event Logs", width=18,
                                      command=self.showtheeventlog);
        showthemodeleventlog.place(x=557, y=170)
        showthemodelfre = Button(self.root, text="Compare the MVPs (Fre)", width=18, command=self.showthemodelfre);
        showthemodelfre.place(x=557, y=200)
        showthemodelpre = Button(self.root, text="Compare the MVPs (Pre)", width=18, command=self.showthemodelpre);
        showthemodelpre.place(x=557, y=230)
        showthepetrinet = Button(self.root, text="Compare the Petri nets", width=18, command=self.showthepetrinet);
        showthepetrinet.place(x=557, y=260)



    def callback(self,eventObject):
        self.comborow.destroy();self.combocolumn.destroy()
        for i in self.cubesdic.keys():
            if (self.combocubes.get())==i:
                self.keycube=i
                alldimensions = list((self.cubesdic[i][self.combomat.get()].keys()))
                dimensions = []
                for dim in alldimensions:
                    if len(dim) > 2:
                        if 'event' in dim or 'object' in dim:
                            dimensions.append(dim)
        self.comborow = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
        self.comborow.grid(row=2, column=4);
        self.comborow.bind("<<ComboboxSelected>>", self.rowcallback)
        self.combocolumn = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
        self.combocolumn.grid(row=2, column=5);
        self.combocolumn.bind("<<ComboboxSelected>>", self.columncallback)

        self.firstlistwidg.append(self.combocolumn)
        self.firstlistwidg.append(self.comborow)



    def rowcallback(self,eventObject):
        tabletoshow=self.cubesdic[self.combocubes.get()][self.combomat.get()][self.comborow.get()]
        self.twoattcomp='00'
        self.combocolumn.destroy()
        for i in self.cubesdic.keys():
            if (self.combocubes.get()) == i:
                self.keycube = i
                alldimensions = list((self.cubesdic[i][self.combomat.get()].keys()))
                dimensions = []
                for dim in alldimensions:
                    if len(dim) > 2:
                        if 'event' in dim or 'object' in dim:
                            dimensions.append(dim)
        self.combocolumn = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
        self.combocolumn.grid(row=2, column=4);
        self.combocolumn.bind("<<ComboboxSelected>>", self.columncallback)

        self.firstlistwidg.append(self.combocolumn)
        self.dfccbx = wizard_UI_single_dimension(self.root, self.cubeview_frame,
                                                     self.result_frame, self.result_canvas, tabletoshow,
                                                     self.firstlistwidg, self.keycube,
                                                     self.df,self.obj_df,self.comborow.get())

    def columncallback(self,eventObject):
        tabletoshow=self.cubesdic[self.combocubes.get()][self.combomat.get()][(self.comborow.get(),self.combocolumn.get())]
        self.twoattcomp='10'
        self.dfccbx=wizard_UI(self.root,self.cubeview_frame,self.result_frame, self.result_canvas, tabletoshow,self.firstlistwidg,self.keycube
                                           ,self.df,self.obj_df,self.comborow.get(),self.combocolumn.get())


    def matcallback(self,eventObject):
        if self.combocolumn.get() == "":
            tabletoshow = self.cubesdic[self.combocubes.get()][self.combomat.get()][self.comborow.get()]
            self.twoattcomp = '00'
            self.combocolumn.destroy()
            for i in self.cubesdic.keys():
                if (self.combocubes.get()) == i:
                    self.keycube = i
                    alldimensions = list((self.cubesdic[i][self.combomat.get()].keys()))
                    dimensions = []
                    for dim in alldimensions:
                        if len(dim) > 2:
                            if 'event' in dim or 'object' in dim:
                                dimensions.append(dim)
            self.combocolumn = ttk.Combobox(self.cubeaddress, width=20, values=dimensions)
            self.combocolumn.grid(row=2, column=4);
            self.combocolumn.bind("<<ComboboxSelected>>", self.columncallback)

            self.firstlistwidg.append(self.combocolumn)
            self.dfccbx = wizard_UI_single_dimension(self.root, self.cubeview_frame,
                                                       self.result_frame, self.result_canvas, tabletoshow,
                                                       self.firstlistwidg, self.keycube,
                                                       self.df, self.obj_df, self.comborow.get())
        else:
            tabletoshow = self.cubesdic[self.combocubes.get()][self.combomat.get()][
                (self.comborow.get(), self.combocolumn.get())]
            self.twoattcomp = '10'
            self.dfccbx = wizard_UI(self.root, self.cubeview_frame, self.result_frame,
                                                 self.result_canvas, tabletoshow, self.firstlistwidg, self.keycube
                                                 , self.df, self.obj_df, self.comborow.get(), self.combocolumn.get())

    def callback2(self,eventObject):
        self.comborow2.destroy();self.combocolumn2.destroy()
        for i in self.cubesdic2.keys():
            if (self.combocubes2.get())==i:
                self.keycube2=i
                alldimensions2 = list((self.cubesdic2[i][self.combomat2.get()].keys()))
                dimensions2= []
                for dim in alldimensions2:
                    if len(dim) > 2:
                        if 'event' in dim or 'object' in dim:
                            dimensions2.append(dim)
        self.comborow2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
        self.comborow2.grid(row=2, column=2);
        self.comborow2.bind("<<ComboboxSelected>>", self.rowcallback2)
        self.combocolumn2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
        self.combocolumn2.grid(row=2, column=4);
        self.combocolumn2.bind("<<ComboboxSelected>>", self.columncallback2)

        self.firstlistwidg2.append(self.combocolumn2)
        self.firstlistwidg2.append(self.comborow2)


    def columncallback2(self,eventObject):
        tabletoshow2=self.cubesdic2[self.combocubes2.get()][self.combomat2.get()][(self.comborow2.get(),self.combocolumn2.get())]
        self.twoatt2comp='10'
        self.dfccbx2=wizard_UI(self.root,self.cubeview_frame2,self.result_frame2, self.result_canvas2, tabletoshow2,self.firstlistwidg2,self.keycube2
                                           ,self.df,self.obj_df,self.comborow2.get(),self.combocolumn2.get())

    def rowcallback2(self,eventObject):
        tabletoshow2=self.cubesdic2[self.combocubes2.get()][self.combomat2.get()][self.comborow2.get()]
        self.twoatt2comp='00'
        self.combocolumn2.destroy()
        for i in self.cubesdic2.keys():
            if (self.combocubes2.get()) == i:
                self.keycube2 = i
                alldimensions2 = list((self.cubesdic2[i][self.combomat2.get()].keys()))
                dimensions2 = []
                for dim in alldimensions2:
                    if len(dim) > 2:
                        if 'event' in dim or 'object' in dim:
                            dimensions2.append(dim)
        self.combocolumn2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
        self.combocolumn2.grid(row=2, column=4);
        self.combocolumn2.bind("<<ComboboxSelected>>", self.columncallback2)
        self.firstlistwidg2.append(self.combocolumn2)

        self.dfccbx2 = wizard_UI_single_dimension(self.root, self.cubeview_frame2,
                                                     self.result_frame2, self.result_canvas2, tabletoshow2,
                                                     self.firstlistwidg2, self.keycube2,
                                                     self.df,self.obj_df,self.comborow2.get())

    def matcallback2(self,eventObject):
        if self.combocolumn2.get() == "":
            tabletoshow2 = self.cubesdic2[self.combocubes2.get()][self.combomat2.get()][self.comborow2.get()]
            self.twoatt2comp = '00'
            self.combocolumn2.destroy()
            for i in self.cubesdic2.keys():
                if (self.combocubes2.get()) == i:
                    self.keycube2 = i
                    alldimensions2 = list((self.cubesdic2[i][self.combomat2.get()].keys()))
                    dimensions2 = []
                    for dim in alldimensions2:
                        if len(dim) > 2:
                            if 'event' in dim or 'object' in dim:
                                dimensions2.append(dim)
            self.combocolumn2 = ttk.Combobox(self.cubeaddress2, width=20, values=dimensions2)
            self.combocolumn2.grid(row=2, column=4);
            self.combocolumn2.bind("<<ComboboxSelected>>", self.columncallback2)
            self.firstlistwidg2.append(self.combocolumn2)

            self.dfccbx2 = wizard_UI_single_dimension(self.root, self.cubeview_frame2,
                                                        self.result_frame2, self.result_canvas2, tabletoshow2,
                                                        self.firstlistwidg2, self.keycube2,
                                                        self.df, self.obj_df, self.comborow2.get())
        else:
            tabletoshow2 = self.cubesdic2[self.combocubes2.get()][self.combomat2.get()][
                (self.comborow2.get(), self.combocolumn2.get())]
            self.twoatt2comp = '10'
            self.dfccbx2 = wizard_UI(self.root, self.cubeview_frame2,
                                                  self.result_frame2, self.result_canvas2, tabletoshow2,
                                                  self.firstlistwidg2, self.keycube2
                                                  , self.df, self.obj_df, self.comborow2.get(), self.combocolumn2.get())

    def showtheeventlog(self):
        try:
            self.model.nodelabel.destroy();self.model.entrynofre.destroy();self.model.edgelabel.destroy();
            self.model.entryedfre.destroy();self.model.applymodel.destroy();self.model.exportmodel.destroy()
            self.model.nodelabel2.destroy();self.model.entrynofre2.destroy();self.model.edgelabel2.destroy();
            self.model.entryedfre2.destroy();self.model.applymodel2.destroy();self.model.exportmodel2.destroy()
        except AttributeError: print("")

        eventlog(self.root, self.dfccbx, self.dfccbx2,self.result_frame,
                            self.result_frame2, self.df, self.obj_df, self.twoattcomp, self.twoatt2comp
                            , self.combomat.get(), self.combomat2.get())

    def showthemodelfre(self):
        try:
            self.model.nodelabel.destroy();self.model.entrynofre.destroy();self.model.edgelabel.destroy();
            self.model.entryedfre.destroy();self.model.applymodel.destroy();self.model.exportmodel.destroy()
            self.model.nodelabel2.destroy();self.model.entrynofre2.destroy();self.model.edgelabel2.destroy();
            self.model.entryedfre2.destroy();self.model.applymodel2.destroy();self.model.exportmodel2.destroy()
        except AttributeError: print("")

        self.model=MVP_frequency(self.root, self.dfccbx, self.dfccbx2,self.result_frame, self.result_frame2,
                                       self.df, self.obj_df, self.twoattcomp, self.twoatt2comp,
                                       self.combomat.get(), self.combomat2.get())

    def showthemodelpre(self):
        try:
            self.model.nodelabel.destroy();self.model.entrynofre.destroy();self.model.edgelabel.destroy();
            self.model.entryedfre.destroy();self.model.applymodel.destroy();self.model.exportmodel.destroy()
            self.model.nodelabel2.destroy();self.model.entrynofre2.destroy();self.model.edgelabel2.destroy();
            self.model.entryedfre2.destroy();self.model.applymodel2.destroy();self.model.exportmodel2.destroy()
        except AttributeError: print("")

        self.model=MVP_performance(self.root, self.dfccbx, self.dfccbx2,self.result_frame, self.result_frame2,
                                       self.df, self.obj_df, self.twoattcomp, self.twoatt2comp,
                                       self.combomat.get(), self.combomat2.get())

    def showthepetrinet(self):
        try:
            self.model.nodelabel.destroy();self.model.entrynofre.destroy();self.model.edgelabel.destroy();
            self.model.entryedfre.destroy();self.model.applymodel.destroy();self.model.exportmodel.destroy()
            self.model.nodelabel2.destroy();self.model.entrynofre2.destroy();self.model.edgelabel2.destroy();
            self.model.entryedfre2.destroy();self.model.applymodel2.destroy();self.model.exportmodel2.destroy()
        except AttributeError: print("")
        self.model=object_centric_petrinet(self.root, self.dfccbx, self.dfccbx2,self.result_frame, self.result_frame2,
                                       self.df, self.obj_df, self.twoattcomp, self.twoatt2comp,
                                       self.combomat.get(), self.combomat2.get())

