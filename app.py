from flask import Flask, render_template, url_for, request
from flaskext.markdown import Markdown
import spacy 
from spacy import displacy
import pandas as pd
nlp = spacy.load("en_core_web_sm")

#Initialise app
app = Flask(__name__, static_url_path='')
Markdown(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':
        allOptions = ['PERSON', 'ORG', 'GPE', 'DATE', 'MONEY', 'EVENT', 'PRODUCT']
        selectedOptions = request.form.getlist('checkbox-index')
        if selectedOptions[0] == 'All':
            selectedOptions = allOptions
        
        print(selectedOptions)
        options = {"ents": selectedOptions}

        rawtext = request.form['rawtext']
        docx = nlp(rawtext)
        html = displacy.render(docx, style='ent', options=options, minify=True)
        displacy_result = html
        # print(request.form.getlist('checkbox-index'))
    return render_template('results.html', rawtext=rawtext, displacy_result=displacy_result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
 