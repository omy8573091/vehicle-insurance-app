# backend/app/config/constants.py
from enum import Enum

class PolicyStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class ClaimStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FRAUD = "fraud"

API_TAGS_METADATA = [
    {
        "name": "policies",
        "description": "Operations with insurance policies",
    },
    {
        "name": "claims",
        "description": "Operations with insurance claims",
    },
    {
        "name": "analytics",
        "description": "Insurance analytics operations",
    },
]