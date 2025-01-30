"""
Protein_Analyser.py
(Part of Find the Superbug, Hanzehogeschool, 2025. Written by Loes Oldhoff)

This script contains one function that can help you scan a translated fragment of DNA for
Open Reading Frames. However, it misses a main() and supporting functions.
Can you complete the script?
"""
import re    # Tells Python we want to use Regular Expressions


def ORF_finder(protein):
    """
    Given a protein sequence, the ORF finder finds amino acid sequences
    starting with a Methionine and ending on a stop codon, also returns
    the longest possible ORF frame in the sequence
    """
    pattern = r'M[A-Z]*\*'
    matches = re.findall(pattern, protein)
    print(f'{len(matches)}, total ORFs found')
    if matches:
        bestmatch = max(matches, key=len)
        print(f'Best match has a length of {len(bestmatch)}')
        print(bestmatch)
    else:
        print("No ORFs found")


