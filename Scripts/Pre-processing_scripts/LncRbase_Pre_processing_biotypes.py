#!/usr/bin/env python
# coding: utf-8

# # Pre-processing of LncRbase data

# ### Purpose:
# 
# AS collected transcriptomic data from [LncRbase](http://bicresources.jcbose.ac.in/zhumur/lncrbase/) and from [Ensembl](http://useast.ensembl.org/biomart/martview/32011cc110c8a8c35ef655b8dcca331b) (Biomart tool).
# 
# Those data collected from LncRbase are initially from GEO platformand were collected from the GES30567 serie. 
# 
# LncRbase provides its own transcript ID (format is like hsaLB_xxxx) so the purpose of this script is first to associate each hsaLB_id to its corresponding Ensembl gene_id and transcript_id.
# Then, we aim filter out non-ambigous transcripts that are found in brain tissue 

# ### Summary of the steps for lncRNAbase data collecting and completing
# 
# 1- we collect all the biotypes from [LncRbase](http://bicresources.jcbose.ac.in/zhumur/lncrbase/)
# 
# 2- we concatenate ALL biotypes of lncRNA data in the brain together
# 
# 3- we prepare the dataset of the whole lncRNAbase by spliting and reformating the fourth column 
# 
# 4- we make the hsaLB ID of all lnc RNA biotypes in the brain only match with the hsaLB ID of the whole lncRbase (brain and all other tissus of human specie) --» by merging both files 
# 
# 5-  we finally make correspond the whole lncRBase dataset with hsaLB in front of their respective Ensembl trancript ID
# 
# 6- we filter out data being in Ensembl database but not in lncRNA database 
# 
# 7- we filter out ambiguous lncRNAs which have come under more than one biotype, are not associated to Ensembl transcript IDs and are open to more than one interpretation.
# 
# 8- Remove duplicates genes (ENSG id duplicated) to generate a file with unique gene_id only so that make a comparison between the genes from coding transcriptome collected in ABA and those from non-coding transcriptome collected from LncRbase
# 
# 9- We store the results into csv file into results folder

import numpy as np 
import pandas as pd


# ### 1- Collecting all lncRNA biotypes in the brain

import os
path_to_lncRbase_pre_processing_folder= "./"
list_of_hsa_brain_biotypes=[]
for file in os.listdir(path_to_lncRbase_pre_processing_folder):
    if file.endswith(".txt"):
        list_of_hsa_brain_biotypes.append(os.path.join(path_to_lncRbase_pre_processing_folder, file))
print(list_of_hsa_brain_biotypes)


# ### 2- Concatenate all the biotypes files 

all_hsa_brain_biotypes = pd.concat( [ pd.read_table(f) for f in list_of_hsa_brain_biotypes ] )
#print("Attention test de feuuuuu !!!", all_hsa_brain_biotypes)

all_hsa_brain_biotypes.columns=["hsa_id", "Avg_FPKM"]
#print("Attention test de feuuuuu !!!", all_hsa_brain_biotypes)

all_hsa_brain_biotypes.to_csv(path_to_lncRbase_pre_processing_folder + "all_hsa_brain_biotypes")

# ### 3- Preparing the whole lncRNA base dataset 

# Upload the file containing chromosome, position and Ensembl transcript ID for all lnc RNA into data frame

lncRbase_dataset=pd.read_table("./hsa_final_LncRBase_with_chr_pos.csv", delimiter=",")


################# Split the content of the fourth column ################

splited_data=lncRbase_dataset["hsa_id_uncleaned"].str.split("|", n=2, expand=True)
lncRbase_dataset["hsa_id"]=splited_data[0]
lncRbase_dataset["transcript_id"]=splited_data[1]
lncRbase_dataset["gene_name"]=splited_data[2]
lncRbase_dataset.drop(columns =["hsa_id_uncleaned"], inplace = True) 

# ### 4- Match of the hsaLB ID of lncRNA in the brain and the hsaLB ID of the whole lncRNA data

