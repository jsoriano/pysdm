# Source files
pysdmdir = $(pythondir)/pysdm
pysdm_PYTHON = \
	pysdm/__init__.py	\
	pysdm/blkid.py		\
	pysdm/constants.py	\
	pysdm/fstab.py		\
	pysdm/pysdm.py		\
	pysdm/SimpleGladeApp.py	

desktopdir = $(datadir)/applications
desktop_DATA = data/pysdm.desktop

# Glade files
uidir = $(datadir)/pysdm
ui_DATA = data/pysdm.glade

# Filesystem data
fsdatadir = $(datadir)/pysdm/fsdata
fsdata_DATA = data/fsdata/*

bin_SCRIPTS = scripts/pysdm

EXTRA_DIST =	\
	$(bin_SCRIPTS)	\
	$(ui_DATA)	\
	$(desktop_DATA)

#SUBDIRS=po
