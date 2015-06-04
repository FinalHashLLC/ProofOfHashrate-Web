from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Share
from utils import *
from config import *
import models
import json

class Shared(object):

	def __init__(self):
	   self.config = Config()
	   self.engine = create_engine(self.config.SQLALCHEMY_DATABASE_URI)
	   self.models = models
	   self.session = None

	def get_session(self):
	    session_maker = sessionmaker()
	    session_maker.configure(bind=self.engine)
	    self.session = session_maker()
	    return self.session

	def store_shares(self, data):
            for line in data.split("\n"):
                if not line.strip():
                   continue

                output = json.loads(line)
                result = output['result']
                for share in result:
                    share = json.loads(share)
                    share['time'] = convert_to_datetime(share['time']).strftime('%Y-%m-%d %H:%M:%S')
                    share = self.add_share(share)
            return None

        def add_share(self, share):
	    if not self.session:
	       self.session = self.get_session()

	    # Check for the share existence
	    exists = self.session.query(Share).filter(Share.share_hash == share['share_hash']).first()
	    if not exists:
               db_share = Share(**share)
	       self.session.add(db_share)
	       self.session.commit()
	       return db_share
	    return None
