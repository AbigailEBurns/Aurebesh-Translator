from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/B2A", methods=["GET", "POST"])
def B2A():
    if request.method == "POST":
        basic_text = request.form.get("basic")
        if len(basic_text) >= 23 or not basic_text:
            return render_template("porgs.html")
        else:
            return render_template("B2A.html", basic_text=basic_text)
    else:
        return render_template("B2A.html")
    

@app.route("/A2B", methods=["GET", "POST"])
def A2B():
    if request.method == "POST":
        aurebesh_text = request.form.get("tbInput")
        if len(aurebesh_text) >= 41 or not aurebesh_text:
            return render_template("porgs.html")
        else:
            return render_template("A2B.html", basic_text=aurebesh_text)
    else:
        return render_template("A2B.html")
    
if __name__ == "__main__":
    app.run(debug=True)