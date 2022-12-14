from flask import Flask, request, render_template, Blueprint, redirect, flash 
import requests
import psycopg2

apiRouting = Blueprint(__name__, "apiRouting")

# connect to api
@apiRouting.route("/", methods = ['GET'])
def getItems():
    response = requests.get('http://localhost:8080/api/v1/items')
    print (response.json())

@apiRouting.route("/getitem")
def get_items(items):
    results=[]

# @apiRouting.route('/', methods=['GET', 'POST'])
# def index():
#     search = grocerydata(request.form)   #find form name
#     if request.method == 'POST':
#         return search_results(search)
#     return render_template('index.html', form=search)

# @apiRouting.route('/results')
# def search_results(search):
#     results = []
#     search_string = search.data['search']
#     if search.data['search'] == '':
#         qry = db.query()  #find db label
#         results = qry.all()
#     if not results:
#         flash('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         return render_template('results.html', results=results)
if __name__ == '__main__':
    apiRouting.run()