from flask import Flask
app=Flask(__name__,static_url_path='/static')

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify')
def classify():
    return render_template('identify.html')

@app.route('/images')
def images():
    return render_template('images.html')



if __name__=='__main__':
    app.run(debug=True)