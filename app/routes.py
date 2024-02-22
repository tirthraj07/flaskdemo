from flask import Flask, Blueprint, render_template, request, redirect
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello World'