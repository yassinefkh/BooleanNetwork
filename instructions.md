# POUR EXECUTER LE PROGRAMME :

- Installer panda
  (avec pip par exemple : pip install panda)
- Installer matplotlib

Dans src/, executez le programme en tapant :
python simulation.py

# Instructions pour modifier les paramètres de simulation :

Le fichier source fourni, "simulation.py", vous permet de simuler des dynamiques de réseaux de régulation biologique. Vous pouvez ajuster plusieurs paramètres pour personnaliser vos simulations. Voici comment procéder :

    Ouvrez le fichier "simulation.py" dans votre éditeur de texte ou votre environnement de développement Python.

    Recherchez la section du code qui ressemble à ceci :

    if __name__ == "__main__":
    size = 20
    connectivity = 2
    num_steps = 40
    mutation_rate = 0.00
    num_trials = 1
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, mutation_rate=mutation_rate)
    print("Attracteurs détectés :", attractors)
    attractor_counts = analyze_attractors(attractors)
    print("Attractor counts:", attractor_counts)

Les variables size, connectivity, num_steps, mutation_rate, et num_trials sont les paramètres de simulation
que vous pouvez modifier selon vos besoins. Voici ce que chacun d'eux signifie :

    size : Détermine la taille du réseau de régulation biologique simulé.
    connectivity : Indique le degré de connectivité entre les composants du réseau.
    num_steps : Spécifie le nombre d'étapes de simulation à effectuer.
    mutation_rate : Contrôle le taux de mutation des composants du réseau (0.00 signifie aucun taux de mutation).
    num_trials : Définit le nombre de répétitions de la simulation à exécuter.

    Modifiez les valeurs de ces variables selon vos préférences.
