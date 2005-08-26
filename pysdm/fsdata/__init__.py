options = {}
defaults = {}

import default
options["default"] = default.options
defaults["default"] = default.defaults

import ext2
options["ext2"] = ext2.options
defaults["ext2"] = ext2.defaults

import ext3
options["ext3"] = ext3.options
defaults["ext3"] = ext3.defaults

import ntfs
options["ntfs"] = ntfs.options
defaults["ntfs"] = ntfs.defaults

import reiserfs
options["reiserfs"] = reiserfs.options
defaults["reiserfs"] = reiserfs.defaults

import swap
options["swap"] = swap.options
defaults["swap"] = swap.defaults

import xfs
options["xfs"] = xfs.options
defaults["xfs"] = xfs.defaults
