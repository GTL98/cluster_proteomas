import os

caminho = '../RAFTS3G/RAFTS3GClusters'
for arquivo in os.listdir(caminho):
    report = arquivo
    break

with open(f'{caminho}/{report}', 'r') as tab:
    conteudo = tab.readlines()
    for item in conteudo:
        cluster = item.split('\t')
        if 'Cluster' in item:
            pass
        else:
            quantidade = int(cluster[1].split('\n')[0])
            if quantidade >= 2:
                with open('cluster.tab', 'a') as tab2:
                    tab2.write(f'Cluster: {cluster[0]}\tQuantidade: {quantidade}\n')