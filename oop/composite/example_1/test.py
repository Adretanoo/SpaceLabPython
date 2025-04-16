from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"📄 File: {self.name}")

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"📁 Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)


if __name__ == "__main__":
    file1 = File("document.txt")
    file2 = File("photo.jpg")
    file3 = File("notes.md")

    folder1 = Folder("Work")
    folder2 = Folder("Personal")

    folder1.add(file1)
    folder2.add(file2)
    folder2.add(file3)

    root = Folder("Root")
    root.add(folder1)
    root.add(folder2)

    root.display()
