from py2neo import Graph, Node, NodeMatcher
import os
import csv

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')
graph = Graph(url + '/db/data', username='neo4j', password='bdma')
print("connected")

def populateTasker():
    with open('taskers.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            username = line['username']
            passportNumber = line['passportNumber']  # take the current line
            profession = line['profession']
            region = line['region']
            user = Node("Tasker", username=username, passportNumber=passportNumber, profession=profession,
                        region=region)
            graph.create(user)
            print("done")

def populateCustomer():
    with open('Customers2.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            username = line['username']
            passportNumber = line['passportNumber']  # take the current line
            user = Node("Customer", username=username, passportNumber=passportNumber)
            graph.create(user)
            print("done")


def findCustomer(user):
    matcher = NodeMatcher(graph)
    user = matcher.match("Customer", username={user}).first()
    # user =graph.match("Tasker", 'username', value).first()
    print(user)


user="chaser"
findCustomer(user)


def find_similarities():
    query = '''
    MATCH (p:Customer), (m:Tasker) 
    OPTIONAL MATCH (p)-[rated:booked]->(m) 
    WITH {item:id(p), weights: collect(coalesce(toInt(rated.priceRating),toInt(rated.qualityRating), toInt(rated.flexScheduleRating)))} as userData 
    WITH collect(userData) as data 
    CALL algo.similarity.pearson.stream(data,{topK:7,similarityCutoff:0.2}) 
    YIELD item1, item2, count1, count2, similarity 
    WITH algo.asNode(item1).username AS from, algo.asNode(item2).username AS to, similarity 
    match(ff:Customer{username:from}) 
    match(tt:Customer{username:to}) 
    MERGE (ff)-[sim:SIMILAR]->(tt) 
    SET sim.similarity=similarity 
    '''
    return graph.run(query)


def update_weight1():
    query = '''
    MATCH (c:Customer)-[b:booked]->(t:Tasker) WITH c,t,avg(1/ToFloat(b.overallRating)) as weight
    CREATE (c)-[w:WEIGHT{value:weight}]->(t)
    '''
    return graph.run(query)


def update_weight2():
    query = '''
    OPTIONAL MATCH (c1:Customer)-[s:SIMILAR]->(c2:Customer) 
    CREATE (c1)-[w:WEIGHT]->(c2) 
    SET w.value=1-ToFloat(s.similarity) 
    '''
    return graph.run(query)


def calculate_shortestpath(username):
    query = '''
    MATCH (start: Customer {username:{username}) 
    CALL algo.shortestPaths.stream(start, 'value',{ 
    nodeQuery:'MATCH(n: Customer) RETURN id(n) as id UNION MATCH(m:Tasker) RETURN id(m) as id', 
    relationshipQuery:'MATCH(n)-[r:WEIGHT]->(m) RETURN id(n) as source, id(m) as target, r.value as weight', graph:'cypher'}) 
    YIELD nodeId, distance 
    WITH algo.asNode(nodeId) AS Node, distance 
    WHERE algo.isFinite(distance) = true AND 'Tasker' IN LABELS(Node) 
    RETURN Node.username, distance 
    ORDER BY distance ASC 
    find_similarities()
    '''
    return graph.run(query)

