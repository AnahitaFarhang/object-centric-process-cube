import pandas as pd
import numpy as np
from tkinter import *
from itertools import combinations
from cube_creation.create_object_dimensions import create_object_dimensions
from cube_creation.create_event_dimensions import create_event_dimensions
from wizard.wizard_operations import wizard_operations
from cube_creation.create_object_event_dimensions import create_object_event_dimensions
from cube_creation.create_event_one_dimension import create_event_one_dimension
from cube_creation.create_object_one_dimension import create_object_one_dimension
from cube_creation.create_objects_differentots_dimensions import create_objects_differentots_dimensions


class input_UI():
    def __init__(self, frame, df, obj_df, root, cubeview_frame, cubeview_frame2, result_frame, result_frame2,
                 canvas_frame, canvas_frame2,cubesdic):
        self.root=root; self.cubeview_frame=cubeview_frame;
        self.cubeview_frame2=cubeview_frame2; self.cubesdic=cubesdic
        self.result_frame=result_frame; self.canvas_frame=canvas_frame;self.canvas_frame2=canvas_frame2
        self.result_frame2=result_frame2
        self.firstdf=df; self.firstobj_df=obj_df
        df = df.head(1);
        df = df.drop(['event_id'], axis=1)
        df_t = df.T;
        self.df_t = df_t.reset_index()
        examples = self.df_t[0].tolist();
        wid1 = len(max(self.df_t['index'].to_list(), key=len))

        EventData_label = Label(frame, text='Event Data', font=('Helvetica', 10, 'bold'));
        EventData_label.grid(row=0, column=1)

        self.eventdims = self.df_t['index'].tolist()
        i = 0
        e = Entry(frame, width=wid1, relief=GROOVE, font=('Helvetica', 10, 'bold'));
        e.grid(row=i + 1, column=1, sticky=NSEW)
        e.insert(END, "Dimension")
        e = Entry(frame, width=wid1, relief=GROOVE, font=('Helvetica', 10, 'bold'));
        e.grid(row=i + 1, column=2, sticky=NSEW)
        e.insert(END, "Example")
        self.cbVarallevent = StringVar(frame);
        self.cbVarallevent.set(0)
        self.chboxallevent = Checkbutton(frame, variable=self.cbVarallevent, command=self.on_check, bg="pink",
                            relief="ridge");
        self.chboxallevent.grid(row=i + 1, column=0);
        self.varlist = [];
        self.checklist = []
        for name in self.eventdims:
            cbVar = StringVar(frame);
            cbVar.set(0)
            chbox = Checkbutton(frame, variable=cbVar, command=self.on_check, bg="pink",
                                relief="ridge");
            chbox.grid(row=i + 2, column=0);
            e = Entry(frame, width=wid1, relief=GROOVE);
            e.grid(row=i + 2, column=1, sticky=NSEW)
            e.insert(END, self.eventdims[i]);
            e = Entry(frame, width=27, relief=GROOVE)
            e.grid(row=i + 2, column=2, sticky=NSEW)
            if type(examples[i]) != list:
                e.insert(END, examples[i])
            else:
                e.insert(END, '{' + (','.join(examples[i])) + '}')
            i = i + 1
            self.checklist.append(chbox)
            self.varlist.append(cbVar)

        # build a table for objects

        self.obj_df = obj_df;
        self.objecttypes = self.obj_df['object_type'].unique();
        dict = {};
        self.dictobjdf = {}
        for o in self.objecttypes:
            dict[o] = []
            obt_df = self.obj_df[self.obj_df["object_type"] == o]
            for i in obt_df.columns:
                try:
                    if not np.isnan(obt_df[i].tolist()).all():
                        dict[o].append(i)
                except TypeError:
                    dict[o].append(i)
            self.dictobjdf[o] = obt_df[dict[o]]
        self.objvarlist = {};
        self.objchecklist = {}
        self.objdims={}
        self.titrobjvarlist = {};
        self.titrobjchecklist = {}
        j = 0
        for ot in self.objecttypes:
            self.objvarlist[ot]=[]
            self.objchecklist[ot] =[]
            df_obt = self.dictobjdf[ot]
            df_obt = df_obt.drop(['object_id', 'object_type'], axis=1)
            if len(df_obt.columns) != 0:
                df_obt = df_obt.head(1);
                df_obt_t = df_obt.T;
                df_obt_t = df_obt_t.reset_index()
                columns = df_obt_t.columns;
                examples = df_obt_t[columns[1]].tolist();
                wid1 = len(max(df_obt_t['index'].to_list(), key=len))

                label = Label(frame, text='   ', font=('Helvetica', 10, 'bold'));
                label.grid(row=0, column=3 + 4 * j)
                label = Label(frame, text=ot + " Data", font=('Helvetica', 10, 'bold'));
                label.grid(row=0, column=5 + 4 * j)

                self.objdims[ot] = df_obt_t['index'].tolist()
                i = 0
                e = Entry(frame, width=wid1, relief=GROOVE, font=('Helvetica', 10, 'bold'));
                e.grid(row=1, column=5 + 4 * j, sticky=NSEW)
                e.insert(END, "Dimension")
                e = Entry(frame, width=wid1, relief=GROOVE, font=('Helvetica', 10, 'bold'));
                e.grid(row=1, column=6 + 4 * j, sticky=NSEW)
                e.insert(END, "Example")
                cbVar = StringVar(frame);
                cbVar.set(0)
                chbox = Checkbutton(frame, variable=cbVar, command=self.on_check, bg="pink", state=DISABLED,
                                    relief="ridge");
                chbox.grid(row=1, column=4 + 4 * j);
                self.titrobjchecklist[ot]=chbox
                self.titrobjvarlist[ot]=cbVar
                i = 0
                for name in self.objdims[ot]:
                    cbVar = StringVar(frame);
                    cbVar.set(0)
                    chbox = Checkbutton(frame, variable=cbVar, command=self.on_check, bg="pink", state=DISABLED,
                                        relief="ridge");
                    chbox.grid(row=i + 2, column=4 + 4 * j);
                    e = Entry(frame, width=wid1, relief=GROOVE);
                    e.grid(row=i + 2, column=5 + 4 * j, sticky=NSEW)
                    e.insert(END, self.objdims[ot][i]);
                    e = Entry(frame, width=27, relief=GROOVE)
                    e.grid(row=i + 2, column=6 + 4 * j, sticky=NSEW)
                    e.insert(END, examples[i])
                    self.objchecklist[ot].append(chbox)
                    self.objvarlist[ot].append(cbVar)
                    i = i + 1
                j = j + 1
        label = Label(frame, text='   ', font=('Helvetica', 10, 'bold'));
        label.grid(row=0, column=6 + 4 * j)
        labelbuildcube = Label(frame, text="Name:",font=('Helvetica', 10, 'bold')); labelbuildcube.grid(row=0,column=6 + 4 * (j+1))
        self.enternamecube = Entry(frame,width=15);self.enternamecube.grid(row=1,column=6 + 4 * (j+1))
        self.cubesdic = {}
        buildthecube = Button(frame, text="Build the Cube", command=self.buildcube);buildthecube.grid(row=2,column=6 + 4 * (j+1))



    def on_check(self):
        if self.cbVarallevent.get() == "1":
            self.chboxallevent["bg"] = "green"
            for i in range(len(self.checklist)):
                self.checklist[i]["bg"] = "green"
                self.checklist[i].select()
        else:
            self.chboxallevent["bg"] = "pink"


        otdim=[]
        for i in range(len(self.eventdims)):
            if self.varlist[i].get() == "1":
                self.checklist[i]["bg"] = "green"
                if self.eventdims[i] in self.objecttypes:
                    otdim.append(self.eventdims[i])
            else:
                self.checklist[i]["bg"] = "pink"


        for ot in self.objecttypes:
            if ot in otdim:
                 self.titrobjchecklist[ot].configure(state='normal')
                 for chbx in self.objchecklist[ot]:
                    chbx.configure(state='normal')
                 try:
                    for i in range(len(self.objdims[ot])):
                        if self.objvarlist[ot][i].get() == "1":
                            self.objchecklist[ot][i]["bg"] = "green"
                        else:
                            self.objchecklist[ot][i]["bg"] = "pink"
                 except KeyError:
                    print("")
            else:
                try:
                   self.titrobjchecklist[ot]["bg"] = "pink"
                   self.titrobjchecklist[ot].configure(state='normal')
                   self.titrobjchecklist[ot].deselect()
                   self.titrobjchecklist[ot].configure(state=DISABLED)
                   for chbx in self.objchecklist[ot]:
                        chbx["bg"] = "pink"
                        chbx.configure(state='normal')
                        chbx.deselect()
                        chbx.configure(state=DISABLED)
                except KeyError:
                    print("")


        for ot in self.objecttypes:
            try:
               if self.titrobjvarlist[ot].get() == "1":
                   self.titrobjchecklist[ot]["bg"] = "green"
                   for i in range(len(self.objdims[ot])):
                       self.objchecklist[ot][i]["bg"] = "green"
                       self.objchecklist[ot][i].select()
               else:
                   self.titrobjchecklist[ot]["bg"] = "pink"
            except KeyError:
                print("")


    def buildcube(self):
        dimensions={}; eventattrs=[]
        for i in range(len(self.varlist)):
            if self.varlist[i].get()=='1':
                if self.eventdims[i]=="event_timestamp":
                    self.firstdf['year0'] = pd.DatetimeIndex(self.firstdf['event_timestamp']).year
                    self.firstdf['month0'] = pd.DatetimeIndex(self.firstdf['event_timestamp']).month
                    self.firstdf['day0'] = pd.DatetimeIndex(self.firstdf['event_timestamp']).day
                    self.firstdf["event_timestamp:year"] = self.firstdf["year0"].astype(str)
                    self.firstdf["event_timestamp:month"] = self.firstdf["year0"].astype(str) + "." + self.firstdf["month0"].astype(str)
                    self.firstdf["event_timestamp:day"] = self.firstdf["year0"].astype(str) + "." + self.firstdf["month0"].astype(
                        str) + "." + self.firstdf["day0"].astype(str)
                    del self.firstdf["year0"]; del self.firstdf["month0"]; del self.firstdf["day0"]
                    eventattrs.append("event_timestamp:year");eventattrs.append("event_timestamp:month");eventattrs.append("event_timestamp:day")
                else:
                    eventattrs.append(self.eventdims[i])
        dimensions["event log"]=eventattrs
        for ot in self.objecttypes:
            objectattrs = []
            if ot in self.objdims.keys():
                for i in range(len(self.objvarlist[ot])):
                    if self.objvarlist[ot][i].get() == '1':
                        objectattrs.append(self.objdims[ot][i])
            dimensions[ot]=objectattrs
        alldimensions=[]
        for i in list(dimensions.values()):
            for j in i:
                alldimensions.append(j)
        comb = combinations(alldimensions, 2)
        attrdict={};  coco1 = [] ;attrdictall={}


        for co in list(comb):
            if co[0] in dimensions["event log"] and co[0] not in self.objecttypes and co[1] in dimensions["event log"] and co[1] not in self.objecttypes:
                evdf=create_event_dimensions(co, self.firstdf).finaldf
                attrdict[co]=evdf;attrdictall[co]=evdf
                df_new = evdf.set_index(co[0]).transpose()
                df_new.reset_index(inplace=True)
                attrdict[(co[1],co[0])]=df_new; attrdictall[(co[1],co[0])]=df_new
            if co[0] in dimensions["event log"] and co[0] not in self.objecttypes and co[1] not in dimensions["event log"]:
                for ot in self.objecttypes:
                    if co[1] in dimensions[ot]:
                        objecteventcube=create_object_event_dimensions(ot, co[1], co[0], self.firstdf, self.firstobj_df)
                        evdf = objecteventcube.finaldf
                        evdfall = objecteventcube.finaldfall
                attrdict[co]=evdf
                attrdictall[co] = evdfall
                df_new = evdf.set_index('').transpose()
                df_new.reset_index(inplace=True)
                attrdict[(co[1],co[0])]=df_new
                df_newall = evdfall.set_index('').transpose()
                df_newall.reset_index(inplace=True)
                attrdictall[(co[1],co[0])]=df_newall
            if co[1] in dimensions["event log"] and co[0] not in dimensions["event log"] and co[0] not in self.objecttypes:
                  for ot in self.objecttypes:
                       if co[0] in dimensions[ot]:
                           objecteventcube2 = create_object_event_dimensions(ot, co[0], co[1], self.firstdf, self.firstobj_df)
                           evdf = objecteventcube2.finaldf
                           evdfall = objecteventcube2.finaldfall
                  attrdict[co]=evdf; attrdictall[co]=evdfall
                  df_new = evdf.set_index('').transpose();df_newall = evdfall.set_index('').transpose()
                  df_new.reset_index(inplace=True); df_newall.reset_index(inplace=True)
                  attrdict[(co[1],co[0])]=df_new; attrdictall[(co[1],co[0])]=df_newall

            #    buildeventobjectcube
            if co[0] not in dimensions["event log"] and co[1] not in dimensions["event log"]:
                for ot in self.objecttypes:
                    if co[0] in dimensions[ot] and co[1] in dimensions[ot]:
                        objectcube=create_object_dimensions(ot, co, self.firstdf, self.firstobj_df)
                        evdf = objectcube.finaldf
                        evdfall=objectcube.finaldfall
                        attrdict[(co[1], co[0])] = evdf; attrdictall[(co[1], co[0])] = evdfall
                        df_new = evdf.set_index('').transpose(); df_newall = evdfall.set_index('').transpose()
                        df_new.reset_index(inplace=True); df_newall.reset_index(inplace=True)
                        attrdict[(co[0], co[1])] = df_new; attrdictall[(co[0], co[1])] = df_newall

                for ot in self.objecttypes:
                    for ot1 in self.objecttypes:
                        if ot!=ot1:
                            if co[0] in dimensions[ot] and co[1] in dimensions[ot1]:
                                if [co[1],co[0]] not in coco1:
                                   coco1.append([co[0],co[1]])
                                   difobjectcube=create_objects_differentots_dimensions(ot, co[0], ot1, co[1], self.firstdf, self.firstobj_df)
                                   evdf = difobjectcube.finaldf; evdfall=difobjectcube.finaldfall
                                   attrdict[(co[1], co[0])] = evdf; attrdictall[(co[1], co[0])] = evdfall
                                   df_new = evdf.set_index('').transpose(); df_newall = evdfall.set_index('').transpose()
                                   df_new.reset_index(inplace=True); df_newall.reset_index(inplace=True)
                                   attrdict[(co[0], co[1])] = df_new; attrdictall[(co[0], co[1])] = df_newall


        for dim in alldimensions:
            if dim in dimensions["event log"]:
                eventcubeonedim=create_event_one_dimension(dim, self.firstdf)
                attrdict[(dim)]=eventcubeonedim.finaldf
                attrdictall[(dim)] = eventcubeonedim.finaldf
            if dim not in dimensions["event log"]:
                for ot in self.objecttypes:
                    if dim in dimensions[ot]:
                       objectcubeonedim=create_object_one_dimension(ot, dim, self.firstdf, self.firstobj_df)
                       attrdict[(dim)] = objectcubeonedim.finaldf
                       attrdictall[(dim)] = objectcubeonedim.finaldfall

        self.cubesdic[self.enternamecube.get()]={'Existence':attrdict,'All':attrdictall}


        resultdf = self.firstdf
        resultobjdf=self.firstobj_df
        for i in list(resultdf.columns):
            if i not in alldimensions:
                if i not in ['object_type', 'event_id', 'event_timestamp'] :
                   del resultdf[i]
        for i in list(resultobjdf.columns):
            if i not in alldimensions:
                if i not in ['object_type', 'object_id'] :
                   del resultobjdf[i]

        wizard_operations(self.root, self.cubeview_frame, self.cubeview_frame2, self.result_frame, self.result_frame2,
                          self.canvas_frame, self.canvas_frame2,self.cubesdic, resultdf, resultobjdf)

