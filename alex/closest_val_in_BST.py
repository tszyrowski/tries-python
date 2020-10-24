'''
Find func that takes in a Binary Search Tree and target integer value
return closes value to that target contained in the BST
Assumptions:
    - single closest value

Binary Search Tree, is a node-based binary tree data structure
    which has the following properties:

    - The left subtree of a node contains only nodes
      with keys lesser than the node s key.
    - The right subtree of a node contains only nodes
      with keys greater than the node s key.
    - The left and right subtree each must also be a binary search tree.
    - There must be no duplicate nodes.

'''
import json

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#------------------------------------------------------------------------------ 
def get_dict_by_id(dict_list, dict_id):
    """find dict where id is a value"""
    for iner_dict in dict_list:
        try:
            if iner_dict["id"] == dict_id:
                d = iner_dict
                return d
        except TypeError as e:
            print(dict_id, dict_list, e)
    return None
#     return next(
#         (iner_dict for iner_dict in dict_list if iner_dict["id"] == dict_id),
#         None
#     )

def find_closest_value_in_Bst_1(tree, target):
    """ Avarage: O(log(n)) time | O(log(N) space
        Worst: O(n) time | O(n) space
    """
    closest = find_closest_value_in_Bst_helper_1(
        tree,
        get_dict_by_id(tree["tree"]["nodes"], tree["tree"]["root"]),
        target,
        float("inf"))
    return closest

def find_closest_value_in_Bst_helper_1(tree_list, inner_tree, target, closest):
    """Find closest value with search dict by id"""
    if inner_tree is None:  # we finish if there is no more node left 
        return closest
    if abs(target - closest) > abs(target - inner_tree["value"]):
        closest = inner_tree["value"]  # update if the current clossest is further than the value
    if target < inner_tree["value"]:  # if this is less we want to return the method with left branch
        return find_closest_value_in_Bst_helper_1(
            get_dict_by_id(tree_list["tree"]["nodes"], inner_tree["left"]),
            target,
            closest)
    elif target > inner_tree["value"]:
        return find_closest_value_in_Bst_helper_1(
            get_dict_by_id(tree_list["tree"]["nodes"], inner_tree["right"]),
            target,
            closest)
    else:  # if the target is equal (netier less nor more) return closest
        return closest
#------------------------------------------------------------------------------ 
def find_closest_value_in_Bst_2(tree, target):
    closest = find_closest_value_in_Bst_helper_2(tree, target, tree.value)
    return closest

