from enum import IntEnum
from typing import Tuple, List


Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


# For illustrative purposes
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        middle: int = (low + high) // 2
        if gene[middle] < key_codon:
            low = middle + 1
        elif gene[middle] > key_codon:
            high = middle - 1
        else:
            return True
    return False


if __name__ == "__main__":
    my_gene: Gene = string_to_gene(gene_str)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

    my_sorted_gene: Gene = sorted(my_gene)
    assert binary_contains(my_sorted_gene, acg) is True
    assert binary_contains(my_sorted_gene, gat) is False
