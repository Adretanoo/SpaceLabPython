from message import Message
from message_decorator import MessageDecorator


mes = Message()
mes.send()

mes_decor = MessageDecorator(mes)
mes_decor.send()