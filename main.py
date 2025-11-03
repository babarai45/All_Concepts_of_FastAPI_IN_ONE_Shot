from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    name = "BABAR"
    return f"""
    <html>
        <body>
            <h1>Hello, {name} 🥰!</h1>
            <h2>Here is the HTTP Request Metadata</h2>
            <p>This request used method: <b>{request.method}</b></p>
            <p>Client host: <b>{request.client.host}</b></p>
            <p>URL: <b>{request.url}</b></p>
            <p>URL: <b>{request.cookies}</b></p>
            <p>URL: <b>{request.headers}</b></p>
        </body>
    </html>
    """
