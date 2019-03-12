
# [G4_nervous_trancriptome] About this project

This repository **G4_nervous_trancriptome** takes part of the global project on [G-Quadruplexes](http://jpperreaultlab.recherche.usherbrooke.ca/fr/G-quadruplexes.php). 
The prupose of this sub-project is to predict G4 structures in the transcriptome of human brain cells .

We mainly chose to use Python with pandas, and Biopython modules.

# Flowchart : Overview of the pipeline 

![Flowchart](https://docs.google.com/drawings/d/14Cs5iPMS-Z0vcLpsSVie-r3-KFr1PyowFp3akx_Seuk/export/png)

# Start the Data Pre-processing

## 1) Prepare your environment 

The directories are set up as below. You will need to download and store the folder "Databases" in your Home.

```
./Home
└── Databases
   │ 
   │── Coding_Transcriptome
   │   │── allen_brain_atlas_microrray_experiment_dataset
   │   │── fasta_seq_collection
   │
   ├── Ensembl_GRCh38_biomart_export
   │  
   └── lncRbase_pre_processing
       │── lncRNA_hsa_biotypes
       │── fasta_seq_collection
```

|Folder                               |Where to find it             |Content             |
|--------------------                 |-------------------        |:-----------------: |
|**Databases**                           |Clone the repository available on github <br/> https://github.com/amandinesandri/G4_nervous_trancriptome/                 |All datasets and processing scripts |
|   **Coding_Transcriptome**             |Inside Databases folder   |Contains all Allen Brain Atlas RNA-seq datasets and dedicated processing scripts |
|   **Ensembl_GRCh38_biomart_export**    |Inside Databases folder   |Contains the whole genome and transcriptome features (list of IDs + FASTA files) |
|   **lncRbase_pre_processing**          |Inside Databases folder   |Contains lncRNA expression in different tissues and dedicated processing scripts |

## 2) Run command lines

### Build the local database
First, download the required folder (Databases) and store it into a folder named "320GB"

### Data preprocessing scripts
These scripts launch the preprocessing of LncRbase data and Allen Brain Atlas data. Therefore, you should download the **lncRbase_pre_processing** folder, **Coding_Transcriptome** folder and **Ensembl_GRCh38_biomart_export** folder from the **Databases** folder of this **G4_nervous_trancriptome** repository.

```bash
python LncRbase_Pre_processing_biotypes.py 
```

```bash
python coding_transcriptome_preprocessing.py
```

### Fasta outputs
This script allows to create fasta file corresponding to the previous brain transcritpome datasets generated. 

```bash
python /Home/Databases/lncRbase_pre_processing/lncRNA_hsa_biotypes/script_to_collect_fasta_files.py
```

*Note: the python files are also available in Jupyter Notebook format .ipynb for a better vizualisation of the data created step by step*

# Useful links 
Datasets can be downloaded from following platform :

[Ensembl website](www.ensembl.org)

[LncRbase platform](http://bicresources.jcbose.ac.in/zhumur/lncrbase/)

[Allen Brain Atlas platform](http://human.brain-map.org/static/download)

# References

 Roberto  Simone, G-quadruplexes : Emerging roles in neurodegenerative diseases and the non-coding transcriptome. 589(14) :1653–1668  

# Authors
```
This file is part of Pr. Scott's lab and Perreault's lab teams in the context of G-quadruplexes researches

```
