"""
Base case for this recursion is when open and close counts are equal,
in which case all parentheses are used, and we append permutation to the result.

We add closed parentheses only when closed < opened, because
if otherwise, we will get unmatched closed parentheses.
"())))"
"""

def generate_parenthesis(n):
    result = []
    def generate(opened_count, closed_count, s):
        if opened_count == closed_count == n:
            result.append(s)
            return

        if opened_count < n:
            generate(opened_count + 1, closed_count, s + "(")

        if closed_count < opened_count:
            generate(opened_count, closed_count + 1, s + ")")

    generate(0, 0, "")

    return result