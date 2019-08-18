# Project Management and Automation
This document contains guidelines and good practices for organizing the project materials. It also contains scripts for automating folder structure generation.

# Project Folder Structure
Each individual has its own repository in the server and a manilla folder with the papers, we are using. The root folder should be titled with the code name of the participant.

Inside this folder, there should be the folder with the materials of the session. The name of each of these session-folders should include the starting date of the session, the code of the participant, and the research timeline info as defined by the research protocol.

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
# Session Folder Structure 
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

# Contents of the session Folder
- **MRI:** This is the folder template for the archive. Individuals projects, e.g., rsfMRI denoising, normalization, statistical analyses, should take place outside of this folder. However, the output of these analyses should be returned for archiving here.

- **Sounds:** It contains the recordings collected for that session. Each sound should be labelled as using Date, Participant's Code, and Phase, e.g.,

> 2019-08-1_HIJ_Phase1_Before.wav

Note this is needed as we will be moving materials for analysis or merging. So, it does not matter if we know this information because of the folder structure, we will still need to have this specific naming convention to avoid ambiguities during the analysis.

- **Batteries:** Scanned Documents of the tests run during the session should be placed in ScannedDocs. 

- **ScannedDocsQoL:** Scanned Documents for Quality of Life filled by patients or relatives should be placed inside `ScannedDocsQoL`.  

- **Database:** Excel files and post-session scoring should be placed inside the `Database/` folder

- **SessioNotes/ProcessInfo:** this folder contains information about the session from the clinician. For example, notes about the type of assessments that were completed; if there are tests that were not conducted because the patient was tired, etc.

# Folder Template
The "folder_template" contains a template for creating a folder structure for the project. So, for every patient that receives treatment or evaluation, we have a folder structure which is the following:


# Creating Folder Structure Automatically
To create this folder structure using the script, continue reading!

## The hard way
Copy 'create_project_folder.py' in the directory you want to create the project and run:

> python create_project_folder.py

***Cons:*** This means that every time you need to use the script, you have to move the script into the specific folder, where you want to create the folder structure.

## The easy way
To avoid dealing with the location of the script every time you want to create a project, a better option is to create an alias of the python script in your .bash_profile that points to its location. To do this, you need to open .bash_profile using your favorite editor like emacs or vim but for most users it is easier with 'nano':

> nano ~/.bash_profile

Then write the following at the end of the file:

> alias ctf="python ~/Documents/GTD/project_templates/code/create_project_folder.py"

When you finish editing press
Ctrl + X and then "Yes" to save and exit.

Now, you can run the script simply by typing in all directories that you have sufficient privileges  

> ctf

## Endnote
The guide is written in Markdown and I use pandoc to generate docx. 

## Updates
Created: Sun 8/18/2019
