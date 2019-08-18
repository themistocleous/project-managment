# Project Management
This folder contains both code for automating tasks for project management and guidelines and good practices for project management.

# Folder Template
The "folder_template" contains a template for creating a folder structure for the project. So, for every patient that receives treatment or evaluation, we have a folder structure which is the following:

___
Participant's Code: 

ABC

Inside the folder of the participant, we have subfolders with the data of the evaluation/treatment. The hierarchy of the folder structure for a phase of the experiment is the following:

```
date_experiment_phase/
|-- MRI/
|   |-- MRI_Images
|   |-- Notes
|
|-- Sounds/
|   |-- Original/
|   |-- Modified/
|   |-- Notes
|
|-- Batteries
|   |-- ScannedDocs/
|   |-- Database/
|   |-- Texts/
|
|-- SessionNotes
|   |-- ProcessInfo
|   |-- Notes
|
|-- README.md
```

To create this structure, continue reading!

# Usage
## The hard way
To create this project structure put 'create_project_folder.py' in the directory you want to create the project and run:

> python create_project_folder.py

***Cons:*** But this means that every time you need to move the script in the specific folder, where you want to create the folder structure.

## The easy way
To avoid dealing with the location of the script every time you want to create a project, a better option is to create an alias of the python script in your .bash_profile that points to its location. To do this, you need to open .bash_profile using your favorite editor like emacs or vim but for most users it is easier with 'nano':

> nano ~/.bash_profile

Then write the following at the end of the file:

> alias ctf="python ~/Documents/GTD/project_templates/code/create_project_folder.py"

When you finish editing press
Ctrl + X and then "Yes" to save and exit.

Now, you can run the script simply by typing in all directories that you have sufficient privileges  

> ctf

# Modify
The folder structure depends on your needs, it is not a fixed structure, so make changes accordingly. 

I would love to hear your comments and suggestions.