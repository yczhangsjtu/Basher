#!/usr/bin/python

import os
import subprocess
import logging
import datetime

RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m'

class Filter:
  def filter(self, record):
    return record.levelno == logging.INFO

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ihandler = logging.StreamHandler()
ihandler.setLevel(logging.INFO)
ihandler.addFilter(Filter())
ihandler.setFormatter(logging.Formatter('[%(asctime)s] {}%(message)s{}'.format(GREEN, NC)))
logger.addHandler(ihandler)

whandler = logging.StreamHandler()
whandler.setLevel(logging.WARNING)
whandler.setFormatter(logging.Formatter('[%(asctime)s] {}%(message)s{}'.format(RED, NC)))
logger.addHandler(whandler)

fhandler = logging.FileHandler('test/result.%s' % datetime.datetime.now().strftime('%Y-%m-%d.%H:%M:%S'))
fhandler.setLevel(logging.DEBUG)
fhandler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(fhandler)

npass, nfail = 0, 0
original_workdir = os.getcwd()
for dirname, subdirs, filenames in os.walk('scripts'):
  for filename in filenames:
    if filename.endswith('_test'):
      os.chdir(original_workdir + '/' + dirname)
      p = subprocess.Popen('./%s' % filename)
      stdout, stderr = p.communicate()
      if p.returncode:
        logger.warning('%s: FAIL' % filename)
        logger.debug('stdout = [%s], stderr = [%s]' % (stdout, stderr))
        nfail += 1
      else:
        logger.info('%s: PASS' % filename)
        npass += 1
      os.chdir(original_workdir)

logger.info("Test result: %d PASS, %d FAIL" % (npass, nfail))
