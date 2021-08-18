from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl


class filter_event_attributes():
    def __init__(self,succint_table,attr,value):
        exploded_table = succint_mdl_to_exploded_mdl.apply(succint_table)
        if 'cardinality' not in attr:
            if type(value) is str:
                if value[0] == "[":
                    vvalue = eval(value)
                else:
                    vvalue = [value]
            self.vvalue = vvalue
            for selection in vvalue:
                self.df0 = exploded_table[exploded_table[attr] == selection]
                self.exploded_table = exploded_table[exploded_table["event_id"].isin(self.df0["event_id"])]
        elif 'cardinality' in attr:
            try: self.df0 = exploded_table[exploded_table[attr] == float(value)]
            except ValueError: self.df0 = exploded_table[exploded_table[attr] == value]
            self.exploded_table = exploded_table[exploded_table["event_id"].isin(self.df0["event_id"])]
        self.df2=exploded_mdl_to_succint_mdl.apply(self.exploded_table)


