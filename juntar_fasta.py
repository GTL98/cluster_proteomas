import os
import time
from Bio import SeqIO
from memoize import memoize


@memoize
def juntar_fasta():
    lista_pastas = [
        'Bacteroides',
        'Bifidobacterium',
        'Lacticaseibacillus',
        'Lactiplantibacillus',
        'Lactobacillus',
        'Levilactobacillus',
        'Ligilactobacillus',
        'Limosilactobacillus',
        'Prevotella',
        'Ruminococcus'

    ]
    for pasta in lista_pastas:
        for arquivo in os.listdir(f'./{pasta}'):
            for registro in SeqIO.parse(f'./{pasta}/{arquivo}', 'fasta'):
                descricao = registro.description.split('[')
                bacteria = ' '.join(arquivo[:-4].split('_'))
                descricao_especie = f'{descricao[0]}[{bacteria}]'
                with open('proteoma_bacterias.faa', 'a') as faa:
                    fasta = f'''>{descricao_especie}
{registro.seq}
'''
                    faa.write(fasta)
    print('Arquivo criado!')


ti = time.perf_counter()
juntar_fasta()
tf = time.perf_counter()
tempo_min = (tf - ti) / 60
print(f'Tempo de espera: {tf - ti:.2f} segundos ({tempo_min:.1f} minutos).')
