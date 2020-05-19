print('Ex 17 - Site wiki.python.org.br/EstruturaSequencial \n Eduardo Sforni')

tamanho = float(input('Quantos metros quadrados será pintado? ( m^2 )\n'))
tamanho = tamanho*1.1 #Adicionar 10%

QntLitros = tamanho / 6
QntLatas = QntLitros / 18
QntGaloes = QntLitros / 3.6
QntLatas = round(QntLatas+0.5,0)
QntGaloes = round(QntGaloes+0.5,0)

QntLatasMix = QntLitros / 18
QntLatasMix = round(QntLatas-0.5,0) #Arredonda para baixo
QntLatasResto = QntLitros % 18
QntGaloesMix = QntLatasResto / 3.6
QntGaloesMix = round(QntGaloesMix+0.5,0) #Arredond para cima

#Possibilida 1 só latas
print('Só latas')
print('Quantidade de latas é de', QntLatas)
print('Custaria', QntLatas*80, 'reais \n')
#Possibilida 2 só galoes
print('Só galões')
print('Quantidade de latas é de', QntGaloes)
print('Custaria', QntGaloes*25, 'reais \n')
#Possibilida 3 mix para melhorar
print('Mix')
print('Quantidade é de', QntLatasMix, 'latas e', QntGaloesMix, 'galões')
print('Preço total é de', QntLatasMix*80+QntGaloesMix*25, 'reais')




