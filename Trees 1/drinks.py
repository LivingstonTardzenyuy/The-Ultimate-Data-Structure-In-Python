#created by kongnyuy livingston

class TreeNode:
    def __init__(self, value, children=[]):
        self.value=value
        self.children=children

    def __str__(self, level=0):
        ret="  " * level + str(self.value) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addChild(self,value):
        self.children.append(value)

treenode=TreeNode("Drinks", [])

cold=TreeNode("Cold", [])
hot=TreeNode("Hot", [])

treenode.addChild(cold)
treenode.addChild(hot)

fanta=TreeNode("Fanta", [])
pamplemous=TreeNode("Pamplemous", [])
nescafe=TreeNode("Nescafe", [])
tea=TreeNode("Tea", [])
cold.addChild(fanta)
hot.addChild(nescafe)

cold.addChild(pamplemous)
hot.addChild(tea)

print(treenode)
