from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head><title>Preview App</title></head>
    <body>
        <h1>Entorno de Preview</h1>
        <p>Esta app se despliega automaticamente en el subdominio asignado.</p>
        <p>v5 - Prueba definitiva de despliegue</p>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}
