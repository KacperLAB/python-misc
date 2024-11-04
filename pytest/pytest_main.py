import os
import time
from datetime import datetime

os.system("python pytest_file_2.py >> results.txt")
time.sleep(0.5)
os.system("pytest >> results.txt")
time.sleep(0.5)

file_name = "%s.txt" % datetime.now().strftime("%Y-%m-%dT%H-%M")
f = open(file_name,"w")
f.write("Test123")
f.close

