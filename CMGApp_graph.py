# Connect to Neo4j
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="bolt://localhost:4579",
    username="neo4j",
    password="saiyan94",
    database="neo4j"
)