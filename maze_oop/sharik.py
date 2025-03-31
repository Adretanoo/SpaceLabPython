
class Sharik:
    def __init__(self, maze, sharik_parameters, correct_path):
        self.maze =
        self.sharik_parameters = sharik_parameters
        self.correct_path = correct_path
        self.path = 0


    def move_right(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] + 1] != '█':
            if self.path > 0 and self.sharik_parameters[1] + 1 == self.correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.path]:
                if self.sharik_parameters[1] + 1 == self.correct_path[-1]:
                    print("Вітаю Шарик пройшов лабіринт!")
                    return False
                print("\nШарик на правельному шляху!")
                self.maze[self.sharik_parameters[1] + 1] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] + 1
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_left(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] - 1] != '█':
            if self.path > 0 and self.sharik_parameters[1] - 1 == self.correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.path]:
                self.maze[self.sharik_parameters[1] - 1] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] - 1
                print("\nШарик на правельному шляху!")
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_down(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] + 20] != '█':
            if self.path > 0 and self.sharik_parameters[1] + 20 == self.correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.path]:
                print("\nШарик на правельному шляху!")
                self.maze[self.sharik_parameters[1] + 20] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] + 20
                self.path += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False



    def move_up(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] - 20] != '█':
            if self.path > 0 and self.sharik_parameters[1] - 20 == self.correct_path[self.path - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.path]:
                self.maze[self.sharik_parameters[1] - 20] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] - 20
                self.path += 1
                print("\nШарик на правельному шляху!")
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False


    # def save_progress(self):
    #     save = input("Зберегти прогрес(+,-):")
    #     if save == '+':
    #         with open("progress.json", 'w') as file:
    #             json.dump(self.arr, file)
    #     else:
    #         with open("progress.json", "r+") as file:
    #             file.truncate(0)


    def display(self):
        print(' '.join(self.maze))
