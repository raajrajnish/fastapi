### FastAPI --> https://fastapi.tiangolo.com/
Modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.FastAPI is a modern API framework that relies heavily on type hints for its capabilities.

### Install FastAPI
    pip install fastapi uvicorn[standard]

### Python type hints --> https://docs.python.org/3/library/typing.html
Python type hints provides runtime support for type hints,The most fundamental support consists of the types Any, Union, Tuple,Callable, TypeVar, and Generic.
    
    def greeting(name: str) -> str:
        return 'Hello ' + name
    
    where name is of type string and return type of greeting is string

Python is a dynamically typed language, hence variable's type is checked at run-time. Python's type hinting
system nudges Python towards static typing, but as the name states, these are merely type hints and not type declarations.

## Generating github token
    go to this url : https://github.com/settings/tokens to generate token or edit token
