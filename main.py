from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI(title='Classification')

@app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")