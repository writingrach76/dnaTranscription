# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:18:06 2021

@author: Ryan
"""

#PRESENT the dictionary
#RT
"""
Global dictionary mapping each codon of 3 nucleotides to its resultant
amino acid name.
"""
translationDict = {
    "UUU":"Phenylalanine",
    "UUC":"Phenylalanine",
    "UUA":"Leucine",
    "UUG":"Leucine",
    "UCU":"Serine",
    "UCC":"Serine",
    "UCA":"Serine",
    "UCG":"Serine",
    "UAU":"Tyrosine",
    "UAC":"Tyrosine",
    "UAA":"Stop",
    "UAG":"Stop",
    "UGU":"Cysteine",
    "UGC":"Cysteine",
    "UGA":"Stop",
    "UGG":"Tryptophan",
    "CUU":"Leucine",
    "CUC":"Leucine",
    "CUA":"Leucine",
    "CUG":"Leucine",
    "CCU":"Proline",
    "CCC":"Proline",
    "CCA":"Proline",
    "CCG":"Proline",
    "CAU":"Histidine",
    "CAC":"Histidine",
    "CAA":"Glutamine",
    "CAG":"Glutamine",
    "CGU":"Arginine",
    "CGC":"Arginine",
    "CGA":"Arginine",
    "CGG":"Arginine",
    "AUU":"Isoleucine",
    "AUC":"Isoleucine",
    "AUA":"Isoleucine",
    "AUG":"Methionine",
    "ACU":"Threonine",
    "ACC":"Threonine",
    "ACA":"Threonine",
    "ACG":"Threonine",
    "AAU":"Asparagine",
    "AAC":"Asparagine",
    "AAA":"Lysine",
    "AAG":"Lysine",
    "AGU":"Serine",
    "AGC":"Serine",
    "AGA":"Arginine",
    "AGG":"Arginine",
    "GUU":"Valine",
    "GUC":"Valine",
    "GUA":"Valine",
    "GUG":"Valine",
    "GCU":"Alanine",
    "GCC":"Alanine",
    "GCA":"Alanine",
    "GCG":"Alanine",
    "GAU":"Aspartic acid",
    "GAC":"Aspartic acid",
    "GAA":"Glutamic acid",
    "GAG":"Glutamic acid",
    "GGU":"Glycine",
    "GGC":"Glycine",
    "GGA":"Glycine",
    "GGG":"Glycine"
}

#RT
#PRESENT THIS
"""
This method takes in a string of nucleotides and checks in groups of 3 until
it finds a starting codon 'AUG' and returns the index where it starts, or
-1 if its not found
"""
def analyzeDNA(line):
    toReturn = -1
    i = 0
    for i in range(len(line)-2):
        codon = line[i:i+3]
        if startCodon(codon):
            toReturn = i
            break

    return toReturn

#RT
#PRESENT THIS
"""
This method takes in a list of codons and returns a list truncated
at the stop codon
"""
def analyzeCodons(codons):
    temp = 0
    for c in codons:
        if stopCodon(c):
            break
        temp+=1
    
    return codons[:temp]

#RT
"""
Returns True if codon is UAG, UGA, or UAA otherwise False
"""
def stopCodon(codon):
    return codon == "UAG" or codon == "UGA" or codon == "UAA"

#RT
"""
Returns True if given codon is AUG otherwise False
"""
def startCodon(codon):
    return codon == "AUG"

#RW  
"""
Given a string of nucleotides and the index of the start codon
this method will return a list of codons beginning with the
starting codon
"""
def toCodons(line, startCodon):
    split_strings = []
    n  = 3
    for index in range(startCodon, len(line)-2, n):
        split_strings.append(line[index : index + n])

    return split_strings

#RW
"""
Converts the DNA nucleotides into their corresponding RNA value
"""
def convertDNAToRNA(line):
    toReturn = ''
    for character in line:
        if character == 'A':
            toReturn = toReturn + 'U'
        elif character == 'T':
            toReturn = toReturn + 'A'
        elif character == 'C':
            toReturn = toReturn + 'G'
        elif character == 'G':
            toReturn = toReturn + 'C'
    return toReturn

#RW
"""
Converts the RNA nucleotides into their corresponding DNA value
"""
def convertRNAtoDNA(line):
    toReturn = ''
    for character in line:
        if character == 'A':
            toReturn = toReturn + 'T'
        elif character == 'T':
            toReturn = toReturn + 'A'
        elif character == 'C':
            toReturn = toReturn + 'G'
        elif character == 'G':
            toReturn = toReturn + 'C'
    return toReturn

#RW
"""
Taking in a list of codons, this translates from a list of nucleotide
triplets to the name of the Amino Acid
"""
def convertRNAtoCodons(codons):
    toReturn = []
    for codon in codons:
        toReturn.append(translationDict[codon])
    return toReturn

#RT +  RW
"""
Opening the file, and for each line of the file analyzing the line of
DNA and printing the resultant list of amino acids. 
"""
inputFile= open("inputFile.txt", "r")
Lines = inputFile.readlines()

for line in Lines:
    line = line.strip()
    line = convertDNAToRNA(line)
    
    start = analyzeDNA(line)
    if start != -1:
        codons = analyzeCodons(toCodons(line, start))
        print(convertRNAtoCodons(codons))
    
    for character in line:
        pass

inputFile.close()