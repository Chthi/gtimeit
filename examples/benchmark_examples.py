#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

from gtimeit import Benchmark

# a bunch of function to benchmark

def with10000char():
    msg = 10000*"g"
    with open("log.txt", "w+") as stream:
        stream.write(msg)

def withOpen(msg="tac-"):
    with open("log.txt", "w+") as stream:
        pass

def withPrint(msg="tac-"):
    print(msg)

def noPrint(msg="chuut"):
    pass

#    ----------

def listExist(l=[]):
    if l :
        pass

def notEmpty(l=[]):
    if l != [] :
        pass

def lenZero(l=[]):
    if len(l) != 0 :
        pass

#    ----------

def declareSimple():
    l = []

def declareInstance():
    l = list()


#    ----------

def count(l):
    n = 0
    for elt in l:
        n += 1
    return n

#    ----------

TO_MATCH = re.compile(r'test_matching_[0-9]+$')
TO_SEARCH = re.compile(r'^test_matching_[0-9]+$')

def matcher(string="test_matching_1"):
    return TO_MATCH.match(string)

def searcher(string="test_matching_1"):
    return TO_SEARCH.search(string)

#    ----------

def plusPuisEgale(i=1):
    return i + 1

# reddit.com/r/Python/comments/wbs1o/best_way_to_increment_of_1_in_python/

# recursive abacus
def recursive_abacus(i=1, n=0):
    return recursive_abacus(i^(1<<n),recursive_abacus(0,n)) if i&(1<<n) else i|i^(1<<n)

# there are 10 type of coders ...
def ten_types(i=1):
    return i++ (lambda j: j()**j())(type(i)) #halike

# dyslexia
def dyslexia(i=1):
    return (sum(range(i))*2)/i # decrement  #halike

# it's all about the context
def context(i=1):
    return 2*i-(sum(range(i))*2)/i # banermatt

# mapreducing
def mapreducing(i=1):
    return __import__('functools').partial(i.__add__, 1)()  #halike

# identity crisis
def identity_crisis(i=1):
    return i+(i is i) # SFJulie1 (kind of) #halike

# be real
def be_real(i=1):
    return int((i-1j**2).real)  #halike

# TIMTOWTDI
def timtowtdi(i=1):
    return int(__import__("os").popen("perl -e'++($a=%d)&&print$a'"%i).read()) # SFJulie1

# Delegation aka someone may know the answer by SciK
def someone(i=1):
    return int(__import__("os").popen("perl -e'use Inline C=>q[int incr(int i){return i-~0^0;}];print incr %d'" % i).read())

# 
def subprocess(i=1):
    return int((lambda x: x('subprocess').check_output([x('sys').executable, '-c', 'print %d++1'%i])))(__import__)  #halike

# inchworm on a stick
def inchworm_on_a_stick(i=1):
    return -~i # Brian

# regexp is a turing complete machine
def regexp(i=1):
    return len(__import__('re').sub('(.)$', '\\1\\1', '1'*i)) #lost-theory (does not work on 0)

#tempis fugit
def tempis_fugit(i=1):
    return i-(lambda t: int(t.time()-(t.sleep(1),t.time())[1]))(__import__('time'))

# being partial by willm
def being_partial(i=1):
    return __import__('itertools').dropwhile(lambda m:m==i, __import__('itertools').count(i)).next()

# pushing to the max 
def pushing_to_the_max(i=1):
    return next(j for j in range(__import__('sys').maxint) if j > i) # nivertius

#might work by flowblok
def might_work(i=1):
    return i+int(round(__import__('random').random()))

# the choice of a GNU generation by sonwell
def gnu_generation(i=1):
    return ((lambda rec, i, A, n: rec(rec, i, A, n))(lambda rec, i, A, n: A if i == 0 else i + abs(i - ((i > -1) - (i < 0)) * rec(rec, abs(i) - 1, A * n, n + 1) / abs(i)), i, 1, 2))

#nothing compares to U by cecedille1 (and sinnead O'connors)
def compares(i=1):
    return cmp(u,0) * len(xrange(-1 , i, cmp(u,0) ) ) if u else 1

# it's a kind of magic by ceceddile1
def magic(i=1):
    return (1).__radd__(i)

# the neighbour of the beast by fabzter & samus_
def neighbour(i=1):
    return int((str(i)[:-1] + {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9'}[str(i)[-1]] if str(i)[-1] in {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9'} else str(addition(int(str(i)[:-1])) if str(i)[:-1] else '1') + '0') if str(i) else '1')

# cloud computing by hhh333
def cloud_computing(i=1):
    return float(__import__('re').findall("%d.?\d* \+ 1 = (\d+\.?\d*)"%i,__import__('requests').get("http://google.com/search", params=dict(q="%f+1"%i)).text)[0])

# In the face of ambiguity, refuse the temptation to guess. by gtr053
def ambiguity(i=1):
    return float(raw_input("Pretty please enter the result of %f + 1: "%x))

# pseudomenon : defeats the truth swapping trick True,False=False,True
def pseudomenon(i=1):
    return i+(True if True else False)

# polyglot by Book mod SFJulie1 
# def polyglot(i=1):
    # q = 0 or """ #=;$A=41;sub A { ~-$A+2}; q' """
    # A=lambda A: -~A  #';
    # print A(41) # python + perl = <3

# se(ct|x)ually amibuous by Brian
def amibuous(i=1):
    return __import__('bisect').bisect(xrange(__import__('sys').maxint), i)






def build(n):
    return [0] * n


if __name__ == "__main__":

    # example 1
    # bm = Benchmark(size=200, multiplicator=10, procedures=[with10000char, withOpen, withPrint, noPrint])
 
    # example 2
    # bm = Benchmark(size=200, multiplicator=10000, procedures=[declareSimple, declareInstance])

    # example 3
    bm = Benchmark(size=200, multiplicator=10000, procedures=[listExist, notEmpty, lenZero])
    
    # example 4
    # prototype
    # bm = Benchmark([len, count], run=False)
    # bm.complexity_run(range(0, 50), constructor=build, multiplicator=100, plot=False)
    # bm.plot(average=False)

    # example 5
    # bm = Benchmark(size=200, multiplicator=10000, procedures=[matcher, searcher])

    procedures = [
        plusPuisEgale,
        recursive_abacus, # unstable
        ten_types,
        # dyslexia, # decrement
        # context, # non constant complexity
        mapreducing,
        identity_crisis,
        be_real,
        # timtowtdi, # very slow
        # someone, # no perl
        # subprocess, # not working
        inchworm_on_a_stick,
        # regexp, # non constant complexity
        # tempis_fugit, # too sleepy
        being_partial,
        # pushing_to_the_max, # memory error
        # might_work, # might work, some times
        # gnu_generation, # non constant complexity
        # compares, # huuu ?
        magic,
        # neighbour, # addition not found
        # cloud_computing, # no requests module
        # ambiguity, # human limited
        pseudomenon,
        amibuous,
    ]

    complex_procedures = [
        recursive_abacus,
        context,
        timtowtdi,
        regexp,
        # to compare whith other
        plusPuisEgale, # faster constant complexity one
        amibuous, # slowest constant complexity one
    ]

    # example 6
    # benchmark on multiples functions
    # bm = Benchmark(procedures, 150, multiplicator=5000)

    # example 7
    # complexity benchmark
    # bm = Benchmark(complex_procedures, run=False)
    # bm.complexity_run(range(1, 500000, 2000))
