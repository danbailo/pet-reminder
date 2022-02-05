from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field
from pydantic import root_validator, validator, validate_email
import yagmail

from utils import get_recipients_from_txt


class LoginSerializer(BaseModel):
    user: str
    password: str


class recipientSerializer(BaseModel):
    recipient: str = Field(None, alias='to')

    @validator('recipient', pre=True)
    @classmethod
    def clean_email(value) -> EmailStr:
        return validate_email(value.strip('\n'))[1]

    class Config:
        allow_population_by_field_name = True


class EmailSerializer(BaseModel):
    recipients: Optional[List[recipientSerializer]] = Field(None, alias='to')
    subject: str = Field('[AVISO-PET] A bolsa mensal caiu!', alias='subject')
    html: Optional[List[str]] = Field(None, alias='contents')

    @root_validator(pre=True)
    @classmethod
    def fill_recipients(cls, root) -> List[recipientSerializer]:
        if not root.get('recipients'):
            root['recipients'] = [
                recipientSerializer(recipient=recipient)
                for recipient in get_recipients_from_txt()]
        return root

    @root_validator(pre=True)
    @classmethod
    def set_email(cls, root):
        if not root.get('html'):
            root['html'] = [
                '<h1>A bolsa caiu!</h1><br>',
                yagmail.inline('../assets/money.gif')]
        return root

    class Config:
        allow_population_by_field_name = True
