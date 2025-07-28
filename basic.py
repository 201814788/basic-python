
print("hello to bioinformatics with python")

#enter sequence
dna_seq="""TATTGTAGTAGGCATATGCTTTTTAATCACATTAATGTGATCAGTATTGATGTTACCATGCGATACAGTC
AGTATCAGTAAATCAGATGTTCGTGTGGCATAGCCCATTTCAACCAGATTGGATTCTGAACTAACGAATT
CATTAGTGATGAAATTGCACTGTGGTTTGATCTGTAAATCAATTCTTTCTGATAGGTGCACTATTGATAT
AACTCTGTATCCAGTTGATTTGTATATTCTGTTTTCATTGCTCTGCTTGCTCTTGCTTATCATCTGCTTC
TGGACTTTAAGTGCATTTTGCTGGGCTACTCTTAGTTTGGTCATTTTGGGATAAAAATTGTGAAAATATT"""
print("DNA sequence:", dna_seq)

#count bases
a_count = dna_seq.count("A")
print("A:",a_count)
if a_count > 0:
    print(f"Adenine count: {a_count}")
else:
    print("Adenine not here")

print("T:", dna_seq.count("T"))

for base in "G":
    count = dna_seq.count("G")
    if count > 0:
        print(f"G: {count}")

#length dequence

print("sequence length:",len(dna_seq))

#specific gene
gene_name = "BRCA!"
gene_seq = dna_seq[:100]
gene_length = len(gene_seq)
print("gene", gene_name)
print("gene sequence (first 100 bases):")
print(gene_seq)
print("Gene length:" ,gene_length)
#types of data
a = "ATCG"
b= 1500
c = 45.5
d = False
print("types:", type(a), type(b) , type(c) , type(d))

#count exon+ introns
exons = 23
introns = 25
print("total element:", exons + introns)
# turn str into int
reads = "3000"
reads_num = int(reads)
print("reads count:",reads_num)
print(dna_seq.lower())
print("slice:",dna_seq[0:150])
#count CG%
gc_count = dna_seq.count('G')+ dna_seq.count('C')
gc_content = (gc_count/ len(dna_seq)*100)
print(f"GC content: {gc_content:.2f}%")
