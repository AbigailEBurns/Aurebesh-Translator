from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)


#define index route for homepage
@app.route("/")
def index():
    return render_template("index.html")


#defines route for basic to aurebesh page
@app.route("/B2A", methods=["GET", "POST"])
def B2A():
    #if ita a post request
    if request.method == "POST":
        #assign user input to a variable
        basic_text = request.form.get("basic")
        #check to make sure the user typed something and that it isnt too long
        if len(basic_text) >= 23 or not basic_text:
            #if it is send to the porg error page
            return render_template("porgs.html")
        else:
            #if everything is good send the user text to the jinja placeholder on the page
            return render_template("B2A.html", basic_text=basic_text)
    #if its a get request
    else:
        #just render the page
        return render_template("B2A.html")
    

#defines route for aurebesh to basic page
@app.route("/A2B", methods=["GET", "POST"])
def A2B():
    #if post
    if request.method == "POST":
        #assign user input to a variable
        aurebesh_text = request.form.get("tbInput")
        #check to make sure the user typed something and that it isnt too long
        if len(aurebesh_text) >= 41 or not aurebesh_text:
            #if it is send to the porg error page
            return render_template("porgs.html")
        else:
            #if everything is good send the user text to the jinja placeholder on the page
            return render_template("A2B.html", basic_text=aurebesh_text)
    #if its a get request
    else:
        #just render the page
        return render_template("A2B.html")
    
if __name__ == "__main__":
    app.run(debug=True)