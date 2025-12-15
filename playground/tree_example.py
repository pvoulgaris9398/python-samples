# https://treelib.readthedocs.io/en/latest/#
from treelib import Tree


def main():
    tree = Tree()
    tree.create_node("Root", "root")
    tree.create_node("Left Child", "left", parent="root")
    tree.create_node("Right Child", "right", parent="root")

    tree.create_node("Left Grandchild", "left_grand", "left")
    tree.create_node("Right Grandchild", "right_grand", "right")

    # print("Tree Structure:")
    # tree.show()

    for node in tree.all_nodes():
        print(node.tag)

    tree.show(line_type="ascii")


if __name__ == "__main__":
    main()
