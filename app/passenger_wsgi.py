# File: passenger_wsgi.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-01-15
import sys, os
virt_binary = "/home/cirrused/public_html/notifier/venv/bin/python"
open('test_log.txt', 'w')
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())
import app as application