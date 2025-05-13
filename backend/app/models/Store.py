class Store(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
