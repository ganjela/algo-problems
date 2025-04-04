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