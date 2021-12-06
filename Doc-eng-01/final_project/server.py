from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

@app.route("/englishToFrench")
def englishToFrench():
    text = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
