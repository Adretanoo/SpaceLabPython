from email_sender import EmailSender
from email_adapter import EmailAdapter


email_old = EmailSender()

adapter = EmailAdapter(email_old)
email_old.send_email("adriantegza@gmail.com","Рахунок")
adapter.send_message("Telegrma","Рахунок поповнео")