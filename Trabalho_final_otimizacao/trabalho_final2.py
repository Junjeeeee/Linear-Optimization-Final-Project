import pandas as pd
from pulp import *

class Alimento:
    def __init__(self, nome, palatabilidade_cafe, palatabilidade_almoco, palatabilidade_jantar, preco, calorias, vitamina_e,
                 carboidrato_disponivel, cinzas, cobre, colesterol, calcio, equivalente_de_folato, ferro, fibras, fosforo,
                 lipidios, magnesio, manganes, niacina, potassio, proteina, riboflavina, selenio, sodio, tiamina,
                 vitamina_a_rae, vitamina_b12, vitamina_b6, vitamina_c, vitamina_d, zinco,
                 acidos_graxos_monossaturados, acidos_graxos_polissaturados, acidos_graxos_saturados, acidos_graxos_trans):
        self.nome = nome
        self.palatabilidade_cafe = palatabilidade_cafe
        self.palatabilidade_almoco = palatabilidade_almoco
        self.palatabilidade_jantar = palatabilidade_jantar
        #self.preco = preco
        self.preco = 1
        self.calorias = calorias
        self.vitamina_e = vitamina_e
        self.carboidrato_disponivel = carboidrato_disponivel
        self.cinzas = cinzas
        self.cobre = cobre
        self.colesterol = colesterol
        self.calcio = calcio
        self.equivalente_de_folato = equivalente_de_folato
        self.ferro = ferro
        self.fibras = fibras
        self.fosforo = fosforo
        self.lipidios = lipidios
        self.magnesio = magnesio
        self.manganes = manganes
        self.niacina = niacina
        self.potassio = potassio
        self.proteina = proteina
        self.riboflavina = riboflavina
        self.selenio = selenio
        self.sodio = sodio
        self.tiamina = tiamina
        self.vitamina_a_rae = vitamina_a_rae
        self.vitamina_b12 = vitamina_b12
        self.vitamina_b6 = vitamina_b6
        self.vitamina_c = vitamina_c
        self.vitamina_d = vitamina_d
        self.zinco = zinco
        self.acidos_graxos_monossaturados = acidos_graxos_monossaturados
        self.acidos_graxos_polissaturados = acidos_graxos_polissaturados
        self.acidos_graxos_saturados = acidos_graxos_saturados
        self.acidos_graxos_trans = acidos_graxos_trans

    def __str__(self):
        return f'Alimento(nome={self.nome}, preco={self.preco}, calorias={self.calorias})'

    def __repr__(self):
        return self.__str__()

# Carregar os dados do CSV
df = pd.read_csv('/home/junj/Documents/codes/Trabalho_final_otimizacao/alimentos_nutricionais.csv', encoding='latin1')



#exit()

