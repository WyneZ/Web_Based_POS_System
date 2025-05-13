class Receipt(Base):
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sale.id"))
    content = Column(Text)  # HTML or raw printer text
    payment = Column(String)  # e.g., "Cash", "Card", "Mobile Payment"
    created_at = Column(DateTime, default=datetime.utcnow)
