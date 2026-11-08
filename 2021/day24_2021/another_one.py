from functools import reduce
import z3

file = "input.txt"

with open(file) as f:
    instrs = [l.strip().split() for l in f.read().splitlines()]

n = 14  # Number of digits.
block = 18

# Gather the "magic numbers" from the ALU program.
addx = []
addy = []
divz = []
for i in range(n):
    divz.append(int(instrs[i*block + 4][-1]))
    addx.append(int(instrs[i*block + 5][-1]))
    addy.append(int(instrs[i*block + 15][-1]))

# Make input ints.
inp = [z3.Int(f'inp_{x}') for x in range(n)]

# Create a z3 solver.
s = z3.Optimize()

# Constrain input to non-zero digits.
s.add(*[1 <= i for i in inp], *[i <= 9 for i in inp])

# Chain constraints. Each iteration will have a separate z variable.
# The constraints added will connect z[i+1] to z[i].
zs = [z3.Int(f'z_{i}') for i in range(n + 1)]
s.add(zs[0] == 0)
for i in range(n):
    x = inp[i] != (zs[i] % 26 + addx[i])
    s.add(zs[i+1] == z3.If(x, (zs[i] / divz[i]) * 26 + inp[i] + addy[i],
                              zs[i] / divz[i]))

s.add(zs[-1] == 0) # Victory constraint.

# Construct full input to optimise (with place value).
full_inp = reduce(lambda acc, x: acc*10 + x, inp, 0)


def get_inp(model):
    return ''.join(str(model[i]) for i in inp)


# Part 1.
s.push()
s.maximize(full_inp)
s.check()
part1 = get_inp(s.model())
print('part1:', part1)
s.pop()