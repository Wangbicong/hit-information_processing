# -*- coding:utf-8 -*-

nodes = [
    "Arad",
    "Mehadia",
    "Bucharest",
    "Neamt",
    "Craiova",
    "Oradea",
    "Dobreta",
    "Pitesti",
    "Eforie",
    "Rimnicu",
    "Fagaras",
    "Sibiu",
    "Giurgiu",
    "Timisoara",
    "Hirsova",
    "Urziceni",
    "Iasi",
    "Vaslui",
    "Lugoj",
    "Zerind",
]

edges = [
    ("Arad", "Zerind", 75),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Rimnicu", 146),
    ("Rimnicu", "Sibiu", 80),
    ("Craiova", "Pitesti", 138),
    ("Pitesti", "Rimnicu", 97),
    ("Sibiu", "Fagaras", 99),
    ("Fagaras", "Bucharest", 211),
    ("Bucharest", "Pitesti", 101),
    ("Giurgiu", "Bucharest", 90),
    ("Bucharest", "Urziceni", 86),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Hirsova", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

direct_distances = {
    "Arad": 366,
    "Mehadia": 241,
    "Bucharest": 0,
    "Neamt": 234,
    "Craiova": 160,
    "Oradea": 380,
    "Dobreta": 242,
    "Pitesti": 100,
    "Eforie": 161,
    "Rimnicu": 193,
    "Fagaras": 176,
    "Sibiu": 253,
    "Giurgiu": 77,
    "Timisoara": 329,
    "Hirsova": 151,
    "Urziceni": 80,
    "Iasi": 226,
    "Vaslui": 199,
    "Lugoj": 244,
    "Zerind": 374
}