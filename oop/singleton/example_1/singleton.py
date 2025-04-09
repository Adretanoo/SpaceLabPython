class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Singleton private constructor")

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance



singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(singleton1 is singleton2)
