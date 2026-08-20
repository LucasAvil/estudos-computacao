import sys

for exp in sys.stdin.read().splitlines():
    if not exp:
        continue

    quant = 0
    ver = 0
    invalido = False

    for i in exp:
        if i == "(":
            ver += 1
            quant += 1
        if i == ")" and ver < 1:
            invalido = True
        if i == ")" and ver >= 1:
            ver -= 1
            quant += 1

    if quant % 2 == 0 and ver == 0 and invalido == False:
        print("correct")
    else:
        print("incorrect")