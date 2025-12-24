import re
from re import Pattern

re_empty = r"\s*\n"
re_any = r"[\s\w\d.]"
re_name = r"(?P<name>\w+)"
re_class = r"(?P<class>\w+)"
re_type = r"(?P<value_type>:\s*(\w+)?)"
re_value = rf"(?P<value>{re_any}+)"

regexes: dict[str, str] = {
	# \s*\n
	"ignore": re_empty,
	# # comment
	"comment": rf"#{re_any}*\n",
	# class ClassName
	"class": rf"class\s+{re_name}{re_empty}",
	# extends BaseClass 
	"extends": rf"extends\s+{re_class}{re_empty}",
	# var var_name: Type = value
	"var": rf"var\s+{re_name}\s*{re_type}?\s*=\s+{re_value}{re_empty}",
	# const const_name: Type = value
	"const": rf"const\s+{re_name}\s*{re_type}?\s*=\s+{re_value}{re_empty}",
	# class ClassName extends BaseClass
	# class ClassName: BaseClass	
	# ? class ClassName <- BaseClass
	"class_extends": rf"class\s+{re_name}(\s*:|\s+extends)\s+{re_class}{re_empty}",
}

compiled: dict[str, Pattern] = {}

def compile_regexes():
	for type, reg in regexes.items():
		# print(type, reg)
		compiled[type] = re.compile(reg)
