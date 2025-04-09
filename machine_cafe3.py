PRIX_BOISSONS = {
    "café": 1.5,
    "thé": 1.0,
    "chocolat": 2.0,
    "coca cola": 2.5
}

STOCK_INITIAL = {
    "café": 5,
    "thé": 1,
    "chocolat": 4,
    "coca cola": 6
}

class AgentBoisson:
    def __init__(self, stock, prix):
        self.stock = stock
        self.prix = prix

    def verifier_stock(self, boisson):
        return self.stock.get(boisson, 0) > 0

    def retirer_boisson(self, boisson):
        if self.verifier_stock(boisson):
            self.stock[boisson] -= 1
            return True
        return False

    def get_prix(self, boisson):
        return self.prix.get(boisson, 0)

class AgentPaiement:
    def __init__(self):
        self.solde = 0

    def inserer_argent(self, montant):
        self.solde += montant

    def verifier_paiement(self, prix):
        return self.solde >= prix

    def reset(self):
        self.solde = 0

class AgentPreparation:
    def preparer_boisson(self, boisson):
        print(f"\n Préparation de votre {boisson} en cours...")

class AgentPrincipal:
    def __init__(self, agent_boisson, agent_paiement, agent_preparation):
        self.agent_boisson = agent_boisson
        self.agent_paiement = agent_paiement
        self.agent_preparation = agent_preparation

    def demarrer(self):
        while True:
            print("\n=== MACHINE À BOISSONS INTELLIGENTE DE THOMAS ===")
            print("Voici les boissons disponibles :")
            for boisson, prix in self.agent_boisson.prix.items():
                stock = self.agent_boisson.stock[boisson]
                print(f" - {boisson.capitalize()} ({prix}€) — Stock: {stock}")

            choix = input("\n Que souhaitez-vous boire ? ").lower()

            if choix not in self.agent_boisson.prix:
                print("Boisson non reconnue.")
                continue

            if not self.agent_boisson.verifier_stock(choix):
                print("Désolé, cette boisson est en rupture de stock.")
                continue

            prix = self.agent_boisson.get_prix(choix)
            print(f"Le prix du {choix} est de {prix}€.")
            
            while True:
                try:
                    montant = float(input("Insérez votre argent (€) : "))
                    self.agent_paiement.inserer_argent(montant)
                except ValueError:
                    print("Montant invalide.")
                    continue

                if self.agent_paiement.verifier_paiement(prix):
                    print("Paiement accepté.")
                    break
                else:
                    reste = prix - self.agent_paiement.solde
                    print(f"Il manque encore {reste:.2f}€. Veuillez insérer davantage.")

            self.agent_boisson.retirer_boisson(choix)
            self.agent_preparation.preparer_boisson(choix)
            print(f"Votre {choix} est prêt. Merci et bonne dégustation !")
            self.agent_paiement.reset()

            again = input("\n Une autre boisson ? (o/n) : ").lower()
            if again != 'o':
                print("Merci d'avoir utilisé la machine de thomas et à bientôt !")
                break


boisson_agent = AgentBoisson(stock=STOCK_INITIAL.copy(), prix=PRIX_BOISSONS)
paiement_agent = AgentPaiement()
preparation_agent = AgentPreparation()
principal_agent = AgentPrincipal(boisson_agent, paiement_agent, preparation_agent)

principal_agent.demarrer()
