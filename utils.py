from datetime import datetime

def retornaDiaSemana(dataDia):

	DIAS = [
    'Segunda-Feira',
    'Terça-Feira',
    'Quarta-Feira',
    'Quinta-Feira',
    'Sexta-Feira',
    'Sábado',
    'Domingo'
	]

	data = datetime.strptime(dataDia, '%Y-%m-%d').date()
	data = data.weekday()
	return DIAS[data]

def retornaTabela(dataDia):

	TABELA = [
    'segunda_segunda',
    'terca_terca',
    'quarta_quarta',
    'quinta_quinta',
    'sexta_sexta',
    'sabado_sabado',
    'domingo_domingo'
	]

	data = datetime.strptime(dataDia, '%Y-%m-%d').date()
	data = data.weekday()
	return TABELA[data]

def formataDisponibilidade(dict):
	
	if dict.get('sete') == 1:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') == 1:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') == 1:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') == 1:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') == 1:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('quatorze') == 1:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') == 1:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') == 1:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') == 1:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})
	
	if dict.get('dezoito') == 1:
		dict.update({'dezoito':'Indisponível'})
	else:
		dict.update({'dezoito':'Disponível'})

	return dict

def formataDisponibilidadeSexta(dict):
	
	if dict.get('seis') == 1:
		dict.update({'seis':'Indisponível'})
	else:
		dict.update({'seis':'Disponível'})

	if dict.get('sete') == 1:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') == 1:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') == 1:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') == 1:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') == 1:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('quatorze') == 1:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') == 1:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') == 1:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') == 1:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})
	
	if dict.get('dezoito') == 1:
		dict.update({'dezoito':'Indisponível'})
	else:
		dict.update({'dezoito':'Disponível'})
	
	if dict.get('dezenove') == 1:
		dict.update({'dezenove':'Indisponível'})
	else:
		dict.update({'dezenove':'Disponível'})
	
	if dict.get('vinte') == 1:
		dict.update({'vinte':'Indisponível'})
	else:
		dict.update({'vinte':'Disponível'})
	
	if dict.get('vinte_um') == 1:
		dict.update({'vinte_um':'Indisponível'})
	else:
		dict.update({'vinte_um':'Disponível'})
	
	if dict.get('vinte_dois') == 1:
		dict.update({'vinte_dois':'Indisponível'})
	else:
		dict.update({'vinte_dois':'Disponível'})

	return dict

def formataDisponibilidadeSabado(dict):
	
	if dict.get('seis') == 1:
		dict.update({'seis':'Indisponível'})
	else:
		dict.update({'seis':'Disponível'})

	if dict.get('sete') == 1:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') == 1:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') == 1:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') == 1:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') == 1:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('quatorze') == 1:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') == 1:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') == 1:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') == 1:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})
	
	if dict.get('dezoito') == 1:
		dict.update({'dezoito':'Indisponível'})
	else:
		dict.update({'dezoito':'Disponível'})

	return dict

def verificandoDisponibilidade(agenda,newDict):
	
	for x in range(len(agenda)):
		if x == 0:
			agenda[x]['status'] = newDict.get('sete')
		elif x == 1:
			agenda[x]['status'] = newDict.get('oito')
		elif x == 2:
			agenda[x]['status'] = newDict.get('nove')
		elif x == 3:
			agenda[x]['status'] = newDict.get('dez')
		elif x == 4:
			agenda[x]['status'] = newDict.get('onze')
		elif x == 5:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 6:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 8:
			agenda[x]['status'] = newDict.get('dezessete')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezoito')


	return agenda

def verificandoDisponibilidadeSexta(agenda,newDict):
	
	for x in range(len(agenda)):
		if x == 0:
			agenda[x]['status'] = newDict.get('seis')
		if x == 1:
			agenda[x]['status'] = newDict.get('sete')
		elif x == 2:
			agenda[x]['status'] = newDict.get('oito')
		elif x == 3:
			agenda[x]['status'] = newDict.get('nove')
		elif x == 4:
			agenda[x]['status'] = newDict.get('dez')
		elif x == 5:
			agenda[x]['status'] = newDict.get('onze')
		elif x == 6:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 8:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezessete')
		elif x == 10:
			agenda[x]['status'] = newDict.get('dezoito')
		elif x == 11:
			agenda[x]['status'] = newDict.get('dezenove')
		elif x == 12:
			agenda[x]['status'] = newDict.get('vinte')
		elif x == 13:
			agenda[x]['status'] = newDict.get('vinte_um')
		elif x == 14:
			agenda[x]['status'] = newDict.get('vinte_dois')


	return agenda

def verificandoDisponibilidadeSabado(agenda,newDict):
	
	for x in range(len(agenda)):
		if x == 0:
			agenda[x]['status'] = newDict.get('sete')
		elif x == 1:
			agenda[x]['status'] = newDict.get('oito')
		elif x == 2:
			agenda[x]['status'] = newDict.get('nove')
		elif x == 3:
			agenda[x]['status'] = newDict.get('dez')
		elif x == 4:
			agenda[x]['status'] = newDict.get('onze')
		elif x == 5:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 6:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 8:
			agenda[x]['status'] = newDict.get('dezessete')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezoito')


	return agenda