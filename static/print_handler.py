import requests
import time
import os
import json

default = requests.get("http://cloudprinter.pythonanywhere.com/get_files")

while True:
    time.sleep(2)
    res = requests.get("http://cloudprinter.pythonanywhere.com/get_files")
    if default.text != res.text:
        # Print the new file and set new files as default
        default = res
        new_file = json.loads(res.text)[-1]
        new_file_without_exts = new_file.split('.')[0]
        print(f"Downloading file: {new_file}")
        os.system(f'curl "https://cloudprinter.pythonanywhere.com/static/files_to_print/{new_file}" --output files_to_print/{new_file}')
        print(f"File downloaded: {new_file}")
        print(f"Executing command: {new_file}")
        os.system(f'2printer -src "files_to_print/{new_file}" -options alerts:no')
        print("Command executed")