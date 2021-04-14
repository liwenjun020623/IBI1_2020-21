def reverse_complement_calculator(seq):
    sequence = []
    reverse_complement = ''
    for i in seq:
        sequence.append(i)
    reverse_sequence = sequence[::-1]
    for base in reverse_sequence:
        if base == 'A' or base == 'a':
            reverse_complement += 'T'
        if base == 'T' or base == 't':
            reverse_complement += 'A'
        if base == 'C' or base == 'c':
            reverse_complement += 'G'
        if base == 'G' or base == 'g':
            reverse_complement += 'C'
    return reverse_complement
# example:
# If the input sequence is ATTCGGCTAAattcGGtTTTaaCtAgAT
# The output will be: ATCTAGTTAAAACCGAATTTAGCCGAAT
print(reverse_complement_calculator('ATTCGGCTAAattcGGtTTTaaCtAgAT'))
