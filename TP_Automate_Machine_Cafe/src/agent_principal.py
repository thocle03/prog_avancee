from agent_boisson import AgentBoisson
from agent_paiement import AgentPaiement
from agent_preparation import AgentPreparation

class AgentPrincipal:
    """
    Agent principal qui gère la coordination entre les agents de la machine à café.
    """

    def __init__(self):
        self.agent_boisson = AgentBoisson()
        self.agent_paiement = AgentPaiement()
        self.agent_preparation = AgentPreparation()
        self.boisson_choisie = None
        self.prix = 0

    def choisir_boisson(self):
        """
        Permet à l'utilisateur de choisir une boisson.
        """
        self.agent_boisson.afficher_menu()
        choix = input(" Choisissez une boisson : ").strip()
        self.prix = self.agent_boisson.verifier_boisson(choix)

        if self.prix:
            self.boisson_choisie = choix
            print(f" {choix} sélectionné. Veuillez insérer {self.prix}€.")
        else:
            print(" Boisson non disponible.")

    def inserer_argent(self):
        """
        Gère l'insertion de l'argent et vérifie le paiement.
        """
        if not self.boisson_choisie:
            print(" Vous devez choisir une boisson d'abord.")
            return

        montant = float(input(f" Insérez de l’argent (€) : "))
        solde = self.agent_paiement.ajouter_argent(montant)
        print(f" Solde total : {solde}€")

        paiement_valide, reste = self.agent_paiement.verifier_paiement(self.prix)

        if paiement_valide:
            print(f" Paiement accepté. Rendu de monnaie : {reste}€.")
            self.agent_preparation.preparer_boisson(self.boisson_choisie)
            self.reinitialiser()
        else:
            print(f" Solde insuffisant. Il manque {reste}€.")

    def reinitialiser(self):
        """
        Remet la machine à son état initial.
        """
        self.boisson_choisie = None
        self.prix = 0
        self.agent_paiement.solde = 0

    def lancer(self):
        """
        Lance l'interface interactive.
        """
        while True:
            print("\n Machine à Café ")
            print("1. Choisir une boisson")
            print("2. Insérer de l’argent")
            print("3. Quitter")
            choix = input("Votre choix : ")

            if choix == "1":
                self.choisir_boisson()
            elif choix == "2":
                self.inserer_argent()
            elif choix == "3":
                print(" Merci et à bientôt !")
                break
            else:
                print(" Choix invalide.")

if __name__ == "__main__":
    agent_principal = AgentPrincipal()
    agent_principal.lancer()
