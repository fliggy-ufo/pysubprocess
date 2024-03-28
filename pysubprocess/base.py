'''Base class for all commands.'''
from copy import deepcopy
import os
import subprocess

class PysubprocessError(Exception):
    pass

class Base:
    def __router(self, invoke_func_name: str, *args, **kwargs):
        try:
            method = getattr(self, invoke_func_name)
            if callable(method):
                return method(*args, **vars(args))
            else:
                raise AttributeError(f"'{invoke_func_name}' command is '\
                                     'not found in '{self.__class__.__name__}' class.")
        except AttributeError as e:
            print(str(e))

class PopenExtra:
    def __init__(self):
        self.origin_popen = None
        self.stdout_data = None
        self.stderr_data = None
        self.success = None

def shell(command) -> 'PopenExtra':
    try:
        popen_extra = PopenExtra()
        copied_envs = deepcopy(os.environ)
        popen_extra.origin_popen = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE, universal_newlines=True, env=copied_envs)
        popen_extra.stdout_data, popen_extra.stderr_data = popen_extra.origin_popen.communicate()
        popen_extra.success = popen_extra.origin_popen.returncode == 0
    except subprocess.CalledProcessError:
        popen_extra.success = False

    return popen_extra
