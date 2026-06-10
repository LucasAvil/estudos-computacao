import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog = 'projeto demo de modulos e libs',
    description='exemplo de uso de comandos em linha de exec'
)

parser.add_argument('arquivo_entrada')

args = parser.parse_args()

def show_parameters():
    print(args.arquivo_entrada)
    
def get_file():
    arquivo = Path(args.arquivo_entrada)
    if not arquivo.exists():
        raise Exception('o arquivo n existe')
    if arquivo.is_dir():
        raise Exception('informe um arquivo nao uma pasta')
    if arquivo.suffix.lower() != '.csv':
        raise Exception('informe um arquivo .csv')
    return arquivo
        
    