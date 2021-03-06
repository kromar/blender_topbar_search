# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "Header Search",
    "description": "Search button for header",
    "author": "Daniel Grauer",
    "version": (1, 0, 4),
    "blender": (2, 82, 0),
    "location": "Header",
    "category": "System"
    "wiki_url": "https://github.com/kromar/blender_topbar_search"

}


def draw_search(self, context):
    if context.region.alignment != 'RIGHT':
        layout = self.layout
        layout.operator(operator="wm.search_menu", text="", icon='VIEWZOOM', emboss=True)


def register():
    bpy.types.VIEW3D_HT_tool_header.append(draw_search)


def unregister():
    bpy.types.VIEW3D_HT_tool_header.remove(draw_search)


if __name__ == "__main__":
    register()
