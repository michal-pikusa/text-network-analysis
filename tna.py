import networkx as nx
from nltk.corpus import stopwords
from tqdm import tqdm
from networkx.algorithms import community
import matplotlib.pyplot as plt
import logging
from random import random

def load_file(filename):
    logging.info('Loading text')
    with open(filename,'r') as f:
        text = f.readlines()
    return text

def preprocess(line):
    stop_words = set(stopwords.words('english'))
    line = [item.lower() for item in line if not item.lower() in stop_words]
    return line

def create_graph(text):
    logging.info('Creating graph')
    word_list = []
    G = nx.Graph()
    pbar = tqdm(total=len(text))
    for line in text:
        line = (line.strip()).split()
        line = preprocess(line)
        for i, word in enumerate(line):
            if i != len(line)-1:
                word_a = word
                word_b = line[i+1]
                if word_a not in word_list:
                    word_list.append(word_a)
                if word_b not in word_list:
                    word_list.append(word_b)
                if G.has_edge(word_a,word_b):
                    G[word_a][word_b]['weight'] += 1
                else:
                    G.add_edge(word_a,word_b, weight = 1)
        pbar.update(1)
    pbar.close()
    return G

def calculate_central_nodes(text_network):
    logging.info('Calculating centrality')
    bc = (nx.betweenness_centrality(text_network,weight='weight'))
    nx.set_node_attributes(text_network, bc, 'betweenness')
    bc_threshold = sorted(bc.values(), reverse=True)[20]
    to_keep = [n for n in bc if bc[n] > bc_threshold]
    filtered_network = text_network.subgraph(to_keep)
    return filtered_network

def create_and_assign_communities(text_network):
    logging.info("Assigning communities")
    communities_generator = community.girvan_newman(text_network)
    top_level_communities = next(communities_generator)
    next_level_communities = next(communities_generator)
    communities = {}
    for community_list in next_level_communities:
        for item in community_list:
            communities[item] = next_level_communities.index(community_list)
    return communities

def draw_final_graph(text_network,communities):
    logging.info('Drawing')
    pos = nx.spring_layout(text_network,scale=2)
    color_list = []
    color_map = []
    community_count = max(communities.values())
    for i in range(0,community_count+1):
        color_list.append((random(), random(), random()))
    for node in text_network:
        color_index = communities[node]
        color_map.append(color_list[color_index])
    betweenness = nx.get_node_attributes(text_network,'betweenness')
    betweenness = [x * 10000 for x in betweenness.values()]
    nx.draw(text_network,with_labels=True,node_size=betweenness,font_size=8,node_color=color_map,width=4,edge_cmap=plt.cm.Blues)
    plt.draw()
    plt.show()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    text = load_file('pubmed.txt')
    text_network = create_graph(text)
    text_network = calculate_central_nodes(text_network)
    communities = create_and_assign_communities(text_network)
    nx.write_gml(text_network, "text_network.gml")
    draw_final_graph(text_network,communities)
    
    
