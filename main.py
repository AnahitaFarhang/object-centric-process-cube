from tkinter import *
from tkinter import filedialog
from input.input_UI import input_UI
from pm4pymdl.objects.ocel.importer import importer as ocel_importer


class main():
    def __init__(self):

        ## root window configuration
        self.root = Tk(); self.root.geometry('600x1200');self.root.title("Object-Centric Process Cube")
        self.root.resizable(False, False) ;  screen_width = self.root.winfo_screenwidth();
        screen_height = self.root.winfo_screenheight(); window_height = 650; window_width = 1250
        x_cordinate = int((screen_width / 2) - (window_width / 2) - 5)
        y_cordinate = int((screen_height / 2) - (window_height / 2) - 50)
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.iconbitmap(r'cubeicon.ico');


        ## sub-menu configuration
        menu=Menu(self.root);self.root.config(menu=menu);filemenu = Menu(menu);
        menu.add_cascade(label='File', menu=filemenu);filemenu.add_command(label='New Cube', command=self.importlog);
        filemenu.add_command(label='Exit', command=self.exitfunction)


        #eventlog-frame configuration
        self.data_container = Frame(self.root, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                                width=1182, height=120, bd=0)
        self.data_canvas = Canvas(self.data_container, width=1182, height=120);
        scrollbar1 = Scrollbar(self.data_container, orient="horizontal", command=self.data_canvas.xview)
        scrollbar2 = Scrollbar(self.data_container, orient="vertical", command=self.data_canvas.yview)
        self.eventlog_frame = Frame(self.data_canvas, width=1182, height=120, bd=0)
        self.eventlog_frame.bind("<Configure>", lambda e: self.data_canvas.configure(scrollregion=self.data_canvas.bbox("all")))
        self.data_canvas.create_window((0, 0), window=self.eventlog_frame, anchor="nw")
        self.data_canvas.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set);
        self.data_container.place(x=20, y=5); scrollbar1.pack(side="bottom", fill="x");scrollbar2.pack(side="right", fill="y")
        self.data_canvas.pack(side="left", fill="both", expand=True)
        self.eventlog_label = Label(self.root, text='OCEL', font=('Helvetica', 10, 'bold')); self.eventlog_label.place(x=15, y=0)


        #cubeview_frame configuration
        self.cubeview_container = Frame(self.root, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                                width=506, height=133, bd=0)
        self.cubeview_canvas = Canvas(self.cubeview_container, width=506, height=133);
        scrollbar1 = Scrollbar(self.cubeview_container, orient="horizontal", command=self.cubeview_canvas.xview)
        scrollbar2 = Scrollbar(self.cubeview_container, orient="vertical", command=self.cubeview_canvas.yview)
        self.cubeview_frame = Frame(self.cubeview_canvas, width=506, height=133, bd=0)
        self.cubeview_frame.bind("<Configure>", lambda e: self.cubeview_canvas.configure(scrollregion=self.cubeview_canvas.bbox("all")))
        self.cubeview_canvas.create_window((0, 0), window=self.cubeview_frame, anchor="nw")
        self.cubeview_canvas.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set);
        self.cubeview_container.place(x=20, y=165); scrollbar1.pack(side="bottom", fill="x");scrollbar2.pack(side="right", fill="y")
        self.cubeview_canvas.pack(side="left", fill="both", expand=True)
        self.cubeview_label = Label(self.root, text='Overview of the Cube', font=('Helvetica', 10, 'bold')); self.cubeview_label.place(x=20, y=155)


        #result_frame configuration
        self.result_container = Frame(self.root, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                                width=570, height=240, bd=0)
        self.result_canvas = Canvas(self.result_container, width=570, height=240);
        scrollbar1 = Scrollbar(self.result_container, orient="horizontal", command=self.result_canvas.xview)
        scrollbar2 = Scrollbar(self.result_container, orient="vertical", command=self.result_canvas.yview)
        self.result_frame = Frame(self.result_canvas, width=570, height=240, bd=0)
        self.result_frame.bind("<Configure>", lambda e: self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all")))
        self.result_canvas.create_window((0, 0), window=self.result_frame, anchor="nw")
        self.result_canvas.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set);
        self.result_container.place(x=20, y=337); scrollbar1.pack(side="bottom", fill="x");scrollbar2.pack(side="right", fill="y")
        self.result_canvas.pack(side="left", fill="both", expand=True)
        self.labelcubemodel = Label(self.root, text='Result', font=('Helvetica', 10, 'bold')); self.labelcubemodel.place(x=20, y=328)


        # cube_view frame2 configuration
        self.cubeview_container2 = Frame(self.root, highlightbackground="gray", highlightcolor="gray",
                                       highlightthickness=1,
                                       width=506, height=133, bd=0)
        self.cubeview_canvas2 = Canvas(self.cubeview_container2, width=506, height=133);
        scrollbar1 = Scrollbar(self.cubeview_container2, orient="horizontal", command=self.cubeview_canvas2.xview)
        scrollbar2 = Scrollbar(self.cubeview_container2, orient="vertical", command=self.cubeview_canvas2.yview)
        self.cubeview_frame2 = Frame(self.cubeview_canvas2, width=506, height=133, bd=0)
        self.cubeview_frame2.bind("<Configure>", lambda e: self.cubeview_canvas2.configure(
            scrollregion=self.cubeview_canvas2.bbox("all")))
        self.cubeview_canvas2.create_window((0, 0), window=self.cubeview_frame2, anchor="nw")
        self.cubeview_canvas2.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set);
        self.cubeview_container2.place(x=697, y=165);
        scrollbar1.pack(side="bottom", fill="x"); scrollbar2.pack(side="right", fill="y")
        self.cubeview_canvas2.pack(side="left", fill="both", expand=True)
        self.cubeview_label2 = Label(self.root, text='Overview of the Cube', font=('Helvetica', 10, 'bold'));
        self.cubeview_label2.place(x=697, y=155)


        # result_frame2 configuration
        self.result_container2 = Frame(self.root, highlightbackground="gray", highlightcolor="gray", highlightthickness=1,
                                    width=570, height=240, bd=0)
        self.result_canvas2 = Canvas(self.result_container2, width=570, height=240);
        scrollbar1 = Scrollbar(self.result_container2, orient="horizontal", command=self.result_canvas2.xview)
        scrollbar2 = Scrollbar(self.result_container2, orient="vertical", command=self.result_canvas2.yview)
        self.result_frame2 = Frame(self.result_canvas2, width=570, height=240, bd=0)
        self.result_frame2.bind("<Configure>", lambda e: self.result_canvas2.configure(
            scrollregion=self.result_canvas2.bbox("all")))
        self.result_canvas2.create_window((0, 0), window=self.result_frame2, anchor="nw")
        self.result_canvas2.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set);
        self.result_container2.place(x=630, y=337);
        scrollbar1.pack(side="bottom", fill="x");
        scrollbar2.pack(side="right", fill="y")
        self.result_canvas2.pack(side="left", fill="both", expand=True)
        self.result_label2 = Label(self.root, text='Result', font=('Helvetica', 10, 'bold'));
        self.result_label2.place(x=630, y=328); self.n=0

        self.root.mainloop()


    def importlog(self):
        _list = self.eventlog_frame.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.destroy()
        if self.n==0:
            self.root.filename = filedialog.askopenfilename(title="Select file", filetypes=(
            ("ocel files", "*.jsonocel"), ("ocel files", "*.xmlocel"), ("all files", "*.*")))
            df, obj_df = ocel_importer.apply(self.root.filename);
            self.obj_df = obj_df;
            self.df = df
            cubesdic={}
        input_UI(self.eventlog_frame, self.df, self.obj_df,self.root,self.cubeview_frame,self.cubeview_frame2,self.result_frame,self.result_frame2,self.result_canvas,self.result_canvas2,cubesdic)

    def exitfunction(self):
        self.root.destroy()

main()