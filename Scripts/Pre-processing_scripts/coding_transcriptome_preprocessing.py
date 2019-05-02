#!/usr/bin/env python
# coding: utf-8

# # Pre-processing of Allen Brain Atlas Genes

# ### Purpose:
# 
# AS collected transcriptomic data from [Allen Brain Atlas](http://human.brain-map.org/static/download) (ABA) and from [Ensembl](http://useast.ensembl.org/biomart/martview/32011cc110c8a8c35ef655b8dcca331b) (Biomart tool).
# 
# Data from ABA have been generated from RNA-sequencing of two postmortem brain from males and females between 18 and 68 years of age, with no known neuropsychiatric or neuropathological history.
# 
# Microarray expression values and rna-seq counts are also provided for each probe targeting a specific gene in 95 samples. The list of the symbols of the genes targeted is also given with their entrez_id associated.
# The purpose of this script is first to associate those gene identifiers to their corresponding Ensembl gene_id and transcript_id and then to filter on rna-seq counts to identify which gene are mostly expressed in the human brain.


import pandas as pd
import os


# ### 1- Collecting all ABA gene names

################# open the file containing list of genes expressend in the human brain ################

mRNA=pd.read_table("./Genes.csv", delimiter=",")
#print(mRNA)


# ### 2- Match of the ABA gene names with the Ensembl ID 

################# open the file containing Ensembl gene and transcript ids################
gene_id_name_trancript_id=pd.read_table("../../../Ensembl_GRCh38_biomart_export/gene_id_name_biotype.txt", delimiter=",")
print(gene_id_name_trancript_id.columns[1])


################ Merge gene and transcript id file with whole ABA gene list file ################
merged_file_containing_id_with_ABA_file=pd.merge(gene_id_name_trancript_id, mRNA, on = gene_id_name_trancript_id.columns[1], how='outer')
#merged_file_containing_id_with_lncRbase_file.drop(columns=["gene_id"], inplace=True)
print(merged_file_containing_id_with_ABA_file)

############ Recording the results properly within a dedicated file  ###########

merged_file_containing_id_with_ABA_file.to_csv("ABA_genes_among_all_ensembl_dataset.csv")

ABA_genes_among_all_ensembl_dataset=pd.read_table("ABA_genes_among_all_ensembl_dataset.csv", delimiter=",")
#print(ABA_genes_among_all_ensembl_dataset)

#Let’s delete all rows for which column ‘gene_id_y’ is empty (it corresponds to data that is absent in ABA)

ABA_genes_with_corresponding_Ensembl_ID = ABA_genes_among_all_ensembl_dataset[ ABA_genes_among_all_ensembl_dataset.gene_id_y.notnull()]

print("petit check number one:", ABA_genes_with_corresponding_Ensembl_ID)


ABA_genes_with_corresponding_Ensembl_ID.to_csv( "ABA_genes_with_corresponding_Ensembl_ID.csv")


#Create the results folder

results_folder="../../Preprocessed_Output_files/"

try:
    os.mkdir(results_folder)
except OSError:
    pass

# Store the preprocesed outputfile into the folder

ABA_genes_with_corresponding_Ensembl_ID.to_csv(results_folder + "final_output_ABA_genes_preprocessed.csv")
####################################"TEMPORAIRE EN ATTENDANT DE MACTHER TOUS LES ALIAS SYNONYMES#################################"
#Let’s delete all rows for which column ‘gene_id_x’ is empty (it corresponds to data that has been detected in ABA but has not the same alias as in Ensembl )

ABA_genes_with_corresponding_Ensembl_ID_TEMPORARY = ABA_genes_with_corresponding_Ensembl_ID[ ABA_genes_with_corresponding_Ensembl_ID.gene_id_x.notnull()]

print("petit check number one:", ABA_genes_with_corresponding_Ensembl_ID_TEMPORARY)