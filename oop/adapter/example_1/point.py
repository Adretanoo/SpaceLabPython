class OldPrinter:
    def print_pdf(self, filename):
        print(f"Старий принтер друкує PDF: {filename}")


class NewPrinter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, filename):
        # Просто викликаємо старий метод через адаптер
        self.old_printer.print_pdf(filename)


old = OldPrinter()           # старий клас
adapter = NewPrinter(old)    # обгортаємо в адаптер

adapter.print("myfile.pdf")  # викликаємо метод, якого в старому класі не було
