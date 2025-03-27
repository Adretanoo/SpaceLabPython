class Sharik:
    def __init__(self, arr):
        self.arr = arr

    def move_right(self, sharik):
        self.arr[sharik[1]] = ' '
        self.arr[sharik[1] + 1] = sharik[0]
        sharik[1] = sharik[1] + 1
        print("\nШарік на правельному шляху!")

    def move_left(self, sharik):
        self.arr[sharik[1]] = ' '
        self.arr[sharik[1] - 1] = sharik[0]
        sharik[1] = sharik[1] - 1
        print("\nШарік на правельному шляху!")

    def move_down(self, sharik):
        self.arr[sharik[1]] = ' '
        self.arr[sharik[1] + 20] = sharik[0]
        sharik[1] = sharik[1] + 20
        print("\nШарік на правельному шляху!")

    def move_up(self, sharik):
        self.arr[sharik[1]] = ' '
        self.arr[sharik[1] - 20] = sharik[0]
        sharik[1] = sharik[1] - 20
        print("\nШарік на правельному шляху!")

    def display(self):
        print(' '.join(self.arr))