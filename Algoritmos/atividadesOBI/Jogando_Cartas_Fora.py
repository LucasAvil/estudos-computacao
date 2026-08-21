import sys
from collections import deque

def resolver():
    entrada = sys.stdin.read().split()

    for n in entrada:
        n = int(n)
        if n == 0:
            break

        pilha = deque(range(1, n +1))
        descartadas = []

        while len(pilha) >= 2:
            pilha.popleft()
            descartadas.append(str(pilha.popleft()))

            pilha.append(pilha.popleft())
        print(f'Discarded cards: {', '.join(descartadas)}')
        print(f'Remaining card: {pilha[0]}')

resolver()