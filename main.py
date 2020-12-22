import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def load_tweets(tweets_path='data/tweets.csv'):
    data = pd.read_csv(tweets_path)

    return data


def load_users(users_path='data/users.csv'):
    data = pd.read_csv(users_path)

    return data



if __name__ == "__main__":
    tweets = load_tweets()
    users = load_users()