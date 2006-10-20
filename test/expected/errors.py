# Generated from the Telepathy spec
"""\
    Copyright (C) 2006 Collabora Limited
  
    This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
  
"""

from dbus import DBusException


class MiscError(DBusException):
    """\
      Raised whenever appropriate.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.SpecAutoGenTest.MiscError'
  
class OtherError(DBusException):
    """\
      Raised at all other times.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.SpecAutoGenTest.OtherError'
  