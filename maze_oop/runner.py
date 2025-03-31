from sharik import Sharik

sharik_parameters = ['*', 22]

maze = ['\n', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '\n',
       '█', f'{sharik_parameters[0]}', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', '█', ' ', ' ', ' ',
       '█', '\n',
       '█', '█', '█', ' ', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', '\n',
       '█', ' ', ' ', ' ', '█', ' ', ' ', ' ', '█', ' ', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', '\n',
       '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█', ' ', '█', '█', '█', '█', '█', '█', '█', '\n',
       '█', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', '\n',
       '█', '█', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', '\n',
       '█', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', '\n',
       '█', ' ', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', '█', '█', '█', '█', '█', '█', '█', '█', '\n',
       '█', ' ', ' ', ' ', '█', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', '\n',
       '█', '█', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', '\n',
       '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', '█', ' ', '█', ' ', ' ', ' ', '█', ' ', ' ', ' ', '█', '\n',
       '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', '\n',
       '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', '█', '\n',
       '█', ' ', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█', '\n',
       '█', ' ', '█', ' ', '█', ' ', ' ', ' ', '█', ' ', '█', ' ', '█', ' ', ' ', ' ', '█', ' ', '█', '\n',
       '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', ' ', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█', '\n',
       '█', ' ', '█', ' ', ' ', ' ', '█', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', '█', '\n',
       '█', ' ', '█', '█', '█', ' ', '█', ' ', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', '█', '█', '\n',
       '█', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', 'X', '\n',
       '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', ]

correct_path = (22, 23, 24, 44, 64, 63, 62, 82, 102, 103, 104, 105, 106, 107, 108, 109, 110, 130, 150, 170, 190, 191,
                192, 193, 194, 195, 196, 197, 198, 218, 238, 237, 236, 256, 276, 296, 316, 315, 314, 334, 354, 355, 356,
                376, 396, 397, 398, 399)

sharik = Sharik(maze,sharik_parameters, correct_path)
sharik.display()

print("┌─────────────────────────────────────────┐")
print("│  Для керування використовуйте   W       │")
print("│                               A S D     │")
print("└─────────────────────────────────────────┘")

while True:
    move = input(':')
    if move == 'd':
        if not sharik.move_right():
            break
    if move == 'a':
        if not sharik.move_left(sharik_parameters):
            break
    if move == 's':
        if not sharik.move_down(sharik_parameters):
            break
    if move == 'w':
        if not sharik.move_up(sharik_parameters):
            break

    sharik.display()
