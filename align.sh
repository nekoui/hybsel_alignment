# align.sh
# Mahan Nekoui mahan.nekoui@gmail.com
# Enacts the main pipeline for the hybsel_alignment tool
# 
# usage ./align.sh [referenceGenome.fasta] [probeList.fastq] [working_directory/]
#
# output of interest: depth.tsv

ref=$1
probes=$2
path=$3

bwa index $ref;
bwa mem -a $ref $probes > $path$"alignment.sam";
python unflagSecondaries.py $path$"alignment.sam";
samtools view -b -o $path$"alignment.bam" $path$"alignment.sam";
samtools sort -O bam -T sort $path$"alignment.bam" > $path$"alignment.sorted.bam";
samtools index $path$"alignment.sorted.bam";
samtools depth $path$"alignment.sorted.bam" > $path$"depth.tsv";