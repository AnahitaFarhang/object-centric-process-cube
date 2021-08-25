from tkinter import *
import tkinter.font as font


class wizard_UI():
    def __init__(self, root, cubeview_frame, result_frame, result_canvas, tabletoshow, firstlistwidg,
                 keycube,succintdf,obj_df,rowname,columnname):

        self.firstobj_df=obj_df;self.first_df=succintdf;self.result_canvas=result_canvas
        self.root=root;
        self.result_frame=result_frame
        myFont = font.Font(size=8)
        self.cubeview_frame=cubeview_frame
        listwidg = self.cubeview_frame.winfo_children()

        self.keycube=keycube;self.obj_df=obj_df;self.rowname=rowname;self.columnname=columnname
        self.cubecellsframe = Frame(self.cubeview_frame,
                                width=1000, height=1000, bd=0)
        self.cubecellsframe.grid(sticky=SW)

        self.eventattrs = succintdf.columns.tolist()
        self.objectattrs=self.firstobj_df.columns.tolist()


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

