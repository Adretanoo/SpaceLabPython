class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance



singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)
