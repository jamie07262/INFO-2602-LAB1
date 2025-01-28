from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') 
  if pref:
    for student in data: 
      if student['pref'] == pref: 
        result.append(student) 
    return jsonify(result) 
  return jsonify(data) 

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id:
      return jsonify(student)

# EXERCISE 1
@app.route('/stats')
def calc_stats():
    countChicken = 0
    countFish = 0
    countVege = 0
    countCSS = 0
    countCSM = 0
    countITM = 0
    countITS = 0
    
    for student in data:
    # calculating food pref
        if student['pref'] == 'Chicken':
            countChicken += 1
        elif student['pref'] == 'Fish':
            countFish += 1
        else:
            countVege += 1

    #calculating students in each programme
        if student['programme'] == 'Computer Science (Special)':
            countCSS += 1
        elif student['programme'] == 'Computer Science (Major)':
            countCSM += 1
        elif student['programme'] == 'Information Technology (Special)':
            countITS += 1
        else: 
            countITM +=1
    
    stat = []
    stat = [{
        'Chicken': countChicken,
        'Computer Science (Major)': countCSM,
        'Computer Science (Special)': countCSS,
        'Fish': countFish,
        'Information Technology (Major)':countITM,
        'Information Technology (Special)': countITS,
        'Vegetable': countVege
    }]

    return jsonify(stat)

# EXERCISE 2
@app.route('/add/<a>/<b>')
def add(a,b):
    result = int(a) + int(b)

    return jsonify(result)

@app.route('/subtract/<a>/<b>')
def subtract(a,b):
    result = int(a) - int(b)

    return jsonify(result)

@app.route('/multiply/<a>/<b>')
def multiply(a,b):
    result = int(a) * int(b)

    return jsonify(result)

@app.route('/divide/<a>/<b>')
def divide(a,b):
    result = float(a) / float(b)

    return jsonify(result)

app.run(host='0.0.0.0', port=8080, debug=True)
