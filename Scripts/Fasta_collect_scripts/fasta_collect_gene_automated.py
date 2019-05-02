#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################################################################################################################################################################
# 						Script to collect fasta for coding transcripto ##########################################################################################################################################################################################

import re
import sys
import csv
from Bio import SeqIO
import nltk
import time
from collections import defaultdict


# Debut du decompte du temps
start_time = time.time()

# Code

#######################################################################################
#                    To store Ensembl IDs and Fasta into a dictionary                 #
#######################################################################################


def read_fasta(ENS_fasta_file):
    f=open(ENS_fasta_file, "r")
    fasta_dict=defaultdict(str) # create an empty fasta_dict which default caracteristic allows to concatenate the sequences one after the other for the same dictionnary key
    #print("list_line ---» \n", f, "\n")
    name=""
    for line in f:
        #print("test de print de ce fichier fake:", f)
        # if your line starts with a > then it is the name of the following sequence
        if line.startswith('>'):
            # name = line[1:-1]  # here I keep the whole ID being the concatenation of ENSG and ENST IDs
            name = line[1:-1].split("|")[0] # here only I keep the ENSG  ID
            #print("voyons les id collectes ----»", name)
            continue  # this means the code after the continue statement will ne executed when the if condition is not true whereas the code before continue stqtement will be executed when if condition is false

        fasta_dict[name]+=line.strip()
        #print("mes ptites lignes concatenees ouiii-----» \n", fasta_dict, "\n")

    #Store dictionnary results into csv file
    w = csv.writer(open("fasta_dict_results.csv", "w"))
    for key, val in fasta_dict.items():
        w.writerow([key, val])
    return fasta_dict



#######################################################################################
#      To Collect the sequence from the dico to new output fasta file                 #
#######################################################################################

# Initialize the final file that we want to create to have a fasta file with desired ids
# The column index is the number of the column of transcriptome file that contains the Ensembl IDs

def fasta_collect(fasta_file, ID_list_file, output_fasta_file):
	fasta_output_file = open(output_fasta_file, "w") 
	trancriptome_file_of_list_of_IDs= csv.reader(open(ID_list_file, 'r'))
	next(trancriptome_file_of_list_of_IDs) # I skip the header

	#create my fasta_dict
	fasta_dict = read_fasta(fasta_file)
	for row in trancriptome_file_of_list_of_IDs:
	    t = str(row[2])
	    #print(t)
	    sequence=fasta_dict.get(t, "Aïe ca n'est pas dans le dico!")
	    # je me fais une ligne de test ci-dessous
	    #sequence=read_fasta("test_id_genes.fasta").get("t", "Aïe ca n'est pas dans le dico!")

	    fasta_output_file.write(">" + t + "\n" + sequence + "\n")

	fasta_output_file.close()

# Affichage du temps d execution et du nombre de loop effectuées
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

#######################################################################################
#     		  To handle arguments of the script  			              #
#######################################################################################
def usage(error_message=False):
    """
Explain how to use the command line and options
    """
    print("Usage: python PATH/TO/fasta_collect_gene_automated.py [OPTIONS...]")
    print("Use -h, -? or --help to show the below options\n")
    print( "Options:")
    print("  -f, --fasta-file\tSupply a fasta file platform")
    print("  -i, --id-list  \tSupply a file of ID and aliases of genes and transcripts")
    print("  -o, --output    \tOutput file name")
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
    for index, arg in enumerate(sys.argv):
        if arg[0] == "-":
            if arg in ["-h","-?","--help"]:
                usage()
            elif arg in ["-e","--error"]:
                option_dict[arg] = True
            elif arg in ["-f","--fasta-file", "-i", "--id-list",  "-o", "--output"]:
                option_dict[arg] = sys.argv[index+1]
            else:
                usage('Argument "%s" not recognized'%arg)
    if len(sys.argv) == 1:
	print("test du dernier if")
        usage()
    try:
        fasta_collect(option_dict.get("-f") or option_dict.get("--fasta-file"), 
		option_dict.get("-i") or option_dict.get("--id-list"),
                option_dict.get("-o") or option_dict.get("--output"))
    except:
        if "-e" in option_dict.keys() or "--error" in option_dict.keys():
            raise
        else:
            usage('An option is missing, incorrect or not authorized')

if __name__ == '__main__':
    main()
