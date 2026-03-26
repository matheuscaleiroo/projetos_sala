from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import session, make_response
from flask import flash
import db
import hashlib
 
app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
 
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
 
        conn = db.get_db()
        cursor = conn.cursor()
 
        user = request.form.get('email')
        password = hashlib.md5(request.form.get('password').encode()).hexdigest()
 
        #vulnerabilidade?
        query = f"SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query,(user,password))
 
        user = cursor.fetchone()
 
        if user:
           
            session['user'] = user['username']
 
            resposta = make_response(redirect(url_for('painel')))
            resposta.set_cookie('tema','dark',max_age=600)
 
            return resposta
       
        else:
            flash('Usuário ou senha inválido')
            return render_template('login.html')
       
    return render_template('login.html')
 
@app.route('/painel')
def painel():
    if 'user' in session:
        return render_template('painel.html')
   
    flash('Efetue o login')
    return redirect(url_for('login'))