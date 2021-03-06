def f(s):
    return 'a' in s

# f: String => Boolean

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    l = L[:]
    for i in range(len(l)):
        if not f(l[i]):
            L.remove(l[i])

    return len(L)

L = ['q', 'a', "c", "d", "3", "e", "f"]
print satisfiesF(L)
print L

