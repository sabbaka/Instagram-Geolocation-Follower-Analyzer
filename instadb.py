from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
from follower import Follower

engine = create_engine('sqlite:///foo.db', echo=True)

metadata = MetaData()

geo_table = Table('geo_table', metadata,
            Column('owner', Integer, primary_key=True),
            Column('user_id', Integer, primary_key=True),
            Column('latitude', String),
            Column('longitude', String),
            Column('country', String),
            Column('code', String)
            )

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
mapper(Follower, geo_table)

