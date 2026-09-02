"""Exercism: Hamming"""


def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands of equal length."""
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b))