import tkinter as tk
from tkinter import messagebox

PRIX_BOISSONS = {
    "☕ Café": 1.5,
    "🍵 Thé": 1.0,
    "🍫 Chocolat": 2.0,
    "🥤 Coca Cola": 2.5
}

STOCK_INITIAL = {
    "☕ Café": 5,
    "🍵 Thé": 3,
    "🍫 Chocolat": 4,
    "🥤 Coca Cola": 6
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
        messagebox.showinfo("Préparation", f"{boisson} est en préparation...")


class MachineBoissonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ Machine à Boissons 🍹")
        self.root.configure(bg="#f0f0f0")

        self.boisson_agent = AgentBoisson(stock=STOCK_INITIAL.copy(), prix=PRIX_BOISSONS)
        self.paiement_agent = AgentPaiement()
        self.preparation_agent = AgentPreparation()

        self.boisson_choisie = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choisissez votre boisson :", font=("Helvetica", 16), bg="#f0f0f0").pack(pady=10)

        for boisson in PRIX_BOISSONS:
            btn = tk.Button(
                self.root,
                text=f"{boisson} - {PRIX_BOISSONS[boisson]}€",
                font=("Helvetica", 14),
                bg="#d4f1f9",
                activebackground="#bce0ea",
                relief="raised",
                command=lambda b=boisson: self.choisir_boisson(b)
            )
            btn.pack(pady=5, padx=20, fill='x')

        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.info_label.pack(pady=15)

        self.entree_montant = tk.Entry(self.root, font=("Helvetica", 12), justify='center')
        self.entree_montant.pack(pady=5)

        self.bouton_valider = tk.Button(
            self.root,
            text="💳 Valider Paiement",
            font=("Helvetica", 12, "bold"),
            bg="#c3fcb5",
            activebackground="#a6e79f",
            command=self.valider_paiement
        )
        self.bouton_valider.pack(pady=10)

    def choisir_boisson(self, boisson):
        if not self.boisson_agent.verifier_stock(boisson):
            messagebox.showwarning("Rupture", f"Désolé, il n'y a plus de {boisson} en stock.")
            return

        self.boisson_choisie = boisson
        prix = self.boisson_agent.get_prix(boisson)
        stock = self.boisson_agent.stock[boisson]
        self.info_label.config(text=f"🛒 Vous avez choisi {boisson} — Prix : {prix}€ | Stock restant : {stock}")
        self.entree_montant.delete(0, tk.END)
        self.paiement_agent.reset()

    def valider_paiement(self):
        if not self.boisson_choisie:
            messagebox.showwarning("Erreur", "Veuillez d'abord choisir une boisson.")
            return

        try:
            montant = float(self.entree_montant.get())
        except ValueError:
            messagebox.showerror("Montant invalide", "Veuillez entrer un montant numérique.")
            return

        self.paiement_agent.inserer_argent(montant)
        prix = self.boisson_agent.get_prix(self.boisson_choisie)

        if self.paiement_agent.verifier_paiement(prix):
            self.boisson_agent.retirer_boisson(self.boisson_choisie)
            self.preparation_agent.preparer_boisson(self.boisson_choisie)
            messagebox.showinfo("✅ Livraison", f"Voici votre {self.boisson_choisie} ! Bonne dégustation 😋")
            self.paiement_agent.reset()
            self.info_label.config(text="")
            self.boisson_choisie = None
            self.entree_montant.delete(0, tk.END)
        else:
            manque = prix - self.paiement_agent.solde
            messagebox.showinfo("Paiement incomplet", f"Il manque encore {manque:.2f}€.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = MachineBoissonApp(root)
    root.mainloop()
