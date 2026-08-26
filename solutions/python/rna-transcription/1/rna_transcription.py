"""Exercism : RNA Transcription"""


def to_rna(dna_strand):
    """Determine the RNA complement of a given DNA sequence"""

    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))