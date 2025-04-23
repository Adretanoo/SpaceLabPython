from spam_filter import SpamHandler
from censor_filter import CensorFilter
from short_message import ShortFilter

spam_filter = SpamHandler()
censor_filter = CensorFilter()
short_filter = ShortFilter()

short_filter.set_next(spam_filter).set_next(censor_filter)


print(short_filter.handle("Привіт дурак"))
print(short_filter.handle("Це спам повідомлення"))
print(short_filter.handle("Гарний день тобі!"))
print(short_filter.handle("i"))
