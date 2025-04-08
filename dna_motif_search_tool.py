def find_motif(dna_sequence, motif):
    dna_sequence = dna_sequence.upper()
    motif = motif.upper()
    count = 0
    positions = []

    i = 0
    while i <= len(dna_sequence) - len(motif):
        if dna_sequence[i:i+len(motif)] == motif:
            count += 1
            positions.append(i + 1)
            i += len(motif)
        else:
            i += 1

    return count, positions

#  This is where the user gives input when the script runs
sequence = input("Enter DNA sequence: ")
motif = input("Enter motif to search: ")

count, positions = find_motif(sequence, motif)
print(f"Motif '{motif}' found {count} times at positions: {positions}")

