from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .model import *
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/get_id')
@login_required
def get_id():
    user = User.query.filter(User.id == current_user.id).first()
    hasil = json_satuan(user)
    return hasil


@auth.route('/get_datas')
@login_required
def get_datas():
    user = User.query.all()
    hasil = json_semua(user)
    return hasil


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view.home'))
    if request.method == 'POST':
        txtUsername = request.form.get('txtUsername')
        txtPassword = request.form.get('txtPassword')
        user = User.query.filter(User.username == txtUsername).first()
        if user and check_password_hash(user.password, txtPassword):
            flash('Login Berhasil', category='success')
            login_user(user, remember=True)
            return redirect(url_for('view.home'))
        else:
            flash('Username atau password salah', category='danger')

    return render_template('login.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('view.home'))
    if request.method == 'POST':
        txtUsername = request.form.get('txtUsername')
        txtPassword = request.form.get('txtPassword')
        user = User(username=txtUsername, password=generate_password_hash(
            txtPassword, method="sha256"))
        db.session.add(user)
        db.session.commit()
        flash('Buat Akun berhasil', category='success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
