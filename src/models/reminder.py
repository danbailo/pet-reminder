from serializers import student_serializer
import requests
import datetime


class Reminder:
    URL: str = 'https://www.fnde.gov.br/digef/rs/spba/publica/pagamento/'
    __student: str = None

    @property
    def student(self):
        return student_serializer.STUDENT_ID

    def _get_last_payment(self) -> datetime.date:
        response = requests.get(self.URL + self.student)
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
