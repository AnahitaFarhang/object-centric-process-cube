import pandas as pd
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl

class create_objects_differentots_dimensions():
    def __init__(self,ot, co0,ot1,co1,df,obj_df):
        # Existence
        firstdim = obj_df[co0].unique().tolist()
        seconddim = obj_df[co1].unique().tolist()
        firstdim = [firstdim for firstdim in firstdim if str(firstdim) != 'nan']
        seconddim = [seconddim for seconddim in seconddim if str(seconddim) != 'nan']
        expl = succint_mdl_to_exploded_mdl.apply(df)
        data = {}
        data[''] = seconddim
        for i in firstdim:
            filobjdf = obj_df[obj_df[co0].isin([i])]
            ids = filobjdf['object_id'].tolist()
            fildf = expl[expl[ot].isin(ids)]
            eventids1=fildf['event_id'].tolist()
            sucfildf = df[df["event_id"].isin(eventids1)]
            filexpl = succint_mdl_to_exploded_mdl.apply(sucfildf)
            nevents = []
            for j in seconddim:
                filobjdf2 = obj_df[obj_df[co1].isin([j])]
                ids = filobjdf2['object_id'].tolist()
                fildf2 = filexpl[filexpl[ot1].isin(ids)]
                nevents.append(len(fildf2['event_id'].tolist()))
            data[i] = nevents
        self.finaldf = pd.DataFrame(data)



        #All
        expl = succint_mdl_to_exploded_mdl.apply(df)
        data = {}
        data[''] = seconddim
        for i in firstdim:
            filobjdf = obj_df[obj_df[co0].isin([i])]
            objectids = filobjdf['object_id'].tolist()
            fildf = expl[expl[ot].isin(objectids)]

            eventsids=fildf['event_id'].tolist()
            fil2df=expl[expl["event_id"].isin(eventsids)]
            alleveinfil2df=fil2df["event_id"].tolist()
            allobjinfil2df=fil2df[ot].tolist()

            notsuitableeventids=[]
            for kk in range(len(allobjinfil2df)):
                if allobjinfil2df[kk] not in objectids:
                       if str(allobjinfil2df[kk])!='nan':
                          notsuitableeventids.append(alleveinfil2df[kk])
            fildf = fildf[fildf['event_id'].isin(notsuitableeventids)== False]

            eventids1=fildf['event_id'].tolist()
            sucfildf = df[df["event_id"].isin(eventids1)]
            filexpl = succint_mdl_to_exploded_mdl.apply(sucfildf)
            nevents = []
            for j in seconddim:
                filobjdf2 = obj_df[obj_df[co1].isin([j])]
                objectids2 = filobjdf2['object_id'].tolist()
                fildf2 = filexpl[filexpl[ot1].isin(objectids2)]

                eventsids2 = fildf2['event_id'].tolist()
                fil2df2 = expl[expl["event_id"].isin(eventsids2)]
                alleveinfil2df2 = fil2df2["event_id"].tolist()
                allobjinfil2df2 = fil2df2[ot].tolist()

                notsuitableeventids2 = []
                for kk in range(len(allobjinfil2df2)):
                    if allobjinfil2df2[kk] not in objectids2:
                        if str(allobjinfil2df2[kk]) != 'nan':
                            notsuitableeventids2.append(alleveinfil2df2[kk])
                fildf2 = fildf2[fildf2['event_id'].isin(notsuitableeventids2) == False]
                nevents.append(len(fildf2['event_id'].tolist()))
            data[i] = nevents
        self.finaldfall = pd.DataFrame(data)



