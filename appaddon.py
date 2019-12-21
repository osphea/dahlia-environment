# Camden Bruce
import os
import time

ans = input ('''
start setup

y/n?: ''')

if ans == 'y':
    print('.dart and .json names will be nammed app you can change this later')
    print('make sure nano is installed')
    time.sleep('3')
    print('enter code for app.dart')
    time.sleep('3')
    os.system("nano pangolin-desktop/lib/applications/app.dart")
    time.sleep('3')
    print('enter application details in application.json')
    os.system("nano pangolin-desktop/lib/application.json")
    time.sleep('3')
    print('enter code in window_space.dart')
    time.sleep('3')
    os.system("nano pangolin-desktop/lib/window_space.dart")
    time.sleep('3')
    print('setup done, ready for apk build')
