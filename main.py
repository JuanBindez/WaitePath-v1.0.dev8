# this is part of the WaitePath project.
#
# Release: v1.0-dev
#
# Copyright (c) 2022-2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import os
import base64
import io

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

"""site to encode images in base64 https://base64.guru/converter/encode/image"""


window = Tk()
window.title("WaitePath v1.0-dev")
window.geometry("1200x650")
window.resizable(True, True)# False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
window['background'] = '#373636'
#foto_icon = PhotoImage(data=base64.b64decode(ICON_LOGO))
#window.iconphoto(True, foto_icon)
image_data = base64.b64decode(image_base64)
img = PhotoImage(data=image_data)


background_label = Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)







if __name__ == "__main__":
    window.mainloop()