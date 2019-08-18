'''
Charalambos Themistocleous
2018

Project/
|-- writing/
|   |-- figures
|   |-- bib
|
|-- statistics/
|   |-- data/
|   |   |-- data.csv
|   |-- figures/
|
|--speech
|   |-- sounds/
|   |-- textgrids/
|   |-- texts/
|
|-- README.md
'''
import os
import sys
import datetime


def main():
    # detect the current working directory and print it
    path = os.getcwd()
    print("The current working directory is %s" % path)
    # as the user to provide a name for the file.
    project_name = input("Provide project's name: ")
    project_name = str(project_name)
    answer = input(
        "A new project will be created in the %s proceed? (yes or no) " % path)
    if answer.lower() in ["yes", "y", "ok"]:
        try:
            os.mkdir(path + "/" + project_name)
            f = open(path + "/" + project_name + "/" + "README.md", "w+")
            f.write("# " + project_name + "\n" + str(datetime.date.today()))
            f.close()
            os.mkdir(path + "/" + project_name + "/writing/")
            os.mkdir(path + "/" + project_name + "/writing/figures/")
            os.mkdir(path + "/" + project_name + "/writing/bib/")
            os.mkdir(path + "/" + project_name + "/writing/notes/")
            os.mkdir(path + "/" + project_name + "/writing/papers/")
            os.mkdir(path + "/" + project_name + "/literature/")
            os.mkdir(path + "/" + project_name + "/literature/papers/")
            os.mkdir(path + "/" + project_name + "/literature/notes")
            os.mkdir(path + "/" + project_name + "/statistics/")
            os.mkdir(path + "/" + project_name + "/statistics/data/")
            os.mkdir(path + "/" + project_name + "/statistics/figures/")
            os.mkdir(path + "/" + project_name + "/statistics/notes/")
            os.mkdir(path + "/" + project_name + "/materials/")
            os.mkdir(path + "/" + project_name + "/materials/sounds/")
            os.mkdir(path + "/" + project_name + "/materials/texts/")
            os.mkdir(path + "/" + project_name +
                     "/materials/analysis/")
            os.mkdir(path + "/" + project_name + "/materials/notes/")
            os.mkdir(path + "/" + project_name + "/scripts/")
            os.mkdir(path + "/" + project_name + "/scripts/code/")
            os.mkdir(path + "/" + project_name + "/scripts/notes/")
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


if __name__ == "__main__":
    main()
