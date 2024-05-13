# alphabet = [int(x) for x in input("Enter job list : ").split()]
# freq = [int(x) for x in input("Enter time job list : ").split()]


# alphabet = ['a','b','c','d','e','f']
# freq = [16,5,12,17,10,25]


alphabet = ['c','e','i','r','s','t','x']
freq = [0.11,0.22,.16,.12,.15,.10,.14]


def makePairs(alphabet,freq):
    tb = {}
    for index in range(len(alphabet)):
        tb[alphabet[index]] = freq[index]
    return tb

# def huffman(data):

#     if len(data) == 2 :
#         return [data[0],data[1]]

#     tree = {}
    
#     tree[data[0] + data[1]] = huffman(data[:2])
    

# x = makePairs(alphabet,freq)
# y = dict(sorted(x.items(), key=lambda item: item[1]))

# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------

from collections import Counter


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    '''
    Function to find Huffman Code
    '''
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    '''
    Function to make tree
    :param nodes: Nodes
    :return: Root of the tree
    '''
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


if __name__ == '__main__':
    # string = 'BCAADDDCCACACAC'
    # freq = dict(Counter(string))
    freq = dict(sorted(makePairs(alphabet,freq).items(), key=lambda item: item[1]))
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(freq)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    for i in encoding:
        print(f'{i} : {encoding[i]}')