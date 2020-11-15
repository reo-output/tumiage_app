# ログイン処理などのまとめ
from flask import Flask, session, redirect
from functools import wraps

# ユーザー名とパスワードの一覧
USER_LOGIN_LIST = {
    'admin':'admin',
    'r.sato': 'hogehoge',
    'j.bezos': 'amazon',
    'l.page': 'google',
    'e.musk': 'tesla',
    's.jobs': 'apple',}

# ログイン確認
def is_login():
    return 'login' in session

# ログイン試行
def try_login(form):
    user = form.get('user', '')
    password = form.get('pw', '')
    # パスワードチェック
    if user not in USER_LOGIN_LIST: return False
    if USER_LOGIN_LIST[user] != password:
        return False
    session['login'] = user
    return True

# ユーザー名取得
def get_id():
    return session['login'] if is_login() else '未ログイン'

# 全ユーザーの情報取得
def get_allusers():
    return [ u for u in USER_LOGIN_LIST ]

# ログアウト
def try_logout():
    session.pop('login', None)

# ログイン必須を処理するデコレーターの定義
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
