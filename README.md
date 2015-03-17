# hybsel_alignment
A tool to assess the efficacy of probes in a hybrid select capture using BWA.

##Requirements
The process uses [BWA](http://bio-bwa.sourceforge.net/) for aligning and [SAMtools](http://samtools.sourceforge.net/) for alignment analysis. Final analysis will be done in Python (to be written).

##Pipeline outline
First, the list of probes is converted to FASTQ with artificially perfect read scores:
 ```
python txt_to_fastq.py inputfile outptfilename
```

This pipeline is executed by ```align.sh```.
```
bwa index [reference.fasta]
bwa mem [reference.fasta] [probes.fastq] > [alignment.sam]
samtools view -b -o [alignment.bam] [alignment.sam]
samtools sort -O bam -T sort [alignment.bam] > [alignment.sorted.bam]
samtools index [alignment.sorted.bam]
samtools depth [alignment.sorted.bam]
```