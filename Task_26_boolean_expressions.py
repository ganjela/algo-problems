def eval_bool_expression(expression):
    stack = []
    operators = ("&", "|", "!")

    for char in expression:
        if char == "(" or char == ",":
            continue

        if char != ")":
            stack.append(char)
        else:
            has_true = False
            has_false = False

            while stack[-1] not in operators:
                value = stack.pop()

                if value == "t":
                    has_true = True
                else:
                    has_false = False

            operator = stack.pop()

            if operator == "!":
                stack.append("t" if not has_true else "f")
            elif operator == "&":
                stack.append("f" if not has_false else "t")
            else:
                stack.append("t" if has_true else "f")

    return stack[-1] == "t"