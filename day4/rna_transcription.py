def to_rna(dna_strand):
    conversion = {
    	'G': 'C',
    	'C': 'G',
    	'T': 'A',
    	'A': 'U'
    }

    return ''.join([conversion[x] for x in dna_strand])
