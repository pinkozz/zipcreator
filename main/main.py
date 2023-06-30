# ENTER FILENAMES THROUGH CONSOLE

import zipfile

newZip = zipfile.ZipFile('YOUR_ZIP_FILENAME.zip', 'w')
newZip.write('test', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()