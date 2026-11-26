
from flask import Flask, render_template, redirect, url_for, jsonify
from pathlib import Path

app = Flask(__name__)

# Pasta onde estão os arquivos HTML
app.template_folder = "templates"
app.static_folder = "static"


# ==========================================
# PÁGINA INICIAL
# ==========================================

@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("entrar.html")


# ==========================================
# SERVIÇOS
# ==========================================

@app.route("/servicos")
def servicos():
    return render_template("serviços.html")


# ==========================================
# SITUAÇÃO ESCOLAR
# ==========================================

@app.route("/situacao")
@app.route("/sit")
def situacao():
    return render_template("sit.html")


# ==========================================
# NOTAS
# ==========================================

@app.route("/notas")
def notas():
    return render_template("notas.html")


# ==========================================
# FREQUÊNCIA
# ==========================================

@app.route("/frequencia")
def frequencia():
    return render_template("frequencia.html")


# ==========================================
# DESEMPENHO
# ==========================================

@app.route("/desempenho")
def desempenho():
    return render_template("desempenho.html")


# ==========================================
# DEPOIMENTOS
# ==========================================

@app.route("/depoimentos")
def depoimentos():
    return render_template("depoimento.html")


# ==========================================
# CONTATO
# ==========================================

@app.route("/contato")
def contato():
    return render_template("contato.html")


# ==========================================
# PERFIL
# ==========================================

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


# ==========================================
# REDIRECIONAMENTOS PARA LINKS ANTIGOS
# ==========================================

@app.route("/entrar.html")
def entrar_html():
    return redirect(url_for("inicio"))


@app.route("/serviços.html")
@app.route("/servicos.html")
def servicos_html():
    return redirect(url_for("servicos"))


@app.route("/sit.html")
@app.route("/SIT.HTML")
@app.route("/SIT")
def sit_html():
    return redirect(url_for("situacao"))


@app.route("/notas.html")
def notas_html():
    return redirect(url_for("notas"))


@app.route("/frequencia.html")
def frequencia_html():
    return redirect(url_for("frequencia"))


@app.route("/desempenho.html")
def desempenho_html():
    return redirect(url_for("desempenho"))


@app.route("/depoimento.html")
def depoimento_html():
    return redirect(url_for("depoimentos"))


@app.route("/contato.html")
def contato_html():
    return redirect(url_for("contato"))


@app.route("/perfil.html")
def perfil_html():
    return redirect(url_for("perfil"))


# ==========================================
# VERIFICAR SE O SERVIDOR ESTÁ FUNCIONANDO
# ==========================================

@app.route("/api/status")
def api_status():
    return jsonify({
        "sistema": "Pé de Meia",
        "status": "funcionando",
        "versao": "1.0"
    })


# ==========================================
# PÁGINA DE ERRO 404
# ==========================================

@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Página não encontrada - Pé de Meia</title>
        <style>
            * {
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(
                    135deg, #087bd9, #064b96
                );
                color: white;
                text-align: center;
                padding: 20px;
            }

            .caixa {
                max-width: 500px;
                background: rgba(255, 255, 255, 0.12);
                padding: 40px;
                border-radius: 20px;
            }

            h1 {
                font-size: 60px;
                margin: 0 0 15px;
            }

            p {
                line-height: 1.6;
            }

            a {
                display: inline-block;
                margin-top: 15px;
                padding: 12px 22px;
                background: white;
                color: #087bd9;
                text-decoration: none;
                font-weight: bold;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="caixa">
            <h1>404</h1>
            <h2>Página não encontrada</h2>
            <p>
                A página que você procura não existe
                ou foi movida.
            </p>
            <a href="/">Voltar ao início</a>
        </div>
    </body>
    </html>
    """, 404


# ==========================================
# EXECUTAR A APLICAÇÃO
# ==========================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
