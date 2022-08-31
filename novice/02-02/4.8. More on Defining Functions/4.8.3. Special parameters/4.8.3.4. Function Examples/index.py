def standart_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standart, *, kwd_only):
    print(pos_only, standart, kwd_only)

# standart_arg(2)
# standart_arg(arg=2)

# pos_only_arg(1)
# pos_only_arg(arg=1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# combined_example(1, 2, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'

def foo(name, /, **kwds):
    return 'name' in kwds
    foo(1, **{'name': 2})
True