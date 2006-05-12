# -*- coding: utf-8 -*-

"""

	blkid.py - Functions that make use of blkid

	© Jaime Soriano Pastor <kronoss@kronoss.org>
	
"""

import re
import os

BLKID_BIN = "/sbin/blkid"
BLKID_CACHE = "/etc/blkid.tab"


def is_mountable(device):
	"""
	Uses blkid to check if the given partition is mountable
		device: the partition to check
	"""
	os.system(BLKID_BIN + " -c /dev/null >> /dev/null")
	return os.system(BLKID_BIN + " | grep " + device + " >> /dev/null")==0


def get_vfstype(device):
	"""
	Returns the filesystem type for the given device
		device: the device
	"""

	os.system(BLKID_BIN + " -c /dev/null >> /dev/null")
	#cache = file("/etc/blkid.tab")
	cache = os.popen(BLKID_BIN + " -c /dev/null " + device)
	filesystem = cache.readline()
	if filesystem == None: return "auto"
	cache.close()
	return re.compile(".+TYPE=\"(\w+)\".+").match(filesystem).groups()[0]
