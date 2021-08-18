from output.filter.filter_event_attributes import filter_event_attributes
from output.filter.filter_objects_existence import filter_objects_existence
from output.filter.filter_objects_all import filter_objects_all
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl


class filter_dimensions():
    def __init__(self,rowname,columnname,selectedcells,obj_df,df,eventdims,objectdims,mat):
        if rowname in eventdims and columnname in eventdims:
            self.fildf=df
            totalnewids=[]
            for i in selectedcells:
                self.fildf= filter_event_attributes(self.fildf, columnname, i[0]).df2
                self.fildf = filter_event_attributes(self.fildf, rowname, i[1]).df2
                newids=self.fildf['event_id'].tolist()
                for i in newids:
                    totalnewids.append(i)
                self.fildf=df
            self.fildf = df[df["event_id"].isin(totalnewids)]
            self.fildf.type="succint"

        if rowname in objectdims and columnname in objectdims:
            objectnames=[]
            for i in range(len(selectedcells)):
                objectnames.append(obj_df.loc[(obj_df[rowname] == selectedcells[i][1])]['object_id'].tolist())
            finalobjects=[]
            for i in range(len(objectnames)):
                for j in objectnames:
                    if j not in finalobjects:
                       finalobjects.append(j)
            finalfinalobjects=[]
            for objlis in finalobjects:
                for obj in objlis:
                    if obj not in finalfinalobjects:
                        finalfinalobjects.append(obj)
            typedf=obj_df[obj_df["object_id"].isin([obj])]
            ot=typedf['object_type'].tolist()[0]
            self.dffilter=df
            if mat=="Existence":
                self.fildf0=filter_objects_existence(self.dffilter,ot,finalfinalobjects).df2
            if mat=="All":
                self.fildf0=filter_objects_all(self.dffilter,ot,finalfinalobjects).df2

            objectnames = []
            for i in range(len(selectedcells)):
                objectnames.append(obj_df.loc[(obj_df[columnname] == selectedcells[i][0])]['object_id'].tolist())
            finalobjects = []
            for i in range(len(objectnames)):
                for j in objectnames:
                    if j not in finalobjects:
                        finalobjects.append(j)
            finalfinalobjects = []
            for objlis in finalobjects:
                for obj in objlis:
                    if obj not in finalfinalobjects:
                        finalfinalobjects.append(obj)
            typedf = obj_df[obj_df["object_id"].isin([obj])]
            ot = typedf['object_type'].tolist()[0]
            self.dffilter = self.fildf0
            if mat=="Existence":
               self.fildf = filter_objects_existence(self.dffilter, ot, finalfinalobjects).df2
            if mat=="All":
                self.fildf = filter_objects_all(self.dffilter, ot, finalfinalobjects).df2

        if rowname in objectdims and columnname in eventdims:
            exploded_table = succint_mdl_to_exploded_mdl.apply(df)
            totalneweventids=[]
            for i in range(len(selectedcells)):
                objectnames=[]
                objectnames.append(obj_df.loc[(obj_df[rowname] == selectedcells[i][1])]['object_id'].tolist())
                objectids=objectnames[0]
                ot = obj_df[obj_df['object_id'].isin(objectids)]['object_type'].tolist()[0]
                expfil1 = exploded_table[exploded_table[ot].isin(objectids)]
                if mat=="All":
                    eventsids = expfil1['event_id'].tolist()
                    fil3df = exploded_table[exploded_table["event_id"].isin(eventsids)]
                    alleveinfil3df = fil3df["event_id"].tolist()
                    allobjinfil3df = fil3df[ot].tolist()
                    notsuitableeventids = []
                    for kk in range(len(allobjinfil3df)):
                        if allobjinfil3df[kk] not in objectids:
                            if str(allobjinfil3df[kk]) != 'nan':
                                notsuitableeventids.append(alleveinfil3df[kk])
                    expfil1 = fil3df[fil3df['event_id'].isin(notsuitableeventids) == False]
                newids = expfil1[expfil1[columnname].isin([selectedcells[i][0]])]['event_id'].tolist()
                for i in newids:
                    totalneweventids.append(i)
            self.fildf = df[df["event_id"].isin(totalneweventids)]
            self.fildf.type="succint"


        if rowname in eventdims and columnname in objectdims:
            exploded_table = succint_mdl_to_exploded_mdl.apply(df)
            totalneweventids=[]
            for i in range(len(selectedcells)):
                objectnames=[]
                objectnames.append(obj_df.loc[(obj_df[columnname] == selectedcells[i][0])]['object_id'].tolist())
                objectids=objectnames[0]
                ot = obj_df[obj_df['object_id'].isin(objectids)]['object_type'].tolist()[0]
                expfil1 = exploded_table[exploded_table[ot].isin(objectids)]
                if mat=="All":
                    eventsids = expfil1['event_id'].tolist()
                    fil3df = exploded_table[exploded_table["event_id"].isin(eventsids)]
                    alleveinfil3df = fil3df["event_id"].tolist()
                    allobjinfil3df = fil3df[ot].tolist()
                    notsuitableeventids = []
                    for kk in range(len(allobjinfil3df)):
                        if allobjinfil3df[kk] not in objectids:
                            if str(allobjinfil3df[kk]) != 'nan':
                                notsuitableeventids.append(alleveinfil3df[kk])
                    expfil1 = fil3df[fil3df['event_id'].isin(notsuitableeventids) == False]
                newids = expfil1[expfil1[rowname].isin([selectedcells[i][1]])]['event_id'].tolist()
                for i in newids:
                    totalneweventids.append(i)
            self.fildf = df[df["event_id"].isin(totalneweventids)]
            self.fildf.type="succint"
