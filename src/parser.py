from regex import *

def parse_line(line: str) -> dict[str, str]:
	for type, pattern in compiled.items():
		matches = pattern.match(f"{line}\n")
		# print(type, pattern.pattern, matches)
		if matches: return {"type": type} | matches.groupdict()
	return {}

def parse_code(code: str)-> dict[int, dict[str, str]]:
	result: dict[int, dict[str, str]] = {}
	i = 0
	for line in code.splitlines():
		an = parse_line(line)
		# print(i, an)

		if an == {}:
			print(f"Syntax error at {i + 1} line:\n\t{line}")
			return {}

		if an["type"] in ["comment", "ignore"]:
			i += 1
			continue
		
		result[i] = an
		i += 1
	
	return result