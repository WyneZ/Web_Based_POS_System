class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String)  # cashier, manager, admin
    is_active = Column(Boolean, default=True)
