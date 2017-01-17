# File: passenger_wsgi.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-01-16
import sys, os
virt_binary = "/home/cirrused/public_html/notifier/venv/bin/python"
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())
from app.app import app as application