numeric_columns = [
    'Palatabildiade Café (0010)', 'Palatabildiade Almoço (0010)', 'Palatabildiade Jantar (0010)', 'Preço', ' Energia (kJ/kcal)',
    'Alfa0tocoferol (Vitami0 E) (mg)', 'Carboidrato disponível (g)', ' Cinzas (g)', ' Cobre (mg)', ' Colesterol (mg)', ' Cálcio (mg)',
    ' Equivalente de folato (mcg)', ' Ferro (mg)', ' Fibra alimentar (g)', ' Fósforo (mg)', ' Lipídios (g)', ' Magnésio (mg)', ' Manganês (mg)',
    ' Niaci0 (mg)', ' Potássio (mg)', ' Proteí0 (g)', ' Riboflavi0 (mg)', ' Selênio (mcg)', ' Sódio (mg)', ' Tiami0 (mg)',
    ' Vitami0 A (RAE) (mcg)', ' Vitami0 B12 (mcg)', ' Vitami0 B6 (mg)', ' Vitami0 C (mg)', ' Vitami0 D (mcg)', ' Zinco (mg)',
    ' Ácidos graxos monoinsaturados (g)', ' Ácidos graxos poliinsaturados (g)', ' Ácidos graxos saturados (g)', ' Ácidos graxos 0ans (g)'
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.fillna(0, inplace=True)

    # Exibir os nomes das colunas para verificar se estão corretos
print(df.columns)

# Exibir os tipos de dados das colunas
print(df.dtypes)

#$exit()


# Criar uma lista de objetos Alimento
alimentos = []
for index, row in df.iterrows():
    alimento = Alimento(
        nome=row['Alimento'],
        palatabilidade_cafe=row['Palatabildiade Café (0010)'],
        palatabilidade_almoco=row['Palatabildiade Almoço (0010)'],
        palatabilidade_jantar=row['Palatabildiade Jantar (0010)'],
        preco=row['Preço'],
        calorias=row[' Energia (kJ/kcal)'],
        vitamina_e=row['Alfa0tocoferol (Vitami0 E) (mg)'],
        carboidrato_disponivel=row['Carboidrato disponível (g)'],
        cinzas=row[' Cinzas (g)'],
        cobre=row[' Cobre (mg)'],
        colesterol=row[' Colesterol (mg)'],
        calcio=row[' Cálcio (mg)'],
        equivalente_de_folato=row[' Equivalente de folato (mcg)'],
        ferro=row[' Ferro (mg)'],
        fibras=row[' Fibra alimentar (g)'],
        fosforo=row[' Fósforo (mg)'],
        lipidios=row[' Lipídios (g)'],
        magnesio=row[' Magnésio (mg)'],
        manganes=row[' Manganês (mg)'],
        niacina=row[' Niaci0 (mg)'],
        potassio=row[' Potássio (mg)'],
        proteina=row[' Proteí0 (g)'],
        riboflavina=row[' Riboflavi0 (mg)'],
        selenio=row[' Selênio (mcg)'],
        sodio=row[' Sódio (mg)'],
        tiamina=row[' Tiami0 (mg)'],
        vitamina_a_rae=row[' Vitami0 A (RAE) (mcg)'],
        vitamina_b12=row[' Vitami0 B12 (mcg)'],
        vitamina_b6=row[' Vitami0 B6 (mg)'],
        vitamina_c=row[' Vitami0 C (mg)'],
        vitamina_d=row[' Vitami0 D (mcg)'],
        zinco=row[' Zinco (mg)'],
        acidos_graxos_monossaturados=row[' Ácidos graxos monoinsaturados (g)'],
        acidos_graxos_polissaturados=row[' Ácidos graxos poliinsaturados (g)'],
        acidos_graxos_saturados=row[' Ácidos graxos saturados (g)'],
        acidos_graxos_trans=row[' Ácidos graxos 0ans (g)']
    )
    alimentos.append(alimento)

#for alimento in alimentos:
#    print(alimento)


class Atributos_pl:
    
    def __init__(self, nome, peso_monetario, peso_palatabilidade, calorias_max_cafe, calorias_max_almoco, calorias_max_jantar, vitamina_e_min, vitamina_e_max, carboidrato_min, carboidrato_max,
                 cinzas_min, cinzas_max, cobre_min, cobre_max, colesterol_min, colesterol_max, calcio_min, calcio_max, equivalente_de_folato_min, equivalente_de_folato_max, ferro_min,
                 ferro_max, fibras_min, fibras_max, fosforo_min, fosforo_max, lipidios_min, lipidios_max, magnesio_min, magnesio_max, manganes_min, manganes_max, niacina_min, niacina_max,
                 potassio_min, potassio_max, proteina_min, proteina_max, riboflavina_min, riboflavina_max, selenio_min, selenio_max, sodio_min, sodio_max, tiamina_min, tiamina_max, vitamina_a_rae_min,
                 vitamina_a_rae_max, vitamina_b12_min, vitamina_b12_max, vitamina_b6_min, vitamina_b6_max, vitamina_c_min, vitamina_c_max, vitamina_d_min, vitamina_d_max, zinco_min, zinco_max,
                 acidos_graxos_monossaturados_min, acidos_graxos_monossaturados_max, acidos_graxos_polissaturados_min, acidos_graxos_polissaturados_max, acidos_graxos_saturados_min,
                 acidos_graxos_saturados_max, acidos_graxos_trans_min, acidos_graxos_trans_max):
        self.nome = nome
        self.peso_monetario = peso_monetario
        self.peso_palatabilidade = peso_palatabilidade
        self.calorias_max_cafe = calorias_max_cafe
        self.calorias_max_almoco = calorias_max_almoco
        self.calorias_max_jantar = calorias_max_jantar
        self.vitamina_e_min = vitamina_e_min
        self.vitamina_e_max = vitamina_e_max
        self.carboidrato_min = carboidrato_min
        self.carboidrato_max = carboidrato_max
        self.cinzas_min = cinzas_min
        self.cinzas_max = cinzas_max
        self.cobre_min = cobre_min
        self.cobre_max = cobre_max
        self.colesterol_min = colesterol_min
        self.colesterol_max = colesterol_max
        self.calcio_min = calcio_min
        self.calcio_max = calcio_max
        self.equivalente_de_folato_min = equivalente_de_folato_min
        self.equivalente_de_folato_max = equivalente_de_folato_max
        self.ferro_min = ferro_min
        self.ferro_max = ferro_max
        self.fibras_min = fibras_min
        self.fibras_max = fibras_max
        self.fosforo_min = fosforo_min
        self.fosforo_max = fosforo_max
        self.lipidios_min = lipidios_min
        self.lipidios_max = lipidios_max
        self.magnesio_min = magnesio_min
        self.magnesio_max = magnesio_max
        self.manganes_min = manganes_min
        self.manganes_max = manganes_max
        self.niacina_min = niacina_min
        self.niacina_max = niacina_max
        self.potassio_min = potassio_min
        self.potassio_max = potassio_max
        self.proteina_min = proteina_min
        self.proteina_max = proteina_max
        self.riboflavina_min = riboflavina_min
        self.riboflavina_max = riboflavina_max
        self.selenio_min = selenio_min
        self.selenio_max = selenio_max
        self.sodio_min = sodio_min
        self.sodio_max = sodio_max
        self.tiamina_min = tiamina_min
        self.tiamina_max = tiamina_max
        self.vitamina_a_rae_min = vitamina_a_rae_min
        self.vitamina_a_rae_max = vitamina_a_rae_max
        self.vitamina_b12_min = vitamina_b12_min
        self.vitamina_b12_max = vitamina_b12_max
        self.vitamina_b6_min = vitamina_b6_min
        self.vitamina_b6_max = vitamina_b6_max
        self.vitamina_c_min = vitamina_c_min
        self.vitamina_c_max = vitamina_c_max
        self.vitamina_d_min = vitamina_d_min
        self.vitamina_d_max = vitamina_d_max
        self.zinco_min = zinco_min
        self.zinco_max = zinco_max
        self.acidos_graxos_monossaturados_min = acidos_graxos_monossaturados_min
        self.acidos_graxos_monossaturados_max = acidos_graxos_monossaturados_max
        self.acidos_graxos_polissaturados_min = acidos_graxos_polissaturados_min
        self.acidos_graxos_polissaturados_max = acidos_graxos_polissaturados_max
        self.acidos_graxos_saturados_min = acidos_graxos_saturados_min
        self.acidos_graxos_saturados_max = acidos_graxos_saturados_max
        self.acidos_graxos_trans_min = acidos_graxos_trans_min
        self.acidos_graxos_trans_max = acidos_graxos_trans_max
        
# Definir os atributos do problema
atributos = Atributos_pl(
    nome='Dieta Exemplo',
    peso_monetario=1,
    peso_palatabilidade=1/10,
    calorias_max_cafe=800,
    calorias_max_almoco=1400,
    calorias_max_jantar=800,
    vitamina_e_min=15, #mg x
    vitamina_e_max=1000,
    carboidrato_min=130, #gx
    carboidrato_max=700,
    cinzas_min=0,#no data
    cinzas_max=1500,
    cobre_min=0.9, #mg
    cobre_max=10,
    colesterol_min=30,#mg
    colesterol_max=200,
    calcio_min=1000,#mg
    calcio_max=2500,
    equivalente_de_folato_min=400,#mcg 
    equivalente_de_folato_max=1000,
    ferro_min=8,#mg
    ferro_max=45,
    fibras_min=14, #g
    fibras_max=500, #no upper limit
    fosforo_min=700, #mg
    fosforo_max=4000,
    lipidios_min=10, #g
    lipidios_max=900, 
    magnesio_min=400, #mg
    magnesio_max=1000,
    manganes_min=2.3, #mg
    manganes_max=5,
    niacina_min=16, #mg 
    niacina_max=35,
    potassio_min=3400, #mg
    potassio_max=6000,
    proteina_min=45, #g
    proteina_max=200, # no upper limit
    riboflavina_min=1.3, #mg
    riboflavina_max=1000,
    selenio_min=55, # mcg
    selenio_max=400, 
    sodio_min=1000, # mg
    sodio_max=4000,
    tiamina_min=1.2, #mg
    tiamina_max=5,
    vitamina_a_rae_min=900, #mcg
    vitamina_a_rae_max=3000,
    vitamina_b12_min=2.4, #mcg
    vitamina_b12_max=1000,
    vitamina_b6_min=1.3, #mg
    vitamina_b6_max=100, 
    vitamina_c_min=90, #mg
    vitamina_c_max=2000,
    vitamina_d_min=15, #mcg
    vitamina_d_max=100,
    zinco_min=11,#mg
    zinco_max=40,
    acidos_graxos_monossaturados_min=0,
    acidos_graxos_monossaturados_max=100, #gramas
    acidos_graxos_polissaturados_min=1.6,
    acidos_graxos_polissaturados_max=100, #gramas
    acidos_graxos_saturados_min=0,
    acidos_graxos_saturados_max=300, #g
    acidos_graxos_trans_min=0,
    acidos_graxos_trans_max=100 #g
)

#exit()

# Definir o problema de otimização
problema = LpProblem("Dieta_Equilibrada", LpMinimize)

# Definir as variáveis de decisão para cada refeição
quantidades_cafe = LpVariable.dicts("Quantidades_Cafe", [alimento.nome for alimento in alimentos], lowBound=0, upBound=3, cat='Integer')
quantidades_almoco = LpVariable.dicts("Quantidades_Almoco", [alimento.nome for alimento in alimentos], lowBound=0, upBound=3, cat='Integer')
quantidades_jantar = LpVariable.dicts("Quantidades_Jantar", [alimento.nome for alimento in alimentos], lowBound=0, upBound=3, cat='Integer')

# Função objetivo
problema += lpSum([
    quantidades_cafe[alimento.nome] * (atributos.peso_monetario * alimento.preco - atributos.peso_palatabilidade * alimento.palatabilidade_cafe) +
    quantidades_almoco[alimento.nome] * (atributos.peso_monetario * alimento.preco - atributos.peso_palatabilidade * alimento.palatabilidade_almoco) +
    quantidades_jantar[alimento.nome] * (atributos.peso_monetario * alimento.preco - atributos.peso_palatabilidade * alimento.palatabilidade_jantar)
    for alimento in alimentos])

problema += lpSum([
    quantidades_cafe[alimento.nome] for alimento in alimentos]) <= 20
problema += lpSum([
    quantidades_almoco[alimento.nome] for alimento in alimentos]) <= 20
problema += lpSum([
    quantidades_jantar[alimento.nome] for alimento in alimentos]) <= 20


# Restrições de calorias para cada refeição
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.calorias for alimento in alimentos]) <= atributos.calorias_max_cafe
problema += lpSum([quantidades_almoco[alimento.nome] * alimento.calorias for alimento in alimentos]) <= atributos.calorias_max_almoco
problema += lpSum([quantidades_jantar[alimento.nome] * alimento.calorias for alimento in alimentos]) <= atributos.calorias_max_jantar

