from webbrowser import open_new
from flask import Flask, redirect, render_template, request, url_for
import json, requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def coversion():
    if request.method=='POST':
        text = request.form.get('ip').lower()
        selected_lang = request.form.get('lang')
        selected_lang=selected_lang.lower()
        api = "http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang="+selected_lang+"&inString=0"+text
        res = requests.get(api)
        output = res.json()
        op=list(output['twords'][0]['options'])
        itrans = output['itrans']
        if itrans not in op:
            op.append(itrans)
        op_new=[]
        for o in op:
            a=o[1:]
            op_new.append(a)
        op_new=list(set(op_new))
        return render_template('output.html', op=op_new)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)