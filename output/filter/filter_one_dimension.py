from output.filter.filter_event_attributes import filter_event_attributes
from output.filter.filter_objects_existence import filter_objects_existence
from output.filter.filter_objects_all import filter_objects_all


class filter_one_dimension():
    def __init__(self,rowname,selectedcells,obj_df,df,eventdims,objectdims,mat):

        if rowname in eventdims:
            self.fildf=df
            totalnewids=[]
            for i in selectedcells:
                self.fildf = filter_event_attributes(self.fildf, rowname, i[1]).df2
                newids=self.fildf['event_id'].tolist()
                for i in newids:
                    totalnewids.append(i)
                self.fildf=df
            self.fildf = df[df["event_id"].isin(totalnewids)]
            self.fildf.type="succint"

        if rowname in objectdims:
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
                if mat == "Existence":
                   self.fildf=filter_objects_existence(self.dffilter,ot,finalfinalobjects).df2
                if mat == "All":
                    self.fildf = filter_objects_all(self.dffilter, ot, finalfinalobjects).df2


