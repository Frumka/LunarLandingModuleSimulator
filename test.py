'''
from System.Diagnostics import Process
p = Process()
p.StartInfo.UseShellExecute = False
p.StartInfo.RedirectStandardOutput = True
p.StartInfo.FileName = 'python'
p.StartInfo.Arguments = 'C:\\Users\\Petr\\Desktop\\test_joy2.py'
print (p.Start())
p.WaitForExit() 
print (p.StandardOutput.ReadToEnd())

import subprocess
#subprocess.check_output(["ls", "-l", "/dev/null"])
'''
def f(x):
    print (x)

import sys
import System
from System.Diagnostics import *
from System.IO import *
from System.Diagnostics import Process
import time
p = Process()
p.StartInfo.RedirectStandardOutput = True
p.StartInfo.RedirectStandardError = True
p.StartInfo.UseShellExecute  = False
p.StartInfo.CreateNoWindow = True
p.StartInfo.FileName = 'C:\\Users\\Petr\\Desktop\\a.exe'
#p.StartInfo.Arguments = 'C:\\Users\\Petr\\Desktop\\test_joy2.py'
#p.OutputDataReceived += f
p.Start()
p.WaitForExit()
print p.StandardOutput.ReadToEnd()