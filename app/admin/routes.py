# admin/routes.py
from . import admin
from flask import render_template

@admin.route('/')
def admin_index():
    return render_template('admin.html')

@admin.route('/blog')
def blog():
    return render_template('admin.html')