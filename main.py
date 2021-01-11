import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.set()


def load_tweets(tweets_path='data/tweets.csv'):
    data = pd.read_csv(tweets_path)

    return data


def load_users(users_path='data/users.csv'):
    data = pd.read_csv(users_path)

    return data


def load_trolls(users_path='data/export.csv'):
    data = pd.read_csv(users_path)

    return data


if __name__ == "__main__":
    # tweets = load_tweets()
    # users = load_users()

    trolls = load_trolls()

    # trolls1 = trolls.groupby(['screen_name']).max().reset_index()

    results = []

    name = None
    j = 0
    k = 0
    use_limit = 15
    for i in range(trolls.shape[0]):
        if name != trolls.loc[i, "screen_name"]:
            if k==use_limit:
                break
            name = trolls.loc[i, "screen_name"]
            j = 0
            k += 1

        if j < 3:
            results.append(trolls.iloc[i].to_list())
            j += 1



    results = pd.DataFrame(results, columns=trolls.columns)

    results['tag'].value_counts().shape

    G = nx.from_pandas_edgelist(results, 'screen_name', 'tag', ['pagerank', 'num'])

    nodes_attr = {}

    trolls_scaling_factor = 200
    tags_scaling_factor = 10
    colors = ['lightblue', 'lightgreen']
    for node in G.nodes:
        if node in results['screen_name'].unique():
            nodes_attr[node] = {
                'size': trolls_scaling_factor * results[results.screen_name == node]['pagerank'].tolist()[0],
                'color': colors[0]}

        else:
            nodes_attr[node] = {'size': tags_scaling_factor* sum(results[results.tag == node]['num'].tolist()),
                                'color': colors[1]}

    plt.figure(figsize=(20, 12))
    nx.draw_networkx(G,
                     #                  pos = nx.spring_layout(G1),
                     #                  pos = nx.circular_layout(G1),
                     pos=nx.nx_agraph.graphviz_layout(G),

                     # node_color=[int(nodes_attr[elem]['color']) for elem in nodes_attr.keys()],
                     node_color=[nodes_attr[elem]['color'] for elem in nodes_attr.keys()],

                     #                  node_size=[v * 100 for v in d.values()]
                     node_size=[nodes_attr[elem]['size'] for elem in nodes_attr.keys()],
                     width=0.2,
                     # alpha=0.5
                     )
    plt.savefig('figures/graph_transparent.png', transparent=True)
    plt.show()
