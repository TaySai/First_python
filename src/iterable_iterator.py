seq = list([1, 2, 3])
print(hasattr(seq, "__iter__"))
try:
    next(seq)
except Exception as e:
    print(e)
iter_seq = iter(seq)
print(hasattr(iter_seq, "__iter__"))
print(next(iter_seq))
print(next(iter_seq))
print(next(iter_seq))
print(next(iter_seq))
