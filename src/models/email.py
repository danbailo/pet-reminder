from typing import Optional

import yagmail

from serializers.email_serializer import LoginSerializer, ContentSerializer
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
        user = LoginSerializer(**infos).dict()
        contents = ContentSerializer()
        yag = yagmail.SMTP(**user)
        yag.send(
            to='danbailoufms@gmail.com',
            subject=contents.subject,
            contents=[contents.html, yagmail.inline('../assets/money.gif')])
        yag.close()
