import glob
from pathlib import Path

path = Path(__file__).parent.parent.absolute()

result = glob.glob("{}/*.py".format(str(path)))

print(len(result))