from Bio import SeqIO
from csv import reader


lista_clusters = []
with open('./arquivo_temp_proteinas.csv') as arquivo:
    leitor = reader(arquivo)
    for linha in leitor:
        lista_clusters.append(linha[0])
    lista_clusters.remove('cluster')

caminho = '../RAFTS3GClusters'
lista_registros = []
lista_registros_temp = []
for cluster in lista_clusters:
    for registro in SeqIO.parse(f'{caminho}/Cluster_{cluster}.fasta', 'fasta'):
        cabecalho = registro.description.split('|')[1].split('.1')[1].strip()
        lista_registros_temp.append(cabecalho)
    lista_registros.append(lista_registros_temp[-1])

dic = {cluster: proteina for cluster, proteina in zip(lista_clusters, lista_registros)}

with open('./clusters_probioticos.csv', 'a') as arquivo:
    for chave, valor in dic.items():
        arquivo.write(f'{chave},{valor}\n')
