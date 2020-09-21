from flask import Flask, render_template, redirect, request
from cs50 import SQL
from slugify import slugify
import sqlite3

generos = ['Comedia', 'Terror', 'Adolescente', 'Aventura', 'Chato']

db = SQL("sqlite:///db/source.db")

app = Flask(__name__)

@app.route("/")
def index():

    seriesDatabase = db.execute("SELECT * FROM series;")
    
    return render_template("index.html", seriesDb = seriesDatabase)

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == 'POST':

        if not request.form.get("descricao"):
            descricao = 'Sem descrição'
        else:
            descricao = request.form.get("descricao")

        slugified = slugify(request.form.get("name"))

        movieDict = {
            'name': request.form.get("name"),
            'name_url': slugified,
            'image_url': request.form.get("url"),
            'descricao': descricao,
            'genero': request.form.get("genero")
        }
        print(movieDict)

        db.execute("INSERT INTO series (name, name_url, image_url, descricao, genero) VALUES ('{name}','{name_url}','{image_url}','{descricao}','{genero}');"
            .format(name=movieDict['name'], name_url=movieDict['name_url'], image_url=movieDict['image_url'], descricao=movieDict['descricao'], genero=movieDict['genero']))

        return redirect('/')
    else:
        return render_template("new.html", generos = generos)


@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == 'POST':

        serieQuery = request.args.get('id')
        if request.form.get('nota') == None:
            return redirect('/review')
        nota = request.form.get('nota').replace('option','')
        comentario = request.form.get('descricao')

        if comentario == '':
            comentario = 'Sem comentário'

        db.execute("INSERT INTO reviews VALUES ({id_serie},{nota},'{comentario}')".format(id_serie=int(serieQuery), nota=int(nota), comentario=comentario))

        notas = db.execute("SELECT nota FROM reviews WHERE id_serie = {id};".format(id=int(serieQuery)))

        somaNota = 0
        for nota in notas:
            somaNota = somaNota + nota['nota']

        averageNote = round(somaNota / len(notas))

        db.execute("UPDATE series SET avg_note = {averageNote} WHERE serie_id = {id};".format(averageNote=averageNote, id=int(serieQuery)))

        return redirect('/')


    else:

        serieQuery = request.args.get('serie')
        
        if serieQuery == None:
            return redirect('/')

        seriesDatabase = db.execute("SELECT * FROM series WHERE name_url = '{serieQuery}';".format(serieQuery=serieQuery))
        reviewDatabase = db.execute("SELECT nota, comentario FROM reviews WHERE id_serie = {id}".format(id=seriesDatabase[0]['serie_id']))

        notas = db.execute("SELECT nota FROM reviews WHERE id_serie = {id}".format(id=seriesDatabase[0]['serie_id']))

        somaNota = 0
        for nota in notas:
            somaNota = somaNota + nota['nota']

        if len(notas) == 0:
            averageNote = 0
        else:
            averageNote = round(somaNota / len(notas))

        return render_template("review.html", serie=seriesDatabase[0], reviews=reviewDatabase, nota=averageNote)
