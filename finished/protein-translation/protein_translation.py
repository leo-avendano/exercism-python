PROTEINS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}

STOP_CONDONS = ('UAA', 'UAG', 'UGA')


def proteins(strand):
    i = 0
    aminoacids = []
    while(i < (len(strand) - 1)):
        condon = strand[i:i+3]
        if condon in STOP_CONDONS:
            break
        elif condon in PROTEINS:
            aminoacids.append(PROTEINS[condon])
        i += 3
    return aminoacids
