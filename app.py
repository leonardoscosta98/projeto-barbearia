from flask import Flask, render_template, redirect, url_for, flash, session
from db import execQuery
from flask import request
from datetime import datetime
from utils import retornaDiaSemana, formataDisponibilidade, verificandoDisponibilidade, retornaTabela, formataDisponibilidadeSexta, verificandoDisponibilidadeSexta, formataDisponibilidadeSabado, verificandoDisponibilidadeSexta

app = Flask(__name__)
app.secret_key = 'barbearia'

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome 
        self.nickname = nickname
        self.senha = senha

usuario = Usuario('Leonardo Costa', 'Leo', '123')    

usuarios = {usuario.nickname : usuario}

@app.route("/")
def index():
	try:
		login = session['usuario_logado']
		return render_template("index.html", login = login)
	except:
		session['usuario_logado'] = None
		return render_template("index.html", login = session['usuario_logado'])
	


@app.route("/agenda", methods=["POST", "GET"])
def agenda():
	
	dia_atual = datetime.today().strftime('%Y-%m-%d')
	search = request.form.get("search","")
	if search != '':
		datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
		dia_da_semana = retornaDiaSemana(search)
	else:
		search= datetime.today().strftime('%Y-%m-%d')
		dia_da_semana = retornaDiaSemana(search)
		datatable= datetime.today().strftime('%d-%m-%Y')
		
	from_tabela = retornaTabela(search)


	if search < dia_atual:	
		flash('Data indisponível'.format(search))
		search = dia_atual
		datatable = datetime.today().strftime('%d-%m-%Y')
		dia_da_semana = retornaDiaSemana(search)
	
	if dia_da_semana in ['Domingo'] and session['usuario_logado'] == None  :
		flash('Desculpe, não atendemos aos Domingos.'.format(search))
		
	
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
	
	if from_tabela not in ['sexta_sexta','sabado_sabado']:
		disponibilidade = verificandoDisponibilidade(agenda,formataDisponibilidade(disponivel[0]))
	elif from_tabela in ['sexta_sexta']:
		disponibilidade = verificandoDisponibilidadeSexta(agenda,formataDisponibilidadeSexta(disponivel[0]))
	elif from_tabela in ['sabado_sabado']:
		disponibilidade = verificandoDisponibilidadeSexta(agenda,formataDisponibilidadeSexta(disponivel[0]))

	
	return render_template("agenda.html", disponibilidades=disponibilidade, filtro=search, datatable=datatable, dia=dia_da_semana, login = session['usuario_logado'])

@app.route("/agendamento/<datatable>/<horario>", methods=["POST", "GET"])
def agendamento(datatable,horario):	

	dia_da_semana = retornaDiaSemana(datatable)

	return render_template("novo.html", datatable=datatable, horario=horario, dia= dia_da_semana, login = session['usuario_logado'])

@app.route("/confirmacao/<datatable>/<horario>", methods=["POST", "GET"])
def confirmacao(datatable,horario):	

	nome = request.form.get("nome","")
	celular = request.form.get("celular","")
	servicos = request.form.get("1","") + request.form.get("2","")+request.form.get("3","")+request.form.get("4","") +request.form.get("5","")+request.form.get("6","")+request.form.get("7","")+request.form.get("8","")+request.form.get("9","")+request.form.get("10","")+request.form.get("11","")+request.form.get("12","")
	observacao = request.form.get("observacao","")

	
	try:
		if horario == '06:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, seis, name, celular, servico, observacao)
						VALUES ('{}','06:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '07:00':
			gravar = execQuery("""
					INSERT INTO agendamento(
					data, disponibilidade, sete, name, celular, servico, observacao)
					VALUES ('{}', '07:00', 1, '{}','{}','{}','{}');""".format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '08:00':
			gravar = execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, oito, name, celular, servico, observacao)
					VALUES ('{}','08:00', 1, '{}','{}','{}','{}');""".format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '09:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, nove, name, celular, servico, observacao)
					VALUES ('{}','09:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '10:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, dez, name, celular, servico, observacao)
					VALUES ('{}','10:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '11:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, onze, name, celular, servico, observacao)
					VALUES ('{}','11:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '14:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, quatorze, name, celular, servico, observacao)
					VALUES ('{}','14:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '15:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, quinze, name, celular, servico, observacao)
					VALUES ('{}','15:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '16:00':
			gravar =execQuery("""
					INSERT INTO agendamento(
					data,disponibilidade, dezesseis, name, celular, servico, observacao)
					VALUES ('{}','16:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '17:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, dezessete, name, celular, servico, observacao)
						VALUES ('{}','17:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '18:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, dezoito, name, celular, servico, observacao)
						VALUES ('{}','18:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '19:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, dezenove, name, celular, servico, observacao)
						VALUES ('{}','19:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '20:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, vinte, name, celular, servico, observacao)
						VALUES ('{}','20:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '21:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, vinte_um, name, celular, servico, observacao)
						VALUES ('{}','21:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)
		elif horario == '22:00':
			gravar = execQuery("""
						INSERT INTO agendamento(
						data,disponibilidade, vinte_dois, name, celular, servico, observacao)
						VALUES ('{}','22:00', 1, '{}','{}','{}','{}'); """.format(datatable,nome, celular, servicos, observacao), onlyExec=True)

	except:
		flash('Falha ao reservar horário, tente novamente!')
		return redirect(url_for('agenda'))


	flash('Horário reservado com sucesso!')
	return redirect(url_for('agenda'))


@app.route("/admin", methods=["POST", "GET"])
def admin():	

	if 'usuario_logado' not in session or session['usuario_logado'] == None:
		return redirect(url_for('login', proxima=url_for('admin')))

	dia_atual = datetime.today().strftime('%Y-%m-%d')
	search = request.form.get("search","")
	if search != '':
		datatable = datetime.strptime(search, '%Y-%m-%d').strftime("%d-%m-%Y")
		dia_da_semana = retornaDiaSemana(search)
	else:
		search= datetime.today().strftime('%Y-%m-%d')
		dia_da_semana = retornaDiaSemana(search)
		datatable= datetime.today().strftime('%d-%m-%Y')
		

	disponibilidade = execQuery("""
		select 
		*
		from agendamento where data = '{}' order by disponibilidade """.format(search))

	return render_template("admin.html", disponibilidades=disponibilidade, filtro=search, datatable=datatable, dia=dia_da_semana, login = session['usuario_logado'])


@app.route('/login')
def login():
    proxima = url_for('admin')

    if request.args.get('proxima') != None:
        proxima = request.args.get('proxima')
    
    return render_template('login.html', proxima=proxima, login = session['usuario_logado'])


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Bem vindo, ' + usuario.nickname+'!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')

    return redirect(url_for('index'))

@app.route('/delete/<id>',methods=['POST', ])
def delete(id):

	if 'usuario_logado' not in session or session['usuario_logado'] == None:
		return redirect(url_for('login', proxima=url_for('admin')))
    
	execQuery("""delete from agendamento where id = {} """.format(id),onlyExec=True) 
	
	return redirect(url_for('admin'))

# if __name__ == "__main__":
app.run(debug=True)
