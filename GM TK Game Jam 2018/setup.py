from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Jogo.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Fantasminha CaArmada",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
