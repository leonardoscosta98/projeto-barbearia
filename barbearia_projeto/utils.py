from datetime import datetime, timedelta

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
	
	if dict.get('sete') != 0:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') != 0:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') != 0:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') != 0:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') != 0:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('treze') != 0:
		dict.update({'treze':'Indisponível'})
	else:
		dict.update({'treze':'Disponível'})
	
	if dict.get('quatorze') != 0:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') != 0:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') != 0:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') != 0:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})


	return dict

def formataDisponibilidadeSexta(dict):
	
	if dict.get('seis') != 0:
		dict.update({'seis':'Indisponível'})
	else:
		dict.update({'seis':'Disponível'})

	if dict.get('sete') != 0:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') != 0:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') != 0:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') != 0:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') != 0:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('treze') != 0:
		dict.update({'treze':'Indisponível'})
	else:
		dict.update({'treze':'Disponível'})
	
	if dict.get('quatorze') != 0:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') != 0:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') != 0:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') != 0:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})
	
	if dict.get('dezoito') != 0:
		dict.update({'dezoito':'Indisponível'})
	else:
		dict.update({'dezoito':'Disponível'})
	
	if dict.get('dezenove') != 0:
		dict.update({'dezenove':'Indisponível'})
	else:
		dict.update({'dezenove':'Disponível'})
	
	if dict.get('vinte') != 0:
		dict.update({'vinte':'Indisponível'})
	else:
		dict.update({'vinte':'Disponível'})
	
	if dict.get('vinte_um') != 0:
		dict.update({'vinte_um':'Indisponível'})
	else:
		dict.update({'vinte_um':'Disponível'})
	

	return dict

def formataDisponibilidadeSabado(dict):
	
	if dict.get('seis') != 0:
		dict.update({'seis':'Indisponível'})
	else:
		dict.update({'seis':'Disponível'})

	if dict.get('sete') != 0:
		dict.update({'sete':'Indisponível'})
	else:
		dict.update({'sete':'Disponível'})
	
	if dict.get('oito') != 0:
		dict.update({'oito':'Indisponível'})
	else:
		dict.update({'oito':'Disponível'})
	
	if dict.get('nove') != 0:
		dict.update({'nove':'Indisponível'})
	else:
		dict.update({'nove':'Disponível'})
	
	if dict.get('dez') != 0:
		dict.update({'dez':'Indisponível'})
	else:
		dict.update({'dez':'Disponível'})
	
	if dict.get('onze') != 0:
		dict.update({'onze':'Indisponível'})
	else:
		dict.update({'onze':'Disponível'})
	
	if dict.get('treze') != 0:
		dict.update({'treze':'Indisponível'})
	else:
		dict.update({'treze':'Disponível'})
	
	if dict.get('quatorze') != 0:
		dict.update({'quatorze':'Indisponível'})
	else:
		dict.update({'quatorze':'Disponível'})
	
	if dict.get('quinze') != 0:
		dict.update({'quinze':'Indisponível'})
	else:
		dict.update({'quinze':'Disponível'})
	
	if dict.get('dezesseis') != 0:
		dict.update({'dezesseis':'Indisponível'})
	else:
		dict.update({'dezesseis':'Disponível'})
	
	if dict.get('dezessete') != 0:
		dict.update({'dezessete':'Indisponível'})
	else:
		dict.update({'dezessete':'Disponível'})

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
			agenda[x]['status'] = newDict.get('treze')
		elif x == 6:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 8:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezessete')


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
			agenda[x]['status'] = newDict.get('treze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 8:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 10:
			agenda[x]['status'] = newDict.get('dezessete')
		elif x == 11:
			agenda[x]['status'] = newDict.get('dezoito')
		elif x == 12:
			agenda[x]['status'] = newDict.get('dezenove')
		elif x == 13:
			agenda[x]['status'] = newDict.get('vinte')
		elif x == 14:
			agenda[x]['status'] = newDict.get('vinte_um')

	return agenda

def verificandoDisponibilidadeSabado(agenda,newDict):
	
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
			agenda[x]['status'] = newDict.get('treze')
		elif x == 7:
			agenda[x]['status'] = newDict.get('quatorze')
		elif x == 8:
			agenda[x]['status'] = newDict.get('quinze')
		elif x == 9:
			agenda[x]['status'] = newDict.get('dezesseis')
		elif x == 10:
			agenda[x]['status'] = newDict.get('dezessete')


	return agenda


def agendamentoSemanal(search,dia_atual):

	if search == dia_atual:
		return True

	
	if dia_atual > search:
		return False
	
	dia_da_semana = retornaDiaSemana(dia_atual)

	dia_atual = datetime.strptime(dia_atual, '%Y-%m-%d').date()
	search    = datetime.strptime(search, '%Y-%m-%d').date()

	if dia_da_semana == 'Domingo':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(6)
	elif dia_da_semana == 'Segunda-Feira':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(5)
	elif dia_da_semana == 'Terça-Feira':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(4)
	elif dia_da_semana == 'Quarta-Feira':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(3)
	elif dia_da_semana == 'Quinta-Feira':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(2)
	elif dia_da_semana == 'Sexta-Feira':
		data_inicio = dia_atual
		data_fim    = dia_atual + timedelta(1)
	elif dia_da_semana == 'Sábado':
		data_inicio = dia_atual
		data_fim    = dia_atual 

	
	if data_inicio <= search <= data_fim:
		return True
	else:
		return False
	
def adicionaServicos(CorteNavalhado,CorteTesoura,CorteMaqTesoura,CorteMaquina,AlisamentoCabelo,PinturaCabelo,PeCabelo,Reflexo,Barba,MarcarBarba,PinturaBarba,SobrancelhaM,SobrancelhaF):

	listaservicos = []

	listaservicos.append(CorteNavalhado)
	listaservicos.append(CorteTesoura)
	listaservicos.append(CorteMaqTesoura)
	listaservicos.append(CorteMaquina)
	listaservicos.append(AlisamentoCabelo)
	listaservicos.append(PinturaCabelo)
	listaservicos.append(PeCabelo)
	listaservicos.append(Reflexo)
	listaservicos.append(Barba)
	listaservicos.append(MarcarBarba)
	listaservicos.append(PinturaBarba)
	listaservicos.append(SobrancelhaM)
	listaservicos.append(SobrancelhaF)
	
	servicosAux = []
	for x in range(len(listaservicos)):
		if listaservicos[x] != '':
			servicosAux.append(listaservicos[x])


	return servicosAux