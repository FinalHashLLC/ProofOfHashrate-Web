# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Enum, Float, Integer, LargeBinary, String, Table, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Share(Base):
    __tablename__ = 'shares'
    id = Column(BigInteger, primary_key=True)
    coin = Column(String(5), nullable=False)
    username = Column(String(120), nullable=False, index=True)
    valid_share = Column(Enum(u'Y', u'N'), nullable=False, index=True)
    valid_block = Column(Enum(u'Y', u'N'), index=True)
    share_hash = Column(String(257), nullable=False)
    difficulty = Column(Float, nullable=False, server_default=text("'0'"))
    time = Column(DateTime, nullable=False, index=True)

