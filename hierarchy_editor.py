bl_info = {    
    "name"         : "Hierarchy Editor",
    "author"       : "Tamir Lousky",
    "version"      : (1, 0, 0),
    "blender"      : (2, 67, 0),
    "category"     : "Node",
    "wiki_url"     : "https://github.com/Tlousky/blender-hierarchy-editor/wiki",
    "download_url" : "https://github.com/Tlousky/blender-hierarchy-editor",
    "description"  : "View and edit parenting relationships with nodes"
    }

import bpy
from bpy_types import NodeTree, Node, NodeSocket

class HierarchyEditor( NodeTree ):
    # Description string
    '''A node tree meant to enable editing object and armature bone parenting 
       and constraints via nodes'''

    bl_idname = 'HierarchyEditorType'
    bl_label = 'Hierarchy Editor' # Label for nice name display
    bl_icon = 'NODETREE'          # Icon identifier
    

# Parent socket type
class ParentSocket( NodeSocket ):
    '''Basic parent socket'''
    bl_idname = 'ParentSocketType'
    bl_label  = 'Parent Node Socket'

    Parent = bpy.props.StringProperty(
        name        = "parent", 
        description = "object parent",
        update      = update_parent
    )

    def update_parent( self, context ):
        '''This function is called when the parent changes. it changes the
           object's parent to match the node inserted into it'''
        
            self.links
            # use the nodetree's links collection to find the node linked to
            # the this socket, and change the object's parent accordingly
        
        return None

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_linked:
            layout.label( text )
        else:
            layout.prop( self, "Parent", text = text )

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)
        
# Basic hierarchy node class. Defines a poll function to enable instantiation.
class BasicHierarchyTreeNode :
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'HierarchyEditorType'
        

