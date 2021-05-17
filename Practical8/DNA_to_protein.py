seq='ATGCGACTACGATCGAGGGCC'
table={'ATG':'M','CGA':'R','CTA':'L', 'TCG':'S', 'AGG':'R', 'GCC':'A'}
i=0
while i<len(seq):
    encoded_amino_acid=seq[i:i+3]
    print(table[encoded_amino_acid],end="")
    i+=3