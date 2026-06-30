"""Converts a DNA strand into its RNA complement."""
def to_rna(dna_strand):
    """
    Transcribe a DNA strand into its RNA complement.

    Each nucleotide in the DNA strand is replaced according to the rules:
        G → C
        C → G
        T → A
        A → U

    If the input is an empty string, an empty string is returned.

    Args:
        dna_strand (str): A string representing the DNA sequence.

    Returns:
        str: The resulting RNA sequence after transcription.
    """
    final_rna = []
    if not dna_strand:
        return ''
    for strand in dna_strand:
        if strand == 'G':
            strand = 'C'
            final_rna.append(strand)
        elif strand == 'C':
            strand = 'G'
            final_rna.append(strand)
        elif strand == 'T':
            strand = 'A'
            final_rna.append(strand)
        elif strand == 'A':
            strand = 'U'
            final_rna.append(strand)
    return ''.join(final_rna)
