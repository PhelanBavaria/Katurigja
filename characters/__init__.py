import os


overview = os.listdir('characters')
overview = [a for a in overview if '.py' not in a]
