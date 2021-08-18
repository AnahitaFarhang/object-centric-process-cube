
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl

class filter_objects_existence():
    def __init__(self,succint_table,attr,value):
        exploded_table = succint_mdl_to_exploded_mdl.apply(succint_table)
        self.df0 = exploded_table[exploded_table[attr].isin(value)]
        self.exploded_table = exploded_table[exploded_table["event_id"].isin(self.df0["event_id"])]
        self.df2=exploded_mdl_to_succint_mdl.apply(self.exploded_table)

