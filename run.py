import os
from flask import Flask,render_template, request, flash, jsonify
import json
import random
import numpy



app = Flask(__name__)
app.secret_key = "its_secure"

@app.route('/', methods=["GET", "POST"])
def index():
     if request.method=="POST":
        print(request.form)
        file= open("user_info.txt", "a")
        file.write("Name:{},Age:{},Grade:{}\n"
                  .format(request.form['name'],request.form['age'],
                  request.form['grade']))
        file.close()
        flash(" Hello {}, Welcome! Let's get started. Choose a grade."
        .format(request.form['name']))
     return render_template("index.html", title = "Home Page")
     
     
    
@app.route('/jk_sk/', methods=["GET", "POST"])
def jk_sk_ans():
    args = request.args
    username = args['username']
    return render_template("jk_sk.html", user=username)
     
     
@app.route('/get_score/api/v1/', methods=["GET", "POST"])
def user_score():
    my_arg = request.args
    post_name = my_arg['name']
    post_score = my_arg['score']
    file_score = open("user_scores.txt", "a")
    file_score.write(post_name + "\n" + post_score + "\n")
    file_score.close()
             
    return jsonify("true")
                
            
                   
@app.route('/checkans/api/v1/', methods=['GET'])
def que_ans():
    my_arg = request.args
    check_ques = my_arg['question']
    check_ans = my_arg['answer']
    check_category = my_arg['category']
    if check_category == "jk_sk":
        file_name = "data/jk_sk.json"
    if check_category == "1-2":
        file_name = "data/one_two.json"
    if check_category == "3-4":
        file_name = "data/three_four.json"
    if check_category == "5":
        file_name = "data/five.json"
    print(file_name, check_category)
    file = open(file_name, "r")
    file_data = file.read()
    file_data = json.loads(file_data)
    print(file_data)
    for items in file_data:
        if (items['question'].rstrip() == check_ques.rstrip().replace('"', '')):
            if items['answer'] == check_ans:
                return jsonify(True)
            else:
                return jsonify(False)
        
@app.route('/get_question/api/v1/', methods=['GET'])
def get_question():
    my_arg = request.args
    check_ans = my_arg['category']
    if check_ans == "jk_sk":
        file_name = "data/jk_sk.json"
    if check_ans == "1-2":
        file_name = "data/one_two.json"
    if check_ans == "3-4":
        file_name = "data/three_four.json"
    if check_ans == "5":
        file_name = "data/five.json"
    file = open(file_name, "r")
    all_questions = json.loads(file.read())
    random_number = random.randint(0, len(all_questions) - 1)
    ask_question = all_questions[random_number]["question"]
    return jsonify(ask_question)
    
    
@app.route('/leadership')
def leadership():
    file = open("user_scores.txt", "r")
    score_data = file.readlines()
    username = []
    score = []
    final_user_list = []
    file.close()
    for i in range(0, len(score_data)):
        if i % 2 == 0:
            username.append(score_data[i].replace('\n',''))
        else:
            score.append(int(score_data[i].replace('\n','')))
    score_index_before_sort = numpy.argsort(score)
    for index in score_index_before_sort:
        final_user_list.append(username[index])
    score = sorted(score)
    if len(score) > 10:
        score = score[-10:]
        final_user_list = final_user_list[-10:]
    return render_template("leadership.html", title = "Leadership Board Page", username =final_user_list , score = score)
       
    

@app.route('/jk_sk')
def jk_sk():
    return render_template("jk_sk.html", title = "Jk/Sk Page")
       
    
@app.route('/one_two')
def one_two():
    return render_template("one_two.html", title = "Grades: 1 / 2 Page")
    
@app.route('/three_four')
def three_four():
    return render_template("three_four.html", title = "Grades: 3 / 4 Page")
    
@app.route('/five')
def five():
    return render_template("five.html", title = "Grade: 5  Page")
 

@app.route('/check_answer/', methods=["GET"])
def check_answer():
    my_arg = request.args
    question = my_arg['question']
    answers = my_arg['answer']
    answer_return = ""
    with open("data/jk_sk.json", 'r') as file1:
        answer_file = json.load(file1)
    for answer in answer_file:
        print(answer)
        if answer['question'] == question:
            if answer['answer'] == answers:
                answer_return = "True"
            else:
                answer_return = "False"
    return jsonify({'result':answer_return})
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)
    