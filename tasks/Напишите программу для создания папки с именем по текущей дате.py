import os
from datetime import date

os.mkdir(f"backup_{date.today().strftime('%d%m%Y')}")