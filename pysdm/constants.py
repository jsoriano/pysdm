# Copyright (C) 2004 Tiago Cogumbreiro <cogumbreiro@users.sf.net>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#
# Authors: Tiago Cogumbreiro <cogumbreiro@users.sf.net>
#
#	Modified by Jaime Soriano Pastor <kronoss@kronoss.org>
#		- Adapted for PySDM

# Get utility functions
from os.path import join, abspath
import sys

application = "pysdm"

# Discover the data dir
root_dir = join(__file__, 
			'..',
			'..',         
			'..')         
root_dir = abspath (root_dir)

data_dir = join (root_dir, 'share', application)
bin_dir = join (root_dir, 'bin')
