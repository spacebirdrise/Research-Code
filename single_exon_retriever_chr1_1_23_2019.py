import pybedtools
import csv
import sys
import os 
import itertools
import numpy
index = 0
c1 = list()
c2 = list()
c1_lines = list()
header = ' '
with open("refGene_hg19_ chr1_1_23_2019.txt") as tsv:
	for line in csv.reader(tsv, dialect="excel-tab"):
			c1_lines.append(line)
			for word in line:
				c1.append(word)

numberOfExons = c1[8::16]

f = open("refGene_hg19_chr1_single_exon_1_24_2019.bed", 'w+')

for i in xrange(len(numberOfExons)):
	if int(numberOfExons[i]) == 1:
		print >> f, c1_lines[i]