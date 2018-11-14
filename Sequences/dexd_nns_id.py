from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import os

directory = os.fsencode(".")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".seq"):
        print(filename)
        f = open("./" + filename, "r")
        nns_seq = f.read()
        nns_seq = Seq(nns_seq, IUPAC.ambiguous_dna)
        split_sequence = nns_seq.split(sep="CGTTATTGATGAA")[1]
        nns_codon = split_sequence[0:3]
        nns_codon_check = split_sequence[3:6]
        print("Sequenced Codon: " + nns_codon)
        print("Check Codon: " + nns_codon_check)
        nns_codon_transcribed = nns_codon.transcribe()
        print("Transcribed Codon: " + nns_codon_transcribed)
        res_id = nns_codon_transcribed.translate()
        print("Mutant Residue: " + res_id + "\n")
