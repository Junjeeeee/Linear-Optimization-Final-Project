import pandas as pd
from pulp import *

class Alimento:
    def __init__(self, nome, palatabilidade_cafe, palatabilidade_almoco, palatabilidade_jantar, preco, calorias, vitamina_e,
                 carboidrato_disponivel, cinzas, cobre, colesterol, calcio, equivalente_de_folato, ferro, fibras, fosforo,
                 lipidios, magnesio, manganes, niacina, potassio, proteina, riboflavina, selenio, sodio, tiamina,
                 vitamina_a_rae, vitamina_a_re, vitamina_b12, vitamina_b6, vitamina_c, vitamina_d, zinco,
                 acidos_graxos_monossaturados, acidos_graxos_polissaturados, acidos_graxos_saturados, acidos_graxos_trans):
        self.nome = nome
        self.palatabilidade_cafe = palatabilidade_cafe
        self.palatabilidade_almoco = palatabilidade_almoco
        self.palatabilidade_jantar = palatabilidade_jantar
        self.preco = preco
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

    

# Carregar os dados do CSV
df = pd.read_csv('/mnt/data/dados.csv')

# Criar uma lista de objetos Alimento
alimentos = []
for index, row in df.iterrows():
    alimento = Alimento(
        nome=row['Alimento'],
        palatabilidade_cafe=row['Palatabildiade Café (0-10)'],
        palatabilidade_almoco=row['Palatabildiade Almoço (0-10)'],
        palatabilidade_jantar=row['Palatabildiade Jantar (0-10)'],
        preco=row['Preço'],
        calorias=row[' Energia (kJ/kcal)'],
        vitamina_e=row['Alfa-tocoferol (Vitamina E) (mg)'],
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
        niacina=row[' Niacina (mg)'],
        potassio=row[' Potássio (mg)'],
        proteina=row[' Proteína (g)'],
        riboflavina=row[' Riboflavina (mg)'],
        selenio=row[' Selênio (mcg)'],
        sodio=row[' Sódio (mg)'],
        tiamina=row[' Tiamina (mg)'],
        vitamina_a_rae=row[' Vitamina A (RAE) (mcg)'],
        vitamina_b12=row[' Vitamina B12 (mcg)'],
        vitamina_b6=row[' Vitamina B6 (mg)'],
        vitamina_c=row[' Vitamina C (mg)'],
        vitamina_d=row[' Vitamina D (mcg)'],
        zinco=row[' Zinco (mg)'],
        acidos_graxos_monossaturados=row[' Ácidos graxos monoinsaturados (g)'],
        acidos_graxos_polissaturados=row[' Ácidos graxos poliinsaturados (g)'],
        acidos_graxos_saturados=row[' Ácidos graxos saturados (g)'],
        acidos_graxos_trans=row[' Ácidos graxos trans (g)']
    )
    alimentos.append(alimento)


class Atributos_pl:
    
    def __init__(self,nome,peso_monetario,peso_palatabilidade,calorias_max_cafe,calorias_max_almoco,calorias_max_jantar,vitamina_e_min,vitamina_e_max,carboidrato_min,carboidrato_max
                 ,cinzas_min,cinzas_max,cobre_min,cobre_max,colesterol_min,colesterol_max,calcio_min,calcio_max,equivalente_de_folato_min,equivalente_de_folato_max,ferro_min
                 ,ferro_max,fibras_min,fibras_max,fosforo_min,fosforo_max,lipidios_min,lipidios_max,magnesio_min,magnesio_max,manganes_min,manganes_max,niacina_min,niacina_max,
                 potassio_min,potassio_max,proteina_min,proteina_max,riboflavina_min,riboflavina_max,selenio_min,selenio_max,sodio_min,sodio_max,tiamina_min,tiamina_max,vitamina_a_rae_min
                 ,vitamina_a_rae_max,vitamina_b12_min,vitamina_b12_max,vitamina_b6_min,vitamina_b6_max,vitamina_c_min,vitamina_c_max,vitamina_d_min,vitamina_d_max,zinco_min,zinco_max,
                 acidos_graxos_monossaturados_min,acidos_graxos_monossaturados_max,acidos_graxos_polissaturados_min,acidos_graxos_polissaturados_max,acidos_graxos_saturados_min,
                 acidos_graxos_saturados_max,acidos_graxos_trans_min,acidos_graxos_trans_max):
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


