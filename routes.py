from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "V-Lens'e Hoş Geldiniz!"
