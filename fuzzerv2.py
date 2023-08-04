from unicorn import *
from unicornafl import *
from module.config import config_unicorn
from module import globs
import yaml
import os


# CONFIG FILE NAME
CONFIG_FILE = 'target.yml'
def get_config_file_path():
    current_file_path = os.path.realpath(__file__)
    config_file_dir = os.path.dirname(current_file_path)
    config_file_path = os.path.join(config_file_dir,CONFIG_FILE)
    print("Config file path: {}".format(config_file_path))
    return config_file_path

def main():
    # step 1 : read config_file
    config_file_path = get_config_file_path()
    with open(config_file_path,'rb') as f:
        file = yaml.load(f,Loader=yaml.FullLoader)
        globs.config_file_info = file
    for v,k in file.items():
        print(v,k)

    # step 2 : config unicorn engine
    config_unicorn()

    # step 3 : set fuzz_input_callback & end_address 
    def place_input_callback(uc, input, persistent_round, data):
        print("fuzz input data: {}".format(input[0:4]))
        globs.fuzz_input = input
    end_address = []
    if 'end_address' in globs.config_file_info:
        end_address = globs.config_file_info['end_address']
        print("end_address: {}".format(end_address))
    uc_afl_fuzz(globs.uc,"wsxk_fuzzer",place_input_callback,end_address)
    return 

if __name__ == "__main__":
    main()