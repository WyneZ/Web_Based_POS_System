class Sale(Base):
    id = Column(Integer, primary_key=True)
    # terminal_id = Column(Integer, ForeignKey("terminal.id"))
    cashier_id = Column(Integer, ForeignKey("user.id"))
    # store_id = Column(Integer, ForeignKey("store.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    total = Column(Float)
    discount = Column(Float, default=0.0)
    tax = Column(Float)
    grand_total = Column(Float)
    payment_status = Column(String, default='paid')  # paid, pending, refunded
