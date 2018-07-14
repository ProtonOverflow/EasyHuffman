# EasyHuffman

## What is it ?
It's only a simple ``Python`` script that calculate encoded data size without encode them. This script isn't very useful but it can permit to approximate maximum compression ratio of a file without compress it. It permits to gain some performances and time if you only want print informations about this file.

## How it works ?

It works with ``Python2`` and ``Python3``.
You have just to type this in your favourite terminal:
``python main.py``

## What is Huffman encoding ?

Huffman is very famous and he invented this encoding which is used by almost every compression algorithms nowadays. It uses the frequence to encode data.
[Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding) explains the process very well.

### Short explaination

Let's take the example of Wikipedia.
The text is ``this is an example of a huffman tree``
![Wiki's example](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Huffman_tree_2.svg/1200px-Huffman_tree_2.svg.png)
The white boxes represent the char(key) on the left and the frequence on the right.
If you go down to the right, each node correspond to ``1``, and if you go down to the left, each node correspond to ``0``.
If you don't understand what I mean, here is a nice drawing:
![Drawing](https://i.imgur.com/4q3yFpK.jpg)
You have to concatenate each bit. That is to say, if you want to get the code of the letter ``o``, you have to concatenate: ``0``, ``0``, ``1``, ``1``, ``0`` which gives: ``00110``.
If we analyse this tree we have this table:

Char | Frequence | Code
--- | --- | ---
Space | 7 | 111
a |	4 |	010
e |	4 |	000
f |	3 |	1101
h |	2 |	1010
i |	2 |	1000
m |	2 |	0111
n |	2 |	0010
s |	2 |	1011
t |	2 |	0110
l |	1 |	11001
o |	1 |	00110
p |	1 |	10011
r |	1 |	11000
u |	1 |	00111
x |	1 |	10010 

The more the frequency of apparition is higher, the less his code's size is long.

To encode the data you have just to replace each by his code.
You can obviously calculate the encoded data size without encode them.
Of course, here is the simple formula:
![Formula](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Cfn_cm%20EncodedSize%3D%5Csum_%7Bc%20%5Cin%20tree%7D%7BFreq%28c%29%20%5Ctimes%20SizeOf%28CodeOf%28c%29%29%29%7D)