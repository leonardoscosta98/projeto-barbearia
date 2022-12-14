from email.policy import default
from flask import Flask, render_template, redirect, url_for, flash, session
from .db import execQuery
from flask import Blueprint
from flask import request
from os import environ
import pytz
from datetime import datetime, timedelta
from .utils import agendamentoSemanal, adicionaServicos, retornaDiaSemana, formataDisponibilidade, verificandoDisponibilidade, retornaTabela, formataDisponibilidadeSexta, verificandoDisponibilidadeSexta, formataDisponibilidadeSabado, verificandoDisponibilidadeSexta

bp = Blueprint("admin", __name__)


@bp.route("/")
def index():
	try:
		login = session['usuario_logado']
		return render_template("index.html", login = login)
	except:
		session['usuario_logado'] = None
		return render_template("index.html", login = session['usuario_logado'])

@bp.route("/agenda", defaults={"dataAnt":""}, methods=["POST", "GET"])
@bp.route("/agenda/<dataAnt>", methods=["POST", "GET"])
def agenda(dataAnt):
	

	Brasil             = pytz.timezone('America/Sao_Paulo')
	dia_atual 		   = datetime.today()
	data_formatada_tz  = dia_atual.replace(tzinfo=pytz.UTC)
	data_formatada_br  = data_formatada_tz.astimezone(Brasil)
	dia_atual 		   = data_formatada_br.strftime('%Y-%m-%d')

	try:
		login = session['usuario_logado']
	except:
		session['usuario_logado'] = None
		login = session['usuario_logado']

	search = request.form.get("search","")
	if search != '':
		datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
	else:
		if dataAnt != '':
			search= dataAnt
			datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
		else:
			search= dia_atual
			datatable= data_formatada_br.strftime('%d-%m-%Y')

	if (search < dia_atual):	
		flash('Falha! Data indisponível para agendamento.')
		search = dia_atual
		datatable = datetime.today().strftime('%d-%m-%Y')
		
	dia_da_semana = retornaDiaSemana(search)

	if ((dia_da_semana in ['Domingo','Segunda-Feira']) and (login == None)):
		search    = datetime.strptime(search, '%Y-%m-%d').date()
		if dia_da_semana == 'Domingo':
			search    = search + timedelta(2)
		elif dia_da_semana == 'Segunda-Feira':
			search    = search + timedelta(1)
		search    = search.strftime('%Y-%m-%d')
		dia_da_semana = retornaDiaSemana(search)

	from_tabela = retornaTabela(search)	

	agenda = execQuery("""
		select 
		*
		from {} """.format(from_tabela))

	disponivel = execQuery("""
		select 
		count(seis) as seis,
		count(sete) as sete,
		count(oito) as oito,
		count(nove) as nove,
		count(dez) as dez,
		count(onze) as onze,
		count(treze) as treze,
		count(quatorze) as quatorze,
		count(quinze) as quinze,
		count(dezesseis) as dezesseis,
		count(dezessete) as dezessete,
		count(dezoito) as dezoito,
		count(dezenove) as dezenove,
		count(vinte) as vinte,
		count(vinte_um) as vinte_um,
		count(vinte_dois) as vinte_dois
		from agendamento where data = '{}' """.format(search))
	
	if from_tabela not in ['sexta_sexta','sabado_sabado','domingo_domingo']:
		disponibilidade = verificandoDisponibilidade(agenda,formataDisponibilidade(disponivel[0]))
	elif from_tabela in ['sexta_sexta']:
		disponibilidade = verificandoDisponibilidadeSexta(agenda,formataDisponibilidadeSexta(disponivel[0]))
	elif from_tabela in ['sabado_sabado', 'domingo_domingo']:
		disponibilidade = verificandoDisponibilidadeSexta(agenda,formataDisponibilidadeSexta(disponivel[0]))


	if  ((login == None) and (agendamentoSemanal(search, dia_atual) == False)):
		flash('Falha! Data indisponível para agendamento.')
		disponibilidade = {}
	
	return render_template("agenda.html", disponibilidades=disponibilidade, filtro=search, datatable=datatable, dia=dia_da_semana, login = login)

