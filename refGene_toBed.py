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
with open("refGene_hg19_chr1_single_exon_cleaned_1_24_2019.bed") as tsv:
	for line in csv.reader(tsv, dialect="excel-tab"):
			c1_lines.append(line)
			for word in line:
				c1.append(word)

chroms = c1[2::16] 
starts = c1[9::16]
ends = c1[10::16]
names = c1[12::16]

f = open("refGene_hg19_cse_bedfile_1_24_2019.bed", 'w+')

for i in xrange(len(chroms)):
	print >> f, chroms[i] + "\t" + starts[i] + "\t" + ends[i] + "\t" + names[i]

f.close()

