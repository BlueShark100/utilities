# Import Module
import os, datetime, sys

files = os.listdir()  # list all the files in the same directory as the program

try:
    if sys.argv[1] == 'help' or sys.argv[1] == '-h':
        print("\nTo specify the name of the backup folder type it after calling the program name")
        print(f"for example:\npython {sys.argv[0]} 'name_of_backup folder'")
        print("If you dont name a backup folder name the program will default to 'backups'\n")
        exit()
    backup_folder = sys.argv[1]
except:
    backup_folder = 'backups'

try:
    os.listdir(backup_folder)
except:
    os.mkdir(backup_folder)

for file in files[:]:
    if not os.path.isdir(file):
        os.system(f"cp '{file}' '{backup_folder}/{file}'")
    else:
        files.remove(file)

with open(f"{backup_folder}/AA_BACKUP_INFO.txt", 'w') as output:
    output.write(f'Last backup occurred at {datetime.datetime.now()}\n')
    output.write(f'Number of files copied: {len(files)}\n')
    output.write(f'List of files:\n')
    for i in range(0, len(files), 2):
        try:
            output.write(f'\n{files[i]:<45}\t{files[i+1]}')
        except:
            output.write(f'\n{files[i]:<45}')

print(f"\n{len(files)} files succsesfully backed up into '{backup_folder}'")

num_hidden_files = 0

for file in files:
    if file.startswith('.'):
        num_hidden_files += 1

print(f"{num_hidden_files} files are hidden with '.'\n")