from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.accounts import router as accounts_router
from app.api.transfers import router as transfers_router
from app.api.transactions import router as transactions_router

app = FastAPI(title="BlueBank API", version="1.0.0")

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(transfers_router)
app.include_router(transactions_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
