import sys, os, time
import numpy as np
#import matplotlib.pyplot as plt
from yaml import load, dump
import networkx as nx



def load_map():
    borders = load(open('borders.yml', 'r'))
    tiles = load(open('tiles.yml', 'r'))
    #print(len(tiles), len(borders))
    G = nx.Graph()
    G.add_edges_from((b['tile1'], b['tile2'], {'type':b['type']}) for b in borders)
    G.add_nodes_from((k, v) for k,v in tiles.items())
    return G














