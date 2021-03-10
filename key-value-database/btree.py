import bisect

class Node:

    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children)

    def set_children(self, children):
        self.children = children or []
        for child in self.children:
            child.parent = self

    def is_leaf(self):
        return len(self.children) == 0

    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None

    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index

    def split(self):
        if self.parent is None:
            return self.split_no_parent()
        return self.split_with_parent()

    def split_no_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        # Create right node
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        # Update left node (self)
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        # Create parent
        parent = Node([key_to_move_up], [value_to_move_up], [self, right_node])
        return parent

    def insert_child(self, insert_index, child): 
        self.children.insert(insert_index, child)
        child.parent = self

    def split_with_parent(self): 
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        # Create right node
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        # Update left node (self)
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        # Add new child to parent
        key_insert_index = self.parent.insert_entry(key_to_move_up, value_to_move_up)
        self.parent.insert_child(key_insert_index + 1, right_node)
        return self.parent

    def __len__(self):
        return len(self.values)


class BTree:

    def __init__(self, split_threshold):
        self.root = Node()
        self.split_threshold = split_threshold 
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return False
        return True
    
    def _add(self, current_node, key, value):
        if current_node.is_leaf(): 
            current_node.insert_entry(key, value) 
        else:
            child_index = current_node.get_insert_index(key) 
            self._add(current_node.children[child_index], key, value)
        if len(current_node) > self.split_threshold: 
            parent = current_node.split()  
            if current_node == self.root: 
                self.root = parent
                self.height += 1
                
    def add(self, key, value):
        self._add(self.root, key, value)
        self.size += 1
        
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)

