def write_to_c_file(program, output_file):
    template = """
#include <stdio.h>

int main() {{
    {modified_program}
    return 0;
}}
"""

    lines = program.split("\n")
    modified_lines = []
    variables = {}

    for line in lines:
        if line.strip() == "":
            continue  # Skip empty lines

        if line[0].isdigit():
            modified_line = f'printf("%d", {line.strip()});'

        elif line.startswith("VAR"):
            parts = line.split("=")
            var_name = parts[0].replace("VAR", "").strip()
            var_value = parts[1].strip()

            if '"' in var_value:
                modified_line = f'char {var_name}[] = {var_value}'
                variables[var_name] = 's'
            else:
                modified_line = f'int {var_name} = {var_value}'
                variables[var_name] = 'd'

        elif line.startswith("ESCREVER"):
            content = line.split("ESCREVER")[1].strip().replace(";", "").strip().replace('"', '')
            if content in variables:
                format_specifier = variables[content]
                if format_specifier == 's':
                    modified_line = f'printf("%s", {content});'
                else:
                    modified_line = f'printf("%d", {content});'
            else:
                modified_line = f'printf("{content}");'
        
        else:
            modified_line = line

        modified_lines.append(modified_line)

    modified_program = "\n".join(modified_lines)
    final_program = template.format(modified_program=modified_program)

    with open(output_file, 'w') as file:
        file.write(final_program)
