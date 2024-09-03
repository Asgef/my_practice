from my_practice.DNA_to_RNA import to_rna  # to_rna_
# from time import perf_counter
# import os


def test_to_rna():
    assert to_rna("C") == "G"
    assert to_rna("G") == "C"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"


# test_dir = os.path.dirname(__file__)
# file_path = os.path.join(test_dir, 'fixtures/dna')
# dna = open(file_path).read()
#
#
# start = perf_counter()
# to_rna(dna)
# print(f'time: {(perf_counter() - start):.02f}')
#
# start = perf_counter()
# to_rna_(dna)
# print(f'time: {(perf_counter() - start):.02f}')
