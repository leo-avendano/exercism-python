def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    hamming_distance = 0
    for index, dna in enumerate(strand_a):
        if dna != strand_b[index]:
            hamming_distance += 1
    return hamming_distance
