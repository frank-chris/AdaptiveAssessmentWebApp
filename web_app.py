<<<<<<< HEAD
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import re
import pandas as pd
from vae.generate_qa import get_qa
from EvaluationEngine.evaluationEngine import getBaseline, getEvaluation
from transformers import BertTokenizer
from ast import literal_eval
import random

args_bert_model = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(args_bert_model)

app = Flask(__name__)
app.debug = True
# run_with_ngrok(app)


DF_PATH = None
QUESTION_COUNTER = 0
DIFFICULTY = 0
SUBJECT = 0
SCORE = 0
SUBJECT_DICT = {0:'history', 1:'geography', 2:'economics'}
ASSESS_DF = None
LAST_ANSWER = None
LAST_QUESTION = None
LAST_CONTEXT = None

def sentence_case(text):
    sentences = re.findall('[^.!?]+[.!?](?:\s|\Z)', text)
    # capitalize the first letter of each sentence
    sentences = [x[0].upper() + x[1:] for x in sentences]
    # combine sentences
    return ''.join(sentences)

def generate(context):
    _, questions, answers = get_qa([context], tokenizer)
    question = sentence_case(questions[0].replace('[CLS]', '').replace('[PAD]', '').replace('[SEP]', ''))
    answer = sentence_case(answers[0].replace('[CLS]', '').replace('[PAD]', '').replace('[SEP]', ''))
    return context, question, answer

def generate_from_available(topic):
    df = pd.read_csv('data/available_contexts.csv', index_col='topic')
    context = df['context'][topic]
    return generate(context)

def assess():
    global QUESTION_COUNTER
    global DIFFICULTY
    global ASSESS_DF
    global SUBJECT
    global SUBJECT_DICT
    global DF_PATH
    ASSESS_DF = pd.read_csv(DF_PATH)
    context, question, answer = literal_eval(ASSESS_DF[SUBJECT_DICT[SUBJECT]][DIFFICULTY])
    return context, question, answer

=======
import os
import sys
from werkzeug.utils import secure_filename
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.debug = True
run_with_ngrok(app)
>>>>>>> 812ecfea332ad2587366a2055af683601facf341

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def choose_mode():
<<<<<<< HEAD
    global QUESTION_COUNTER
    global DIFFICULTY
    global SUBJECT
    global SUBJECT_DICT
    global LAST_ANSWER
    global LAST_CONTEXT
    global LAST_QUESTION
    global SCORE
    global DF_PATH
=======
>>>>>>> 812ecfea332ad2587366a2055af683601facf341
    if request.form.get("generate"):
        return render_template('generate.html', data=[])
    elif request.form.get("assess"):
        return render_template('assess.html', data=[])
<<<<<<< HEAD
    elif request.form.get("context"):
        context, question, answer = generate(request.form["context"])
        return render_template('generate_results.html', data=[context, question, answer])
    elif request.form.get("economics"):
        context, question, answer = generate_from_available("economics")
        return render_template('generate_results.html', data=[context, question, answer])
    elif request.form.get("geography"):
        context, question, answer = generate_from_available("geography")
        return render_template('generate_results.html', data=[context, question, answer])
    elif request.form.get("history"):
        context, question, answer = generate_from_available("history")
        return render_template('generate_results.html', data=[context, question, answer])
    elif request.form.get("biology"):
        context, question, answer = generate_from_available("biology")
        return render_template('generate_results.html', data=[context, question, answer])
    elif request.form.get("assess_1"):
        DF_PATH = 'data/adaptive_assess_1.csv'
        QUESTION_COUNTER = 0
        DIFFICULTY = 0
        SUBJECT = random.randint(0,9) % 3
        SCORE = 0
        LAST_CONTEXT, LAST_QUESTION, LAST_ANSWER = assess()
        return render_template('assess_results.html', data=[LAST_CONTEXT, LAST_QUESTION, ''])
    elif request.form.get("assess_2"):
        DF_PATH = 'data/adaptive_assess_2.csv'
        QUESTION_COUNTER = 0
        DIFFICULTY = 0
        SUBJECT = random.randint(0,9) % 3
        SCORE = 0
        LAST_CONTEXT, LAST_QUESTION, LAST_ANSWER = assess()
        return render_template('assess_results.html', data=[LAST_CONTEXT, LAST_QUESTION, ''])
    elif request.form.get("answer"):
        user_answer =  request.form['answer']
        QUESTION_COUNTER += 1
        
        baseline_score = getBaseline(LAST_ANSWER, LAST_CONTEXT)
        evaluation_score = getEvaluation(LAST_QUESTION, LAST_ANSWER, LAST_CONTEXT, user_answer)
        print(evaluation_score, (baseline_score - 0.05))
        correct = evaluation_score > (baseline_score - 0.05)
        mtype = 0
        if correct:
            DIFFICULTY += 1
            SCORE += 1
            mtype = 1
            message = 'Your previous answer was good, a harder one this time.'
        else:
            SUBJECT += 1
            SUBJECT %= 3
            message = 'Your previous answer was poor. Changing the topic.'
        
        if QUESTION_COUNTER == 3:
            if mtype:
                message = 'Your previous answer was good.'
            else:
                message = 'Your previous answer was poor.'
            return render_template('assess_final.html', data=[SCORE, message])
        context, question, LAST_ANSWER = assess()
        return render_template('assess_results.html', data=[context, question, message])               
=======
>>>>>>> 812ecfea332ad2587366a2055af683601facf341
    else:
        return render_template('index.html')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run()
>>>>>>> 812ecfea332ad2587366a2055af683601facf341
