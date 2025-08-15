#read and open fast_file and creat dictionary 
fast_file="/media/helen-hany/Biotechnology/bioinformatics/python/lrngth/test.fasta"
sequence={}
header=""
for line in open(fast_file) :
    line = line.strip()
    if line.startswith(">"):
        header= line [1:]
        sequence[header] = ""
    else:
        sequence[header] += line
#print header then sequence
for h,seq in sequence.items():
    print(f">{h}")
    print(seq)
#count bases and GC_content
for h,seq in sequence.items():
    length=len(seq)
    A = seq.count("A")
    T = seq.count("T")
    G= seq.count("G")
    C=seq.count("C")
    GC=((G+C)/length*100)

    print(f"header{h} : {length}")
    print(f"A : {A} , T : {T} , G : {G} , C : {C}")
    print(f"GC% : {GC : .2f}%")
#reverse complement DNA
for h,seq in sequence.items():
    complement={
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"
    }
    rev_seq = seq[::-1]
    rev_comp= ""
    for base in rev_seq:
        rev_comp += complement[base]
    print(f"> {h}")
    print("=" * 30)
    print(f"reverse : {rev_comp}")

#search about spectic gene or codon in sequence and heighlight thos gene by different color:
for h,seq in sequence.items():
    gene="ATG"
    RED = "\033[91m"
    END = "\033[0m"
    hightligth_seq= seq.replace(gene,RED + gene + END)
    
    print(f">{h}")
    print(hightligth_seq)
#count how many apper this gene or codon in sequence:
for h,seq in sequence.items():
    codo="ATG"
    count=seq.count(codo)
    print(f"\n seq : {h}")
    print(f"ATG : {count}")

#Transcription
for h,seq in sequence.items():
    rna_seq=seq.replace("T","U")
    print(f">{h}")
    print( f"RNA_seq : {rna_seq}")

#Translation
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

for h,seq in sequence.items():
    protein = ""
    for i in range(0 ,len(seq)-2,3):
         codon=seq[i : i+3]
         amino_acid = codon_table.get(codon,"X")
         protein += amino_acid
    print(F">{h}")
    print(f"protein :{protein}")







