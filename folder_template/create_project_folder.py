'''
Charalambos Themistocleous
2019


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
'''
import os
import sys
import datetime


def main():
    # detect the current working directory and print it
    path = os.getcwd()
    now = str(datetime.datetime.now())
    print("The current working directory is %s" % path)
    # as the user to provide a name for the file.
    participants_code = input("\nProvide Participant's Code: ")
    project_name = input("\nProvide Experiment's Phase: ")
    project_name = str(now[0:9]+"_"+participants_code.upper()+"_"+project_name)
    answer = input(
        "A new project will be created in the %s proceed? (yes or no) " % path)
    if answer.lower() in ["yes", "y", "ok"]:
        try:
            os.mkdir(path + "/" + project_name)
            f = open(path + "/" + project_name + "/" + "README.md", "w+")
            f.write("# " + project_name + "\n" + str(datetime.date.today()))
            f.close()
            os.mkdir(path + "/" + project_name + "/MRI/")
            os.mkdir(path + "/" + project_name + "/MRI/MRI_Images/")
            os.mkdir(path + "/" + project_name + "/MRI/MRI_Transformed/")
            os.mkdir(path + "/" + project_name + "/MRI/Notes/")
            os.mkdir(path + "/" + project_name + "/Sounds/")
            os.mkdir(path + "/" + project_name + "/Sounds/Original/")
            os.mkdir(path + "/" + project_name + "/Sounds/Modified/")
            os.mkdir(path + "/" + project_name + "/Sounds/Notes/")
            os.mkdir(path + "/" + project_name + "/Batteries/")
            os.mkdir(path + "/" + project_name +
                     "/Batteries/ScannedDocsSession/")
            os.mkdir(path + "/" + project_name + "/Batteries/ScannedDocsQoL/")
            os.mkdir(path + "/" + project_name + "/Batteries/Database/")
            os.mkdir(path + "/" + project_name + "/Batteries/Texts/")
            os.mkdir(path + "/" + project_name + "/SessionNotes/")
            os.mkdir(path + "/" + project_name + "/SessionNotes/ProcessInfo/")
            os.mkdir(path + "/" + project_name + "/SessionNotes/Notes/")
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


if __name__ == "__main__":
    main()
