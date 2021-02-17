#!c:\python_goit\sorting-files-in-a-folder\lesson_7\myvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'clean-folder','console_scripts','clean-folder'
__requires__ = 'clean-folder'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('clean-folder', 'console_scripts', 'clean-folder')()
    )
