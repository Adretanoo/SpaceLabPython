from home_facade import SmartHomeFacade
from datetime import datetime

facade = SmartHomeFacade()
now = datetime.now()


if now.hour > 19:
    facade.night_mode()
else:
    facade.morning_mode()