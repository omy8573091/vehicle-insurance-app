# backend/app/models/insurance.py
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime
from app.models.base import Base

class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"
    
    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String, unique=True, index=True)
    customer_id = Column(Integer, index=True)
    vehicle_id = Column(Integer, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    premium_amount = Column(Float)
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Claim(Base):
    __tablename__ = "claims"
    
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("insurance_policies.id"))
    claim_date = Column(Date)
    claim_amount = Column(Float)
    description = Column(String)
    status = Column(String, default="pending")
    is_fraud = Column(Boolean, default=False)
    fraud_probability = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)