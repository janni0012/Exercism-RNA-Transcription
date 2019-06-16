def to_rna(dna_strand):
    transcription = { "G" : "C", "C" : "G", "T" : "A", "A" : "U"}
    if len(dna_strand)>0:
        for  i in range(len(dna_strand)):
            dna_strand[i] = transcription[dna_strand[i]]
            return dna_strand
