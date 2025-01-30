"""
DNA_Checker.py
(Part of Find the Superbug, Hanzehogeschool, 2025. Written by Loes Oldhoff)

This script will help you analyse and work with .fasta files
Fasta is a file format scientist use to save DNA data
They contain one or more headers (regular fasta or multifasta), these headers
start with the '>' symbol, and contain the name/id of the DNA fragment
The rest of the file contains the sequence (DNA, RNA or protein)
.fasta is just text data, you can open in any text editor

All functions in this script are complete and work, except the main()
all the way at the bottom of the script.
See if you can call the functions in the right order and with the right input
in the def main()
"""

def multifasta_to_multiple_files(filename):
    """ Split a multifasta into multiple files """
    headers = []
    sequences = []
    # Take all data from the multifasta file, append to the lists
    with open(filename, 'r') as multifasta:
        dna = ''
        for line in multifasta:
            line = line.strip()
            if line.startswith('>'):
                headers.append(line)
                if dna:
                    sequences.append(dna)
                    dna = ''
            else:
                dna += line
        sequences.append(dna)

    # Then write data to new files
    for i in range(len(sequences)):
        with open(str(headers[i]).replace('>', '') + '.fasta', 'w') as output_file:
            output_file.write(headers[i] + '\n')
            dna_to_write = sequences[i]
            while len(dna_to_write) > 0:
                output_file.write(dna_to_write[0:70] + '\n')
                dna_to_write = dna_to_write[70:]


def read_fasta(filename):
    """ Reads a .fasta/.fna file and returns the header and sequence as
    separate strings """
    header = ''
    sequence = ''
    with open(filename, 'r') as fasta:
        for line in fasta:
            line = line.strip()
            if line.startswith('>'):
                header += line
            else:
                sequence += line
    print(f"Read Fasta file - Header: \n {header} \n Sequence length: {len(sequence)} Nucleotides")
    return header, sequence


def get_GC_percentage(sequence):
    """Calculates the percentage of C and G nucleotides in a dna sequence
    Takes a string as input
    """
    sequence = sequence.upper()  # Make the DNA sequence all uppercase
    C = sequence.count('C')
    G = sequence.count('G')
    total = len(sequence)
    GC_percentage = ((G+C)/total)*100  # Calculate the average
    print(f"GC Percentage: {GC_percentage}%")


def main():
    """ Dit is de main functie, roep hierin de andere functies aan """
    print("Running DNA_Checker.py")
    # Voeg hier je code toe

main()
