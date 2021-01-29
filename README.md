# SMSDG

SMSDG (Semantic Metrics based on semantic dependency graph) is a tool for extraction of file—level semantic metrics.

# Metrics

## Semantic Metric

| Semantic Metric                      | Description                   |
| :------------------------------ | ------------------------------------------------------------ |
| Dependent Count (DC)              | Number of files that semantically depends on the file.     |
| Sum of Dependent Weight (SDW)     |Sum of the semantic weight of the edges formed by fileand the files that semantically depend on it. |
|Average of Dependency Weight (ADW) |Average of the semantic weight of the edges formed by file and the files that semantically depend on it: ADW=SDW/DC.   |
| Longest Dependency Path(LDP)        | Number of files involved in the longest path of file in the semantic dependency graph.      |
| Impact Space File Count (ISF)       | Number of files involved in file’s impact space.          |
| Sum of Files’ Weight (SFW)          | Sum of similarity weights between file and the other files involved in its impact space.      |
| Average of Files’ Weight (AFW)      | Average of similarity weights between file and the other files inits impact space .AFW=SFW/ISF  |
| Impact Space Weight (ISW)           | Sum of the weights of all edges in the sub graph (i.e. the impact space).                 |
|Average Weight of Impact Space (AWIS)| Average weight of file’s impact space: AWIS=ISWf/n, where n is the number of edges in the impact space.|
|Semantic Similarity Sum (SSS)        | Sum of the similarity between a file and all files in the same project.                 |
|Semantic similarity average (SSA)    |Average of the similarity between a file and all files in the same project.  |





# Features




# Usage

###  1) Set up Java environment and Python environment
you should set up Java environment.(jdk1.8)
you should set up Python3.0 environment.(64 bit)
you should set up understand environment.(64 bit)

###  2)Use 
before compile the source code,you should set Program parameters:
< projectName_Write > < projectName > < readString > < writeString >  < udb_path > < Write_path >


- < **projectName_Write** >. The folder for storing data created by the project name, for example: projectName_Write + "_data".
- < ** projectName** >. The name of the project.
- < **filename.csv** >. Project file name exported with [understand].
(https://scitools.com/).
- < **readString** >. Storage path of project file name.
- < **writeString** >.Storage path of exported semantic indicators
- < **udb_path** >.  The path of the UDB generated by the project import [understand]
(https://scitools.com/).
- < **Write_path** >.The storage path of the intermediate file generated by the program.

Please **be sure** to use files in the **same** **format** as the **example**, and ensure that they are in the **same order**, otherwise the results may be inaccurate.

#### Example
before run this project, you should **Compile Configurations** and set Program arguments:
-projectName_Write = "xerces1.2".
-projectName = "xerces-1.2.0-src".
-readString = Project name file path parameter.
-writeString = Semantic metrics file path parameter.
-udb_path = UDB path parameters.
-Write_path=Intermediate file path parameter.

then run the project, You will get the semantic metrics file of this project as shown below:https://github.com/SDGSemantic/SDG_Semanticcode/blob/main/xerces1.2_filename_metric.csv

