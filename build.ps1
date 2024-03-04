py -m pip install build --upgrade
py -m build $PSScriptRoot

# deactivate

py -m pip install $PSScriptRoot\dist\pylualinker-0.1.0-py3-none-any.whl --force-reinstall
PyLuaLinker -h