from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head><title>Preview App</title></head>
    <body>
        <h1>Entorno de Preview Funcionando</h1>
        <p>Esta app se despliega automaticamente en el subdominio asignado.</p>
        <p>v2 - Cambio de prueba para PR</p>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}
