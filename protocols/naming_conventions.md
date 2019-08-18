# File Naming Conventions
This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.

Many researchers have their own coding style guidelines. In the event of any conflicts, such project-general guides take precedence for the project.

## General
1. ***Dates format:*** YYYY_MM_DD 2019_08_16 (zero padded dates).
2. ***Numbers:*** For sequential numbering, use leading zeros to ensure files sort properly. For example, use "01, 02 ... 09, etc” instead of "1, 2 ... 9, etc.". Else files are getting sorted in unexpected ways for instance 1, 10, 2, etc.
3. ***Characters and Spaces:*** Do not use special characters and spaces all together (like ~ ! @ # $ %, etc). Spaces are not recognized by some software.
Use underscores (file_name), dashes (file-name), no separation (filename), or camel case (FileName) instead.
4. Naming Consistency is extremely important.

## Context 
1. Do not use cryptic codes (e.g. even you, will forget what is the meaning of this name: asdj243–1sdf.docx in a couple of months). The filenames should be clear for everybody.
2. Avoid using names that are too general or too wordy. You need to strike a good balance between the two. So,
- **Very generic names or very long names are bad:** 
    - a_structure, my_list, info 
    - svPPA_primary_progressive_aphasia_mri_data_and_spel8ling_materials_battery.txt
    - Don’t name "a", "b", or “me”.
- **Short Names and specific are good:** DNN_Phase1_MRI.t1, DNN_Spelling.xls
3. When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)

## Naming Sounds, Batteries, and MRI materials
08_16_2019_Pre_Phase1_ABN_XXXXX.wav

Date_Experiment_Participant.extension


## Updates
Created: Sat 8/17/2019