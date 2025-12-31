from fastapi import FastAPI, Query
import os, time, socket

app = FastAPI()
HOST = socket.gethostname()

@app.get("/")
def root():
    return {
        "ok": True,
        "hostname": HOST,
        "service": os.getenv("RAILWAY_SERVICE_NAME", "unknown"),
    }

@app.get("/work")
def work(ms: int = Query(300, ge=0, le=5000)):
    time.sleep(ms / 1000.0)
    return {"worked_ms": ms, "hostname": HOST}
