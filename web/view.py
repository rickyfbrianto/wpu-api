from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required

view = Blueprint('view', __name__)


@view.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)
