import re

# Чтение файла
with open("queryes.md", "r", encoding="utf-8") as file:
    content = file.read()

# Извлечение блоков кода с Python
python_code_blocks = re.findall(r"```python\n(.*?)```", content, re.DOTALL)

# Запись только кода в новый файл
with open("python_code.md", "w", encoding="utf-8") as output_file:
    for block in python_code_blocks:
        output_file.write(block.strip() + "\n\n")

print("Файл с кодом сохранен как 'python_code.md'.")

import re

# Путь к вашему файлу
input_file_path = "python_code.md"
output_file_path = "python_code_2222.py"

# Флаг для отслеживания многострочных комментариев
inside_multiline_comment = False

with open(input_file_path, "r", encoding="utf-8") as infile, open(output_file_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Удаляем ">>> " из начала строки
        line = re.sub(r'^\s*>>> ', '', line)

        # Проверяем начало или конец многострочного комментария
        if '"""' in line or "'''" in line:
            if not inside_multiline_comment:  # Если начало
                inside_multiline_comment = True
            else:  # Если конец
                inside_multiline_comment = False
            continue  # Пропускаем строки с многострочными комментариями

        if inside_multiline_comment:
            continue  # Пропускаем строки внутри многострочных комментариев

        # Удаляем однострочные комментарии
        line = re.sub(r'#.*', '', line).rstrip()

        # Если строка не пустая, записываем её
        if line.strip():
            outfile.write(line + "\n")