from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI(title="España WhatsApp Lead Agent")


class EventIn(BaseModel):
    source: str
    payload: dict


@app.get('/health')
def health():
    return {'ok': True}


@app.post('/webhooks/whatsapp')
async def whatsapp_webhook(req: Request):
    data = await req.json()
    return {'received': True, 'provider_payload': data}


@app.post('/api/v1/events')
def create_event(event: EventIn):
    return {'stored': True, 'source': event.source, 'payload': event.payload}
