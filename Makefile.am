# Source files
pysdmdir = $(pythondir)/pysdm
pysdm_PYTHON = \
	pysdm/__init__.py	\
	pysdm/blkid.py		\
	pysdm/constants.py	\
	pysdm/fstab.py		\
	pysdm/options_ui.py	\
	pysdm/pysdm.py		\
	pysdm/SimpleGladeApp.py	\
	pysdm/fsdata/*

desktopdir = $(datadir)/applications
desktop_DATA = data/pysdm.desktop

# Glade files
uidir = $(datadir)/pysdm
ui_DATA = data/pysdm.glade

bin_SCRIPTS = scripts/pysdm

EXTRA_DIST =	\
	$(bin_SCRIPTS)	\
	$(ui_DATA)	\
	$(desktop_DATA)

#SUBDIRS=po
