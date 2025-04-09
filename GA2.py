import random

cities = ["A", "B", "C", "D", "E"]

POPULATION_SIZE = 10
GENERATIONS = 50
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

def generate_individual():
    individual = cities[:]
    random.shuffle(individual)
    return individual

def initialize_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def evaluate(individual):
    return sum(ord(individual[i]) - ord(individual[i - 1]) for i in range(1, len(individual)))

def roulette_wheel_selection(population):
    fitness_values = [1 / (1 + evaluate(ind)) for ind in population]  # Inverser pour minimiser
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, weights=probabilities, k=1)[0]

def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return min(tournament, key=evaluate)  # Sélectionne le meilleur du tournoi

def crossover(parent1, parent2):
    cut = random.randint(1, len(cities) - 2)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(selection_method="tournament"):
    population = initialize_population()

    for generation in range(GENERATIONS):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            if selection_method == "roulette":
                parent1 = roulette_wheel_selection(population)
                parent2 = roulette_wheel_selection(population)
            else:
                parent1 = tournament_selection(population)
                parent2 = tournament_selection(population)
            
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = sorted(new_population, key=evaluate)[:POPULATION_SIZE]

    best_solution = min(population, key=evaluate)
    print(f"Meilleur chemin trouvé : {best_solution}, Score : {evaluate(best_solution)}")

genetic_algorithm(selection_method="tournament")