def to_rna(dna_strand):
    transcription = { "G" : "C", "C" : "G", "T" : "A", "A" : "U"}
    for  i in range(len(dna_strand)):
        dna_strand[i] = transcription[dna_strand[i]]
