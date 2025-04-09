# backend/app/graphql/schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.insurance import InsurancePolicy, Claim
from app.services.insurance_service import InsuranceService

class InsurancePolicyType(SQLAlchemyObjectType):
    class Meta:
        model = InsurancePolicy

class ClaimType(SQLAlchemyObjectType):
    class Meta:
        model = Claim

class Query(graphene.ObjectType):
    policies = graphene.List(InsurancePolicyType)
    policy = graphene.Field(InsurancePolicyType, policy_id=graphene.Int())
    claims = graphene.List(ClaimType)
    claim = graphene.Field(ClaimType, claim_id=graphene.Int())
    claims_analytics = graphene.Field(
        graphene.JSONString,
        year=graphene.Int(),
        month=graphene.Int()
    )

    def resolve_policies(self, info):
        return InsuranceService.get_all_policies()

    def resolve_policy(self, info, policy_id):
        return InsuranceService.get_policy_by_id(policy_id)

    def resolve_claims(self, info):
        return InsuranceService.get_all_claims()

    def resolve_claim(self, info, claim_id):
        return InsuranceService.get_claim_by_id(claim_id)

    def resolve_claims_analytics(self, info, year=None, month=None):
        return InsuranceService.get_claims_analytics(year, month)

schema = graphene.Schema(query=Query)