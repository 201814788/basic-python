fast_file="/media/helen-hany/Biotechnology/bioinformatics/python/try/sequence(4).fasta"
with open (fast_file) as f:
     print(f.read())

#way2
fast_file="/media/helen-hany/Biotechnology/bioinformatics/python/try/sequence(4).fasta"
with open (fast_file) as f:
     for line in f:
          line = line.strip()
          print(line)
    
#way 3
fast_file="test.fasta"
sequence={}
header = ""
for line in open(fast_file):
     line=line.strip()
     if line.startswith(">"):
          header = line[1:]
          sequence [header] = ""
     else:
          sequence[header] += line
for h,seq in sequence.items():
     print(f">{h}")
     print(seq)  


# way4
fast_file="/media/helen-hany/Biotechnology/bioinformatics/python/try/sequence(4).fasta"

fasta= open(fast_file)
print(fasta.readline())

