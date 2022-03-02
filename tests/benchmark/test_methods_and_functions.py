
from gtimeit import Benchmark

class Foo:
    def do_something():
        pass

def do_something():
    pass

Benchmark([Foo.do_something, do_something])