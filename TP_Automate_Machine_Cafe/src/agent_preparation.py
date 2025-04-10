import time

class AgentPreparation:
    """
    Prépare et livre la boisson sélectionnée.
    """

    def preparer_boisson(self, boisson):
        print(f" Préparation de votre {boisson} en cours...")
        time.sleep(2)
        print(f" {boisson} est prêt ! ")
