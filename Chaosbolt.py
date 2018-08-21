from random import randint as d
from numpy import arange as AR

# Requires 1 of 4 'jump' options and 1 of 3 'type' options to be chosen

JO = 3
'''Jump Options:
0 = Only original bolt decides jumps
1 = If original and crit damage decide to jump seperately
2 = If original and crit decide together but max 1
3 = If original and crit jump on every pair (fun mode)'''

TO = 1
''' Type Options:
0 = Only original bolt decides damage type (2d8)
1 = Original bolt and crit decide damage types independently (2d8+2d8)
2 = Both bolts give damage options (4d8)'''

SAM = 4  # Spellcasting ability modifiers, probably Charisma
Prof = 2  # Your proficiency

Attack = d(1, 20)
OAttack = d(1, 20)

Type = ["Acid", "Cold", "Fire", "Force", "Lightning", "Poison",
        "Psychic", "Thunder"]

Level = int(input("What spell level are you casting at? 1-9 "))

Advantage = int(input("Do you have advantage? 1/0 "))
autocrit = int(input("Do you have autocrit [paralysed etc.]? 1/0 "))
crit = autocrit
jump = 0

D = []
C = []

Mods = SAM + Prof
Attack = max(Attack, Advantage * OAttack)
if Attack == 20:
    crit = 1
Attack = Attack + Mods

D = [d(1, 8), d(1, 8)]
if crit == 1:
    C = [d(1, 8), d(1, 8)]

J = []
JumpTypes = []
Q = []

N = 0
while N < Level:
    D.append(d(1, 6))
    N = N + 1
    if crit == 1:
        C.append(d(1, 6))

if JO == 0:
    if D[0] == D[1]:
        jump = 1  # if only original can jump
elif JO == 1:
    if D[0] == D[1]:
        jump = jump + 1
    if crit == 1 and (C[0] == C[1]):
        jump = jump + 1  # if crit and original treated as seperate chances to jump
elif JO == 2:
    if crit == 1:
        if D[0] in [D[1], C[0], C[1]] or D[1] in [C[0], C[1]] or C[0] == C[1]:
            jump = 1
    else:
        if D[0] == D[1]:
            jump = 1  # if crit and original can jump together but only once
elif JO == 3:
    if D[0] == D[1]:
        jump += 1
    if crit == 1:
        if C[0] == C[1]:
            jump += 1
        if D[0] == C[0]:
            jump += 1
        if D[1] == C[1]:
            jump += 1
        if D[0] == C[1]:
            jump += 1
        if D[1] == C[0]:
            jump += 1  # if crit and original can jump together on every pair
else:
    print "Jump option is wrong."

if TO == 0:
    if D[0] != D[1]:
        Types = [Type[D[0]-1], Type[D[1]-1]]
    else:
        Types = Type[D[0]-1]
    if len(Types) == 1:
        WriteTypes = Types[0]+" damage."
    else:
        WriteTypes = Types[0]+" or "+Types[1]+" damage."  # if original only ones to choose damage type
elif TO == 1:
    if crit == 0:
        if D[0] != D[1]:
            Types = [Type[D[0]-1], Type[D[1]-1]]
        else:
            Types = [Type[D[0]-1]]
    else:
        if D[0] != D[1]:
            Type1 = [Type[D[0]-1], Type[D[1]-1]]
        else:
            Type1 = Type[D[0]-1]
        if C[0] != C[1]:
            Type2 = [Type[C[0]-1], Type[C[1]-1]]
        else:
            Type2 = Type[C[0]-1]
    if len(Types) == 1:
        WriteTypes = Types[0] + " damage."
    elif len(Types) == 2:
        WriteTypes = Types[0] + " or " + Types[1] + " damage."
    else:
        if len(Type1) == 1:
            WriteType1 = Type1[0]+" damage"
        else:
            WriteType1 = Type1[0]+" or "+Type1[1]+" damage"
        if len(Type2) == 1:
            WriteType2 = Type2[0]+" damage."
        else:
            WriteType2 = Type2[0]+" or "+Type2[1]+" damage."  # if original and crit damage split into two different types
elif TO == 2:
    if crit == 0:
        if D[0] != D[1]:
            Types = [Type[D[0]-1], Type[D[1]-1]]
        else:
            Types = Type[D[0]-1]
    else:
        H = []
        for a in [[D[0], D[1], C[0], C[1]]]:
            if a-1 not in H:
                H.append(a-1)
    if len(H) == 0:
        if len(Types) == 1:
            WriteTypes = Types[0]+" damage."
        else:
            WriteTypes = Types[0] + " or " + Types[1] + " damage."
    elif len(H) == 1:
        WriteTypes = Type[H[0]] + " damage."
    elif len(H) == 2:
        WriteTypes = Type[H[0]] + " or " + Type[H[1]] + " damage."
    elif len(H) == 3:
        WriteTypes = Type[H[0]] + ", " + Type[H[1]] + " or " + Type[H[2]] + " damage."
    else:
        WriteTypes = Type[H[0]] + ", " + Type[H[1]] + ", " + Type[H[2]] + " or " + Type[H[3]] + " damage."  # if any of original or crit choose damage

i = 0
OCJump = jump
while i < jump:
    A = d(1, 8)
    B = d(1, 8)
    Y = 0
    P = 0
    while P < Level:
        Y += d(1, 6)
        P += 1
    J.append(A+B+Y)
    Q.append([A, B])
    if A == B:
        jump += 1
    JumpTypes.append(Type[A-1])
    JumpTypes.append(Type[B-1])
    i += 1

if crit == 1 and autocrit != 1:
    print "Crit! Guaranteed hit."
elif autocrit == 1:
    print "Crit! " + Attack + " to hit."
else:
    print "To hit: " + str(max(Attack, Advantage * OAttack))
if TO == 1 and len(Types) == 0:
    print "Doing " + str(sum(D)) + " points of " + WriteType1
    print "and " + str(sum(C)) + " points of " + WriteType2
else:
    print "Doing " + str(sum(D + C)) + " points of " + WriteTypes
if jump != 0:
    if OCJump == 1:
        print "And jumping!"
    else:
        print "And jumping " + str(OCJump) + " times! (" + str(AR(1,OCJump+1)) + ")"
    i = 0
    while i < jump:
        if JumpTypes[2*i] == JumpTypes[(2*i)+1]:
            print "Jump " + str(i+1) + " does " + str(J[i]) + " points of " + str(JumpTypes[2*i]) + " damage and jumps! ([" + str(max(OCJump+1,i+1)) + "])"
            OCJump += 1
        else:
            print "Jump " + str(i+1) + " does " + str(J[i]) + " point of " + str(JumpTypes[2*i]) + " or " + str(JumpTypes[(2*i)+1]) + " damage."
        i += 1
        if i == 50:
            print "Wow! This jumped 50 times. That's enough I think."
            i = jump
