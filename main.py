from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import time, socket, os

app = FastAPI()
HOST = socket.gethostname()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def ui():
    return FileResponse("static/index.html")

@app.get("/api/info")
def info():
    return JSONResponse({
        "ok": True,
        "hostname": HOST,
        "service": os.getenv("RAILWAY_SERVICE_NAME", "unknown"),
    })

@app.get("/work")
def work(ms: int = Query(300, ge=0, le=5000)):
    time.sleep(ms / 1000.0)
    return {"worked_ms": ms, "hostname": HOST}
