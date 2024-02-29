"""
Example:
BEHAVIORAL Design Patterns
___OBSERVER___
"""


class ObservablePerson:
    name = "Default User"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"I am {self.name}"

    def register_observer(self, observer):
        # record an observer
        self._observers.append(observer)

    def notify_observers(self, message):
        # each Observer is notified
        # by calling the notify function from the Observer class
        for obs in self._observers:
            obs.notify(self, message)


class Observer:
    def __init__(self, name, observable):
        # when the Observer is instantiated, it is registered in the list of
        # observations of the Observable object
        self.name = name
        observable.register_observer(self)

    def notify(self, observable, message):
        print(f"Observer: {self.name} Got message: {message}")
        print(f" from observable obj: {observable}")


subject = ObservablePerson()
observer_obj1 = Observer("observer_one", subject)
observer_obj2 = Observer("observer_two", subject)

# at the time of the call, both observer objects receive notification
subject.notify_observers("An event occurred....")