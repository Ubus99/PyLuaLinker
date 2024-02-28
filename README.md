# PyLuaLinker

A python utility for linking LUA source files into one LUA file.

To install run `pip install PyLuaLinker`

## How-To:

### setting up a new project:

Run:

`PyLuaLinker new [path]`

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
     "src_dir": [""]  
}  
```
|        key          |                description:                  |
|--------------------:|----------------------------------------------|
|```"app_name":```    | is the name of the file created by the linker|
|```"entry_point":``` | is the name of your main source file         |
|```"src_dir":```     | is a list of paths (absolute or relative) to all required LUA source files|

for an example look at [the linker test project](https://github.com/Ubus99/PyLuaLinker/tree/30b7094eda02b48246ca1661aca9f709e919d81f/tests/project)

### marking import statements

To mark a `require()` statement for static linking, comment `--> static` in the same line.   
Other types of import statement are currently not supported.   

This allows for hybrid static / dynamic importing and for your source program to be either run conventionally or linked without modification.

### building a project:

To link your project enter

`PyLuaLinker build [buildscript.json]`

## Contributing;

This repository is open for issues and merge requests, but since I made this on a whim, I might drop support at any time.    
If I ever stop responding, remember that all code written for this project is licensed [GPLv3](https://www.gnu.org/licenses/gpl-3.0.de.html), so you can always copy it and make changes for yourself.
