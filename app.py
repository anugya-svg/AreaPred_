import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Endvr_proj.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction[0]==[0]:
        return render_template("safe.html")
    else:
        return render_template("unsafe.html")
@app.route('/about')
def about():
    return render_template('aboutuspage.html')
@app.route('/team')
def team():
    return render_template('teampage.html')


@app.route('/contact')
def contact():
    return render_template('newcontact.html')
if __name__ == "__main__":
    app.run(debug=True)