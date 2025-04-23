from machine_mediator import MachineMediator
from alarm_clock import AlarmClock
from coffee_machine import CoffeeMachine

mediator = MachineMediator()

alarm = AlarmClock(mediator)
coffee = CoffeeMachine(mediator)
mediator.set_components(alarm, coffee)

alarm.ring()
