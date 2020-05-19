print('Ex 18 - Site wiki.python.org.br/EstruturaSequencial \n Eduardo Sforni')

tamanho = float(input('Qual é o tamanho do arquivo para download (MB)? \n'))
velocidade = float(input('Qual é valocidade da sua internet (Mbps)? \n'))

tempo = tamanho / velocidade #Em segundos

tempo = tempo / 60 #Tempo em minutos
tempo = round(tempo,2)
print('Demorará', tempo, 'minuto(s)')