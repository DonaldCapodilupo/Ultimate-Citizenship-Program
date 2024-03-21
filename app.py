from flask import Flask,render_template,redirect,url_for, request

app = Flask(__name__)


@app.route('/',  methods=["POST", "GET"])
def main_Menu():
    if request.method == "POST":
        button_clicked = request.form['submit_button']
        return redirect(url_for("trivia_Quiz"))
    else:
        return render_template("Quiz.html") #Main Menu.html

@app.route('/Trivia-Quiz',  methods=["POST", "GET"])
def trivia_Quiz():
    if request.method == "POST":
        button_clicked = request.form['submit_button']
        if button_clicked == "Return Home":
            return redirect(url_for("main_Menu"))

        return redirect(url_for("main_Menu"))
    else:
        return render_template("Quiz.html")



if __name__ == '__main__':
    app.run()
