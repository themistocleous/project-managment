# Project Management
This folder contains both code for automating tasks for project management and guidelines and good practices for project management.

# Overall Folder Structure
Each individual has its own repository in the server and a manilla folder with the papers we are using. The root folder is titled with the code name of the participant.

Inside this folder, there is the folder with the materials of the session. Each of these session folders should include the starting date of the session, the code of the participant, and the research timeline info as defined by the research protocol.

Here is an example of a fictional folder structure and how it will look like

```
|-- ABC/
|   |--  2019-08-1_ABC_Phase1_Before/
|   |--  2019-10-1_ABC_Phase1_After/
|
|-- EFG/
|   |--  2019-08-1_EFG_Phase1_Before/
|   |--  2019-10-1_EFG_Phase1_After/
|   |--  2019-08-1_EFG_Phase1_2wp/
|   |--  2019-10-1_EFG_Phase1_3mp/
|   |--  2019-08-1_EFG_Phase2_Before/
|   |--  2019-10-1_EFG_Phase2_After/
|   |--  2019-08-1_EFG_Phase2_2wp/
|   |--  2019-10-1_EFG_Phase2_3mp/
|
|-- HIJ/
|   |--  2019-08-1_HIJ_Phase1_Before/
|   |--  2019-10-1_HIJ_Phase1_After/
|   |--  2019-08-1_HIJ_Phase1_2wp/
|   |--  2019-10-1_HIJ_Phase1_3mp/
|   |--  2019-08-1_HIJ_Phase2_Before/
|...
```

___
# Session Structure 
The session folder, includes hierarchically organized folders with the collected materials from MRI session (if there is a scheduled MRI for that session) and the therapy batteries. 

```
date_experiment_phase/
|-- MRI/
|   |-- MRI_Images
|   |-- MRI_Transformed
|   |-- Notes
|
|-- Sounds/
|   |-- Original/
|   |-- Modified/
|   |-- Notes
|
|-- Batteries
|   |-- ScannedDocsSession/
|   |-- ScannedDocsQoL/
|   |-- Database/
|   |-- Texts/
|
|-- SessionNotes
|   |-- ProcessInfo
|   |-- Notes
|
|-- README.md
```

# Contents of Project Folder
- This is the folder template for the archive. Individuals projects, e.g., rsfMRI denoizing, normalization, statistical analyses, should take place outside this folder. However, the output of these project should be returned for archiving here.

- Scanned Documents of the tests run during the session should be placed in ScannedDocs. 

- Scanned Documents for Quality of Life filled by patients or relatives should be placed inside `ScannedDocsQoL`.  

- Excel files and post-session scoring should be placed inside the `Database/` folder

- SessioNotes/ProcessInfo: this folder contains information about the session from the clinician. For example, notes about the type of assessments that were completed; if there are tests that were not conducted because the patient was tired, etc.

# Folder Template
The "folder_template" contains a template for creating a folder structure for the project. So, for every patient that receives treatment or evaluation, we have a folder structure which is the following:


# Creating Folder Structure
To create this structure, continue reading!
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


## Updates
Created: Sun 8/18/2019
