class AgentBoisson:
    def __init__(self, stock):
        self.stock = stock

    def verifier_stock(self, boisson):
        return self.stock.get(boisson, 0) > 0

    def retirer_boisson(self, boisson):
        if self.verifier_stock(boisson):
            self.stock[boisson] -= 1
            return True
        return False


class AgentPaiement:
    def __init__(self):
        self.montant_recu = 0

    def inserer_argent(self, montant):
        self.montant_recu += montant

    def verifier_paiement(self, prix):
        return self.montant_recu >= prix

    def reset(self):
        self.montant_recu = 0


class AgentPreparation:
    def __init__(self):
        self.etat = "pret"

    def preparer_boisson(self, boisson):
        print(f"☕ Préparation de la boisson : {boisson}...")
        self.etat = "en cours"
        self.etat = "pret"
        print("✅ Boisson prête !")
        return True


class AgentPrincipal:
    def __init__(self):
        self.etat = "Menu"
        self.boisson = None
        self.prix_boisson = 2 
        self.agent_boisson = AgentBoisson({"café": 5, "thé": 3, "chocolat": 6, "coca cola":8})
        self.agent_paiement = AgentPaiement()
        self.agent_preparation = AgentPreparation()

    def transition(self, action=None):
        if self.etat == "Menu":
            print("Choisissez une boisson (café, thé, chocolat, coca cola) :")
            self.boisson = input().lower()
            if self.agent_boisson.verifier_stock(self.boisson):
                self.etat = "Attente Paiement"
            else:
                print("❌ Boisson en rupture de stock.")
                self.etat = "Menu"

        elif self.etat == "Attente Paiement":
            print(f"Insérez {self.prix_boisson}€ :")
            montant = float(input("Montant inséré : "))
            self.agent_paiement.inserer_argent(montant)
            self.etat = "Validation"

        elif self.etat == "Validation":
            if self.agent_paiement.verifier_paiement(self.prix_boisson):
                self.etat = "Préparation"
            else:
                print("❌ Paiement insuffisant.")
                self.etat = "Attente Paiement"

        elif self.etat == "Préparation":
            if self.agent_boisson.retirer_boisson(self.boisson):
                self.agent_preparation.preparer_boisson(self.boisson)
                self.etat = "Livraison"
            else:
                print("❌ Erreur de stock.")
                self.etat = "Menu"

        elif self.etat == "Livraison":
            print(f"✅ Voici votre {self.boisson}. Merci !")
            self.agent_paiement.reset()
            self.boisson = None
            self.etat = "Menu"

    def run(self):
        print("=== Machine à Café Multi-Agent ===")
        while True:
            self.transition()


if __name__ == "__main__":
    agent_principal = AgentPrincipal()
    agent_principal.run()
