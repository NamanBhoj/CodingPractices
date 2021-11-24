def test(x) -> str: # the -> str annotation is here to just tell that this function returns a string
                    # -> it does not force the function to return a string but
    x ="hello"
    return x

a = test("hi")
print(a)


def test1(a) -> bool: # see here we have an annotation bool but it doesnt forces the function to return only bool

    return "hi"

print(test1('hello'))    