# Restrições de nutrientes (para todas as refeições combinadas)
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_e + quantidades_almoco[alimento.nome] * alimento.vitamina_e + quantidades_jantar[alimento.nome] * alimento.vitamina_e for alimento in alimentos]) >= atributos.vitamina_e_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_e + quantidades_almoco[alimento.nome] * alimento.vitamina_e + quantidades_jantar[alimento.nome] * alimento.vitamina_e for alimento in alimentos]) <= atributos.vitamina_e_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.carboidrato_disponivel + quantidades_almoco[alimento.nome] * alimento.carboidrato_disponivel + quantidades_jantar[alimento.nome] * alimento.carboidrato_disponivel for alimento in alimentos]) >= atributos.carboidrato_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.carboidrato_disponivel + quantidades_almoco[alimento.nome] * alimento.carboidrato_disponivel + quantidades_jantar[alimento.nome] * alimento.carboidrato_disponivel for alimento in alimentos]) <= atributos.carboidrato_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.cinzas + quantidades_almoco[alimento.nome] * alimento.cinzas + quantidades_jantar[alimento.nome] * alimento.cinzas for alimento in alimentos]) >= atributos.cinzas_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.cinzas + quantidades_almoco[alimento.nome] * alimento.cinzas + quantidades_jantar[alimento.nome] * alimento.cinzas for alimento in alimentos]) <= atributos.cinzas_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.cobre + quantidades_almoco[alimento.nome] * alimento.cobre + quantidades_jantar[alimento.nome] * alimento.cobre for alimento in alimentos]) >= atributos.cobre_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.cobre + quantidades_almoco[alimento.nome] * alimento.cobre + quantidades_jantar[alimento.nome] * alimento.cobre for alimento in alimentos]) <= atributos.cobre_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.colesterol + quantidades_almoco[alimento.nome] * alimento.colesterol + quantidades_jantar[alimento.nome] * alimento.colesterol for alimento in alimentos]) >= atributos.colesterol_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.colesterol + quantidades_almoco[alimento.nome] * alimento.colesterol + quantidades_jantar[alimento.nome] * alimento.colesterol for alimento in alimentos]) <= atributos.colesterol_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.calcio + quantidades_almoco[alimento.nome] * alimento.calcio + quantidades_jantar[alimento.nome] * alimento.calcio for alimento in alimentos]) >= atributos.calcio_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.calcio + quantidades_almoco[alimento.nome] * alimento.calcio + quantidades_jantar[alimento.nome] * alimento.calcio for alimento in alimentos]) <= atributos.calcio_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.equivalente_de_folato + quantidades_almoco[alimento.nome] * alimento.equivalente_de_folato + quantidades_jantar[alimento.nome] * alimento.equivalente_de_folato for alimento in alimentos]) >= atributos.equivalente_de_folato_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.equivalente_de_folato + quantidades_almoco[alimento.nome] * alimento.equivalente_de_folato + quantidades_jantar[alimento.nome] * alimento.equivalente_de_folato for alimento in alimentos]) <= atributos.equivalente_de_folato_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.ferro + quantidades_almoco[alimento.nome] * alimento.ferro + quantidades_jantar[alimento.nome] * alimento.ferro for alimento in alimentos]) >= atributos.ferro_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.ferro + quantidades_almoco[alimento.nome] * alimento.ferro + quantidades_jantar[alimento.nome] * alimento.ferro for alimento in alimentos]) <= atributos.ferro_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.fibras + quantidades_almoco[alimento.nome] * alimento.fibras + quantidades_jantar[alimento.nome] * alimento.fibras for alimento in alimentos]) >= atributos.fibras_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.fibras + quantidades_almoco[alimento.nome] * alimento.fibras + quantidades_jantar[alimento.nome] * alimento.fibras for alimento in alimentos]) <= atributos.fibras_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.fosforo + quantidades_almoco[alimento.nome] * alimento.fosforo + quantidades_jantar[alimento.nome] * alimento.fosforo for alimento in alimentos]) >= atributos.fosforo_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.fosforo + quantidades_almoco[alimento.nome] * alimento.fosforo + quantidades_jantar[alimento.nome] * alimento.fosforo for alimento in alimentos]) <= atributos.fosforo_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.lipidios + quantidades_almoco[alimento.nome] * alimento.lipidios + quantidades_jantar[alimento.nome] * alimento.lipidios for alimento in alimentos]) >= atributos.lipidios_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.lipidios + quantidades_almoco[alimento.nome] * alimento.lipidios + quantidades_jantar[alimento.nome] * alimento.lipidios for alimento in alimentos]) <= atributos.lipidios_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.magnesio + quantidades_almoco[alimento.nome] * alimento.magnesio + quantidades_jantar[alimento.nome] * alimento.magnesio for alimento in alimentos]) >= atributos.magnesio_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.magnesio + quantidades_almoco[alimento.nome] * alimento.magnesio + quantidades_jantar[alimento.nome] * alimento.magnesio for alimento in alimentos]) <= atributos.magnesio_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.manganes + quantidades_almoco[alimento.nome] * alimento.manganes + quantidades_jantar[alimento.nome] * alimento.manganes for alimento in alimentos]) >= atributos.manganes_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.manganes + quantidades_almoco[alimento.nome] * alimento.manganes + quantidades_jantar[alimento.nome] * alimento.manganes for alimento in alimentos]) <= atributos.manganes_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.niacina + quantidades_almoco[alimento.nome] * alimento.niacina + quantidades_jantar[alimento.nome] * alimento.niacina for alimento in alimentos]) >= atributos.niacina_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.niacina + quantidades_almoco[alimento.nome] * alimento.niacina + quantidades_jantar[alimento.nome] * alimento.niacina for alimento in alimentos]) <= atributos.niacina_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.potassio + quantidades_almoco[alimento.nome] * alimento.potassio + quantidades_jantar[alimento.nome] * alimento.potassio for alimento in alimentos]) >= atributos.potassio_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.potassio + quantidades_almoco[alimento.nome] * alimento.potassio + quantidades_jantar[alimento.nome] * alimento.potassio for alimento in alimentos]) <= atributos.potassio_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.proteina + quantidades_almoco[alimento.nome] * alimento.proteina + quantidades_jantar[alimento.nome] * alimento.proteina for alimento in alimentos]) >= atributos.proteina_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.proteina + quantidades_almoco[alimento.nome] * alimento.proteina + quantidades_jantar[alimento.nome] * alimento.proteina for alimento in alimentos]) <= atributos.proteina_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.riboflavina + quantidades_almoco[alimento.nome] * alimento.riboflavina + quantidades_jantar[alimento.nome] * alimento.riboflavina for alimento in alimentos]) >= atributos.riboflavina_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.riboflavina + quantidades_almoco[alimento.nome] * alimento.riboflavina + quantidades_jantar[alimento.nome] * alimento.riboflavina for alimento in alimentos]) <= atributos.riboflavina_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.selenio + quantidades_almoco[alimento.nome] * alimento.selenio + quantidades_jantar[alimento.nome] * alimento.selenio for alimento in alimentos]) >= atributos.selenio_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.selenio + quantidades_almoco[alimento.nome] * alimento.selenio + quantidades_jantar[alimento.nome] * alimento.selenio for alimento in alimentos]) <= atributos.selenio_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.sodio + quantidades_almoco[alimento.nome] * alimento.sodio + quantidades_jantar[alimento.nome] * alimento.sodio for alimento in alimentos]) >= atributos.sodio_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.sodio + quantidades_almoco[alimento.nome] * alimento.sodio + quantidades_jantar[alimento.nome] * alimento.sodio for alimento in alimentos]) <= atributos.sodio_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.tiamina + quantidades_almoco[alimento.nome] * alimento.tiamina + quantidades_jantar[alimento.nome] * alimento.tiamina for alimento in alimentos]) >= atributos.tiamina_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.tiamina + quantidades_almoco[alimento.nome] * alimento.tiamina + quantidades_jantar[alimento.nome] * alimento.tiamina for alimento in alimentos]) <= atributos.tiamina_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_a_rae + quantidades_almoco[alimento.nome] * alimento.vitamina_a_rae + quantidades_jantar[alimento.nome] * alimento.vitamina_a_rae for alimento in alimentos]) >= atributos.vitamina_a_rae_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_a_rae + quantidades_almoco[alimento.nome] * alimento.vitamina_a_rae + quantidades_jantar[alimento.nome] * alimento.vitamina_a_rae for alimento in alimentos]) <= atributos.vitamina_a_rae_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_b12 + quantidades_almoco[alimento.nome] * alimento.vitamina_b12 + quantidades_jantar[alimento.nome] * alimento.vitamina_b12 for alimento in alimentos]) >= atributos.vitamina_b12_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_b12 + quantidades_almoco[alimento.nome] * alimento.vitamina_b12 + quantidades_jantar[alimento.nome] * alimento.vitamina_b12 for alimento in alimentos]) <= atributos.vitamina_b12_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_b6 + quantidades_almoco[alimento.nome] * alimento.vitamina_b6 + quantidades_jantar[alimento.nome] * alimento.vitamina_b6 for alimento in alimentos]) >= atributos.vitamina_b6_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_b6 + quantidades_almoco[alimento.nome] * alimento.vitamina_b6 + quantidades_jantar[alimento.nome] * alimento.vitamina_b6 for alimento in alimentos]) <= atributos.vitamina_b6_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_c + quantidades_almoco[alimento.nome] * alimento.vitamina_c + quantidades_jantar[alimento.nome] * alimento.vitamina_c for alimento in alimentos]) >= atributos.vitamina_c_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_c + quantidades_almoco[alimento.nome] * alimento.vitamina_c + quantidades_jantar[alimento.nome] * alimento.vitamina_c for alimento in alimentos]) <= atributos.vitamina_c_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_d + quantidades_almoco[alimento.nome] * alimento.vitamina_d + quantidades_jantar[alimento.nome] * alimento.vitamina_d for alimento in alimentos]) >= atributos.vitamina_d_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.vitamina_d + quantidades_almoco[alimento.nome] * alimento.vitamina_d + quantidades_jantar[alimento.nome] * alimento.vitamina_d for alimento in alimentos]) <= atributos.vitamina_d_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.zinco + quantidades_almoco[alimento.nome] * alimento.zinco + quantidades_jantar[alimento.nome] * alimento.zinco for alimento in alimentos]) >= atributos.zinco_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.zinco + quantidades_almoco[alimento.nome] * alimento.zinco + quantidades_jantar[alimento.nome] * alimento.zinco for alimento in alimentos]) <= atributos.zinco_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_monossaturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_monossaturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_monossaturados for alimento in alimentos]) >= atributos.acidos_graxos_monossaturados_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_monossaturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_monossaturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_monossaturados for alimento in alimentos]) <= atributos.acidos_graxos_monossaturados_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_polissaturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_polissaturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_polissaturados for alimento in alimentos]) >= atributos.acidos_graxos_polissaturados_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_polissaturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_polissaturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_polissaturados for alimento in alimentos]) <= atributos.acidos_graxos_polissaturados_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_saturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_saturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_saturados for alimento in alimentos]) >= atributos.acidos_graxos_saturados_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_saturados + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_saturados + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_saturados for alimento in alimentos]) <= atributos.acidos_graxos_saturados_max

problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_trans + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_trans + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_trans for alimento in alimentos]) >= atributos.acidos_graxos_trans_min
problema += lpSum([quantidades_cafe[alimento.nome] * alimento.acidos_graxos_trans + quantidades_almoco[alimento.nome] * alimento.acidos_graxos_trans + quantidades_jantar[alimento.nome] * alimento.acidos_graxos_trans for alimento in alimentos]) <= atributos.acidos_graxos_trans_max




# Restrições de palatabilidade (mínimo 1/5 da soma das palatabilidades totais)
total_palatabilidade_cafe = lpSum([quantidades_cafe[alimento.nome] * alimento.palatabilidade_cafe for alimento in alimentos])
total_palatabilidade_almoco = lpSum([quantidades_almoco[alimento.nome] * alimento.palatabilidade_almoco for alimento in alimentos])
total_palatabilidade_jantar = lpSum([quantidades_jantar[alimento.nome] * alimento.palatabilidade_jantar for alimento in alimentos])
problema += total_palatabilidade_cafe >= 1/5 * (total_palatabilidade_cafe + total_palatabilidade_almoco + total_palatabilidade_jantar)
problema += total_palatabilidade_almoco >= 1/5 * (total_palatabilidade_cafe + total_palatabilidade_almoco + total_palatabilidade_jantar)
problema += total_palatabilidade_jantar >= 1/5 * (total_palatabilidade_cafe + total_palatabilidade_almoco + total_palatabilidade_jantar)

# Resolver o problema
problema.solve()

# Exibir a solução
solucao = {
    "cafe": {alimento.nome: quantidades_cafe[alimento.nome].varValue if quantidades_cafe[alimento.nome].varValue > 0 else 0 for alimento in alimentos},
    "almoco": {alimento.nome: quantidades_almoco[alimento.nome].varValue if quantidades_almoco[alimento.nome].varValue > 0 else 0 for alimento in alimentos},
    "jantar": {alimento.nome: quantidades_jantar[alimento.nome].varValue if quantidades_jantar[alimento.nome].varValue > 0 else 0 for alimento in alimentos}
}

# Filtrar apenas os alimentos com quantidades maiores que zero
solucao_cafe = {key: value for key, value in solucao['cafe'].items() if value > 0}
solucao_almoco = {key: value for key, value in solucao['almoco'].items() if value > 0}
solucao_jantar = {key: value for key, value in solucao['jantar'].items() if value > 0}

# Exibir os resultados
print("Solução para o café:")
print(solucao_cafe)

print("\nSolução para o almoço:")
print(solucao_almoco)

print("\nSolução para o jantar:")
print(solucao_jantar)