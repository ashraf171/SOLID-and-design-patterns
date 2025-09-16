from abc import ABC, abstractmethod

# واجهة الاستراتيجية
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

# استراتيجيات مختلفة
class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, amount):
        return amount - (amount * self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount

    def apply_discount(self, amount):
        return max(0, amount - self.discount)

# كلاس Cart
class Cart:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def total(self):
        amount = sum(self.items)
        return self.strategy.apply_discount(amount)
cart = Cart(NoDiscount())
cart.add_item(100)
cart.add_item(50)
print("without :", cart.total())

cart.set_strategy(PercentageDiscount(10))
print("with 10%:", cart.total())

cart.set_strategy(FixedDiscount(30))
print("with 30:", cart.total())
#______________2_______________
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

class EmailObserver:
    def update(self, message):
        print(f"[EMAIL] {message}")

class SMSObserver:
    def update(self, message):
        print(f"[SMS] {message}")

subject = Subject()
subject.attach(EmailObserver())
subject.attach(SMSObserver())
#____________3_____________
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            return ValueError("Unknown type")

animal = AnimalFactory.create_animal("dog")
animal.speak()
#_____________4______________
class OldPrinter:
    def print_text(self, msg):
        print(f"OldPrinter: {msg}")

class NewPrinter:
    def print(self, msg, style="plain"):
        print(f"NewPrinter [{style}]: {msg}")

class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer

    def print_message(self, msg):
        if isinstance(self.printer, OldPrinter):
            self.printer.print_text(msg)
        elif isinstance(self.printer, NewPrinter):
            self.printer.print(msg, style="bold")


old = PrinterAdapter(OldPrinter())
new = PrinterAdapter(NewPrinter())

old.print_message("Hello from old printer")
new.print_message("Hello from new printer")

