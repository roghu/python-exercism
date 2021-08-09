DNA_TO_RNA = {"C": "G", "G": "C", "T": "A", "A": "U"}


def to_rna(dna_strand: str) -> str:
    return "".join(DNA_TO_RNA[letter] for letter in dna_strand)
