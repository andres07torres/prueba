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
        <p>v9 - Cambio nuevo</p>
    </body>
    </html>
    """

@app.get("/nueva-pantalla", response_class=HTMLResponse)
def nueva_pantalla():
    return """
    <html>
    <head><title>Nueva Pantalla</title></head>
    <body>
        <h1>Esta es la nueva pantalla</h1>
        <p>Funcionalidad agregada desde feature/nueva-pantalla</p>
        <a href="/">Volver al inicio</a>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}