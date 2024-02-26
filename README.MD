# PyLuaLinker

A python utility for linking LUA source files into one LUA file.

> currently no builds available, to use download and initialize using pipenv

## How-To:

### setting up a new project:

Run:

`main.py new [path]`

to initialize a new project at [path].  
The result should look like this:

```
[path]/   
├── src   
└── buildscript.json
```

**buildscript.json** defines your application name, entry point and any source directories.

```
{  
     "app_name": "",   
     "entry_point": "",  
     "src_dir": []  
}  
```
|        key          |                description:                  |
|--------------------:|----------------------------------------------|
|```"app_name":```    | is the name of the file created by the linker|
|```"entry_point":``` | is the name of your main source file         |
|```"src_dir":```     | is a list of paths (absolute or relative) to all required LUA source files|

for an example look at [the example implementation](https://github.com/Ubus99/PyLuaLinker/tree/30b7094eda02b48246ca1661aca9f709e919d81f/tests/project)

### building a project:

To link your project enter

> main.py build [buildscript.json]

## Contributing;

This repository is open for issues and merge requests, but since I made this on a whim, I might drop support at any time.    
If I ever stop responding, remember that all code written for this project is licensed [GPLv3](https://www.gnu.org/licenses/gpl-3.0.de.html), so you can always copy it and make changes for yourself.
