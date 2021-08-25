# OCPC: Object-Centric-Process-Cube

This project introduces a stand-alone object-centric process cube tool built on the PM4PY-MDL process mining framework. Process cubes are developed to compare processes with each other, however, the existing process cubes can compare the processes with single case notion with each other. In reality, there exist processes such as Purchase-to-Pay processes with multiple case notions, e.g., order, item, and customer that are called object-centric processes. In this application, we provide a framework where you can compare processes with multiple interacting objects with each other. The application is written in Python  Tk  GUI  toolkit as the user interface. At the moment, the application has three parts:
- [Input](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/input): In this module, you can upload an OCEL log using the submenu for inserting a log. An example of OCEL is located in [example_OCEL](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/example_OCEL) which contains information about a Purchase-to-Pay process within the objects involved in that such as orders and items. In this module, we visualize the imported OCEL in separate tables that show the attributes of events and objects. Afterward, the user can select the dimensions of the process cube to create a process cube. The details of cube creation steps are found in module cube creation.  The comprehensive information regarding OCEL is explained in [OCEL Standard Document](http://ocel-standard.org/). 
- [Wizard](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/wizard): When the cube is created, it is possible to visualize the process cube in two different windows. The user can simply apply process cube operations such as slice/dice by selecting columns and rows to visualize the cube. There are some possibilities after selecting the desired slices\dices:
    - Visualizing the extracted OCEL: The user can see the extracted event log from process cube operations. Furthermore, the information of objects is shown in separate tables.
    - Discovering an MVP  model: It is possible to discover (frequency/performance annotated) [MVP models](https://arxiv.org/pdf/2001.02562.pdf) from extracted OCEL which shows the process model with all the objects involved in that.
    - Discovering an Object-Centric Petri Net: It is possible to discover an [Object-Centric Petri Nets](https://arxiv.org/pdf/2010.02047.pdf) from extracted OCEL which shows the Petri Net with all the objects involved in that.  
- [Output](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/output): In this module,  we compare the extracted event logs/ MVP  models/ Object-Centric Petri Nets of the selected cells with each other. The process models of the selected slices/dices are configured side-by-side which makes the comparison easy.
## Requirements
To run the application the packages that are specified in  [requirements file ](https://github.com/AnahitaFarhang/object-centric-process-cube/blob/main/requirements.txt) need to be installed on your local system beforehand. These commands are required as the prerequisites for the program:
```
Numpy  1.18.0
Tk 0.1.0
pm4pymdl 0.0.36
Pillow 8.2.0
Tkfilebrowser  2.3.2
Pandastable  0.12.2.post1
Pandas  1.1.4
Toolz  0.11.1
Tkreadonly 0.6.1

```

## Usage
To run the programe, you need only to run the [main module](https://github.com/AnahitaFarhang/object-centric-process-cube/blob/main/main.py).






