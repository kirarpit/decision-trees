# Decision Trees with Chi-Square

## About
- This is a very basic implementation of a ML technique to make predictions called Decision Trees.
- It uses Gini-index to calculate Information Gain by calculating data impurity/entropy.
- Chi-square test is used to determine when to stop growing the tree.

## Problem Description
Splice junctions are points on a DNA sequence at which superfluous DNA is removed during the process of protein creation in higher organisms. The problem posed in this dataset is to recognise, given a sequence of DNA, the boundaries between exons (the parts of the DNA sequence retained after splicing) and introns (the parts of the DNA sequence that are spliced out). This problem consists of two subtasks: recognising exon/intron boundaries (referred to as EI sites), and recognising intron/exon boundaries (IE sites). (In the biological community, IE borders are referred to as ""acceptors"" while EI borders are referred to as ""donors"".)

Attributes predicted: given a position in the middle of a window 60 DNA sequence elements (called "nucleotides" or "base-pairs"), decide if this is a

- "intron -> exon" boundary (IE) [These are sometimes called "donors"]
- "exon -> intron" boundary (EI) [These are sometimes called "acceptors"]
- neither (N)
