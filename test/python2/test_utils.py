from erlport import Atom, erlang

def switch(n):
    result = 0
    for i in range(n):
        result = erlang.call(Atom("python2_tests"), Atom("test_callback"),
            [result, i])
    return n

def identity(v):
    return v

def length(v):
    return len(v)

def print_string(s):
    print s.to_string()