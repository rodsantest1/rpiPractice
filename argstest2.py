#!/usr/bin/env python

# The shebang line above allows us to run like this:
# ./argstest2.py
# chmod +x argstest2.py
# https://youtu.be/7tYEsT2dzlo 

import sys

# Shell commands  
# %Run  
# %Debug argstest2.py Rodney

print("Arguments ", sys.argv, " ", len(sys.argv))

if len(sys.argv) >= 2:
    print("Greater than 1")
else:
    print("Less than 1")
    
