# Task: "Convert DNA to RNA"

# DNA and RNA are sequences of nucleotides.
#
# Four nucleotides in DNA:
# Adenine (A)
# Cytosine (C)
# Guanine (G)
# Thymine (T)
#
# Four nucleotides in RNA:
# Adenine (A)
# Cytosine (C)
# Guanine (G)
# Uracil (U)
#
# An RNA strand is assembled based on a DNA strand by sequentially replacing
# each nucleotide:
# G -> C
# C -> G
# T -> A
# A -> U
#
# Write a function to_rna that takes a DNA strand and returns the
# corresponding RNA strand (performs DNA transcription).
#


# Задача: "Преобразование DNA в RNA"
# ДНК и РНК это последовательности нуклеотидов.
#
# Четыре нуклеотида в ДНК:
# Аденин (A)
# Цитозин (C)
# Гуанин (G)
# Тимин (T)
#
# Четыре нуклеотида в РНК:
# Аденин (A)
# Цитозин (C)
# Гуанин (G)
# Урацил (U)
#
# Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого
# нуклеотида:
# G -> C
# C -> G
# T -> A
# A -> U
#
# Напишите функцию to_rna, которая принимает на вход цепь ДНК и возвращает
# соответствующую цепь РНК (совершает транскрипцию ДНК).


# Example:
# dna.to_rna('ACGTGGTCTTAA')  # 'UGCACCAGAAUU'


MAPPING = {
        'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'
    }


def to_rna(dna):

    result = []

    for ncltd in dna:
        result.append(MAPPING[ncltd])

    return ''.join(result)


# Решение учителя:


def to_rna_(dna):
    return ''.join(map(MAPPING.get, dna))
#  Данная функция работает немного быстрей

# Шаблон - диспетчеризация, map()
