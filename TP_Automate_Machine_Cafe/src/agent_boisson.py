class AgentBoisson:
    """
    Gère la sélection et la vérification des boissons disponibles.
    """

    def __init__(self):
        self.boissons = {
            "Espresso": 1.50,
            "Café Latte": 2.00,
            "Thé": 1.00,
            "Jus": 2.50
        }

    def afficher_menu(self):
        """
        Affiche le menu des boissons disponibles.
        """
        print("\n MENU DES BOISSONS")
        for boisson, prix in self.boissons.items():
            print(f"- {boisson} : {prix}€")

    def verifier_boisson(self, boisson):
        """
        Vérifie si la boisson est disponible.
        """
        return self.boissons.get(boisson, None)
