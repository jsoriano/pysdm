#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Python module pysdm.py
# Autogenerated from pysdm.glade
# Generated on Wed Aug 31 02:25:13 2005

# Warning: Do not modify any context comment such as #--
# They are required to keep user's code

import os
import gtk
import re

import constants
from options_ui import *
from blkid import *
from fstab import *

from SimpleGladeApp import SimpleGladeApp
from SimpleGladeApp import bindtextdomain

app_name = "pysdm"
app_version = "0.3"

glade_dir = ""
locale_dir = ""

import gettext
gettext.install(app_name)
#bindtextdomain(app_name, locale_dir)

PARTITIONS = "/proc/partitions"
FSTAB = "/etc/fstab"
DEFAULT_MOUNT = "/media"

class Mainwindow(SimpleGladeApp):

    def __init__(self, path = os.path.join (constants.data_dir, "pysdm.glade"),
                 root="mainWindow",
                 domain=app_name, **kwargs):
        path = os.path.join(glade_dir, path)
        SimpleGladeApp.__init__(self, path, root, domain, **kwargs)

    #-- Mainwindow.new {
    def new(self):
	self.main_widget.set_title(_("Storage Device Manager"))
        #Load fstab data
        self.fstab = Fstab(FSTAB)

        self.current_FS = None

        #Initializes partition tree
        ptree = self.get_widget("partitiontree")
        column = gtk.TreeViewColumn(_("Partition List"), gtk.CellRendererText(), text=0)
        ptree.append_column(column)
        self.refresh_partitions(self, None)

        self.get_widget("frame3").set_sensitive(False)
    #-- Mainwindow.new }

    #-- Mainwindow custom methods {
    def refresh_panel(self, partition):
        """
        Update General Information for the partition given

        partition:
            The name of the partition in /dev tree
        """
        filesystem = self.fstab.getFS("/dev/" + partition, None)
        name = re.split('/', filesystem.file)
        name = name[len(name)-1]

        name_entry = self.get_widget("name_entry")
        mountpoint_entry = self.get_widget("mountpoint_entry")
        type_entry = self.get_widget("type_entry")

        self.get_widget("frame3").set_sensitive(True)

        #Root filesystem cannot be modified
        if filesystem.file == "/" or cmp(filesystem.vfstype, "swap")==0:
            self.get_widget("name_entry").set_sensitive(False)
            self.get_widget("openmountpoint").set_sensitive(False)
            self.get_widget("mount_button").set_sensitive(False)
        else:
            self.get_widget("name_entry").set_sensitive(True)
            self.get_widget("openmountpoint").set_sensitive(True)
            self.get_widget("mount_button").set_sensitive(True)

        name_entry.set_text(name)
        mountpoint_entry.set_text(filesystem.file)
        type_entry.set_text(filesystem.vfstype)

        self.get_widget("status_bar").push(0, self.current_FS.spec)

    
    def get_options(self):
        return re.compile(",").split(self.get_widget("options_entry").get_text())

    def set_options(self, options_array):
        options_str = options_array[0]
        for option in options_array[1:]:
            options_str = options_str + "," + option
        self.get_widget("options_entry").set_text(options_str)
        self.current_FS.mntops = options_array


    def auto_configure(self, partition):
        """
        Autoconfirures a new partition

        partition:
            The name of the partition in /dev tree to autoconfigure

        TODO:
            - Detect filesystem and select options for it
        """
        vfstype = get_vfstype("/dev/" + partition)
        self.fstab.addFS(Filesystem("/dev/" + partition, DEFAULT_MOUNT + "/" + partition, vfstype, ["defaults"], "0", "0"))


    def get_partitions(self):
        """
        Find the partitions in the system
        """

        partitions = []
        partitions_file = open(PARTITIONS, "r")
        lines = partitions_file.readlines()
        for line in lines[2:]:
            partition = re.split('\W+', line)[4]
            try:
                os.stat("/dev/" + partition)
                partitions.append(partition)
            except OSError:
                pass
        return partitions
    #-- Mainwindow custom methods }

    #-- Mainwindow.refresh_partitions {
    def refresh_partitions(self, widget, *args):
        """
        Updates partition tree
        """

        ptree = self.get_widget("partitiontree")
        partitions = self.get_partitions()
        model = gtk.TreeStore(str)
        lastdevice = partitions[0]
        iter = model.append(None, (partitions[0],))

        for partition in partitions[1:]:
            device = partition[:len(partition)-1]
            if lastdevice != device:
                lastdevice = partition
                iter = model.append(None, (partition,))
            else:
                if is_mountable("/dev/" + partition):
                    model.append(iter, (partition,))

        ptree.set_model(model) 
    #-- Mainwindow.refresh_partitions }

    #-- Mainwindow.on_partitiontree_cursor_changed {
    def on_partitiontree_cursor_changed(self, widget, *args):
        ptree = self.get_widget("partitiontree")
        selection = ptree.get_selection()
        model, selected = ptree.get_selection().get_selected()

        #User has selected a device
        if len(ptree.get_selection().get_selected_rows()[1][0])==1: 
            return

        partition = model.get_value(selected, 0)

        #If exists a configuration in FSTAB
        if self.fstab.getFS("/dev/" + partition, None) != None:
            self.current_FS = self.fstab.getFS("/dev/" + partition, None)
            self.refresh_panel(partition)
            self.set_options(self.current_FS.mntops)
        else:
            ask_configure = gtk.Dialog(_("Configure now?"), self.main_widget, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
            ask_configure.vbox.pack_start(gtk.Label("\n" + partition + _(" hasn't been configured.\nDo you want to configure it now?\n")))
            ask_configure.show_all()
            result = ask_configure.run()
            ask_configure.destroy()
            if result == gtk.RESPONSE_ACCEPT:
                self.auto_configure(partition)
                self.current_FS = self.fstab.getFS("/dev/" + partition, None)
                self.refresh_panel(partition)
                self.set_options(self.current_FS.mntops)
            else:
                return

    #-- Mainwindow.on_partitiontree_cursor_changed }

    #-- Mainwindow.on_name_entry_changed {
    def on_name_entry_changed(self, widget, *args):
        path = re.split("/", self.current_FS.file)
        npath = ""
        for folder in path[1:len(path)-1]:
            npath = npath + "/" + folder
        
        npath = npath + "/" +  widget.get_text()
        self.get_widget("mountpoint_entry").set_text(npath)
        
        self.current_FS.file = npath
    #-- Mainwindow.on_name_entry_changed }

    #-- Mainwindow.on_openmountpoint_clicked {
    def on_openmountpoint_clicked(self, widget, *args):
        filechooser = gtk.FileChooserDialog(_("Select a file for mountpoint..."), self.main_widget, action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons=(gtk.STOCK_OPEN, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
        filechooser.set_modal(True)
        filechooser.set_current_folder(DEFAULT_MOUNT)
        filechooser.show()
        response = filechooser.run()
        filechooser.hide()
        if response == gtk.RESPONSE_ACCEPT:
            self.get_widget("mountpoint_entry").set_text(filechooser.get_filename())
            self.current_FS.file = filechooser.get_filename()
        
            name = re.split('/', self.current_FS.file)
            name = name[len(name)-1]
            self.get_widget("name_entry").set_text(name)

        filechooser.destroy()
    #-- Mainwindow.on_openmountpoint_clicked }

    #-- Mainwindow.on_options_entry_changed {
    def on_options_entry_changed(self, widget, *args):
        self.current_FS.mntops = self.get_options()
    #-- Mainwindow.on_options_entry_changed }

    #-- Mainwindow.on_defaults_button_clicked {
    def on_defaults_button_clicked(self, widget, *args):
        self.set_options(["defaults"])
    #-- Mainwindow.on_defaults_button_clicked }

    #-- Mainwindow.on_open_options_clicked {
    def on_open_options_clicked(self, widget, *args):
        dialog = option_dialog(self.current_FS.vfstype, title=_("Select options"), flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, buttons=(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
        dialog.set_value(self.current_FS.mntops)
        if dialog.run() == gtk.RESPONSE_ACCEPT:
            self.set_options(dialog.get_value())
        dialog.destroy()
    #-- Mainwindow.on_open_options_clicked }

    #-- Mainwindow.on_mount_button_clicked {
    def on_mount_button_clicked(self, widget, *args):
        try:
            os.makedirs(self.current_FS.file)
        except OSError:
            pass

        mount_ret = self.current_FS.mount()

	if mount_ret==0:
            return
        elif mount_ret==256:
            error_message = _("The file system is busy.\nCan't be remounted with the new location")
        else:
            error_message = _("The file system can't be mounted\nmount returned error:") + str(mount_ret)
        print error_message
	dialog = gtk.Dialog(_("Mount error"), self.main_widget, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
	dialog.vbox.set_border_width(10)
	dialog.vbox.pack_start(gtk.Label(error_message))
        dialog.show_all()
        dialog.run()
        dialog.destroy()

    #-- Mainwindow.on_mount_button_clicked }

    #-- Mainwindow.on_apply_clicked {
    def on_apply_clicked(self, widget, *args):
        os.rename(FSTAB, FSTAB + ".BAK")
        for filesystem in self.fstab.filesystems:
            try:
                os.makedirs(filesystem.file)
            except OSError:
                pass
        self.fstab.toFile(FSTAB)
    #-- Mainwindow.on_apply_clicked }


#-- main {

def main():
    main_window = Mainwindow()

    main_window.run()

if __name__ == "__main__":
    main()

#-- main }
