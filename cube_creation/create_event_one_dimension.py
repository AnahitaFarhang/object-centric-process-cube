import pandas as pd
from pm4pymdl.algo.mvp.utils import succint_mdl_to_exploded_mdl, exploded_mdl_to_succint_mdl


class create_event_one_dimension():
    def __init__(self ,dim, df):
        exploded_table0 = succint_mdl_to_exploded_mdl.apply(df)
        exploded_table = exploded_table0.copy()
        exploded_table = exploded_table.dropna(subset=[dim], how="any")
        exploded_table[dim] = exploded_table[dim].astype(str)
        values = dict(exploded_table[dim].value_counts())
        values1 = list()
        for x, y in values.items():
           values1.append({dim: x, "count": y})

        self.finaldf = pd.DataFrame(values1)


