from real_subject import RealSubject


class SubjectProxy(RealSubject):

    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print("Проксі передає запит до реального об'єкта")
        self.real_subject.request()