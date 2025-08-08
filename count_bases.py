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

for h,seq in sequence.items():
    A= seq.count("A")
    T= seq.count("T")
    G = seq.count("G")
    C = seq.count("c")
    print(f"{h} -> A:{A} ,T:{T} ,C:{C}, G:{G}")

for h, seq in sequence.items():
    base_count = {}
    