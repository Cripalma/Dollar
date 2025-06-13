from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"} if requests.get("https://dolarapi.com/v1/dolares").ok else {"status": "error"}

@app.get("/dolar")
def dolar():
    data = requests.get("https://dolarapi.com/v1/dolares").json()[0]
    return {"compra": data["compra"], "venta": data["venta"]}

@app.get("/euro")
def euro():
    data = requests.get("https://dolarapi.com/v1/euros").json()[0]
    return {"compra": data["compra"], "venta": data["venta"]}
