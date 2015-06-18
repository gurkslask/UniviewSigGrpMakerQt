from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('main.py', 'Win32GUI')
]

setup(name='UniViewSigGrpMakerQt',
      version = '0.1',
      description = 'Qt application for making Signal groups for Uniview',
      options = dict(build_exe = buildOptions),
      executables = executables)
