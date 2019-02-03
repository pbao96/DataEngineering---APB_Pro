from flask import Flask, flash, redirect, render_template, request, url_for
import pymongo
import os
from mgdb import get_data, create_db

app = Flask(__name__)
app.config.from_object('config')

client = pymongo.MongoClient("mongodb://localhost:27017/apb_project")

url = 'https://www.data.gouv.fr/fr/datasets/r/32803cb2-0e0f-41f1-a32e-1fd9ee4fd141'
df = get_data(url)
collection = create_db(client,url)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    try:
        search_term = request.form["input"]
        category = request.form["select_cat"]
        limit = request.form["limit"]
        return render_template('results.html',res=collection.find({category: search_term})[:int(limit)],l=len(df))
    except Exception:
        print("Bad input!")
        return render_template('search.html', active='search')

@app.route('/search/')
def search():
    return render_template('search.html', active="search")

@app.route('/About/')
def about():
    return render_template('about.html', active='about', data=df.head().to_html(classes='table table-stripped table-hover') )

if __name__ == '__main__':
    app.run(debug=True, port=2745)
