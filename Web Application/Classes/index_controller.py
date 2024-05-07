from flask import render_template, session
from Models.user_model import Users
from Classes.auth_controller import login_check

def index():
    """
    Отображает домашнюю страницу, с или без меню входа и иконки пользователя, если он вошел
    """
    # Получаем данные пользователя из сессии, если пользователь вошел
    User = session.get('LoginedUser', None) if login_check() else None
    
    return render_template('index.html', LoginedUser=User)