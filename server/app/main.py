from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from prometheus_fastapi_instrumentator import Instrumentator
from database import Base, engine
from user.routes import router as user_router
from imageprocessing import router as image_router
from augmenation import router as augmenation_router

app = FastAPI(title="Приложение аугментации")
Base.metadata.create_all(bind=engine)

Instrumentator().instrument(app).expose(app)

app.include_router(image_router)
app.include_router(augmenation_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    #allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create initialized database table
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)  

@app.get('/', tags=["root"])
async def root():
    return "Hello World!"

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)