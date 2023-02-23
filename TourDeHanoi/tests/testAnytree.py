from logging import root

from anytree.exporter import DotExporter


def nodenamefunc(node):
    return '%s:%s' % (node.name, node.depth)

def nodeattrfunc(node):
    return 'label="%s"' % node.name

def edgeattrfunc(node, child):
    return 'label="%s:%s"' % (node.name, child.name)

def edgetypefunc(node, child):
    return '--'

for line in DotExporter(root, graph="graph",
                        nodenamefunc=nodenamefunc,
                        nodeattrfunc=lambda node: "shape=box",
                        edgeattrfunc=edgeattrfunc,
                        edgetypefunc=edgetypefunc):
    print(line)