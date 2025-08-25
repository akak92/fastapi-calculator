from fastapi import FastAPI
from app.api.routes.calculator import router as calculator_router

def create_app() -> FastAPI:
    app = FastAPI(title="Calculator API", version="1.0.0")
    app.include_router(calculator_router, prefix="/calculator", tags=["calculator"])

    # Endpoint raíz
    @app.get("/")
    def root():
        return {"message": "Welcome to calculator!"}
    return app

app = create_app()
