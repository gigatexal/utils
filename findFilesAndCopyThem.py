import os
import shutil

# globals
output_dir_toplevel = '<dest>'

extension_folder_mapping = {'.mp4':output_dir_toplevel + '/' + 'movies',
                            '.mkv':output_dir_toplevel + '/' + 'movies',
                            '.flv':output_dir_toplevel + '/' + 'movies',
                            '.m4v':output_dir_toplevel + '/' + 'movies',
                            '.qt':output_dir_toplevel + '/' + 'movies',
                            '.avi':output_dir_toplevel + '/' + 'movies'
                           }

def files(path=None):
   if path is not None:
      yield from (os.path.join(dir, file) for dir, subdir, files in os.walk(path) for file in files)
   return None

def filter_files_by_extension(path = None, extension={}):
   f = files(path)
   yield from (file for file in f if os.path.splitext(file)[1] in extension.keys())       

def file_copy(file=None):
   destination = extension_folder_mapping[os.path.splitext(file)[1]]
   os.makedirs(name=destination, exist_ok=True)
   try:
      shutil.copy(file, destination)
   except:
      return (file, destination + '/' + file, 'Failure')
   return (file, destination + '/' + file, 'Success')

f = filter_files_by_extension(path = '/<source>/', extension = extension_folder_mapping)

files_copied = list(map(file_copy, f))
print(files_copied)
