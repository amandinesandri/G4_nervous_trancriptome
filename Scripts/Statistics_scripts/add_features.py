#!/usr/bin/env python
from Bio import SeqIO
import sys
import re

import pandas as pd
import os

#print("\n\n\n Please pay attention to have well modified the file containing the features. The column that contains all ENSGxxxx gene IDs must be named \"description\" \n\n Please make also sure the delimiters of both prediction and feature files are tabulation \n\n")
def features(prediction_score_file, features_file, output):
	"""
	Add features from Ensembl to prediction file from G4screener
	"""
	prediction=pd.read_csv(prediction_score_file, sep=None, engine="python") #open prediction file obtained from G4 screene
	features=pd.read_csv(features_file, sep=None, engine='python') #open features file downloaded from Biomart

	merge=pd.merge(prediction, features, on = prediction.columns[1], how='outer') #merge following ENSG ID
	#remove all IDs in features file but not in prediction file
	merge.dropna(axis=0, how='any', inplace=True)	
	merge.to_csv(output)



def usage(error_message=False):
    """
    Instructions to use this script add_features.py.    
    """
    print "Usage: python PATH/TO/add_features.py [OPTIONS...]"
    print "Use -h, -? or --help to show this message\n"
    print "Options:"
    print "  -p, --prediction-file\tTake the file obtained from G4screener"
    print "  -f, --features     \tTake the name of the Features file and its path"
    print "  -o, --output    \tTake the name of the Output file and its path"
    print "  -e, --error     \tRaise errors and exceptions\n"
    if error_message:
        print "UsageError:", error_message
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
            elif arg in ["-f","--features",
                    "-p","--prediction-file",
                    "-o","--output"]:
                option_dict[arg] = sys.argv[no+1]
            else:
                usage('Argument "%s" not recognized'%arg)
    if len(sys.argv) == 1:
        usage()
    try:
        features(option_dict.get("-p") or option_dict.get("--prediction-file"),
		option_dict.get("-f") or option_dict.get("--features"),
                option_dict.get("-o") or option_dict.get("--output"))
    except:
        if "-e" in option_dict.keys() or "--error" in option_dict.keys():
            raise
        else:
            usage('An option is missing, incorrect or not authorized')

if __name__ == '__main__':
    main()
