# https://github.com/gitpython-developers/GitPython/blob/c8e303ffd3204195fc7f768f7b17dc5bde3dd53f/git/diff.py#L248
# https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff

import sys
import pandas as pd
import difflib as dl


file1 = "/Users/francescoghizzo/Downloads/pipe-fapesp/ZDB 101 v7/FEI_Metodos especif v2.xlsx"

file2 = "/Users/francescoghizzo/Desktop/FEI_Metodos especif v2.xlsx"

workbook1 = pd.ExcelFile(file1)

workbook2 = pd.ExcelFile(file2)


# first test: diff sheet number and names

sheet_names1 = workbook1.sheet_names

sheet_names2 = workbook2.sheet_names

# add an if here: if sheet_names1 != sheet_names2, print diff, then break. 
# Else, proceed to compare every sheet one by one

sys.stdout.writelines(diff.unified_diff(sheet_names1, sheet_names2))


# second test: diff only sheets which have the same name

sheet_names1_set = set(sheet_names1)

sheet_names2_set = set(sheet_names2)

sheet_names_intersect = set.intersection(sheet_names1_set, sheet_names2_set)

# Here I create a dictionary of dataframes, one for each Excel workbook. 
# The keys are the sheet names and the values store the sheet content

dict1 = {sheet_name: pd.read_excel(workbook1, sheet_name) for sheet_name in sheet_names_intersect}

dict2 = {sheet_name: pd.read_excel(workbook2, sheet_name) for sheet_name in sheet_names_intersect}

differ = False

for key in dict1.keys():

    if dict1[key].equals(dict2[key]):
    
        pass

    else:

        print('Sheet "' + key + '":')
        
        print(dict1[key].compare(dict2[key]))

        differ = True
