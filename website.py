from flask import Flask
from crons.models import Base, Share # Your non-Flask-SQLAlchemy models...
from flask_sqlalchemy import SQLAlchemy
from crons.config import Config

app =  Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)

@app.route('/')
def root():
    shares = db.session.query(Share).all()
    response = ''
    response += "<head><title>Mintsy Proof Of Hashrate Site</title></head>"
    response += "<body>"
    for share in shares:
	response += "<br><p>At {time} You found a {coin} share with a difficulty of {difficulty} which {valid_share} a valid share and {valid_block} a valid block. It resulted in a hash of {share_hash}.</p>".format(**share.__dict__)
    return response

if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True) 
