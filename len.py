fasta="/media/helen-hany/Biotechnology/bioinformatics/python/lrngth/test.fasta"
header=""
sequence ={}
for line in open(fasta):
    line =line.strip()
    if line.startswith(">"):
        header=line [1:]
        sequence[header]=""
    else:
        sequence[header]+= line
for h, seq in sequence.items():
    print(f">{h}")
    print(seq)

#full len
print("length:",len(sequence))

for h,seq in sequence.items():
    print(f"header:{h}, lenght: {len(seq)}")

#count bases:

for h,seq in sequence.items():
    A= seq.count("A")
    T= seq.count("T")
    G = seq.count("G")
    C = seq.count("c")
    print(f"\n🧬 seq: {h}")
    print(f"A:{A}")
    print(f"T,{T}")
    print(f"G:,{G}")
    print(f"C:{C}")

