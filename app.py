from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/book')
def book():
    return render_template("book.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
    

@app.route('/achk', methods=['GET','POST'])
def achk():
    if(request.method== 'POST'):
        Name= request.form['firstname']
        Email=request.form['mail']
        return render_template('achk.html', firstname=Name, mail=Email)
@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if(request.method== 'POST'):
        Name= request.form['firstname']
        return render_template('feedback.html', firstname=Name)




if __name__=='__main__':
    app.run(debug=True)

