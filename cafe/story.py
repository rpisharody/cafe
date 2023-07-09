import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('story', __name__)

@bp.route('/')
def index():
    stories = [
        {
            'author': 'pacheek',
            'title' : 'Mistaken for malware',
            'link' : 'https://soupault.app/blog/mistaken-for-malware/',
            'tags' : ['security', 'web'],
            'timestamp': '18 hours ago',
            'upvotes': 33
        },
        {
            'author': 'pacheek',
            'title' : 'How I hacked my Casio F-91W Digital Watch',
            'link' : 'https://medium.com/@matteo.pisani.91/how-i-hacked-casio-f-91w-digital-watch-892bd519bd15',
            'tags' : ['hardware'],
            'timestamp': '21 hours ago',
            'upvotes': 24
        },        
    ]
    return render_template('story/index.html', stories=stories)