@bp.route("/agendamento/<datatable>/<horario>", methods=["POST", "GET"])
def agendamento(datatable,horario):	

	try:
		login = session['usuario_logado']
	except:
		session['usuario_logado'] = None
		login = session['usuario_logado']

	dia_da_semana = retornaDiaSemana(datatable)

	return render_template("novo.html", datatable=datatable, horario=horario, dia= dia_da_semana, login = session['usuario_logado'])

@bp.route("/confirmacao/<datatable>/<horario>", methods=["POST", "GET"])
def confirmacao(datatable,horario):	

	nome = request.form.get("nome","")
	nome = nome.replace("'",'')
	nome = nome.replace('"','')
	celular = ''.join(filter(lambda i: i if i.isdigit() else None, request.form.get("celular","")))     
	servicos = str(adicionaServicos(request.form.get("CorteNavalhado",""),request.form.get("CorteTesoura",""),request.form.get("CorteMaqTesoura",""),request.form.get("CorteMaquina",""),request.form.get("AlisamentoCabelo",""),request.form.get("PinturaCabelo",""),request.form.get("PeCabelo",""),request.form.get("Reflexo",""),request.form.get("Barba",""),request.form.get("MarcarBarba",""),request.form.get("PinturaBarba",""),request.form.get("SobrancelhaM",""),request.form.get("SobrancelhaF","") )) 
	servicos = servicos.replace(',','\n')
	servicos = servicos.replace("'",'')
	servicos = servicos.replace("[",'')
	servicos = servicos.replace("]",'')
	observacao = request.form.get("observacao","")

	disponivel = execQuery("""
		select
		count(disponibilidade) as disponibilidade
		from agendamento 
		where disponibilidade= '{}'
		and  data = '{}' """.format(horario, datatable ))
	
	if disponivel[0].get('disponibilidade') > 0:
		flash('Falha! Horário indisponível, tente outro horário!')
		return redirect(url_for('admin.agenda'))

	try:
		if horario == '06:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, seis, name, celular, servico, observacao)
						VALUES ('{}','06:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '07:00':
			gravar = execQuery("""
					INSERT INTO public.agendamento(
					data, disponibilidade, sete, name, celular, servico, observacao)
					VALUES ('{}', '07:00', true, '{}','{}','{}','{}');""".format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '08:00':
			gravar = execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, oito, name, celular, servico, observacao)
					VALUES ('{}','08:00', true, '{}','{}','{}','{}');""".format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '09:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, nove, name, celular, servico, observacao)
					VALUES ('{}','09:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '10:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, dez, name, celular, servico, observacao)
					VALUES ('{}','10:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '11:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, onze, name, celular, servico, observacao)
					VALUES ('{}','11:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '13:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, treze, name, celular, servico, observacao)
					VALUES ('{}','13:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '14:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, quatorze, name, celular, servico, observacao)
					VALUES ('{}','14:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '15:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, quinze, name, celular, servico, observacao)
					VALUES ('{}','15:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '16:00':
			gravar =execQuery("""
					INSERT INTO public.agendamento(
					data,disponibilidade, dezesseis, name, celular, servico, observacao)
					VALUES ('{}','16:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '17:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, dezessete, name, celular, servico, observacao)
						VALUES ('{}','17:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '18:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, dezoito, name, celular, servico, observacao)
						VALUES ('{}','18:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '19:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, dezenove, name, celular, servico, observacao)
						VALUES ('{}','19:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '20:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, vinte, name, celular, servico, observacao)
						VALUES ('{}','20:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '21:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, vinte_um, name, celular, servico, observacao)
						VALUES ('{}','21:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '22:00':
			gravar = execQuery("""
						INSERT INTO public.agendamento(
						data,disponibilidade, vinte_dois, name, celular, servico, observacao)
						VALUES ('{}','22:00', true, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)

	except:
		flash('Falha ao reservar horário, tente novamente!')
		return redirect(url_for('admin.agenda'))


	flash('Horário reservado com sucesso!')
	return redirect(url_for('admin.agenda', dataAnt=datatable))

@bp.route("/admin", defaults={"dataAnt":""}, methods=["POST", "GET"])
@bp.route("/admin/<dataAnt>", methods=["POST", "GET"])
def admin(dataAnt):	

	try:
		login = session['usuario_logado']
	except:
		session['usuario_logado'] = None
		login = session['usuario_logado']

	if 'usuario_logado' not in session or login == None:
		return redirect(url_for('admin.login'))

	Brasil             = pytz.timezone('America/Sao_Paulo')
	dia_atual 		   = datetime.today()
	data_formatada_tz  = dia_atual.replace(tzinfo=pytz.UTC)
	data_formatada_br  = data_formatada_tz.astimezone(Brasil)
	dia_atual 		   = data_formatada_br.strftime('%Y-%m-%d')
	search = request.form.get("search","")
	
	if search != '':
		datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
	else:
		if dataAnt != '':
			search = datetime.strptime(dataAnt, '%d-%m-%Y').strftime("%Y-%m-%d")		 
			datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
		else:
			search= dia_atual
			datatable= data_formatada_br.strftime('%d-%m-%Y')
		

	dia_da_semana = retornaDiaSemana(search)	

	disponibilidade = execQuery("""
		select 
		*
		from agendamento where data = '{}' order by disponibilidade """.format(search))

	return render_template("admin.html", disponibilidades=disponibilidade, filtro=search, datatable=datatable, dia=dia_da_semana, login = session['usuario_logado'])


@bp.route('/login')
def login():
	try:
		login = session['usuario_logado']
	except:
		session['usuario_logado'] = None
		login = session['usuario_logado']
	
	proxima = url_for('admin.admin')
		
	return render_template('login.html', proxima=proxima, login = session['usuario_logado'])


@bp.route('/autenticar', methods=['POST', ])
def autenticar():

		Brasil             = pytz.timezone('America/Sao_Paulo')
		dia_atual 		   = datetime.today()
		data_formatada_tz  = dia_atual.replace(tzinfo=pytz.UTC)
		data_formatada_br  = data_formatada_tz.astimezone(Brasil)
		dia_atual 		   = data_formatada_br.strftime('%Y-%m-%d')

		usuario_usuario = execQuery("""
		select 
		*
		from usuarios_usuarios where login = '{}' and pass = '{}' """.format(request.form['usuario'], request.form['senha']))

		if usuario_usuario == []:
			flash('Falha! Usuário não logado.')
			return redirect(url_for('admin.login'))
		
		size_db = execQuery("""
		SELECT
		pg_size_pretty (
			pg_database_size ('{}')
		);""".format(environ.get('DATABASE_NAME')))
		
		size_db = size_db[0].get('pg_size_pretty').replace(' kB', '')
		size_db = size_db.replace(' MB', '')
		size_db = float(size_db)

		if (size_db / 1000) >= 18:
			execQuery("""delete from agendamento where data < '{}' """.format(dia_atual),onlyExec=True) 

		session['usuario_logado'] = usuario_usuario[0].get('login')
		flash('Bem vindo, ' + usuario_usuario[0].get('login')+'!')
		proxima_pagina = request.form['proxima']
		return redirect(proxima_pagina)

@bp.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')

    return redirect(url_for('admin.index'))

@bp.route('/delete/<id>/<datatable>',methods=['POST', ])
def delete(id, datatable):

	if 'usuario_logado' not in session or session['usuario_logado'] == None:
		return redirect(url_for('admin.login', proxima=url_for('admin.admin')))
    
	execQuery("""delete from agendamento where id = {} """.format(id),onlyExec=True) 
	
	return redirect(url_for('admin.admin', dataAnt= datatable))

@bp.route('/pagamento/<id>/<datatable>',methods=['POST','GET'])
def pagamento(id,datatable):
	
	pagamento = execQuery("""select pagamento from agendamento where id = '{}' """.format(id))

	if pagamento[0].get('pagamento') == True:
		execQuery("""UPDATE public.agendamento SET pagamento = null where id = '{}' """.format(id), onlyExec=True)
	else:
		execQuery("""UPDATE public.agendamento SET pagamento = True where id = '{}' """.format(id), onlyExec=True)


	return redirect(url_for('admin.admin', dataAnt= datatable))
