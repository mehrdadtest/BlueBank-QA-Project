from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.auth import router as auth_router
from app.api.accounts import router as accounts_router
from app.api.transfers import router as transfers_router
from app.api.transactions import router as transactions_router

app = FastAPI(
    title="BlueBank API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(transfers_router)
app.include_router(transactions_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app.mount(
    "/css",
    StaticFiles(directory=FRONTEND_DIR / "css"),
    name="css",
)

app.mount(
    "/js",
    StaticFiles(directory=FRONTEND_DIR / "js"),
    name="js",
)


@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/dashboard.html", include_in_schema=False)
def serve_dashboard():
    return FileResponse(FRONTEND_DIR / "dashboard.html")
