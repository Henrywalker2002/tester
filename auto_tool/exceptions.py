class InvalidCommandException(Exception):
    def __init__(self, command):
        self.message = f"Invalid command: {command}"
        self.command = command 
        

class AssertException(Exception):
    def __init__(self, command, target , value):
        self.message = f"Assert failed: {target} {value}"
        self.command = command
        self.target = target
        self.value = value
    
    def __str__(self) -> str:
        return self.message


class InvalidTargetException(Exception):
    def __init__(self, target):
        self.message = f"Invalid target: {target}"
        self.target = target


class InvalidKeyChoicesException(Exception):
    def __init__(self, key):
        self.message = f"Invalid key: {key}"
        self.key = key


class InvalidValueChoicesException(Exception):
    def __init__(self, value):
        self.message = f"Invalid value: {value}"
        self.value = value