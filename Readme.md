
# [G4_nervous_trancriptome] About this project

This repository **G4_nervous_trancriptome** takes part of the global project on [G-Quadruplexes](http://jpperreaultlab.recherche.usherbrooke.ca/fr/G-quadruplexes.php). 
The prupose of this sub-project is to predict G4 structures in the transcriptome of human brain cells .

We mainly chose to use Python with pandas, and Biopython modules.

# Flowchart : Overview of the pipeline 

![Flowchart](https://docs.google.com/drawings/d/14Cs5iPMS-Z0vcLpsSVie-r3-KFr1PyowFp3akx_Seuk/export/png)

# Start the Data Pre-processing

## 1) Prepare your environment 

The directories are set up as below. You will need to download and store the folder "Databases".

```
./Home
└── Databases
   │ 
   │── Coding_Transcriptome
   │   │── ABA_genes_with_corresponding_Ensembl_ID.csv
   │   │── Genes.csv
   │
   ├── Ensembl_GRCh38_biomart_export
       │── Ensembl_whole_human_transcriptome.fasta
       │── Ensembl_whole_human_genome.fasta
   │  
   └── lncRbase_transcriptome
       │── all_hsa_brain_biotypes
       │── LncRbase_in_brain_only_with_Ensembl_ID_without_ambigous
 └── Scripts
   │ 
   │── Pre-processing_scripts
   │   │── LncRbase_Pre_processing_biotypes.py
   │   │── coding_transcriptome_preprocessing.py
   │
   ├── Fasta_collect_scripts
       │── fasta_collect_gene_automated.py
       │── fasta_collect_transcript_automated.py
   ├── Statistics_scripts
       │── add_features.py
       │── box_plot.py
       │── summary_statistics.py
```

|Folder                               |Where to find it             |Content             |
|--------------------                 |-------------------        |:-----------------: |
|**Databases**                           |Clone the repository available on github <br/> https://github.com/amandinesandri/G4_nervous_trancriptome/                 |All datasets used to predict G4 |
|   **Coding_Transcriptome**             |Inside Databases folder   |Contains all Allen Brain Atlas RNA-seq datasets and dedicated processing scripts |
|   **Ensembl_GRCh38_biomart_export**    |Inside Databases folder   |Contains the whole genome and transcriptome features (list of IDs + FASTA files) |
|   **lncRbase_transcriptome**          |Inside Databases folder   |Contains lncRNA expression in different tissues and dedicated processing scripts |
|**Scripts**                           |Clone the repository available on github <br/> https://github.com/amandinesandri/G4_nervous_trancriptome/                 |All scripts used to preprocess data, collect their fasta, generate statistics and plot results |
## 2) Run command lines

### Data preprocessing scripts
These scripts launch the preprocessing of LncRbase data and Allen Brain Atlas data. Therefore, you should download the **lncRbase_pre_processing** folder, **Coding_Transcriptome** folder and **Ensembl_GRCh38_biomart_export** folder from the **Databases** folder of this **G4_nervous_trancriptome** repository.

*Note: It is important to pay attention that the script is executed in the same directory *

```bash
python LncRbase_Pre_processing_biotypes.py 
```

```bash
python coding_transcriptome_preprocessing.py
```

### Fasta outputs
This script allows to create fasta file corresponding to the previous brain transcritpome datasets generated. 

```bash

Usage: python PATH/TO/fasta_collect_gene_automated.py [OPTIONS...]
Use -h, -? or --help to show the below options

Options:
  -f, --fasta-file	Supply a fasta file platform
  -i, --id-list  	Supply a file of ID and aliases of genes and transcripts
  -o, --output    	Output file name
  -e, --error     	Raise errors and exceptions

```

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
