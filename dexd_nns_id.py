from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import os

directory = os.fsencode("./Sequences")

filenames = []

def sample_num(filename):
    return int(filename.split("D")[1].split("_")[0])
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".seq"):
        filenames.append(filename)
        print(filename)
        
print()           
filenames = sorted(filenames, key = sample_num)
print(filenames)
print()
            
for filename in filenames:
    print(filename)
    f = open("./Sequences/" + filename, "r")
    nns_seq = f.read()
    nns_seq = Seq(nns_seq, IUPAC.ambiguous_dna)
    if "CGTTATTGATGAA" in nns_seq:
        split_sequence = nns_seq.split(sep="CGTTATTGATGAA")[1]
        nns_codon = split_sequence[0:3]
        nns_codon_check = split_sequence[3:6]
        print("Sequenced Codon: " + nns_codon)
        print("Check Codon: " + nns_codon_check)
        nns_codon_transcribed = nns_codon.transcribe()
        print("Transcribed Codon: " + nns_codon_transcribed)
        res_id = nns_codon_transcribed.translate()
        print("Mutant Residue: " + res_id + "\n")
    else:
        print("Matching string not found\n")
