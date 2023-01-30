import matplotlib.pyplot as plt
import matplotlib.lines as mlines

fig, ax = plt.subplots()

layers = [
    3,
    1,
    6,
    3,
    8,
    2,
    7,
    6,
    3
]

def form_links(layers):
    links = []
    for i in range(1, len(layers)):
        for this_layer_node in range(layers[i]):
            for prec_layer_node in range(layers[i - 1]):
                link = (i - 1, prec_layer_node, i, this_layer_node)
                links.append(link)
    return links

links = form_links(layers)

def coord(layers, link):
    part_width = 1.0 / layers_len
    part_height1 = 1.0 / layers[link[0]]
    part_height2 = 1.0 / layers[link[2]]
    return [(part_width / 2.0 + part_width * link[0], part_width / 2.0 + part_width * link[2]),
            (part_height1 / 2.0 + part_height1 * link[1], part_height2 / 2.0 + part_height2 * link[3])]

widths = 1
heights = 1

layers_len = len(layers)
part_width = widths / layers_len


for l in links:
    coords = coord(layers, l)
    print(coords)
    ax.add_line(mlines.Line2D(coords[0], coords[1], marker='o',markeredgecolor='red', mew=5))
plt.show()

