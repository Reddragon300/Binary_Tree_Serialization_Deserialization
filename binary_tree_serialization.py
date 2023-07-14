# Write a function to serialize and deserialize a binary tree into a string representation.

# Define the Binary Tree Node class:

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # Implement the serialize function:


def serialize(root):
    if root is None:
        return "None"  # Representing an empty node as "None"

    # Preorder traversal: Root -> Left -> Right
    left_subtree = serialize(root.left)
    right_subtree = serialize(root.right)

    # Print the current node's value during serialization
    print("Serializing node with value:", root.value)

    return str(root.value) + "," + left_subtree + "," + right_subtree


# Implement the deserialize function:


def deserialize(data):
    def build_tree(nodes):
        # Get the next node value from the list
        value = nodes.pop(0)
        if value == "None":
            return None

        # Create a new node with the current value
        node = TreeNode(int(value))

        # Print the current node's value during deserialization
        print("Deserializing node with value:", node.value)

        # Recursively build left and right subtrees
        node.left = build_tree(nodes)
        node.right = build_tree(nodes)

        return node

    # Split the string representation into a list of node values
    nodes = data.split(",")
    return build_tree(nodes)

# Testing the implementation:


# Create a binary tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Serialize the tree
serialized = serialize(root)
print("Serialized tree:", serialized)
print()

# Deserialize the tree
deserialized = deserialize(serialized)
print("Deserialized tree:", deserialized)
