from modules.math_operations.core.executor import execute_string

expression = input()

result = execute_string(expression)
formatted_result = "{:.2f}".format(result)
print(formatted_result)

