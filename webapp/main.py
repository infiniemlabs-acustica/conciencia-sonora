'''
Archivo principal del proyecto, 
todo nuestro código Python estará en este archivo 
(rutas, conexión MySQL, validación, etc.).
'''

from flask import Flask, render_template, request, redirect, url_for, session
import re

from db import DB
from logs import Logs

try:
    app = Flask(__name__)
    db = DB()
    app.secret_key = 'cualquiercosa'

    # http://localhost:5000/cslogin/ - this will be the login page, we need to use both GET and POST requests
    @app.route('/concienciasonora/login/', methods = ['GET', 'POST'])
    def login():
        # Output message if something goes wrong...
        msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # Create variables for easy access
            username = request.form['username']
            password = request.form['password']
            # Check if account exists using MySQL            
            qi = 'SELECT * FROM cuentas WHERE username = %s AND password = %s'
            values = (username, password)
            account = db.getWhere(qi,values)
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[1]
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Usuario o contraseña incorrecta'

        # Show the login form with message (if any)
        return render_template('index.html', msg=msg)
    
    # http://localhost:5000/cslogin/logout - this will be the logout page
    @app.route('/concienciasonora/logout')
    def logout():
        # Remove session data, this will log the user out
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        # Redirect to login page
        return redirect(url_for('login'))    
    
    # http://localhost:5000/cslogin/register - this will be the registration page, we need to use both GET and POST requests
    @app.route('/concienciasonora/register', methods=['GET', 'POST'])
    def register():
        # Output message if something goes wrong...
        msg = ''
        # Check if "username", "password" and "email" POST requests exist (user submitted form)
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            # Create variables for easy access
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            
            # Check if account exists using MySQL            
            qi = 'SELECT * FROM cuentas WHERE username = %s'
            values = (username,)
            account = db.getWhere(qi,values)
            # If account exists show error and validation checks
            if account:
                msg = 'La cuenta ya existe!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Email invalido!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'El usuario solo debe contener caracteres y números!'
            elif not username or not password or not email:
                msg = 'Por favor completar el formulario!'
            else:
                # Account doesnt exists and the form data is valid, now insert new account into accounts table
                qi = 'INSERT INTO cuentas VALUES (NULL, %s, %s, %s)'
                values = (username, password, email)
                account = db.insert(qi,values)
                msg = 'You have successfully registered!'

        elif request.method == 'POST':
            # Form is empty... (no POST data)
            msg = 'Por favor completar el formulario!'
        # Show registration form with message (if any)
        return render_template('register.html', msg=msg)

    # http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
    @app.route('/concienciasonora/home')
    def home():
        # Check if user is loggedin
        if 'loggedin' in session:
            # User is loggedin show them the home page
            return render_template('home.html', username=session['username'])
        # User is not loggedin redirect to login page
        return redirect(url_for('login'))

    # http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
    @app.route('/concienciasonora/profile')
    def profile():
        # Check if user is loggedin
        if 'loggedin' in session:
            # We need all the account info for the user so we can display it on the profile page

            qi = 'SELECT * FROM cuentas WHERE id = %s'
            values = (session['id'],)
            account = db.getWhere(qi,values)
            print(account)
            # Show the profile page with account info
            return render_template('profile.html', account=account)
        # User is not loggedin redirect to login page
        return redirect(url_for('login'))
    
    # con host='0.0.0.0', se puede acceder desde cualquier cliente externo, a la direccion del equipo que se ejecuta el servidor flask
    app.run(host='0.0.0.0', port=5000, debug=True)

except Exception as e:
    logs = Logs()
    logs.appendFile(e)
    
    print(e)