from cx_Freeze import *

includefiles = ["icon.ico",'icons2']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Smart Note Pad",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\SmartNotePad.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Smart Note Pad1",
    author="Rahul Mishra",
    name="Smart Note Pad1",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="SmartNotePad.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
