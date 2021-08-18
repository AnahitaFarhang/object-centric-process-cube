from tkinter import *
import tkinter.font as font


class wizard_UI_single_dimension():
    def __init__(self,root,scrollable_frame_cubeview,scrollable_frame_model, canvasmodel,tabletoshow,firstlistwidg,keycube,succintdf,obj_df,rowname):
        self.firstobj_df=obj_df;self.first_df=succintdf;self.canvasmodel=canvasmodel
        self.root=root;self.scrollable_frame_model=scrollable_frame_model
        myFont = font.Font(size=8)
        self.scrollable_frame_cubeview=scrollable_frame_cubeview
        listwidg = self.scrollable_frame_cubeview.winfo_children()

        self.keycube=keycube;self.obj_df=obj_df;self.rowname=rowname;

        self.eventattrs = succintdf.columns.tolist()
        self.objectattrs=self.firstobj_df.columns.tolist()
        self.cubecellsframe = Frame(self.scrollable_frame_cubeview,
                                width=1000, height=1000, bd=0)
        self.cubecellsframe.grid(sticky=SW)

        for item in listwidg:
            if item.winfo_children():
                listwidg.extend(item.winfo_children())
        for i in listwidg:
            if i not in firstlistwidg:
                i.destroy()
        self.columns = tabletoshow.columns

        for i in range(len(self.columns)):
            e = Entry(self.cubecellsframe, width=15, relief=GROOVE)
            e.grid(row=4, column=i+1, sticky=NSEW)
            e.insert(END, self.columns[i])
            e['font'] = myFont
        self.firstcolumn = tabletoshow[self.columns[0]].to_list()

        for j in range(len(self.firstcolumn)):
            e = Entry(self.cubecellsframe, width=15, relief=GROOVE)
            e.grid(row=j + 5, column=1, sticky=NSEW)
            e.insert(END, self.firstcolumn[j])
            e['font'] = myFont
        self.columns = list(self.columns)
        self.columns.pop(0)

        self.rowschbx = [];
        self.rowsvar = []
        for i in range(len(self.firstcolumn)):
            self.colschbx = [];
            self.colsvar = []
            for j in range(len(self.columns)):
                cbVar = StringVar(self.cubecellsframe)
                cbVar.set(0)
                chbox = Checkbutton(self.cubecellsframe, variable=cbVar, text=tabletoshow.iloc[i][self.columns[j]], command=self.on_check,
                                    width=15,
                                    bg="pink",
                                    relief="ridge")
                chbox.grid(row=i + 5, column=j + 2, sticky=NSEW);
                self.colschbx.append(chbox)
                self.colsvar.append(cbVar)
            self.rowschbx.append(self.colschbx)
            self.rowsvar.append(self.colsvar)


    def on_check(self):
        for j in range(len(self.columns)):
            for i in range(len(self.firstcolumn)):
                if self.rowsvar[i][j].get() == "1":
                    self.rowschbx[i][j]["bg"] = "green"
                else:
                    self.rowschbx[i][j]["bg"] = "pink"


