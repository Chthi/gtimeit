

from gtimeit import execTimeList, display_performances

class Foo:
    @execTimeList
    def do_something():
        pass

@execTimeList
def do_something():
    pass

Foo.do_something()
do_something()

display_performances()



from gtimeit import Benchmark

Benchmark([Foo.do_something, do_something])