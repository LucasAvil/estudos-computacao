import sys

def main ():
    entrada = sys.stdin.read().split()

    if not entrada:
        return

    alunos_unicos = set(entrada[1:])

    print(len(alunos_unicos))

main()