from flask import Flask, render_template, request, redirect

app = Flask(__name__)

agendamentos = []

@app.route("/")
def index():
    return render_template("index.html", agendamentos=agendamentos)

@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    servico = request.form["servico"]
    data = request.form["data"]

    agendamentos.append({
        "nome": nome,
        "servico": servico,
        "data": data
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)