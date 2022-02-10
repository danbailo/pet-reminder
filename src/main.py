from models.reminder import Reminder
from models.email import Email
from models.database import Database


if __name__ == '__main__':
    database = Database()
    reminder = Reminder()
    # email = Email()

    has_paid = reminder.has_new_payment()
    # if not has_paid:
    #     exit()
    data = {
        'id': None,
        'last_payment': None,
        'has_sent_email': None,
    }
    Payment = database.TABLES_HOOK.get('PAYMENT')
    session = database.connect_db()
    breakpoint()
    if last_payment := session.query(Payment).order_by(
                               Payment.id.desc()).first():
        if not last_payment.has_sent_email:
            payment = Payment(has_sent_email=True)
            session = database.connect_db()
            session.add(payment)
            session.close()
