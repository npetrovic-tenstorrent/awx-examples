import subprocess
import os

output_stream = os.popen('ls -al')
output_stream.read()


