#!/usr/bin/python
import collections
import heapq
from functools import total_ordering
from random import random
from math import ceil

@total_ordering
class Node(object):

    def __init__(self, key=None, weight=None):
        self._key = key
        self._weight = weight
        self._random = random()
        self._children = []

    def addChild(self, obj):
        self._children.append(obj)

    def __eq__(self, other):
        return (self._weight, self._random) == (other._weight, other._random)

    def __lt__(self, other):
        return (self._weight, self._random) < (other._weight, other._random)

def calcFreq(bytes):
    # We calculate the frequency of each byte
    return [(code, count) for code, count in dict(collections.Counter(bytes)).items()]

def encode(freq):
    # We make the tree and the nodes
    data = [Node(x[0], x[1]) for x in freq]
    heapq.heapify(data)

    while len(data) >= 2:
        child1 = heapq.heappop(data)
        child2 = heapq.heappop(data)
        parent = Node(None, child1._weight + child2._weight)
        parent.addChild(child1)
        parent.addChild(child2)

        heapq.heappush(data, parent)

    return data

def traverseTree(root, code, keycode):
    # We get the codes
    if len(root._children) == 0:
        keycode[root._key] = code
        return
    traverseTree(root._children[0], code+'0', keycode)
    traverseTree(root._children[1], code+'1', keycode)

def getCodes(tree):
    # It returns the codes of each byte
    code = ""
    keycode = dict()
    traverseTree(tree[0], code, keycode)
    return keycode

def encodeData(data, codes):
    # It replaces each byte by his code
    result = ""
    for c in data:
        if c not in codes.keys():
            print("Weird error, %c is not in the byte array."%c)
        else:
            result += codes[c]
    
    return result

def main():
    #sample = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    sample = "this is an example of a huffman tree"
    sample_ba = sample.encode()
    init_size = len(sample)
    print("Init data: %s"%sample)
    print("Init size: %d bytes"%init_size)

    freq = calcFreq(sample_ba)
    tree = encode(freq)
    codes = getCodes(tree)

    compressed_size = sum([len(codes[code]) * count for (code, count) in freq]) / 8.0
    print("Compressed size: %d bytes"%ceil(compressed_size))

    encoded = encodeData(sample_ba, codes)
    encoded_size = len(encoded) / 8.0
    print("Encoded data: %s"%encoded)
    assert(encoded_size == compressed_size)

    compression_ratio = init_size / compressed_size
    space_savings = (1.0 - compressed_size / init_size) * 100.0
    print("Compression Ratio: {}".format(compression_ratio))
    print("Space savings: {} %".format(space_savings))

if __name__ == "__main__":
    main()