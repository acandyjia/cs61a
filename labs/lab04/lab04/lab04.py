def flatten(str):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    >>> x = [[1, [2, 3], [4, [5, 6]]]]
    >>> flatten(x)
    [1, 2, 3, 4, 5, 6]
    >>> x
    [[1, [2, 3], [4, [5, 6]]]]
    >>> x = [[1, [1, [1, [1, 1, [1, 1, [1]]]], 1]]]
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, [1, [1, 1, [1, 1, [1]]]], 1]]]
    """
    "*** YOUR CODE HERE ***"
    s=list(str)
    index =0
    length=len(s)
    while index<length:
        if type(s[index])==int:
            index+=1
        else:
            s[index:index+1]=s[index]
            length=len(s)
    
    return s

if __name__=='__main__':
    flatten()


def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    >>> my_map(lambda x: abs(x), [1, -1, 5, 3, 0])
    [1, 1, 5, 3, 0]
    >>> my_map(lambda x: print(x), ['cs61a', 'summer', '2023'])
    cs61a
    summer
    2023
    [None, None, None]
    """
    return [fn(x) for x in seq]


def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    >>> my_filter(lambda x: (x + 5) % 3 == 0, [1, 2, 3, 4, 5])
    [1, 4]
    >>> my_filter(lambda x: print(x), [1, 2, 3, 4, 5])
    1
    2
    3
    4
    5
    []
    >>> my_filter(lambda x: max(5, x) == 5, [1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5]
    """
    return [i for i in seq if pred(i)]


def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    ans = seq[0]
    for i in seq[1:]:
        ans=combiner(ans,i)

    return ans


def my_map_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(my_map)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def my_filter_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(my_filter)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> s1 = [1, 3, 5]
    >>> s2 = [2, 4, 6]
    >>> merge(s1, s2)
    [1, 2, 3, 4, 5, 6]
    >>> s1
    [1, 3, 5]
    >>> s2
    [2, 4, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    >>> merge([2, 3, 4], [2, 4, 6])
    [2, 2, 3, 4, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    len_l ,len_r = len(lst1), len(lst2)
    def merge1(l,r):
        if l>=len_l:
            return lst2[r:]
        if r>=len_r:
            return lst1[l:]

        if lst1[l]<lst2[r]:
            return [lst1[l]] + merge1(l+1,r)
        else :
            return [lst2[r]]+merge1(l,r+1)
        
    return merge1(0,0)




def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return len(list((filter(lambda x: x==x[::-1],map(lambda x : x.lower(),L)))))
