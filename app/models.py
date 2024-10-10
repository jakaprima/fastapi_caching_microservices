from sqlmodel import SQLModel, Field, Session, select
from typing import Optional


class Payload(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    list_1: str
    list_2: str
    output: str

    @classmethod
    def check_payload_exists(cls, session: Session, list_1: str, list_2: str):
        instance = session.exec(
            select(cls).where(
                (cls.list_1 == list_1) & (cls.list_2 == list_2)
            )
        ).first()
        return instance

    @classmethod
    def create(cls, session: Session, list_1: str, list_2: str, output: str):
        newInstance = cls(list_1=list_1, list_2=list_2, output=output)
        session.add(newInstance)
        session.commit()
        session.refresh(newInstance)
        return newInstance
    
    @classmethod
    def get(cls, session: Session, payload_id: str):
        return session.exec(select(Payload).where(Payload.id == payload_id)).first()    
