# backend/app/services/insurance_service.py
from datetime import datetime
from typing import Optional, Dict, Any
from app.crud.insurance import InsuranceCRUD
from app.models.insurance import InsurancePolicy, Claim
from app.utils.analytics import calculate_fraud_probability
from app.db.session import get_db

class InsuranceService:
    @staticmethod
    def get_all_policies():
        db = next(get_db())
        return InsuranceCRUD.get_all_policies(db)
    
    @staticmethod
    def get_policy_by_id(policy_id: int) -> Optional[InsurancePolicy]:
        db = next(get_db())
        return InsuranceCRUD.get_policy_by_id(db, policy_id)
    
    @staticmethod
    def get_all_claims():
        db = next(get_db())
        return InsuranceCRUD.get_all_claims(db)
    
    @staticmethod
    def get_claim_by_id(claim_id: int) -> Optional[Claim]:
        db = next(get_db())
        return InsuranceCRUD.get_claim_by_id(db, claim_id)
    
    @staticmethod
    def get_claims_analytics(year: Optional[int] = None, month: Optional[int] = None) -> Dict[str, Any]:
        db = next(get_db())
        claims = InsuranceCRUD.get_claims_by_period(db, year, month)
        
        total_claims = len(claims)
        valid_claims = sum(1 for claim in claims if claim.status == "approved")
        fraudulent_claims = sum(1 for claim in claims if claim.is_fraud)
        
        return {
            "total_claims": total_claims,
            "valid_claims": valid_claims,
            "fraudulent_claims": fraudulent_claims,
            "approval_rate": valid_claims / total_claims if total_claims else 0,
            "fraud_rate": fraudulent_claims / total_claims if total_claims else 0,
            "year": year,
            "month": month
        }