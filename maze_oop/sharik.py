import json


class Sharik:
    def __init__(self, maze, sharik_parameters, correct_path):
        self.maze = maze
        self.sharik_parameters = sharik_parameters
        self.correct_path = correct_path

    def move_right(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] + 1] != '█':
            if self.sharik_parameters[2] > 0 and self.sharik_parameters[1] + 1 == self.correct_path[
                self.sharik_parameters[2] - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.sharik_parameters[2]]:
                if self.sharik_parameters[1] + 1 == self.correct_path[-1]:
                    print("Вітаю Шарик пройшов лабіринт!")
                    return False
                print("\nШарик на правельному шляху!")
                self.maze[self.sharik_parameters[1] + 1] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] + 1
                self.sharik_parameters[2] += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_left(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] - 1] != '█':
            if self.sharik_parameters[2] > 0 and self.sharik_parameters[1] - 1 == self.correct_path[
                self.sharik_parameters[2] - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.sharik_parameters[2]]:
                self.maze[self.sharik_parameters[1] - 1] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] - 1
                print("\nШарик на правельному шляху!")
                self.sharik_parameters[2] += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_down(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] + 20] != '█':
            if self.sharik_parameters[2] > 0 and self.sharik_parameters[1] + 20 == self.correct_path[
                self.sharik_parameters[2] - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.sharik_parameters[2]]:
                print("\nШарик на правельному шляху!")
                self.maze[self.sharik_parameters[1] + 20] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] + 20
                self.sharik_parameters[2] += 1
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def move_up(self):
        self.maze[self.sharik_parameters[1]] = ' '
        if self.maze[self.sharik_parameters[1] - 20] != '█':
            if self.sharik_parameters[2] > 0 and self.sharik_parameters[1] - 20 == self.correct_path[
                self.sharik_parameters[2] - 1]:
                print("Шарик злякався і втік! Гра закінчена.")
                return False
            if self.sharik_parameters[1] == self.correct_path[self.sharik_parameters[2]]:
                self.maze[self.sharik_parameters[1] - 20] = self.sharik_parameters[0]
                self.sharik_parameters[1] = self.sharik_parameters[1] - 20
                self.sharik_parameters[2] += 1
                print("\nШарик на правельному шляху!")
                return True
            else:
                print("Шарик заблукав, гра закінчена.")
                return False
        print("Шарик вдарилася об стіну, гра закінчена.")
        return False

    def save_progress(self):
        with open("progress.json", "w", encoding="utf-8") as file:
            json.dump(self.sharik_parameters, file)

    def load_progress(self):
        with open("progress.json", "r", encoding="utf-8") as file:
            self.maze[self.sharik_parameters[1]] = " "
            self.sharik_parameters = json.load(file)
            self.maze[self.sharik_parameters[1]] = "*"
            return self.sharik_parameters

    def display(self):
        print(' '.join(self.maze))
