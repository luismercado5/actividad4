# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:56:01 2023

@author: luis mercado
"""

import tkinter as tk
from tkinter import messagebox

class EvaluadorExpresiones:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluador de Expresiones")

        self.expresion_label = tk.Label(root, text="Ingrese la expresión:")
        self.expresion_label.pack()

        self.expresion_entry = tk.Entry(root)
        self.expresion_entry.pack()

        self.evaluar_button = tk.Button(root, text="Evaluar", command=self.evaluar_expresion)
        self.evaluar_button.pack()

    def evaluar_expresion(self):
        expresion = self.expresion_entry.get()
        try:
            resultado = self.evaluar(expresion)
            messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def evaluar(self, expresion):
        # Evaluar la expresión
        return eval(expresion)

# Función principal
def main():
    root = tk.Tk()
    evaluador = EvaluadorExpresiones(root)
    root.mainloop()

if __name__ == "__main__":
    main()
