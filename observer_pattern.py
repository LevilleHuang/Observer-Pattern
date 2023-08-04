import abc


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, subject: "Observable"):
        pass


class Observable:

    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
