from fastapi import FastAPI
from Routes import base ,data


app=FastAPI()

app.include_router(base.Base_router)
app.include_router(data.data_router)
