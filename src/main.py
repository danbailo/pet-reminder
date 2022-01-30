from models.reminder import Reminder
from models.email import Email

if __name__ == '__main__':
    reminder = Reminder(student_id=None)
    email = Email()
    if reminder.has_new_payment():
        email.send_message()
