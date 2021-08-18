import pandas as pd
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl


class create_event_dimensions():
    def __init__(self ,co, df):
        attr1=co[0]; attr2=co[1]
        expl0=succint_mdl_to_exploded_mdl.apply(df)
        expl = expl0.copy() ;expl[attr1] = expl[attr1].astype(str);expl[attr2] = expl[attr2].astype(str)
        c1 = list(set(["event_id", "event_activity", "event_timestamp", attr1])); sub1 = expl[c1].dropna()
        sub1 = sub1.groupby(["event_id", attr1]);sub1 = sub1.first().reset_index();
        c2 = list(set(["event_id", attr2])); sub2 = expl[c2].dropna().groupby(["event_id", attr2]).first().reset_index()
        sub1.type = 'exploded';succ1 = exploded_mdl_to_succint_mdl.apply(sub1);succ1[attr1] = succ1[attr1].astype(str);
        merged = succ1.merge(sub2, left_on="event_id", right_on="event_id")
        if attr2 not in merged.columns:
            merged[attr2] = merged[attr2 + "_y"]
        if attr1 not in merged.columns:
             merged[attr1] = merged[attr1 + "_x"]
        unique1 = sorted(list(succ1[attr1].unique())); unique2 = sorted(list(sub2[attr2].unique()))
        count_values = merged.groupby([attr1, attr2]).size().to_dict();ret_dictio = {}
        for v1 in unique1:
            if type(v1) is str and len(v1) > 0 and v1[0] == "[":
                v1l = eval(v1)
            else:
                v1l = v1
            if type(v1l) is list:
                all_combos = v1l
            else:
                all_combos = [v1]
            for comb in all_combos:
                if not comb in ret_dictio:
                   ret_dictio[comb] = {attr1: comb}
            for v2 in unique2:
                if (v1, v2) in count_values:
                    if not str(v2) in ret_dictio[comb]:
                        ret_dictio[comb][str(v2)] = 0
                    ret_dictio[comb][str(v2)] = ret_dictio[comb][str(v2)] + count_values[(v1, v2)]
        ret_list = [y for x, y in ret_dictio.items()]
        for i in range(len(ret_list)):
            if type(ret_list[i][attr1]) is tuple:
               ret_list[i][attr1] = str(list(ret_list[i][attr1]))
            else:
               pass
        self.df = pd.DataFrame(ret_list);
        self.finaldf = self.df.fillna(0)



