# Import Modules
import os, datetime, sys

# because this program uses commandline arguments specific to Linux/Unix
# sys.platform will give us the platform we are on
# ┍━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━┑
# │ System              │ Value               │
# ┝━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━┥
# │ Linux               │ linux or linux2 (*) │
# │ Windows             │ win32               │
# │ Windows/Cygwin      │ cygwin              │
# │ Windows/MSYS2       │ msys                │
# │ Mac OS X            │ darwin              │
# ┕━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━┙

accepted_platforms = ["darwin", "linux", "linux2"]

# I havent actually tested this on other platforms but hopefully it works sys.platform
if sys.platform not in accepted_platforms:
    print("\nThis program will only work on MacOS and Linux because of\nthe use of commandline arguments, if you think this was a\nmistake feel free to edit the program to bypass this\n")
    exit()

# this will return all the files and directorys (aka folders) in 
# the same directory as the program as a list of strings
files = os.listdir()  # list all the files in the same directory as the program

# try if an argument in the command line was given
try:
    # if its a help argument, give the help info and exit
    if sys.argv[1] == 'help' or sys.argv[1] == '-h':
        print("\nTo specify the name of the backup folder type it after calling the program name")
        print(f"for example:\npython {sys.argv[0]} 'name_of_backup folder'")
        print("If you dont name a backup folder name the program will default to 'backups'\n")
        exit()
    # if we kept going, the argument is the name for the backup folder
    backup_folder = sys.argv[1] 
except:
    # no argument? no problem. default the name of the backup folder
    backup_folder = 'backups'

try:
    os.listdir(backup_folder)  # check if the backup folder exists
except:
    os.mkdir(backup_folder)  # if it doesn't, create it

for file in files[:]:  # files[:] creates a copy using slicing in python
    if not os.path.isdir(file):  # if its not a directory
        # use the linux/unix system command to copy the files over to the backup folder
        os.system(f"cp '{file}' '{backup_folder}/{file}'")
        # os.system is the same as running the command in terminal
    else:  # if it IS a directory, remove it from the list so we know we didnt copy it
        files.remove(file)

with open(f"{backup_folder}/AA_BACKUP_INFO.txt", 'w') as output:  # open the output file in write mode
    # add some stats to the text file for context when this program was last run
    output.write(f'Last backup occurred at {datetime.datetime.now()}\n')
    output.write(f'Number of files copied: {len(files)}\n')
    output.write(f'List of files:\n')
    # I made it two rows so it's kinda fancy
    for i in range(0, len(files), 2):
        try:
            # using files:45 makes the string take up at least 45 characters regardless
            # using files:<45 (adding the less than sign) makes it left-aligned
            output.write(f'\n{files[i]:<45}\t{files[i+1]}')
        except:
            # the first one will try two files but if we are at the end
            # of an odd numbered list of files we only print one
            output.write(f'\n{files[i]:<45}')

# print to terminal what just happened so there's some confirmation
print(f"\n{len(files)} files succsesfully backed up into '{backup_folder}'")

# below I'm using list comprehension in python
# Look it up its super cool! 
hidden_files = [x for x in files if x.startswith(".")]
# adds all items from the files list if it starts with '.'

print(f"{len(hidden_files)} files are hidden with '.'\n")