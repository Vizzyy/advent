with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')
assignment_pairs = [[[int(number) for number in spots.split('-')] for spots in assignment.split(',')] for assignment in inputs]

[print(pair) for pair in assignment_pairs]


def check_overlap(seq1, seq2):
    if seq1[0] >= seq2[0] and seq1[0] <= seq2[1]:
        return True
    elif seq1[1] >= seq2[0] and seq1[1] <= seq2[1]:
        return True
    if seq2[0] >= seq1[0] and seq2[0] <= seq1[1]:
        return True
    elif seq2[1] >= seq1[0] and seq2[1] <= seq1[1]:
        return True
    else:
        return False


overlapping_count = 0
for seq1, seq2 in assignment_pairs:
    if check_overlap(seq1, seq2):
        overlapping_count += 1

print(overlapping_count)
