#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

	fstab.py - Abstraction class for fstab file.

	© Jaime Soriano Pastor <kronoss@kronoss.org>
	
"""

import re



class Filesystem:
	spec = ""
	file = ""
	vfstype = ""
	mntops = []
	freq = ""
	passno = ""

	def __init__(self, spec, file, vfstype, mntops, freq, passno):
		self.spec = spec
		self.file = file
		self.vfstype = vfstype
		self.mntops = mntops
		self.freq = freq
		self.passno = passno

	def toTab(self):
		if len(self.mntops) > 0:
			ops = self.mntops[0]

			for op in self.mntops[1:]:
				ops = ops + "," + op
		else:
			ops = "defaults"
			self.mntops = "defaults"

		return self.spec + "\t" + self.file + "\t" + self.vfstype + "\t" + ops + "\t" + self.freq + "\t" + self.passno

	def __repr__(self):
		return self.toTab()



class Fstab:
	"Abstraction class for fstab file"
	filesystems = []


	def __init__(self, fstab):
		self.fromFile(fstab)


	def addFS(self, fs):
		self.filesystems.append(fs)


	def getFS(self, spec, file):
		i=0
		for fs in self.filesystems:	
			if (fs.spec==spec and (fs.file==file or file==None)) or (fs.file==file and spec==None):
				return fs
			i = i + 1
		return None


	def delFS(self, spec, file):
		i = self.getFS(spec, file)
		if i == None:
			return None
		else:
			deleted = self.filesystems[i]
			del self.filesystems[i]
			return deleted


	def parseFS(self, fs):
		exp = "^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d)\s+(\d)\s+$"
		fields = re.compile(exp).match(fs)
		if fields==None:
			return None
		else:
			fields = fields.groups()
			return Filesystem(fields[0], fields[1], fields[2], re.split(",",fields[3]), fields[4], fields[5]);


	def fromFile(self, fstab):
		fstabfile = file(fstab, "r")
		n = 0

		for line in fstabfile.readlines():
			parsed = self.parseFS(line)
			if parsed != None:
				self.addFS(parsed)

		fstabfile.close()


	def toTab(self):
		ret = ""
		for fs in self.filesystems:
			ret = ret + fs.toTab() + "\n"
		return ret

	def	toFile(self, fstab):
		fstabfile = file(fstab, "w")
		fstabfile.write(self.toTab())
		fstabfile.close()


	def __repr__(self):
		return self.toTab()
