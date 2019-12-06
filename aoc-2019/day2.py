import itertools

with open('input_day2') as f:
    input_seq = list(map(int, f.read().split(',')))


def run_system(input_seq, noun=12, verb=2):
    seq = list(input_seq)
    seq[1] = noun
    seq[2] = verb
    i = 0
    while True:
        op = seq[i]
        if op == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
        elif op == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
        elif op == 99:
            break
        else:
            print('[ERROR] Unknown opcode.')
        i += 4
    return seq[0]


# Part 1
print(run_system(input_seq))

# Part 2
target_value = 19690720
for (noun, verb) in itertools.permutations(range(100), 2):
    if run_system(input_seq, noun=noun, verb=verb) == target_value:
        print(100 * noun + verb)
        break
