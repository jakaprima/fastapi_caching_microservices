import asyncio
from fastapi import FastAPI, Depends, HTTPException
from app.models import Payload
from app.database import get_session, init_db, engine
from sqlmodel import Session
from app.utils import transformer_function, interleave_lists
from pydantic import BaseModel

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Initialize the database at startup
    init_db()

class PayloadRequest(BaseModel):
    list_1: list[str]
    list_2: list[str]

@app.post("/payload")
async def create_payload(payload_request: PayloadRequest, session: Session = Depends(get_session)):
    list_1 = payload_request.list_1
    list_2 = payload_request.list_2
    if len(list_1) != len(list_2):
        raise HTTPException(status_code=400, detail="Both lists must same length")

    # Transform strings asynchronously for simulation hit external service
    transformed_list1 = await asyncio.gather(*(transformer_function(item) for item in list_1))
    transformed_list2 = await asyncio.gather(*(transformer_function(item) for item in list_2))

    # Interleave the transformed lists
    interleaved_payload = interleave_lists(transformed_list1, transformed_list2)
    payload_str = ", ".join(interleaved_payload)

    with Session(engine) as session:
        # check exist
        instance = Payload.check_payload_exists(session, str(list_1), str(list_2))
        if instance:
            return {"message": "Payload already exists", "payload_id": instance.id}
        # Create new payload if it doesn't exist
        newInstance = Payload.create(session, str(list_1), str(list_2), payload_str)
    return {"id": newInstance.id, "output": newInstance.output}

@app.get("/payload/{payload_id}")
def get_payload(payload_id: int, session: Session = Depends(get_session)):
    instance = Payload.get(session, payload_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Payload not found")
    return {"output": instance.output}
