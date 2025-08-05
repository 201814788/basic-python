fasta_file = "/media/helen-hany/Biotechnology/bioinformatics/python/DNA_analysis/dna.fasta"
output_file = "dna_analysis_results.txt"
with open(fasta_file) as file:
    sequence = {}
    header = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            header = line
            newheader = header.replace(">", "")
            sequence[newheader] = ""
            print(newheader)
        else:
            sequence[newheader] += line
#2-full length
for header in sequence:
    print(f"{header}:{len(sequence[header])}")

#3-count bases
for name, seq in sequence.items():
    count_A = seq.count("A")
    count_T = seq.count("T")
    count_G = seq.count("G")
    count_C = seq.count("C")
    
    print(f"\n🧬 seq: {name}")
    print(f"A: {count_A}")
    print(f"T: {count_T}")
    print(f"G: {count_G}")
    print(f"C: {count_C}")

for name , seq in sequence.items():
    base_count = {"A":0,"T":0,"C":0,"G":0}
    for base in seq:
        if base in base_count:
            base_count[base] +=1
    print(f"\n{name}")
    for base, count in base_count.items():
        print(f"{base}:{count}")


#percent each bases
for name, seq in sequence.items():
    count_A = seq.count("A")
    count_T = seq.count("T")
    count_C = seq.count("C")
    count_G = seq.count("G")
    total = len(seq)

    percent_A = (count_A / total)*100
    percent_T = (count_T / total)*100
    percent_C = (count_C / total)*100
    percent_G = (count_G / total)*100

    gc_content = ((count_C + count_G)/total)*100

    print(f"\nseq: {name}")
    print(f"A : {count_A} ({percent_A:.2f}%)")
    print(f"T : {count_T} ({percent_T:.2f}%)")
    print(f"C : {count_C} ({percent_C:.2f}%)")
    print(f"G : {count_G} ({percent_G:.2f}%)")
    print(f"Full length : {total}")
    print(f"G + C = {count_G + count_C}")
    print(f"GC content : {gc_content:.2f}%")

#search "ATG"
query = input("ATG:").strip().upper()
for name , seq in sequence.items():
    count = seq.count(query)
    print(f"\n seq: {name}")
    print(f"ATG:'{query}':{count}")



#reverse complement;
complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}
for header, dna_seq in sequence.items():
    reverse_complement = ""
    for base in dna_seq:
        reverse_complement = complement.get(base, "N") + reverse_complement
    
    print(f">reverse_complement_{header}")
    print(reverse_complement)

#turn DNA to RNA
for name , seq in sequence.items():
    rna_seq = seq.replace("T","U")
    print(f"\n seq :{name}")
    print(f"RNA : {rna_seq}")

#translate to protein
codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W",
}


def translate_dna(seq):
    protein = ""
    for i in range(0, len(seq)-2,3):
        codon = seq[i:i+3]
        amino_acid = codon_table.get(codon,"X")
        protein += amino_acid
    return protein
for name, seq in sequence.items():
    protein_seq = translate_dna(seq)
    print(f"\n seq :{name}")
    print(f"protein : {protein_seq}")

print("✅ data : dna_analysis_results.txt")
