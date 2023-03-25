import os
import shlex
import subprocess

PORT = 5000

if __name__ == '__main__':
    p = subprocess.run(shlex.split(f'python server.py'))
    if p.returncode != 0:
        pid = subprocess.run(shlex.split(f'lsof -i :{PORT}'), stdout=subprocess.PIPE).stdout.decode().split('\n')[1].split()[1]
        os.kill(int(pid), 15)
        subprocess.run(shlex.split(f'python server.py'))
