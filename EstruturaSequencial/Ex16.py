print('Ex 16 - Site wiki.python.org.br/EstruturaSequencial \n Eduardo Sforni')

tamanho = float(input('Quantos metros quadrados será pintado? ( m^2 )\n'))
QntLitros = tamanho / 3
QntLatas = QntLitros / 18
QntLatas = round(QntLatas+0.5, 0)  #maneira fácil de arredondar pra cima
print('Você precisa de', QntLatas, 'latas de tinta')
print('Custará', QntLatas*80, 'reais')



