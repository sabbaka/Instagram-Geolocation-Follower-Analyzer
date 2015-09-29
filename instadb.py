from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///foo.db')

metadata = MetaData()

geo_table = Table('geo_table', metadata,
            Column('user_id', Integer, primary_key=True),
            Column('geotag', String),
            Column('country', String)
            )

metadata.create_all(engine)

Session = sessionmaker(bind=engine)

