from tkinter import *
from PIL import ImageTk
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pm4pymdl.visualization.petrinet import visualizer as petri_vis_factory
from pm4pymdl.algo.mvp.get_logs_and_replay import algorithm as petri_factory
from pm4pymdl.visualization.mvp.gen_framework3 import visualizer as visualizer
from output.filter.filter_dimensions import filter_dimensions
from output.filter.filter_one_dimension import filter_one_dimension


class object_centric_petrinet():
    def __init__(self, root, dfccbx, dfccbx2, result_frame, result_frame2, df,obj_df, twoatt, twoatt2
                 , mat1, mat2):
        self.root=root
        self.dfccbx=dfccbx
        self.dfccbx2=dfccbx2
        self.result_frame=result_frame
        self.result_frame2=result_frame2
        self.df=df
        self.obj_df=obj_df
        self.twoatt=twoatt
        self.twoatt2=twoatt2
        self.mat1=mat1
        self.mat2=mat2

        #window1
        _list = self.result_frame.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        self.minedgefre = 2;
        self.minnodefre = 2

        if self.twoatt=='00':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])
            self.fildf = filter_one_dimension(self.dfccbx.rowname, selectedcells, self.obj_df,
                                                               self.df, self.dfccbx.eventattrs,
                                                               self.dfccbx.objectattrs,self.mat1).fildf
        if self.twoatt=='10':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])
            self.fildf = filter_dimensions(self.dfccbx.rowname, self.dfccbx.columnname, selectedcells, self.obj_df, self.df,
                                            self.dfccbx.eventattrs, self.dfccbx.objectattrs,self.mat1).fildf


        param = {}
        param["min_node_freq"] = self.minnodefre
        param["min_edge_freq"] = self.minedgefre
        self.gmodel = petri_factory.apply(self.fildf, parameters=param)
        gvizg = petri_vis_factory.apply(self.gmodel, parameters={"format": "png"})
        petri_vis_factory.save(gvizg, "model.png")
        visualizer.save(gvizg, "model1.png")
        self.img = Image.open("model1.png");
        self.picg = ImageTk.PhotoImage(self.img, master=self.result_frame);
        self.panelg = Label(self.result_frame, image=self.picg);
        self.panelg.pack()

        self.nodelabel = tk.Label(self.root, text="Min Node Frequency:", font=('Helvetica', 8, 'bold'))
        self.nodelabel.place(x=20, y=602)
        self.entrynofre = tk.Entry(self.root, width=5)
        self.entrynofre.place(x=140, y=602)
        self.edgelabel = tk.Label(self.root, text="Min Edge Frequency:", font=('Helvetica', 8, 'bold'))
        self.edgelabel.place(x=180, y=602)
        self.entryedfre = tk.Entry(self.root, width=5)
        self.entryedfre.place(x=300, y=602)
        self.applymodel = Button(self.root, text="Apply", width=10, command=self.showthemodelfunc1)
        self.applymodel.place(x=345, y=602)

        self.exportmodel = Button(self.root, text="Export the Model", width=15, command=self.exportmodel)
        self.exportmodel.place(x=465, y=602)

        #window2
        _list = self.result_frame2.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        self.minnodefre2 = 2;
        self.minedgefre2 = 2

        if self.twoatt2=='00':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_one_dimension(self.dfccbx2.rowname, selectedcells2, self.obj_df,
                                                               self.df, self.dfccbx2.eventattrs,
                                                               self.dfccbx2.objectattrs,self.mat2).fildf
        if self.twoatt2=='10':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_dimensions(self.dfccbx2.rowname, self.dfccbx2.columnname, selectedcells2, self.obj_df, self.df,
                                            self.dfccbx2.eventattrs, self.dfccbx2.objectattrs, self.mat2).fildf

        param2 = {}
        param2["min_node_freq"] = self.minnodefre2
        param2["min_edge_freq"] = self.minedgefre2
        self.gmodel2 = petri_factory.apply(self.fildf2, parameters=param2)
        gvizg2 = petri_vis_factory.apply(self.gmodel2, parameters={"format": "png"})
        petri_vis_factory.save(gvizg2, "model2.png")
        self.img2 = Image.open("model2.png");
        self.picg2 = ImageTk.PhotoImage(self.img2, master=self.result_frame2);
        self.panelg2 = Label(self.result_frame2, image=self.picg2);
        self.panelg2.pack()


        self.nodelabel2 = tk.Label(self.root, text="Min Node Frequency:",font=('Helvetica', 8, 'bold'))
        self.nodelabel2.place(x=630, y=602)
        self.entrynofre2 = tk.Entry(self.root,width=5)
        self.entrynofre2.place(x=750, y=602)
        self.edgelabel2 = tk.Label(self.root, text="Min Edge Frequency:", font=('Helvetica', 8, 'bold'))
        self.edgelabel2.place(x=790, y=602)
        self.entryedfre2 = tk.Entry(self.root, width=5)
        self.entryedfre2.place(x=910, y=602)
        self.applymodel2=Button(self.root, text="Apply", width=10, command=self.showthemodelfunc2)
        self.applymodel2.place(x=955, y=602)
        self.exportmodel2 = Button(self.root, text="Export the Model", width=15, command=self.exportmodel2)
        self.exportmodel2.place(x=1060, y=602)


    def showthemodelfunc1(self):
        #window1
        _list = self.result_frame.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        try:
            if self.dfccbx.entrynofre.get() != '':
                self.minnodefre = int(self.dfccbx.entrynofre.get());
                self.minedgefre = int(self.dfccbx.entryedfre.get())

            else:
                self.minnodefre = 2;
                self.minedgefre = 2
        except AttributeError:
            self.minnodefre = 2;
            self.minedgefre = 2
        if self.twoatt=='00':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])

            self.fildf = filter_one_dimension(self.dfccbx.rowname, selectedcells, self.obj_df,
                                                               self.df, self.dfccbx.eventattrs,
                                                               self.dfccbx.objectattrs,self.mat1).fildf
        if self.twoatt=='10':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])

            self.fildf = filter_dimensions(self.dfccbx.rowname, self.dfccbx.columnname, selectedcells, self.obj_df, self.df,
                                            self.dfccbx.eventattrs, self.dfccbx.objectattrs,self.mat1).fildf

        param = {}
        param["min_node_freq"] = self.minnodefre
        param["min_edge_freq"] = self.minedgefre
        self.gmodel = petri_factory.apply(self.fildf, parameters=param)
        gvizg = petri_vis_factory.apply(self.gmodel, parameters={"format": "png"})
        petri_vis_factory.save(gvizg, "model1.png")
        visualizer.save(gvizg, "model1.png")
        self.img = Image.open("model1.png");
        self.picg = ImageTk.PhotoImage(self.img, master=self.result_frame);
        self.panelg = Label(self.result_frame, image=self.picg);
        self.panelg.pack()

    def showthemodelfunc2(self):
        #window2
        _list = self.result_frame2.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        try:
            if self.dfccbx2.entrynofre.get() != '':
                self.minnodefre2 = int(self.dfccbx2.entrynofre.get());
                self.minedgefre2 = int(self.dfccbx2.entryedfre.get())

            else:
                self.minnodefre2 = 2;
                self.minedgefre2 = 2
        except AttributeError:
            self.minnodefre2 = 2;
            self.minedgefre2 = 2

        if self.twoatt2=='00':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_one_dimension(self.dfccbx2.rowname, selectedcells2, self.obj_df,
                                                               self.df, self.dfccbx2.eventattrs,
                                                               self.dfccbx2.objectattrs,self.mat2).fildf
        if self.twoatt2=='10':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_dimensions(self.dfccbx2.rowname, self.dfccbx2.columnname, selectedcells2, self.obj_df, self.df,
                                            self.dfccbx2.eventattrs, self.dfccbx2.objectattrs,self.mat2).fildf

        param2 = {}
        param2["min_node_freq"] = self.minnodefre2
        param2["min_edge_freq"] = self.minedgefre2
        self.gmodel2 = petri_factory.apply(self.fildf2, parameters=param2)
        gvizg2 = petri_vis_factory.apply(self.gmodel2, parameters={"format": "png"})
        petri_vis_factory.save(gvizg2, "model2.png")
        self.img2 = Image.open("model2.png");
        self.picg2 = ImageTk.PhotoImage(self.img2, master=self.result_frame2);
        self.panelg2 = Label(self.result_frame2, image=self.picg2);
        self.panelg2.pack()


    def exportmodel(self):
        img = Image.open("model1.png");
        filename = filedialog.asksaveasfilename(defaultext=".png", initialfile='image.png',
                                                filetypes=[("Pictures", "*.png"), ("All files", "*")])
        img.save(filename)

    def exportmodel2(self):
        img2 = Image.open("model2.png");
        filename = filedialog.asksaveasfilename(defaultext=".png", initialfile='image.png',
                                                filetypes=[("Pictures", "*.png"), ("All files", "*")])
        img2.save(filename)
        #image.save(a)
