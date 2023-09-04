from csv import reader


def indices_clusters(proteina: str):
    with open('./clusters_probioticos.csv', 'r') as arquivo:
        leitor = reader(arquivo)
        lista = []
        for linha in leitor:
            if proteina in linha[1]:
                lista.append(linha[0])

    titulo = ''
    if proteina == 'carbono':
        titulo = 'Metabolismo do carbono e transporte de carboidratos'
    elif proteina == 'estresse':
        titulo = 'Resistência ao estresse'
    elif proteina == 'tolerancia':
        titulo = 'Tolerância ao suco gástrico'
    elif proteina == 'adesao':
        titulo = 'Capacidade de adesão'
    elif proteina == 'bacteriocina':
        titulo = 'Bacteriocinas'
    elif proteina == 'folico':
        titulo = 'Biossíntese do ácido fólico'
    elif proteina == 'EPS':
        titulo = 'Biossíntese do EPS'
    elif proteina == 'beta galactosidase':
        titulo = 'Beta galactosidase'
    elif proteina == 'manosidase':
        titulo = 'Manosidase'
    elif proteina == 'sialidase':
        titulo = 'Sialidase'
    elif proteina == 'fucosidase':
        titulo = 'Fucosidase'
    elif proteina == 'fosfolipase':
        titulo = 'Fosfolipase'
    elif proteina == 'biliar':
        titulo = 'Resistência ao ácido biliar'
    elif proteina == 'hypothetical':
        titulo = 'Proteínas hipotéticas'

    with open('./indices_clusters.txt', 'a') as txt:
        txt.write(f'{titulo}\n')
        txt.write('\tQuantidade:\n')
        txt.write(f'\t\t- {len(lista)}\n')
        txt.write('\tClusters:\n')
        for item in lista:
            txt.write(f'\t\t- {item}\n')
        txt.write('#####\n\n')


lista_proteinas = [
    'carbono',
    'estresse',
    'tolerancia',
    'adesao',
    'bacteriocina',
    'folico',
    'EPS',
    'beta galactosidase',
    'manosidase',
    'sialidase',
    'fucosidase',
    'fosfolipase',
    'biliar',
    'hypothetical'
]
for proteina in lista_proteinas:
    indices_clusters(proteina)
