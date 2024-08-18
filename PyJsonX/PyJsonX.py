import re
import ast
import json

def adjust_indentation(code_str):
    lines = code_str.splitlines()
    indent_level = min(len(re.match(r'^\s*', line).group()) for line in lines if line.strip())
    adjusted_lines = [line[indent_level:] for line in lines]
    return '\n'.join(adjusted_lines)

def add_indentation(code_str, indent_size=4):
    indent = ' ' * indent_size
    return '\n'.join(indent + line for line in code_str.splitlines())

def remove_single_line_comments(json_str):
    pattern = r'//.*'
    return '\n'.join(re.sub(pattern, '', line).rstrip() for line in json_str.splitlines())

def remove_block_comments(text):
    return re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

def execute_python_code(code):
    local_vars = {}
    wrapped_code = "result = ''\n"
    wrapped_code += "def main():\n"
    wrapped_code += add_indentation(adjust_indentation(code))
    wrapped_code += "\nresult = main()"
    try:
        exec(wrapped_code, globals(), local_vars)
    except Exception as e:
        return f"Error executing code: {e}"
    return str(local_vars.get('result', ''))

def replace_python_code_tags(pyjson):
    pattern = re.compile(r'<\?py(.*?)\?>', re.DOTALL)
    def replacement_function(match):
        code = match.group(1)
        return execute_python_code(code)
    return pattern.sub(replacement_function, pyjson)

def execute(pyjson):
    cleaned_str = remove_block_comments(remove_single_line_comments(pyjson))
    processed_str = replace_python_code_tags(cleaned_str)
    try:
        processed_obj = ast.literal_eval(processed_str)
    except (ValueError, SyntaxError) as e:
        return f"Error processing JSON: {e}"
    return json.dumps(processed_obj, indent=4, ensure_ascii=False)

def execute_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        pyjson = file.read()
    
    result = execute(pyjson)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(result)