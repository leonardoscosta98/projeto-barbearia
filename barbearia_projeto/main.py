from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, flash, session

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
	try:
		login = session['usuario_logado']
		return render_template("index.html", login = login)
	except:
		session['usuario_logado'] = None
		return render_template("index.html", login = session['usuario_logado'])

