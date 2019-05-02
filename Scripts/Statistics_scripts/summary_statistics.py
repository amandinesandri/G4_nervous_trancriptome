#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import sys
import matplotlib.patches
import pylab

data1=valeurs pour une catégorie en particulier

data_01 = [1,2,3,4,5,6,7,8,9]
data_02 = [15,16,17,18,19,20,21,22,23,24,25]
data_03 = [5,6,7,8,9,10,11,12,13]

BoxName = ['data 01','data 02','data 03']

data = [data_01,data_02,data_03]

plt.boxplot(data)

plt.ylim(0,30)

pylab.xticks([1,2,3], BoxName)

plt.savefig('MultipleBoxPlot02.png')
plt.show()
 

def box_plot(file_name, category):
    df=pd.read_csv(file_name)
    values = df[category].value_counts().keys().tolist()
    counts = df[category].value_counts().tolist()
    patches, texts = plt.pie(counts, startangle=90)
    plt.legend(patches, values, loc="lower")

    plt.title('Percentage_of_' + category)

    handles = []
    for i, l in enumerate(values):
        handles.append(matplotlib.patches.Patch(color=plt.cm.Set3((i)/8.), label=l))
        plt.legend(handles,values, bbox_to_anchor=(0.85,1.025), loc="upper left")
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    
        plt.savefig(category+"_box_plot"+'.png')
        table=pd.DataFrame({
        'category':values,
        'count':counts})
        
    table.to_csv(category+"_counts")

def usage(error_message=False):
    """
    Provide the user with instructions to use add_features.py.    
    """
    print("Usage: python PATH/TO/add_features.py [OPTIONS...]")
    print("Use -h, -? or --help to show this message\n")
    print("Options:")
    print("  -f, --file-name\tTake the name of the file where there is the features to be plotted")
    print("  -n, --column-name    \tTake the name of the column containing the values to be plotted")
    print("  -c, --category     \tTake the name of the column containing the categories to be plotted")
    print("  -e, --error     \tRaise errors and exceptions\n")
    if error_message:
        print("UsageError:", error_message)
        sys.exit(500)
    else:
        sys.exit(0)

def main():
    """
    Handles arguments.
    """
    option_dict = {}
    for no, arg in enumerate(sys.argv):
        if arg[0] == "-":
            if arg in ["-h","-?","--help"]:
                usage()
            elif arg in ["-v","--verbose",
                    "-e","--error"]:
                option_dict[arg] = True
            elif arg in ["-f","--file-name",
                    "-c","--category"]:
                option_dict[arg] = sys.argv[no+1]
            else:
                usage('Argument "%s" not recognized'%arg)
    if len(sys.argv) == 1:
        usage()
    try:
        box_plot(option_dict.get("-f") or option_dict.get("--file-name"),
                option_dict.get("-c") or option_dict.get("--category"))
    except:
        if "-e" in option_dict.keys() or "--error" in option_dict.keys():
            raise
        else:
            usage('An option is missing, incorrect or not authorized')

if __name__ == '__main__':
    main()