################# Filter the whole previous lncRbase_dataset to keep brain lncRNA only ################

lncRbase_brain_dataset=pd.read_table("./all_hsa_brain_biotypes", delimiter=",")
#print(lncRbase_brain_dataset)

           
############ Recording the results properly within a dedicated file  ###########

################ Merge whole lncRbase data file with brain lncRNA content file ################
merged_whole_lncRbase__with_brain_lnc_file=pd.merge(lncRbase_brain_dataset, lncRbase_dataset, on = lncRbase_brain_dataset.columns[1], how='outer')
print(merged_whole_lncRbase__with_brain_lnc_file)
merged_whole_lncRbase__with_brain_lnc_file.to_csv("data_from_whole_lncRbase_and_brain_LncRbase_merged.csv")


# ### 5- Match of the hsaLB ID of whole lncRNA  and the Ensembl ID 

################# Associate each transcript_id with gene_id ################

################# open the file containing gene and transcript ids################
gene_id_name_trancript_id=pd.read_table("../../Ensembl_GRCh38_biomart_export/gene_id_name_transcript_id_TSL_biotype.txt", delimiter=",")
print(gene_id_name_trancript_id.columns[1])

################ Merge gene and transcript id file with lncRbase file ################
merged_file_containing_id_with_lncRbase_file=pd.merge(gene_id_name_trancript_id, merged_whole_lncRbase__with_brain_lnc_file, on = gene_id_name_trancript_id.columns[1], how='outer')
#merged_file_containing_id_with_lncRbase_file.drop(columns=["gene_id"], inplace=True)
print(merged_file_containing_id_with_lncRbase_file)

############ Recording the results properly within a dedicated file  ###########

merged_file_containing_id_with_lncRbase_file.to_csv("data_from_Ensembl_and_LncRbase_merged.csv")


# ### 6- Extract the data of lncRNA in the brain only 
# #### the principle is to remove any data without its FPKM value mesuring transcript quantity in the brain

data_from_Ensembl_and_LncRbase_merged=pd.read_table("data_from_Ensembl_and_LncRbase_merged.csv", delimiter=",")
#print(data_from_Ensembl_and_LncRbase_merged)

#Let’s delete all rows not corresponding to lnc RNA data i.e all rows for which column ‘Avg_FPKM’ is empty
LncRbase_in_brain_only_with_Ensembl_ID = data_from_Ensembl_and_LncRbase_merged[ data_from_Ensembl_and_LncRbase_merged.Avg_FPKM.notnull()]

print("check du dataset de lncRNA only in the brain", LncRbase_in_brain_only_with_Ensembl_ID)
LncRbase_in_brain_only_with_Ensembl_ID.to_csv("LncRbase_in_brain_only_with_Ensembl_ID.csv")


# ### 7- we filter out ambiguous lncRNAs which have come under more than one biotype, are not associated to Ensembl transcript IDs and are open to more than one interpretation.

#Let’s delete all rows not corresponding to non ambigous lnc RNA data i.e all rows for which column ‘gene_id’ is empty
LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous = LncRbase_in_brain_only_with_Ensembl_ID[ LncRbase_in_brain_only_with_Ensembl_ID.gene_id.notnull()]

print("check du dataset de lncRNA only in the brain", LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous)

LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous.to_csv("LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous.csv")


# ### 8 - remove duplicates genes (ENSG id duplicated) to generate a file with unique gene_id only 

import subprocess

subprocess.call(['./LncRbase_in_brain_only_genes_duplicates_counts.sh']) 

# two files are created:
## LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous_genes_duplicates_only.csv  

## LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous_genes_duplicates_counts.csv 

## the second file could be used for a comparison with ABA genes list.

# ### 9- Store the results into csv file into results folder

#Create the results folder

results_folder="../Preprocessed_Output_files/"

try:
    os.mkdir(results_folder)
except OSError:
    pass

# Store the preprocesed outputfile into the folder
LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous.to_csv(results_folder + "final_output_LncRbase_preprocessed.csv")




