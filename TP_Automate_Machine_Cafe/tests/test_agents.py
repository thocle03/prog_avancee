import unittest
from src.agent_boisson import AgentBoisson
from src.agent_paiement import AgentPaiement

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.agent_boisson = AgentBoisson()
        self.agent_paiement = AgentPaiement()

    def test_boisson_disponible(self):
        self.assertEqual(self.agent_boisson.verifier_boisson("Espresso"), 1.50)
        self.assertIsNone(self.agent_boisson.verifier_boisson("Coca"))

    def test_paiement_suffisant(self):
        self.agent_paiement.ajouter_argent(2)
        paiement, rendu = self.agent_paiement.verifier_paiement(1.50)
        self.assertTrue(paiement)
        self.assertEqual(rendu, 0.50)

    def test_paiement_insuffisant(self):
        self.agent_paiement.ajouter_argent(1)
        paiement, manque = self.agent_paiement.verifier_paiement(1.50)
        self.assertFalse(paiement)
        self.assertEqual(manque, 0.50)

if __name__ == "__main__":
    unittest.main()
