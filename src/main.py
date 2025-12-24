import regex
import parser
import exec

test_code = """
# class SomeClass
# extends Object
# class SomeClass extends Object
class SomeClass: Object
# test comment
var some_var = 3
const some_const: int = 5
# error
"""
regex.compile_regexes()
parsed_code = parser.parse_code(test_code)
# print(parsed_code)
compiled_class = exec.create_class(parsed_code, test_code)
print(compiled_class)