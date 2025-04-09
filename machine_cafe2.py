PRIX_BOISSONS = {
    "café": 1.5,
    "thé": 1.0,
    "chocolat": 2.0,
    "coca cola": 2.5
}

STOCK_INITIAL = {
    "café": 5,
    "thé": 3,
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
        print(f"Préparation de votre {boisson}...")

class AgentPrincipal:
    def __init__(self, agent_boisson, agent_paiement, agent_preparation):
        self.agent_boisson = agent_boisson
        self.agent_paiement = agent_paiement
        self.agent_preparation = agent_preparation
        self.etat = "Menu"
        self.boisson = None

    def choisir_boisson(self, boisson):
        print(f"Vous avez choisi : {boisson}")
        if self.agent_boisson.verifier_stock(boisson):
            self.boisson = boisson
            self.etat = "Attente Paiement"
            print(f"Veuillez insérer {self.agent_boisson.get_prix(boisson)}€.")
        else:
            print("Désolé, cette boisson n'est plus disponible.")

    def inserer_argent(self, montant):
        if self.etat == "Attente Paiement":
            self.agent_paiement.inserer_argent(montant)
            if self.agent_paiement.verifier_paiement(self.agent_boisson.get_prix(self.boisson)):
                self.etat = "Validation"
                self.valider_paiement()

    def valider_paiement(self):
        print("Paiement accepté.")
        self.etat = "Préparation"
        if self.agent_boisson.retirer_boisson(self.boisson):
            self.agent_preparation.preparer_boisson(self.boisson)
            self.etat = "Livraison"
            self.livrer_boisson()
        else:
            print("Erreur lors du traitement de la commande.")
        self.agent_paiement.reset()

    def livrer_boisson(self):
        print(f"Voici votre {self.boisson}. Bonne dégustation !")
        self.etat = "Menu"

boisson_agent = AgentBoisson(stock=STOCK_INITIAL.copy(), prix=PRIX_BOISSONS)
paiement_agent = AgentPaiement()
preparation_agent = AgentPreparation()
principal_agent = AgentPrincipal(boisson_agent, paiement_agent, preparation_agent)

principal_agent.choisir_boisson("café")
principal_agent.inserer_argent(1)
principal_agent.inserer_argent(0.5) 
