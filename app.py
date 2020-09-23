from flask import Flask, request, render_template
from pipeline import lower, remove_punctuation, remove_stopwords, stem_text, lemmatize_text

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():
    response = request.form
    keys = response.keys()
    original_text = request.form['text']
    text = request.form['text']
    if 'lowercase' in keys:
        text = lower(text)
    if 'punct' in keys:
        text = remove_punctuation(text)
    if 'stp' in keys:
        text = remove_stopwords(text)
    if 'stem' in keys:
        if response['stem'] == 'stem':
            text = stem_text(text)
        elif response['stem'] == 'lem':
            text = lemmatize_text(text)
        else:
            pass
    return render_template('output.html', original_text=original_text,text=text)


if __name__ == '__main__':
    app.run()
