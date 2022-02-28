from fractions import Fraction
pegs = [4,17,50]
peg_gaps = []

num_pegs = len(pegs)
accumulator = 0
for peg in pegs:
    if pegs.index(peg)==0:
        accumulator -=pegs[pegs.index(peg)]
        continue
    if pegs.index(peg)!=num_pegs-1: #Not the first or last peg
        if pegs.index(peg)%2: #Should be true on odd index
            accumulator+= 2*pegs[pegs.index(peg)]
        else:
            accumulator-= 2*pegs[pegs.index(peg)]
    if pegs.index(peg)==num_pegs-1: #Last peg
        if pegs.index(peg)%2:
            accumulator+= pegs[pegs.index(peg)]
        else:
            accumulator-= pegs[pegs.index(peg)]
print(accumulator)

last_radius = accumulator
first_radius = 2*accumulator
if num_pegs%2!=1: #Formulas show a pattern of /3 with even number of pegs
    first_radius/=3    
first_radius = Fraction(first_radius).limit_denominator()
print(first_radius.numerator, first_radius.denominator)

for i in range(num_pegs-1):
    peg_gaps.append(pegs[i+1]-pegs[i])
for i in range(num_pegs-1):
    if peg_gaps[i] < 2:
        print('[-1,-1]')
print(peg_gaps)

