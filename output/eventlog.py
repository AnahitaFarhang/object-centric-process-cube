from output.filter.filter_one_dimension import filter_one_dimension
from output.eventlog_UI import eventlog_UI
from output.filter.filter_dimensions import filter_dimensions


class eventlog():
    def __init__(self, root, dfccbx, dfccbx2, result_frame, result_frame2, df, obj_df, twoatt, twoatt2
                 , mat1, mat2):
        self.root=root
        self.dfccbx=dfccbx
        self.dfccbx2=dfccbx2
        self.result_frame=result_frame
        self.result_frame2=result_frame2
        self.df=df
        self.obj_df=obj_df
        self.twoatt=twoatt
        self.twoatt2=twoatt2
        self.mat1=mat1
        self.mat2=mat2


        _list = self.result_frame.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        try:
            if self.dfccbx.entrynofre.get() != '':
                self.minnodefre = int(self.dfccbx.entrynofre.get());
                self.minedgefre = int(self.dfccbx.entryedfre.get())
                self.dfccbx.nodelabel.destroy();
                self.dfccbx.entrynofre.destroy()
                self.dfccbx.edgelabel.destroy();
                self.dfccbx.entryedfre.destroy()
                self.dfccbx.applymodel.destroy();
                self.dfccbx.applymodel.destroy()
            else:
                self.minnodefre = 2;
                self.minedgefre = 2
        except AttributeError:
            self.minnodefre = 2;
            self.minedgefre = 2


        if self.twoatt=='00':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])
            self.fildf = filter_one_dimension(self.dfccbx.rowname, selectedcells, self.obj_df,
                                                               self.df, self.dfccbx.eventattrs,
                                                               self.dfccbx.objectattrs,self.mat1).fildf
        if self.twoatt=='10':
            selectedcells = []
            for j in range(len(self.dfccbx.columns)):
                for i in range(len(self.dfccbx.firstcolumn)):
                    if self.dfccbx.rowsvar[i][j].get() == "1":
                        selectedcells.append([self.dfccbx.columns[j], self.dfccbx.firstcolumn[i]])
            self.fildf = filter_dimensions(self.dfccbx.rowname, self.dfccbx.columnname, selectedcells,
                                                         self.obj_df, self.df,
                                                         self.dfccbx.eventattrs, self.dfccbx.objectattrs
                                                         , self.mat1).fildf

        eventlog_UI(self.root, self.result_frame, self.fildf, self.obj_df)


        _list = self.result_frame2.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        try:
            if self.dfccbx2.entrynofre.get() != '':
                self.minnodefre = int(self.dfccbx2.entrynofre.get());
                self.minedgefre = int(self.dfccbx2.entryedfre.get())
                self.dfccbx2.nodelabel.destroy();
                self.dfccbx2.entrynofre.destroy()
                self.dfccbx2.edgelabel.destroy();
                self.dfccbx2.entryedfre.destroy()
                self.dfccbx2.applymodel.destroy();
                self.dfccbx2.applymodel.destroy()
            else:
                self.minnodefre = 2;
                self.minedgefre = 2
        except AttributeError:
            self.minnodefre = 2;
            self.minedgefre = 2


        if self.twoatt2 == '00':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_one_dimension(self.dfccbx2.rowname, selectedcells2, self.obj_df,
                                                               self.df, self.dfccbx2.eventattrs,
                                                               self.dfccbx2.objectattrs,self.mat2).fildf
        if self.twoatt2 == '10':
            selectedcells2 = []
            for j in range(len(self.dfccbx2.columns)):
                for i in range(len(self.dfccbx2.firstcolumn)):
                    if self.dfccbx2.rowsvar[i][j].get() == "1":
                        selectedcells2.append([self.dfccbx2.columns[j], self.dfccbx2.firstcolumn[i]])
            self.fildf2 = filter_dimensions(self.dfccbx2.rowname, self.dfccbx2.columnname, selectedcells2,
                                                         self.obj_df, self.df,
                                                         self.dfccbx2.eventattrs, self.dfccbx2.objectattrs
                                                         , self.mat2).fildf

        eventlog_UI(self.root, self.result_frame2, self.fildf2, self.obj_df)