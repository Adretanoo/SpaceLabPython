from email_adapter import EmailAdapter
from telegram_notifier import TelegramNotifier
from legacy_email_sender import LegacyEmailSender



old_email_sender = LegacyEmailSender()
email_sender_adapter = EmailAdapter(old_email_sender)

email_sender_adapter.send("adriantegza@gmail.com","Оплатіть підписку на анощому сайті")


telegram_notifier = TelegramNotifier()
telegram_notifier.send("@Adritanoo","Оплатіть підписку в тг")