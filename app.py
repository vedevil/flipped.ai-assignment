from webbrowser import open_new
from flask import Flask, redirect, render_template, request, url_for
import json, requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def coversion():
    if request.method=='POST':
        text = request.form.get('ip').lower()
        selected_lang = request.form.get('lang')
        selected_lang=selected_lang.lower()
        req_api = "http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang="+selected_lang+"&inString=0"+text
        res = requests.get(req_api)
        output = res.json()
        op=list(output['twords'][0]['options'])
        itrans = output['itrans']
        if itrans not in op:
            op.append(itrans)
        op_new=[]
        for o in op:
            a=o[1:]
            op_new.append(a)
        #op_new=list(set(op_new))
        return render_template('output.html', op=op_new)
    else:
        return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        selected_str=request.form.get('suggestions')
        selected_str=selected_str+' '
        try:
            file1 = open("static/myresult.txt", "a+", encoding='utf-16')  # append mode
            file1.write(selected_str)
            file1.close()
        except:
            f= open('static/myresult.txt', 'w', encoding='utf-16') 
            f.write(selected_str)
        return render_template('index.html')
    else:
        selected_str=request.form.get('suggestions')
        selected_str=selected_str+' '
        try:
            file1 = open("static/myresult.txt", "a+", encoding='utf-16')  # append mode
            file1.write(selected_str)
            file1.close()
        except:
            f= open('static/myresult.txt', 'w', encoding='utf-16') 
            f.write(selected_str)
        return redirect('/')

@app.route('/clear', methods=['POST','GET'])
def clear():
    os.remove("static/myresult.txt")
    return "History cleared"



if __name__ == "__main__":
    app.run(debug=True)