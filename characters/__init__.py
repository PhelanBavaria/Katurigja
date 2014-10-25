import os


overview = os.listdir('characters')
print(overview)
overview = [a.remove('.yml') for a in overview if '.yml' in a]
