class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    barcode = Column(String, unique=True)  # QR or EAN code
    base_price = Column(Float)
    final_price = Column(Float, default=base_price)  # Final price after discount and tax
    description = Coulum(Text)
    stock = Column(Integer)
    tax_rate = Column(Float, default=0.0)  # Tax rate in percentage
    is_active = Column(Boolean, default=True)
