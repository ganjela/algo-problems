def calculate_operations(expression):
    result = []
    for i in range(len(expression)):
        operation = expression[i]
        if operation == "+" or operation == "-" or operation == "*":
            sub_str1 = expression[0 : i]
            sub_str2 = expression[i + 1 : ]
            sub_str1_result = calculate_operations(sub_str1)
            sub_str2_result = calculate_operations(sub_str2)
            for i in sub_str1_result :
                for j in sub_str2_result:
                    if operation == "*":
                        result.append(int(i) * int(j))
                    if operation == "+":
                        result.append(int(i) + int(j))
                    if operation == "-":
                        result.append(int(i) - int(j))
    if len(result) == 0:
        result.append(int(expression))
    return result