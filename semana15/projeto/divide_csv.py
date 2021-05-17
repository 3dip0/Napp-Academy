import csv
import os

def divideCSV():
	deletar()
	with open('candidatura.csv') as arquivo:
		read = csv.DictReader(arquivo)
		ano = ''
		anoAuxiliar = ''
		for linha in read:
			anoAuxiliar = linha['ano_eleicao']
			if anoAuxiliar == ano:
				with open(f'eleicao_{ano}.csv', 'a') as arquivo:
					write = csv.writer(arquivo)
					write.writerow(linha.values())
			else:
				print(linha['ano_eleicao'])
				ano = linha['ano_eleicao']
				with open(f'eleicao_{ano}.csv', 'a') as arquivo:
					write = csv.writer(arquivo)
					write.writerow(linha)

def deletar():
	with open('candidatura.csv') as arquivo:
		read = csv.DictReader(arquivo)
		for linha in read:
			try:
				os.remove(f"eleicao_{linha['ano_eleicao']}.csv")
			except:
				pass

divideCSV()
