# ENTER FILENAMES THROUGH CONSOLE

import zipfile

# Test a block of code for errors
try:
    # Open zip-file and compress test.txt
    newZip = zipfile.ZipFile('zipname.zip', 'w')
    newZip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
# Handle the error
except Exception as e:
    print(e)

# Close the file
newZip.close()