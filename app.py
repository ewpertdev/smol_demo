from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fir@localhost/gastos_demo'
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Necesario para sessions
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # Especifica el nombre exacto de la tabla
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    # Define la relación con expenses
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Expense(db.Model):
    __tablename__ = 'expenses'  # Especifica el nombre exacto de la tabla
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    
    expenses = Expense.query.filter_by(user_id=session['user_id']).all()
    total = sum(float(expense.amount) for expense in expenses)
    return render_template('index.html', 
                         expenses=expenses, 
                         total=total, 
                         username=session.get('username'))

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        session['user_id'] = user.id
        session['username'] = user.username
        return jsonify({'message': 'Login correcto'})
    
    return jsonify({'error': 'Email o contraseña incorrectos'}), 401

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'El email ya está registrado'}), 400
        
    user = User(
        email=data['email'],
        username=data['username'],
        password_hash=generate_password_hash(data['password'])
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'Usuario registrado correctamente'})

@app.route('/api/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 401
        
    data = request.get_json()
    expense = Expense(
        description=data['description'],
        amount=data['amount'],
        user_id=session['user_id']
    )
    db.session.add(expense)
    db.session.commit()
    return jsonify({'message': 'Gasto añadido'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 