def find_closest_value_in_Bst_helper_2(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest

def find_closest_value_in_Bst_3(tree, target):
    """Not finished."""
    closest = float("inf")
    node_id = tree["root"]
    current_node = tree["nodes"]["id"]
    for node in tree["nodes"]: pass

func = find_closest_value_in_Bst_1  # function to test

def test_find_closest_value_in_Bst(trees):
    for case, tree in trees.items():
        print(case)
        received = func(tree, tree["target"])
        assert tree["closest"] == received
        print(f"{case} is ok")

trees = {
"case1": json.loads("""{
    "target": 12,
    "tree": {
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": null, "right": null, "value": 22},
            {"id": "13", "left": null, "right": "14", "value": 13},
            {"id": "14", "left": null, "right": null, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": null, "right": null, "value": 5},
            {"id": "2", "left": "1", "right": null, "value": 2},
            {"id": "1", "left": null, "right": null, "value": 1}
        ],
        "root": "10"
    },
    "closest": 0
}"""),
"case2": json.loads("""{
    "tree": {
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": null, "right": null, "value": 22},
            {"id": "13", "left": null, "right": "14", "value": 13},
            {"id": "14", "left": null, "right": null, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": null, "right": null, "value": 5},
            {"id": "2", "left": "1", "right": null, "value": 2},
            {"id": "1", "left": null, "right": null, "value": 1}
        ],
        "root": 12
    },
    "target": 12,
    "closest": 0
}"""),
"case3": json.loads("""{
    "target": 100,
    "tree": {
      "nodes": [
        {"id": "100", "left": "5", "right": "502", "value": 100},
        {"id": "502", "left": "204", "right": "55000", "value": 502},
        {"id": "55000", "left": "1001", "right": null, "value": 55000},
        {"id": "1001", "left": null, "right": "4500", "value": 1001},
        {"id": "4500", "left": null, "right": null, "value": 4500},
        {"id": "204", "left": "203", "right": "205", "value": 204},
        {"id": "205", "left": null, "right": "207", "value": 205},
        {"id": "207", "left": "206", "right": "208", "value": 207},
        {"id": "208", "left": null, "right": null, "value": 208},
        {"id": "206", "left": null, "right": null, "value": 206},
        {"id": "203", "left": null, "right": null, "value": 203},
        {"id": "5", "left": "2", "right": "15", "value": 5},
        {"id": "15", "left": "5-2", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": "57", "value": 22},
        {"id": "57", "left": null, "right": "60", "value": 57},
        {"id": "60", "left": null, "right": null, "value": 60},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": "3", "value": 2},
        {"id": "3", "left": null, "right": null, "value": 3},
        {"id": "1", "left": "-51", "right": "1-2", "value": 1},
        {"id": "1-2", "left": null, "right": "1-3", "value": 1},
        {"id": "1-3", "left": null, "right": "1-4", "value": 1},
        {"id": "1-4", "left": null, "right": "1-5", "value": 1},
        {"id": "1-5", "left": null, "right": null, "value": 1},
        {"id": "-51", "left": "-403", "right": null, "value": -51},
        {"id": "-403", "left": null, "right": null, "value": -403}
      ],
      "root": "100"
    },
    "closest": 0
}"""),
"case4": json.loads("""{
    "target": 208,
    "tree": {
      "nodes": [
        {"id": "100", "left": "5", "right": "502", "value": 100},
        {"id": "502", "left": "204", "right": "55000", "value": 502},
        {"id": "55000", "left": "1001", "right": null, "value": 55000},
        {"id": "1001", "left": null, "right": "4500", "value": 1001},
        {"id": "4500", "left": null, "right": null, "value": 4500},
        {"id": "204", "left": "203", "right": "205", "value": 204},
        {"id": "205", "left": null, "right": "207", "value": 205},
        {"id": "207", "left": "206", "right": "208", "value": 207},
        {"id": "208", "left": null, "right": null, "value": 208},
        {"id": "206", "left": null, "right": null, "value": 206},
        {"id": "203", "left": null, "right": null, "value": 203},
        {"id": "5", "left": "2", "right": "15", "value": 5},
        {"id": "15", "left": "5-2", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": "57", "value": 22},
        {"id": "57", "left": null, "right": "60", "value": 57},
        {"id": "60", "left": null, "right": null, "value": 60},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": "3", "value": 2},
        {"id": "3", "left": null, "right": null, "value": 3},
        {"id": "1", "left": "-51", "right": "1-2", "value": 1},
        {"id": "1-2", "left": null, "right": "1-3", "value": 1},
        {"id": "1-3", "left": null, "right": "1-4", "value": 1},
        {"id": "1-4", "left": null, "right": "1-5", "value": 1},
        {"id": "1-5", "left": null, "right": null, "value": 1},
        {"id": "-51", "left": "-403", "right": null, "value": -51},
        {"id": "-403", "left": null, "right": null, "value": -403}
      ],
      "root": "100"
    },
    "closest": 0
}"""),
"case5": json.loads("""{
  "target": 4500,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case6": json.loads("""{
  "target": 4501,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case7": json.loads("""{
  "target": -70,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case8": json.loads("""{
  "target": 2000,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case9": json.loads("""{
  "target": 6,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case10": json.loads("""{
  "target": 30000,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case11": json.loads("""{
  "target": -1,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case12": json.loads("""{
  "target": 29751,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}"""),
"case13": json.loads("""{
  "target": 29749,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  },
    "closest": 0
}""")}

if __name__ == '__main__':
    test_find_closest_value_in_Bst(trees)
    