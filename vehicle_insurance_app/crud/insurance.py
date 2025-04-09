# backend/app/crud/insurance.py
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.models.insurance import InsurancePolicy, Claim

class InsuranceCRUD:
    @staticmethod
    def get_all_policies(db: Session) -> List[InsurancePolicy]:
        return db.query(InsurancePolicy).all()
    
    @staticmethod
    def get_policy_by_id(db: Session, policy_id: int) -> Optional[InsurancePolicy]:
        return db.query(InsurancePolicy).filter(InsurancePolicy.id == policy_id).first()
    
    @staticmethod
    def get_all_claims(db: Session) -> List[Claim]:
        return db.query(Claim).all()
    
    @staticmethod
    def get_claim_by_id(db: Session, claim_id: int) -> Optional[Claim]:
        return db.query(Claim).filter(Claim.id == claim_id).first()
    
    @staticmethod
    def get_claims_by_period(db: Session, year: Optional[int] = None, month: Optional[int] = None) -> List[Claim]:
        query = db.query(Claim)
        if year:
            query = query.filter(db.extract('year', Claim.claim_date) == year)
        if month:
            query = query.filter(db.extract('month', Claim.claim_date) == month)
        return query.all()