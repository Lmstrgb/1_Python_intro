# import sys
# str1="абракадабра"
# print(len(str1))

# print (sys.prefix) 
import os
import sys
python_path=os.path.dirname(sys.executable)
python_version = sys.version
print(f'Путь: {python_path}, версия: {python_version}')