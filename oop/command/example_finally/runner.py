from player import Player
from pause_command import PauseCommand
from play_command import PlayCommand
from stop_command import StopCommand
from remote_control import RemoteControl

player = Player()

# commands
play_command = PlayCommand(player)
pause_command = PauseCommand(player)
stop_command = StopCommand(player)

# remote control
remote = RemoteControl()


remote.set_command(play_command)
remote.press_button()
remote.set_command(pause_command)
remote.press_button()

remote.set_command(stop_command)
remote.press_button()
