# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/minilab/')
def minilab():
    return render_template("minilab.html")

@app.route('/logicgate/')
def logicgate():
    return render_template("logicgate.html")

@app.route('/colorcodes/')
def colorcodes():
    return render_template("colorcodes.html")

@app.route('/binary/', methods=['GET','POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    return render_template('rgb.html', images=image_data())

@app.route('/greetkatie', methods=['GET', 'POST'])
def greetkatie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetkatie.html", name=name)
    # starting and empty input default
    return render_template("greetkatie.html", name="Katie")

@app.route('/greetshreya', methods=['GET', 'POST'])
def greetshreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetshreya.html", name=name)
    # starting and empty input default
    return render_template("greetshreya.html", name="Shreya")

@app.route('/greetderek', methods=['GET', 'POST'])
def greetderek():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetderek.html", name=name)
    # starting and empty input default
    return render_template("greetderek.html", name="Derek")

@app.route('/greetkian', methods=['GET', 'POST'])
def greetkian():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetkian.html", name=name)
    # starting and empty input default
    return render_template("greetkian.html", name="Kian")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
