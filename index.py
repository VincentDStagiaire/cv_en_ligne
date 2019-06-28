from flask import url_for, render_template, request, redirect, Flask
from translate import french, english

app = Flask(__name__)
# if __name__ == "__main__":
#     app.run(host='172.16.25.226', port="5000")

@app.route('/')
def index_french():
    return render_template("base.html", language=french)

@app.route('/english')
def index_english():
    return render_template("base.html", language=english)



# TO DO :
# Changer les photos => mettre en repsonsive    https://www.alsacreations.com/article/lire/1621-responsive-images-srcset.html
# Faire trie dans les fichiers
# Pusher sur git
# Continuer pour la traduction
