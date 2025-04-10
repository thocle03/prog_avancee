class AgentPaiement:
    """
    Gère le paiement et vérifie si le montant est suffisant.
    """

    def __init__(self):
        self.solde = 0

    def ajouter_argent(self, montant):
        """
        Ajoute de l'argent au solde.
        """
        self.solde += montant
        return self.solde

    def verifier_paiement(self, prix):
        """
        Vérifie si le paiement est suffisant.
        """
        if self.solde >= prix:
            return True, self.solde - prix  # Rendu de monnaie
        else:
            return False, prix - self.solde  # Montant manquant
