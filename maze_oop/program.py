from sharik import Sharik

sharik = ['*',21]

arr = ['\n','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','\n',
       f'{sharik[0]}',' ',' ',' ','█',' ',' ',' ',' ',' ','█',' ',' ',' ','█',' ',' ',' ','█','\n',
       '█','█','█',' ','█',' ','█','█','█','█','█',' ','█',' ','█','█','█',' ','█','\n',
       '█',' ',' ',' ','█',' ',' ',' ','█',' ',' ',' ','█',' ',' ',' ',' ',' ','█','\n',
       '█',' ','█','█','█','█','█',' ','█',' ','█',' ','█','█','█','█','█','█','█','\n',
       '█',' ',' ',' ',' ',' ',' ',' ',' ',' ','█',' ','█',' ',' ',' ',' ',' ','█','\n',
       '█','█','█',' ','█','█','█','█','█',' ','█',' ','█','█','█','█','█',' ','█','\n',
       '█',' ','█',' ','█',' ',' ',' ',' ',' ','█',' ',' ',' ',' ',' ',' ',' ','█','\n',
       '█',' ','█',' ','█',' ','█','█','█',' ','█','█','█','█','█','█','█','█','█','\n',
       '█',' ',' ',' ','█',' ','█',' ','█',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','\n',
       '█','█','█','█','█',' ','█',' ','█','█','█',' ','█','█','█','█','█',' ','█','\n',
       '█',' ',' ',' ',' ',' ','█',' ','█',' ','█',' ',' ',' ','█',' ',' ',' ','█','\n',
       '█',' ','█','█','█','█','█',' ','█',' ','█','█','█',' ','█',' ','█','█','█','\n',
       '█',' ','█',' ',' ',' ',' ',' ','█',' ',' ',' ',' ',' ','█',' ',' ',' ','█','\n',
       '█',' ','█',' ','█','█','█','█','█',' ','█','█','█','█','█',' ','█',' ','█','\n',
       '█',' ','█',' ','█',' ',' ',' ','█',' ','█',' ','█',' ',' ',' ','█',' ','█','\n',
       '█',' ','█',' ','█','█','█',' ','█',' ','█',' ','█',' ','█','█','█',' ','█','\n',
       '█',' ','█',' ',' ',' ','█',' ','█',' ','█',' ',' ',' ',' ',' ','█',' ','█','\n',
       '█',' ','█','█','█',' ','█',' ','█',' ','█','█','█','█','█',' ','█','█','█','\n',
       '█',' ',' ',' ',' ',' ',' ',' ','█',' ',' ',' ',' ',' ','█',' ',' ',' ',' ','\n',
       '█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',]


sharik_object = Sharik(arr)

maze = ' '.join(arr)
print(maze)

while(True):
       move = input(':')
       if move == 'd':
              sharik_object.move_right(sharik)
       if move == 'a':
              sharik_object.move_left(sharik)
       if move == 's':
              sharik_object.move_down(sharik)
       if move == 'w':
              sharik_object.move_up(sharik)
       print(sharik_object.display())
