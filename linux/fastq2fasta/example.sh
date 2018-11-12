#!/bin/bash

awk '{if(NR%4 == 1){print ">" substr($0, 2)}}{if(NR%4 == 2){print}}' test.fastq > out.fa
