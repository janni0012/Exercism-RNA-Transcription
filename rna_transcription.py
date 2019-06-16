def to_rna(dna_strand):
    transcription = { "G" : "C", "C" : "G", "T" : "A", "A" : "U"}
    if len(dna_strand)>0:
        rna = []
        for  i in range(len(dna_strand)):
            rna.append(transcription[dna_strand[i]])
        return "".join(rna)
    else:
        return ""
    