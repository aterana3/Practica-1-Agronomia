from Bio import SeqIO

registro = SeqIO.read("homo_sapiens_18S_rRNA.fasta", "fasta")

rna_sequence = registro.seq.transcribe()


print("ID:", registro.id)
print("Descripción:", registro.description)
print("Longitud de la secuencia:", len(rna_sequence))
print("Frecuencia de nucleótidos:")
for base in "AUCG":
    print(f"{base}: {rna_sequence.count(base)} ({rna_sequence.count(base)/len(rna_sequence)*100:.2f}%)")

