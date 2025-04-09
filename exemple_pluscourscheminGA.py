import random

cities = ["A", "B", "C", "D", "E"]

POPULATION_SIZE = 10
GENERATIONS = 50
MUTATION_RATE = 0.1

def generate_individual():
    individual = cities[:]
    random.shuffle(individual)
    return individual

def initialize_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def evaluate(individual):
    return sum(ord(individual[i]) - ord(individual[i - 1]) for i in range(1, len(individual)))

def select_parents(population):
    return random.sample(population, 2)

def crossover(parent1, parent2):
    cut = random.randint(1, len(cities) - 2)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    population = initialize_population()

    for generation in range(GENERATIONS):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = sorted(new_population, key=evaluate)[:POPULATION_SIZE]

    best_solution = min(population, key=evaluate)
    print(f"Meilleur chemin trouvé : {best_solution}, Score : {evaluate(best_solution)}")

genetic_algorithm()
