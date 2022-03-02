from flask import Flask, flash, redirect, render_template, request
from grpc import server

import sys

sys.path.append('../../twitterWordCounterApplication/server')
from twitter_word_counter import mostCommonWordsFromUser

sys.path.append('../')
from forms import mostCommonWordsFromUserForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'c1d67d639284d774604d8c77f59c3d6e'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = mostCommonWordsFromUserForm(request.form)
    results = []
    if request.method == 'POST' and form.validate():
        results = mostCommonWordsFromUser(form.username, form.count)
    return render_template('home.html', form=form, results = results)

@app.route('/here')
def here():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)