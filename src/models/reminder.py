import datetime
import requests
from typing import Optional

from defaults import STUDENT_ID
from serializers.student_serializer import StudentSerializer


class Reminder:
    URL: str = 'https://www.fnde.gov.br/digef/rs/spba/publica/pagamento/'
    __student_id: str = None

    def __init__(self, student_id: Optional[str] = None) -> None:
        self.__student_id = student_id

    @property
    def student_id(self):
        if self.__student_id is None:
            return STUDENT_ID
        return self.__student_id

    def _get_last_payment(self) -> datetime.date:
        student_id = StudentSerializer(id=self.student_id)
        response = requests.get(self.URL + student_id.id)
        last_payment = (response.json()["programas"][0]['entidades']
                        ['15461510000133']['funcoes']['49']['pagamentos'][-1])
        date_payment = last_payment['data'].split('/')
        return datetime.date(
            year=int(date_payment[2]),
            month=int(date_payment[1]),
            day=int(date_payment[0]))

    def has_new_payment(self) -> bool:
        now = datetime.datetime.now().date()
        if now == self._get_last_payment():
            return True
        else:
            False
