from .. import globs
from unicorn import *
from unicorn.x86_const import *
import sys
def config_unicorn_x64():
    # step 1: set arch
    uc = Uc(UC_ARCH_X86,UC_MODE_64)
    # step 2: set sp/pc
    if 'pc' not in globs.config_file_info:
        print("Label `pc` is needed in config file!")
        sys.exit(1)
    if 'initial_sp' not in globs.config_file_info:
        print("Label `initial_sp` is needed in config file!")
        sys.exit(1) 
    uc.reg_write(UC_X86_REG_RIP,globs.config_file_info['pc'])
    uc.reg_write(UC_X86_REG_RSP,globs.config_file_info['initial_sp'])
    # step 3: set mmap

    # setp 4: set handlers
    return