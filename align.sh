ref=$1
probes=$2
path=$3

bwa index $ref;
bwa mem $ref $probes > $path$"alignment.sam";
samtools view -b -o $path$"alignment.bam" $path$"alignment.sam";
samtools sort -O bam -T sort $path$"alignment.bam" > $path$"alignment.sorted.bam";
samtools index $path$"alignment.sorted.bam";
samtools depth $path$"alignment.sorted.bam" > $path$"depth.tsv";