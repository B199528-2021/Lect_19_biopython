#!/usr/local/bin/python3

import os
import subprocess
import shutil
import re
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO


# NCBI requirement
Entrez.email = "s2223450@ed.ac.uk"

# # get the api key 
# api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip()
# print("My API key:")
# print(api_key.decode('utf-8'))

# Entrez.api_key = api_key.decode('utf-8')

# search NCBI using COX1 and mammals as organism
print("\nNCBI search result:")
protein_result = Entrez.read(Entrez.esearch(db="protein", term="COX1[PROT] AND mammals[ORGN] NOT PARTIAL"))
print(protein_result)

# get the number of records
print("\nNumber of records:")
print(protein_result["Count"])


# get the average length of the proteins

# get the GI/accession numbers
print("\nAccession numbers:")
print(protein_result['IdList'])
acclist = protein_result['IdList']

# test for one accessionnumber first
print("\nTest for one accession number first:")
accession = acclist[0]
print(accession)

# get the fasta record 
print("\nFASTA record:")
fasta_file = Entrez.efetch(db="protein",id=accession,rettype="fasta")
record = SeqIO.read(fasta_file, "fasta")
print(record)

# get the genbank record 
print("\nGenbank record:")
gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
record = SeqIO.read(gb_file, "genbank")
print(record)



exit()

# to avoid regenerating every time:
records = SeqIO.parse(protein_result, "genbank")
MyGenbank_record = next(records)

print(MyGenbank_record)





# # loop through accession numbers
# for accessionnr in acclist:
    
    # 
    