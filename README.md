# hybsel_alignment
A tool to assess the efficacy of probes in a hybrid select capture using BWA.

#Pipeline outline
'''
bwa index [reference.fasta]
bwa mem [reference.fasta] [probes.fastq] > [alignment.sam]
samtools view -b -o [alignment.bam] [alignment.sam]
samtools sort -O bam -T sort [alignment.bam] > [alignment.sorted.bam]
samtools index [alignment.sorted.bam]
samtools depth [alignment.sorted.bam]
'''