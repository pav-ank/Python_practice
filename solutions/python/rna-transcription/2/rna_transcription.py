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

    if not dna_strand:
        return ''
        
    final_rna = []
    
    mapping = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A', 
        'A' : 'U'
    }
    for base in dna_strand:
        final_rna.append(mapping[base])
    return ''.join(final_rna)