def resolve_pl(atributos): #recebe um objeto do tipo atributos_pl
    prob = LpProblem("ProblemaLinear", LpMinimize)
    Q_a = LpVariable.dicts("Q_a", range(3*len(alimentos)), lowBound=0) # pra cada alimento temos 3 variaveis de decisao, usar ela no café da manha, no almoço ou no jantar

    for x in range(len(Q_a)):
        prob += Q_a[x]*(alimentos[x//3].preco)
        if x%3 == 0:
            prob += -Q_a[x]*(alimentos[x//3].palatabilidade_cafe) # se o modulo 0 é referente a usar o alimento no café
        if x%3 == 1:
            prob += -Q_a[x]*(alimentos[x//3].palatabilidade_almoco) # se o modulo 0 é referente a usar o alimento no almoço
        if x%3 == 2:
            prob += -Q_a[x]*(alimentos[x//3].palatabilidade_jantar) # se o modulo 0 é referente a usar o alimento na janta

    #restrições fortes:

    #minimo de palatabilidade para cada refeição (a palatabilidade da refeição deve ser maior que 1/5 da palatabilidade total)
    prob += lpSum(alimentos[x//3].palatabilidade_cafe * Q_a[x] for x in range(0,len(Q_a),3))  >=  lpSum(alimentos[a//3].palatabilidade_cafe * Q_a[a] for a in range(0,len(Q_a),3)) + lpSum(alimentos[b//3].palatabilidade_almoco * Q_a[b] for b in range(1,len(Q_a),3)) + lpSum(alimentos[c//3].palatabilidade_jantar * Q_a[c] for x in range(2,len(Q_a),3)) * 1/5
    prob += lpSum(alimentos[x//3].palatabilidade_almoco * Q_a[x] for x in range(1,len(Q_a),3))  >=  lpSum(alimentos[a//3].palatabilidade_cafe * Q_a[a] for a in range(0,len(Q_a),3)) + lpSum(alimentos[b//3].palatabilidade_almoco * Q_a[b] for b in range(1,len(Q_a),3)) + lpSum(alimentos[c//3].palatabilidade_jantar * Q_a[c] for x in range(2,len(Q_a),3)) * 1/5
    prob += lpSum(alimentos[x//3].palatabilidade_jantar * Q_a[x] for x in range(2,len(Q_a),3))  >=  lpSum(alimentos[a//3].palatabilidade_cafe * Q_a[a] for a in range(0,len(Q_a),3)) + lpSum(alimentos[b//3].palatabilidade_almoco * Q_a[b] for b in range(1,len(Q_a),3)) + lpSum(alimentos[c//3].palatabilidade_jantar * Q_a[c] for x in range(2,len(Q_a),3)) * 1/5

    #min e max de calorias por refeição
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(0,len(Q_a),3)) >= atributos.calorias_min_cafe
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(0,len(Q_a),3)) <= atributos.calorias_max_cafe
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(1,len(Q_a),3)) >= atributos.calorias_max_almoco
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(1,len(Q_a),3)) <= atributos.calorias_max_almoco
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(2,len(Q_a),3)) >= atributos.calorias_max_jantar
    prob += lpSum(alimentos[x//3].calorias * Q_a[x] for x in range(2,len(Q_a),3)) <= atributos.calorias_max_jantar

    #min e max de cada nutriente
    prob += lpSum(alimentos[x//3].vitamina_e * Q_a[x] for x in range(len(Q_a))) >= atributos.vitamina_e_min
    prob += lpSum(alimentos[x//3].vitamina_e * Q_a[x] for x in range(len(Q_a))) <= atributos.vitamina_e_max
    #falta preencher pra todos os outros nutrientes


    prob.solve()

    # Exibir resultados
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    print("Valor da função objetivo = ", value(prob.objective))