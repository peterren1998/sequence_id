from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

comparison_dna_seq = Seq("CGTTATTGATGAA", IUPAC.unambiguous_dna)
f = open("/Users/peter/Desktop/Research/dna_c_cl/Sequencing/2/Sequences/01-D18_A01_015.seq", "r")
nns_seq = f.read()
nns_seq = Seq(nns_seq, IUPAC.ambiguous_dna)
nns_codon = nns_seq.split(sep="CGTTATTGATGAA")[1][0:3]
print(nns_codon)
nns_codon_transcribed = nns_codon.transcribe()
print(nns_codon_transcribed)
res_id = nns_codon_transcribed.translate()
print(res_id)
