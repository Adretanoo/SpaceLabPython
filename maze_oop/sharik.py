class Sharik:
    def __init__(self, arr):
        self.arr = arr
        self.path = 0


    def move_right(self, sharik, correct_path):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] + 1] != '█':
            if self.path > 0 and sharik[1] + 1 == correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if sharik[1] == correct_path[self.path]:
                if sharik[1] + 1 == correct_path[-1]:
                    print("Вітаю Шарик пройшов лабіринт!")
                    return False
                print("\nШарик на правельному шляху!")
                self.arr[sharik[1] + 1] = sharik[0]
                sharik[1] = sharik[1] + 1
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_left(self, sharik, correct_path):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] - 1] != '█':
            if self.path > 0 and sharik[1] - 1 == correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if sharik[1] == correct_path[self.path]:
                self.arr[sharik[1] - 1] = sharik[0]
                sharik[1] = sharik[1] - 1
                print("\nШарик на правельному шляху!")
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_down(self, sharik, correct_path):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] + 20] != '█':
            if self.path > 0 and sharik[1] + 20 == correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if sharik[1] == correct_path[self.path]:
                print("\nШарик на правельному шляху!")
                self.arr[sharik[1] + 20] = sharik[0]
                sharik[1] = sharik[1] + 20
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False



    def move_up(self, sharik, correct_path):
        self.arr[sharik[1]] = ' '
        if self.arr[sharik[1] - 20] != '█':
            if self.path > 0 and sharik[1] - 20 == correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if sharik[1] == correct_path[self.path]:
                self.arr[sharik[1] - 20] = sharik[0]
                sharik[1] = sharik[1] - 20
                self.path += 1
                print("\nШарик на правельному шляху!")
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def display(self):
        print(' '.join(self.arr))
