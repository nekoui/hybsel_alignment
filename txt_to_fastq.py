"""
Converts a text file of 1 sequence per row to a FASTQ file with artificially perfect quality scores.
"Perfect" taken to be 93 per Sanger standards. 
python txt_to_fastq.py inputfile outptfilename
"""

__author__ = "Mahan Nekoui mahan.nekoui@gmail.com"

import sys
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

PERFECT_SCORE = 93

with open(sys.argv[1]) as f:
    probes = f.readlines()

# get rid of newline chars
probes = [probe.replace("\n","") for probe in probes]

# build the artificial "perfect" quality score (93 is the max value in Sanger fastq)
qualList = np.tile(PERFECT_SCORE,len(probes[0])).tolist()

# build the list of seqrecord objects using the probes from the file and the perfect qual score
probeRecords = []
for i in xrange(len(probes)):
    probeRecord = SeqRecord(Seq(probes[i], generic_dna), id=("Probe_%i"%i),
    	description="Artificially perfect quality")
    probeRecord.letter_annotations["phred_quality"] = qualList
    probeRecords.append(probeRecord)

# output the list of seqrecord objects in fastq file format
output_handle = open(sys.argv[2], "w")
SeqIO.write(probeRecords, output_handle, "fastq")