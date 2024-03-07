import os
try:
  import scratchattach as scratch3
except:
  os.system("pip install -U scratchattach")
  import scratchattach as scratch3

session = scratch3.login("username", "password")

#list of commands: https://github.com/TimMcCool/scratchattach/wiki/#cloud-variables
