from threading import Lock, Thread
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the metaclass because it is best suited for this purpose.
    """

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = ""
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        if not value:
            self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """


if __name__ == "__main__":
    # The client code.
    results = set()
    lock: Lock = Lock()
    def test_singleton(value: str, _, __) -> None:
        singleton = Singleton(value)
        with lock:
            results.add(singleton.value)
    process1 = Thread(target=test_singleton, args=("Foo"))
    process2 = Thread(target=test_singleton, args=("Bar"))
    process1.start()
    process2.start()
    assert len(results) == 1

   # single thread tests 
    s1 = Singleton("dsa")
    s2 = Singleton("DSA")

    assert id(s1) == id(s2)

