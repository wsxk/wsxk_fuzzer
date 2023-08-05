from . import globs
from unicorn import *
from unicorn.x86_const import *
from typing import Optional
import sys
import importlib

def set_memory_map(uc: Optional[Uc]):
    for name,region in globs.config_file_info["memory_map"].items():
        prot = UC_PROT_NONE
        if 'permissions' not in region:
            prot = UC_PROT_ALL
        else: 
            if 'r' in region['permissions']:
                prot |= UC_PROT_READ
            if 'w' in region['permissions']:
                prot |= UC_PROT_WRITE
            if 'x' in region['permissions']:
                prot |= UC_PROT_EXEC
        print("Mmap {} at baseaddr:{},size:{},permissions:{}".format(name,region['base_addr'],region['size'],prot))
        uc.mem_map(region['base_addr'],region['size'],prot)
        if 'file_path' in region:
            if 'file_size' not in region:
                print("Label `file_size` is needed in config file!")
                sys.exit(1)
            file_size = region['file_size']
            file_offset = 0
            load_offset = 0
            with open(region['file_path'],'rb') as fp:
                fp.seek(file_offset)
                region_data = fp.read(file_size)
                uc.mem_write(region['base_addr']+load_offset,region_data)
            print("Loading {} bytes in file {} at {}".format(file_size,region['file_path'],region['base_addr']+load_offset))
    return

def set_handlers(uc: Optional[Uc]):
    handlers = globs.config_file_info['handlers']
    print("handlers:")
    print(handlers)
    for name,config in handlers.items():
        handler = config['handler']
        mod_name, func_name = handler.rsplit('.', 1)
        module = importlib.import_module(mod_name)
        
        func_obj = getattr(module,func_name)
        hook_addr = config['addr']
        print("Hook addr: {} with {} {}".format(hex(hook_addr),mod_name,func_name))
        uc.hook_add(UC_HOOK_CODE,func_obj,begin=hook_addr,end=hook_addr)
    return

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
    if 'memory_map' not in globs.config_file_info:
        print("Label `memory_map` is needed in config file!")
        sys.exit(1)
    for name,region in globs.config_file_info['memory_map'].items():
        print(name,region)
    set_memory_map(uc)
    
    # setp 4: set handlers
    if 'handlers' in globs.config_file_info:
        print("handlers detected... set handlers...")
        set_handlers(uc)
    else:
        print("No handlers detected.... that's ok")
    globs.uc = uc
    return

def test_handlers():
    module = importlib.import_module("handlers.generic")
    func_obj = getattr(module, "test")
    func_obj()

if __name__ == "__main__":
    test_handlers()