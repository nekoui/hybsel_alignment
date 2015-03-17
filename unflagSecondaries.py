"""
Edits a SAM file to remove any flags for secondary alignment. This allows the same probe to be reused in the hybrid select process.
python unflagSecondaries.py alignment.sam
"""

__author__ = "Mahan Nekoui mahan.nekoui@gmail.com"

import sys

filename = sys.argv[1] 
with open(filename) as f:
    content = f.readlines()

newContent = []
for i in xrange(len(content)):
    firstTabIndex = content[i].find('\t')
    secondTabIndex = content[i][firstTabIndex+1:].find('\t')+firstTabIndex+1
    flagArea = content[i][firstTabIndex+1:secondTabIndex]
    if ('256' in flagArea):
        newContent.append(content[i][0:firstTabIndex]+'\t0'+content[i][secondTabIndex:])
    else:
        newContent.append(content[i])
        
with open(filename,'w') as w:
    w.writelines(newContent)