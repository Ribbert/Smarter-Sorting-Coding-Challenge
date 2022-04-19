from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
import re

app = Flask(__name__)

listOfItems = [["Benadryl", "Diphenhydramine HCl"], ["Purell Hand Sanitizer", "Ethyl Alcohol, Water"]]

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('productInput') == 'Input New Product':
            return(redirect("http://127.0.0.1:5000/input"))
        elif request.form.get('productView') == 'View All Products':
            return(redirect("http://127.0.0.1:5000/view"))
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template("index.html")

@app.route("/input", methods=['GET'])
def inputView():
    return render_template('inputTemp.html')    

@app.route("/input", methods=['POST'])
def input():
    if(request.form.get('doneInputting') == 'Complete Input'):
        nameToAdd = request.form['name']
        global listOfItems
        ingredientToAdd = request.form['ingredients']
        listOfItems.append([nameToAdd, ingredientToAdd])
        print("something")
        return(redirect("http://127.0.0.1:5000"))

@app.route("/view", methods=['GET', 'POST'])
def view():
    print("SomethingElse")
    return render_template('viewTemp.html',data=listOfItems)