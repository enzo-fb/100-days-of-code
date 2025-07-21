"""Padrões de Design"""


# Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Factory
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Au au!"


class Cat(Animal):
    def speak(self):
        return "Miau!"


def animal_factory(tipo):
    if tipo == "dog":
        return Dog()
    elif tipo == "cat":
        return Cat()
    else:
        raise ValueError("Tipo desconhecido")


# Observer
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Recebido: {message}")


# Exemplos de uso
if __name__ == "__main__":
    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print("Singleton:", s1 is s2)

    # Factory
    animal = animal_factory("dog")
    print("Factory:", animal.speak())

    # Observer
    subject = Subject()
    observer1 = Observer()
    observer2 = Observer()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.notify("Olá, Observers!")
