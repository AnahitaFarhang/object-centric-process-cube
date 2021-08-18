import pandas as pd
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl


class create_object_event_dimensions():
    def __init__(self,ot,co0, co1, df,obj_df):

        #Existance
        firstdim = obj_df[co0].unique().tolist()
        seconddim = df[co1].unique().tolist()
        firstdim = [firstdim for firstdim in firstdim if str(firstdim) != 'nan']
        seconddim = [seconddim for seconddim in seconddim if str(seconddim) != 'nan']
        expl = succint_mdl_to_exploded_mdl.apply(df)
        data = {}
        data[''] = seconddim
        for i in firstdim:
            filobjdf = obj_df[obj_df[co0].isin([i])]
            ids = filobjdf['object_id'].tolist()
            fildf = expl[expl[ot].isin(ids)]
            nevents = []
            for j in seconddim:
                filfildf = fildf[fildf[co1].isin([j])]
                nevents.append(len(filfildf['event_id'].tolist()))
            data[i] = nevents

        self.finaldf = pd.DataFrame(data)

        #Forall
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
            nevents = []
            for j in seconddim:
                filfildf = fildf[fildf[co1].isin([j])]
                nevents.append(len(filfildf['event_id'].tolist()))
            data[i] = nevents
        self.finaldfall = pd.DataFrame(data)
