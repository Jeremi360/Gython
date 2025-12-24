def create_class(parsed_code: dict[int, dict] = {}, lines: str = ""):
	class_dir: dict = {}
	errors_count = 0
	for i, statement in parsed_code.items():
		line = lines.splitlines()[i]
		match statement["type"]:
			case "class" | "extends" | "class_extends":
				errors_count += reg_class(class_dir, statement, i, line)
			case "var":
				errors_count += reg_var(class_dir, statement, i, line)
			case "const":
				errors_count += reg_const(class_dir, statement, i, line)
	if errors_count > 0: return {}
	return class_dir

def code_error(error_mess: str, i: int, line: str):
	print(f"Code error: {error_mess} at {i + 1} line:\n\t{line}")

def reg_class(class_dir: dir, statement: dict, i:int, line: str) -> int:
	errors_count = 0
	statement_name = statement["name"]
	statement_type = statement["type"]
	if statement_type in ["class", "class_extends"]:
		if "class" not in class_dir.keys():
			class_dir["class"] = {
				"name": statement_name,
				"line": i
			}
		else:
			code_error("Another class declaration", i, line)
			errors_count += 1

	if statement_type in ["extends", "class_extends"]:
		if not "extends" in class_dir.keys():
			class_dir["extends"] = {
				"name": statement["class"],
				"line": i
			}
		else:
			code_error("Another base class declaration", i, line)
			errors_count += 1

	return errors_count

def reg_var(class_dir: dir, statement: dict, i:int, line: str) -> int:
	errors_count = 0
	statement_name = statement["name"]
	statement_type = statement["type"]
	if statement_type in ["var"]:
		if "vars" not in class_dir.keys(): class_dir["vars"] = {}
		if statement_name in class_dir["vars"].keys():
			code_error(rf"Another var {statement_name} declaration", i, line)
			errors_count += 1
		else: class_dir["vars"][statement_name] = {
			"type": statement["value_type"],
			"value": statement["value"],
			"line": i
		}
	return errors_count

def reg_const(class_dir: dir, statement: dict, i:int, line: str) -> int:
	errors_count = 0
	statement_name = statement["name"]
	statement_type = statement["type"]
	if statement_type in ["const"]:
		if "consts" not in class_dir.keys(): class_dir["consts"] = {}
		if statement_name in class_dir["consts"].keys():
			code_error(rf"Another const {statement_name} declaration", i, line)
			errors_count += 1
		else: class_dir["consts"][statement_name] = {
			"type": statement["value_type"],
			"value": statement["value"],
			"line": i
		}
	return errors_count