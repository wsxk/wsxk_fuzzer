from unicorn import *
from unicorn.x86_const import *
from .. import globs
import os

def test():
    print("test")

def malloc(uc, address, size, user_data):
    uc.reg_write(UC_X86_REG_RAX, 0x00201000)
    uc.reg_write(UC_X86_REG_RIP,address+size)

def scanf(uc, address, size, user_data):
    uc.mem_write(0x201000, globs.fuzz_input)
    uc.reg_write(UC_X86_REG_RIP,address+size)

def printf(uc, address, size, user_data):
    uc.reg_write(UC_X86_REG_RIP,address+size)

def puts(uc, address, size, user_data):
    uc.reg_write(UC_X86_REG_RIP,address+size)
    data=uc.mem_read(0x00201000,30)
    length = 0
    for i in range(len(data)):
        if(data[i]!=0):
            length+=1
            continue
        break
    if length>20:
        os.abort()