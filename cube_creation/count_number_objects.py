

class count_number_objects():
    def __init__(self,obj_df,dict):
        num_object={}
        for key in dict:
            num_object[key] = {}
            for v in dict[key]:
                values=obj_df[v].unique()
                valuess=values.tolist()
                cleanedList = [x for x in valuess if (str(x)!= 'nan')]
                num_object[key][v]={}
                for vv in cleanedList:
                    num_object[key][v][vv]=len(obj_df[obj_df[v] == vv])
        self.num_object=num_object