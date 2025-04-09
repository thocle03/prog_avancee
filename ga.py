#initialiser la population
#
#choisir croisement
#
#

import random

cities = ["Paris", "Versailles", "Feucherolles", "Rouen", "Nice"]

distances = {
    ("Paris", "Versailles"): 20, ("Paris", "Feucherolles"): 35, ("Paris", "Rouen"): 135, ("Paris", "Nice"): 930,
    ("Versailles", "Feucherolles"): 18, ("Versailles", "Rouen"): 125, ("Versailles", "Nice"): 950,
    ("Feucherolles", "Rouen"): 120, ("Feucherolles", "Nice"): 960,
    ("Rouen", "Nice"): 1000
}

def generate_individual():
    individual = cities[:]
    random.shuffle(individual)
    return individual

def evaluate(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        pair = (individual[i], individual[i + 1])
        reverse_pair = (individual[i + 1], individual[i])
        total_distance += distances.get(pair, distances.get(reverse_pair, float('inf')))
    return total_distance

def select_parents(population):
    return sorted(population, key=evaluate)[:2]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    remaining = [city for city in parent2 if city not in child]
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining.pop(0)
    return child

def mutate(individual):
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm(generations=50, population_size=10):
    population = [generate_individual() for _ in range(population_size)]
    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:
                child = mutate(child)
            new_population.append(child)
        population = new_population
    best_solution = min(population, key=evaluate)
    return best_solution, evaluate(best_solution)

best_route, best_distance = genetic_algorithm()

print("Best Route:", best_route)
print("Total Distance:", best_distance)
