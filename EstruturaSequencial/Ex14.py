print('Ex 14 - Site wiki.python.org.br/EstruturaSequencial \n Eduardo Sforni')
imprimir = 'n'
excedente = 0
multa =0
while imprimir != 's':
    pesoPeixe = float(input('Escreva o peso do peixe (kg) \n'))
    if pesoPeixe > 50:
        excedente = excedente + pesoPeixe - 50
        multa = excedente*4
    imprimir = input('Deseja finalizar operação e imprimir resultados? (s/n) \n ')

print('Excedente', excedente, 'kg')
multa = round(multa, 2)
print('Multa', multa, 'reais')