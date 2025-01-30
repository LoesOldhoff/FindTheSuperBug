"""
DNA_Checker.py
(Part of Find the Superbug, Hanzehogeschool, 2025. Written by Loes Oldhoff)

This script will help you translate DNA to protein, similar to what happens in our cells (and of course in bacteria!)
However, this script is not in working order yet. The most important function, translate() is broken
Can you repair it?

Once your have made a Protein Translation, you can use 'write_fasta()' to write it to a new .fasta file
"""

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
    print(f"Read 1 Fasta file - Gene found: \n {header} \n Sequence length: {len(sequence)} Nucleotides")
    return header, sequence

def translate(sequence):
    """Takes a nucleotide (dna) sequence and translates it to protein
    similar to what a human ribosome would do
    Returns a list of 3 protein sequences (for the 3 reading frames)
    """
    codontab = {
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S',
        'TCT': 'S', 'TTC': 'F', 'TTT': 'F',
        'TTA': 'L', 'TTG': 'L', 'TAC': 'Y',
        'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*',
        'TGG': 'W', 'CTA': 'L', 'CTC': 'L',
        'CTG': 'L', 'CTT': 'L', 'CCA': 'P',
        'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q',
        'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
        'CGG': 'R', 'CGT': 'R', 'ATA': 'I',
        'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T',
        'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
        'AAA': 'K', 'AAG': 'K', 'AGC': 'S',
        'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
        'GTT': 'V', 'GCA': 'A', 'GCC': 'A',
        'GCG': 'A', 'GCT': 'A', 'GAC': 'D',
        'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G',
        'GGT': 'G'}

    proteins = []
    for frame in range(3):   #  Runs the code 3 times, one time for each reading frame
        sequence_to_translate = sequence[frame:]
        for i in range(0, len(sequence_to_translate), 3):
            codon = sequence_to_translate[i: i+3] 
            print(codon)
        
            # Insert missing code here 
    
    return proteins

def write_fasta(header, sequence, output_filename):
    """Writes a fasta file. needs to be given a header, a sequence and
    a filename (if not present, file will be made upon running the code)

    Careful!! This function can and will write over existing files and erase them
    Mind the filename!!
    """
    with open(output_filename, 'w') as output:
        output.write(header + '\n')
        while len(sequence) > 0:
            output.write(sequence[0:70] + '\n')
            sequence = sequence[70:]

def main():
    file_to_translate = ''
    header, sequence = read_fasta(file_to_translate)
    protein = translate(sequence)
    write_fasta(header, protein, 'test_output.fasta')


main()
