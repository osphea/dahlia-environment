# Camden Bruce
import os
import time

ans = input ('''
ENV INSTALLER
=====================================

this will install the DahliaOS development environment

=====================================

Environment Includes

* pangolin-desktop

* armadillo

* appaddon.py (lets you add new apps to pangolin

y/n?: ''')

if ans == 'y':
    print('make sure wget and git is installed')
    time.sleep(3)
    os.system("wget https://raw.githubusercontent.com/dahlia-os/dahlia-environment/master/appaddon.py")
    os.system("git clone https://github.com/dahlia-os/pangolin-desktop.git")
    os.system("git clone https://github.com/dahlia-os/armadillo.git")
