from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:////tmp/test.db')
meta = MetaData()
iniciativa = Table(
    'iniciativa', meta,
    Column('id', Integer, primary_key=True),
    Column('titulo', String(200)),
    Column('metodologia', String(200)),
    Column('publico_alvo', String(200)),
    )

meta.create_all(engine)
