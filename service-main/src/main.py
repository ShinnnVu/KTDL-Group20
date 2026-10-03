from fastapi import FastAPI

from src.api.routes.health import router as health_router
from src.middleware.timing import add_process_time_header

app = FastAPI(title="KTDL-Group20")
app.middleware("http")(add_process_time_header)
app.include_router(health_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "KTDL-Group20 API is running"}
