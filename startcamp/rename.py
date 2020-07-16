import os

root_path = os.getcwd()
file_path = os.path.join(root_path, 'dummy')

os.chdir(file_path)

files = os.listdir('.')

for f in files:
    os.rename(f, f'SAMSUNG_{f}')
    # os.replace(f, f.replace('SAMSUNG_','SAFFY_'))
