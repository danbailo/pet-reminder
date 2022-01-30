from pydantic import BaseModel


class LoginSerializer(BaseModel):
    user: str
    password: str


class ContentSerializer(BaseModel):
    subject: str = '[AVISO-PET] A bolsa mensal caiu!'
    html: str = (
        '<h1>A bolsa caiu!</h1><br>'
    )
