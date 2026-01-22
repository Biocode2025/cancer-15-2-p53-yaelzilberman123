import random

def Read_DNA(file_name):
    dna = "" # dna string
    with open(file_name, "r") as file:
        for line in file:
            if line[0] != ">": # check if line is part of dna
                dna += line.strip() # add lune to dna
    
    return dna # return the dna string


def DNA_RNA_Cod(dna):
    return dna.replace("T", "U") # replace all T's with U's to translate dna


def Read_dict(file_name):
    codon_aa_dict = dict() # create dict for codons and amino acids

    with open(file_name, 'r') as file:
        for line in file:
            codon_aa_dict[line[0:3]] = line[4:5] # match codon with amino acid

    return codon_aa_dict # return the new dictionary


def RNA_Protein(rna, codon_aa_dict):
    protein = "" 
    for i in range(0, len(rna)- 2 , 3):
        codon = rna[i:i+3]
        aa = codon_aa_dict.get(codon, "")
        if aa == "*": # check if its a break codon
            break
        protein += aa # if not, add to protein
    return protein


def Mutate_DNA(seq):
    index = random.randrange(0, len(seq))
    bases = ["A", "T", "G", "C"]
    bases.remove(seq[index])
    rand_base = random.randrange(0, 3)
    mot_seq = list(seq)
    mot_seq[index] = bases[rand_base]
    return "".join(mot_seq)

def write_Data(protein, mutated_protein, shortened, file_name):
    with open(file_name, 'w') as file: # open the results file

        # overwrite all file data with the new mutated DNA
        file.write(">Original_p53_protein\n")
        file.write(protein + "\n\n")

        file.write(">Mutated_p53_protein\n")
        file.write(mutated_protein + "\n\n")

        file.write(">Conclusion\n")
        file.write(f"Did it shorten: {shortened}")

        



dna = Read_DNA("data/p53_sequence.fa")
rna = DNA_RNA_Cod(dna)
codon_aa_dict = Read_dict("data/Codon_AA.txt")

mutated_dna = dna

for i in range(3):
    mutated_dna = Mutate_DNA(mutated_dna)

mutated_rna = DNA_RNA_Cod(mutated_dna)

protein = RNA_Protein(rna, codon_aa_dict)
mutated_protein = RNA_Protein(mutated_rna, codon_aa_dict)
shortened = True if len(protein) > len(mutated_protein) else False

write_Data(protein,mutated_protein,shortened,"results/results.fasta")



