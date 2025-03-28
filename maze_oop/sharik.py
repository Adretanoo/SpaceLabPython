class Sharik:
    def __init__(self, arr):
        self.arr = arr

    def move_right(self, sharik):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] + 1] != '█':
            self.arr[sharik[1] + 1] = sharik[0]
            sharik[1] = sharik[1] + 1
            print("\nШарик на правельному шляху!")
            return True
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_left(self, sharik):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] - 1] != '█':
            self.arr[sharik[1] - 1] = sharik[0]
            sharik[1] = sharik[1] - 1
            print("\nШарик на правельному шляху!")
            return True
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_down(self, sharik):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] + 20] != '█':
            self.arr[sharik[1] + 20] = sharik[0]
            sharik[1] = sharik[1] + 20
            print("\nШарик на правельному шляху!")
            return True
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_up(self, sharik):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] - 20] != '█':
            self.arr[sharik[1] - 20] = sharik[0]
            sharik[1] = sharik[1] - 20
            print("\nШарик на правельному шляху!")
            return True
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def display(self):
        print(' '.join(self.arr))
