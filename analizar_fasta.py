from Bio import SeqIO

registro = SeqIO.read("zea_mays_gene.fna", "fasta")
secuencia = registro.seq

print("ID:", registro.id)
print("Descripción:", registro.description)
print("Longitud de la secuencia:", len(secuencia))
print("Frecuencia de nucleótidos:")
for base in "ATCG":
    print(f"{base}: {secuencia.count(base)} ({secuencia.count(base)/len(secuencia)*100:.2f}%)")
