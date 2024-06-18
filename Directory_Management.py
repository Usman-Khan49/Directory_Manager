import os
import pathlib
import shutil


directory_path = 'F:/'

os.chdir(directory_path)
if os.path.exists(directory_path):
    print('Current Working Directory: ', os.getcwd())
else:
    print('No Such Directory Was Found')


file_extensions = {
    # Images
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "tiff": "Images",
    "svg": "Images",
    "heic": "Images",
    
    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "rtf": "Documents",
    "odt": "Documents",
    "epub": "Documents",
    "mobi": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    
    # Audio
    "mp3": "Audio",
    "wav": "Audio",
    "aac": "Audio",
    "flac": "Audio",
    "ogg": "Audio",
    "m4a": "Audio",
    "wma": "Audio",
    
    # Video
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "flv": "Videos",
    "wmv": "Videos",
    "m4v": "Videos",
    
    # Archives
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    "bz2": "Archives",
    
    # Executables
    "exe": "Executables",
    "bat": "Executables",
    "sh": "Executables",
    "msi": "Executables",
    "app": "Executables",
    
    # Code
    "py": "Code",
    "java": "Code",
    "c": "Code",
    "cpp": "Code",
    "cs": "Code",
    "js": "Code",
    "html": "Code",
    "css": "Code",
    "php": "Code",
    "rb": "Code",
    "go": "Code",
    "rs": "Code",
    "swift": "Code",
    "sql": "Code",
    "xml": "Code",
    "json": "Code",
    "yml": "Code",
    "yaml": "Code",
    
    # Fonts
    "ttf": "Fonts",
    "otf": "Fonts",
    "woff": "Fonts",
    "woff2": "Fonts",
    
    # System
    "sys": "System",
    "dll": "System",
    "ini": "System",
    "cfg": "System",
    "log": "Logs",
    
    # Others
    "iso": "Disk Images",
    "dmg": "Disk Images",
    "ics": "Calendar",
    "vcf": "Contacts",
    "bak": "Backups",
    "torrent": "Torrents",
    "apk": "Mobile Apps",
    "ipa": "Mobile Apps"
}
others_dir = "Others"
if not os.path.exists(others_dir):
    os.mkdir(others_dir)

# Iterating through files     
for file in os.listdir(os.getcwd()): 
    if os.path.isfile(file):  # Ensure we're processing only files
        file_extension = pathlib.Path(file).suffix.strip('.').lower()
        target_folder = file_extensions.get(file_extension, others_dir)
        
        # Ensure the target folder exists
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        
        # Move the file to the target folder
        newpath = os.path.join(target_folder, file)
        shutil.move(file, newpath)
        print(f"Moved file {file} to {target_folder}")
    else:
        print(f"Skipping directory: {file}")

    
    
            
        
            