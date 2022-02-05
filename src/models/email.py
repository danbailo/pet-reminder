from typing import Optional

import yagmail

from serializers.email_serializer import EmailSerializer, LoginSerializer
from defaults import EMAIL_LOGIN, EMAIL_PASSWORD


class Email:
    __user: str = None
    __password: str = None

    def __init__(
        self,
        user: Optional[str] = None,
        password: Optional[str] = None
    ) -> None:
        self.__user = user
        self.__password = password

    @property
    def user(self):
        if self.__user is None:
            return EMAIL_LOGIN
        else:
            return self.__user

    @property
    def password(self):
        if self.__password is None:
            return EMAIL_PASSWORD
        else:
            return self.__password

    def send_message(self) -> None:
        infos = {
            'user': self.user,
            'password': self.password,
        }
        yag = yagmail.SMTP(**LoginSerializer(**infos).dict())
        body = EmailSerializer().dict(by_alias=True)
        body['to'] = [recipient['to'] for recipient in body.get('to', {})]
        yag.send(**body)
        yag.close()
