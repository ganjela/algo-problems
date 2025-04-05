"""
We are given N passengers and first passenger lost the ticket.
Assume that she (she's blonde) takes place of passenger M. Some time after,
when M boards, instead of finding another seat he tells her to find another sit
(both cases are same, because one person still has to randomly find a seat).
So, she goes to another sit until N-th persons sit and hers are left.
In which case choosing the right sit is %50
"""
def calculate_probability(n):
    return 1 / 2 if n != 1 else 1