
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl

class filter_objects_all():
    def __init__(self, succint_table, attr, value):
        expl=succint_mdl_to_exploded_mdl.apply(succint_table)
        fildf = expl[expl[attr].isin(value)]
        eventsids = fildf['event_id'].tolist()
        fil3df = expl[expl["event_id"].isin(eventsids)]
        alleveinfil3df = fil3df["event_id"].tolist()
        allobjinfil3df = fil3df[attr].tolist()
        notsuitableeventids = []
        for kk in range(len(allobjinfil3df)):
            if allobjinfil3df[kk] not in value:
                if str(allobjinfil3df[kk]) != 'nan':
                    notsuitableeventids.append(alleveinfil3df[kk])
        fildf = fildf[fildf['event_id'].isin(notsuitableeventids) == False]
        self.df2=exploded_mdl_to_succint_mdl.apply(fildf)

