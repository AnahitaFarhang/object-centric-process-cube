# OCPC: Object-Centric-Process-Cube

This project introduces a stand-alone object-centric process cube tool built on the PM4PY-MDL process mining framework. The application is witten in Python  Tk  GUI  toolkit  as  the  user interface . At the moment, the application has three parts:
- [Input](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/input): In this module, you can uploude an OCEL log using the submenue for inserting a log. An example of OCEL is located in [example_OCEL](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/example_OCEL) which contains information about a Purchase-to-Pay process within the objects involved in that such as orders and items. In this module, we vizualize the imported OCEL in separate tables that show the attributs of events and objects. Afterward, the user can select the dimensions of the process cube to create a process cube. The details of cube creation steps are found in module cube creation.  The comprehensive information regarding OCEL is explained in [OCEL Standard Document](http://ocel-standard.org/). 
- [Wizard](https://github.com/AnahitaFarhang/object-centric-process-cube/tree/main/wizard): When the cube is created, it is possible to vizuialize the process cube in two different windows. The user can simply apply process cube operations such as slice/dice by selecting columns and rows to visuilize the cube. There are some possibilities after selecting the desired slices\dices:
    - Visualizing the extracted OCEL: The user can see the extracted event log from process cube operations. Furthure, the information of objects are shown in separate tables.
    - Discovering an MVP  model : It is possible to discover (frequency/performace annotated) [MVP models](https://arxiv.org/pdf/2001.02562.pdf) from extracted OCEL which shows the process model with all the objects involved in that.
    - Dicoveying an Object-Centric Petri Net: It is possible to discover an[Object-Centric Petri Nets](https://arxiv.org/pdf/2010.02047.pdf) from extracted OCEL which shows the Petri Net with all the objects involved in that.  
- Output
## Requirements
## Usage


