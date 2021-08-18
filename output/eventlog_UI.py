
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl


class eventlog_UI(Frame):
    def __init__(self,root,scrollable_frame_model,df,obj_df):

        self.root=root; self.root.iconbitmap(r'cubeicon.ico')
        self.df=df; self.obj_df=obj_df

        try:
            del self.df['event_timestamp']
            del self.df['event_timestamp:year']
            del self.df['event_timestamp:month']
            del self.df['event_timestamp:day']
        except KeyError: print("")
        frame1 = Frame(scrollable_frame_model, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                               width=10, height=10, bd=0)
        self.labeldata = Label(frame1, text='Data: ', font=('Helvetica', 10, 'bold'));
        self.labeldata.grid(row=0,column=0)
        frame1.grid(row=0,column=0)
        columns=list(self.df.columns)
        self.ots=[]
        for i in columns:
            if 'event' not in i:
                self.ots.append(i)
        #self.ots=self.obj_df['object_type'].unique().tolist()
        combolist=['event log']
        for ot in self.ots:
            combolist.append(ot)
        self.combocubes = ttk.Combobox(frame1, width=15, values=combolist)
        self.combocubes.grid(row=0, column=1)
        self.combocubes.current(0)
        self.combocubes.bind("<<ComboboxSelected>>", self.checkdata)
        self.frame2 = Frame(scrollable_frame_model, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                               width=500, height=400, bd=0)
        self.frame2.grid(row=1,column=0)
        n = list(self.df.columns)
        pt = Table(self.frame2, dataframe=self.df, showtoolbar=0, showstatusbar=0)
        columns = self.df.columns.tolist()
        for i in range(len(columns)):
            pt.columncolors[n[i]] = 'RosyBrown1'
        pt.show()

    def checkdata(self,eventObject):
        if self.combocubes.get()=='event log':
            n = list(self.df.columns)
            pt = Table(self.frame2, dataframe=self.df, showtoolbar=0, showstatusbar=0)
            columns=self.df.columns.tolist()
            n = list(self.df.columns)
            for i in range(len(columns)):
                pt.columncolors[n[i]] = 'RosyBrown1'
            pt.show()
        if self.combocubes.get() in self.ots:
            exp=succint_mdl_to_exploded_mdl.apply(self.df)
            objects=exp[self.combocubes.get()].unique().tolist()
            obj_df2=self.obj_df[self.obj_df["object_id"].isin(objects)]
            for col in obj_df2.columns:
                if obj_df2[col].isnull().tolist()[0]==True:
                    del obj_df2[col]
            pt = Table(self.frame2, dataframe=obj_df2, showtoolbar=0, showstatusbar=0)
            columns = obj_df2.columns.tolist()
            n = list(obj_df2.columns)
            for i in range(len(columns)):
                pt.columncolors[n[i]] = 'peach puff'
            pt.show()



