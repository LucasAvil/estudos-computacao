def funcao_teste(x):
    if x == 0:
        return
    print(f'chamou {x}')
    funcao_teste(x-1)
    
funcao_teste(10)