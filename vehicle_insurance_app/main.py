# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp
from graphene import Schema
from app.config import get_settings, API_TAGS_METADATA
from app.graphql.schema import Query
import logging
from app.utils.logging import configure_logging
from app.models.base import Base
from app.db.session import engine

settings = get_settings()
configure_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_tags=API_TAGS_METADATA
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GraphQL endpoint
app.add_route(
    "/graphql",
    GraphQLApp(schema=Schema(query=Query))
)

@app.on_event("startup")
async def startup():
    # Create database tables
    Base.metadata.create_all(bind=engine)
    logging.info("Database tables created")

@app.get("/health")
def health_check():
    return {"status": "healthy"}