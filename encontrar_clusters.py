import time
from Bio import SeqIO
from memoize import memoize


@memoize
def encontrar_cluster():
    lista_proteina_bacteria = []
    for registro in SeqIO.parse('./proteoma_probioticos.faa', 'fasta'):
        cabecalho = registro.description.split('.1')[1].split('[')
        linha_csv = cabecalho[0].strip()
        bacteria = cabecalho[1][:-1].strip()
        lista_proteina_bacteria.append(f'{linha_csv},{bacteria}')

    with open('./arquivo_temp.csv', 'r') as csv:
        conteudo = csv.readlines()
        lista_csv = []
        for linha in conteudo:
            lista_csv.append(linha)

    lista_temp = []
    for linha_csv in lista_csv:
        for proteina_bacteria in lista_proteina_bacteria:
            if proteina_bacteria in linha_csv:
                lista_temp.append(linha_csv)

    with open('./arquivo_temp_proteinas.csv', 'a') as csv:
        csv.write('cluster,proteina,bacteria,quantidade\n')
        for item in lista_temp:
            csv.write(f'{item}')


ti = time.perf_counter()
encontrar_cluster()
tf = time.perf_counter()
tempo_min = (tf - ti) / 60
print(f'Tempo de espera: {tf - ti:.2f} segundos ({tempo_min:.1f} minutos).')
