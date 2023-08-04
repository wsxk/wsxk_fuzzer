from . import globs 
from .arch import x32,x64,arm,arm64
import sys
def config_unicorn():
    if 'arch' not in globs.config_file_info:
        print("Label `arch` is needed in config file!")
        sys.exit(1)
    arch = globs.config_file_info['arch']
    if arch == 'x32':
        x32.config_unicorn_x32()
    if arch == 'x64':
        x64.config_unicorn_x64()
    if arch == 'arm':
        arm.config_unicorn_arm()
    if arch == 'arm64':
        arm64.config_unicorn_arm64()
    return