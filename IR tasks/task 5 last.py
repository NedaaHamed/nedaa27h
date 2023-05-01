from binarytree import build, Node
def remove_node(root, value):
    if root is None:
        return None
    if root.value == value:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min = searchmin(root.right)
            root.value = min.value
            root.right = remove_node(root.right, min.value)
    elif value < root.value:
        root.left = remove_node(root.left, value)
    else:
        root.right = remove_node(root.right, value)
    return root

def searchmin(root):
    while root.left is not None:
        root = root.left
    return root
# construct a binary tree for a list of integers
data = [4, 2, 6, 1, 3, 5, 7]
root = build(data)

while True:
    print("Current tree: ")
    print(root)
    choice = input("Enter 1 to add a new element or 2 to delete an element: ")
    
    if choice == '1':
        # ask the user for the value of the new element
        val = int(input("Enter the value of the new element: "))
        node = Node(val)
        if root is None:
            root = node
        else:
            curr = root
            while True:
                if val < curr.value:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    elif choice == '2':
        value = int(input("Enter the value of the element to be deleted: "))
        root = remove_node(root, value)
    else:
        print("Invalid choice. Please try again.")