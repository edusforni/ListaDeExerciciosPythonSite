print('Ex 15 - Site wiki.python.org.br/EstruturaSequencial \n Eduardo Sforni')

salH = float(input('Quantos reais você ganha por hora trabalhada? \n'))
trabH = float(input('Quantas horas você trabalhou esse mês? \n'))

print('Seu salário bruto é de', salH*trabH, 'reais')
dIR = salH*trabH*0.11
print('Você pagou', dIR, 'de IR')
dINSS = salH*trabH*0.08
print('Você pagou', dINSS, 'de INSS')
dSINDICATO = salH*trabH*0.05
print('Você pagou',dSINDICATO, 'de Sindicato')
salLiquido = salH*trabH - dIR - dSINDICATO - dINSS
print('Seu salário liquido é de', salLiquido, 'reais')

