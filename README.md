# 📊 Sondage Flask

> Une application web de sondage interactif développée avec Flask, permettant de collecter les réponses des participants et de les stocker dans une base de données SQLite.

---

## 🏗️ Architecture

Le projet suit une séparation claire des responsabilités :

- **Backend** — Application web développée avec **Flask**, gérant les routes, la logique métier et les interactions avec la base de données.
- **Frontend** — Interface HTML/CSS épurée avec gestion des formulaires et affichage dynamique via **Jinja2**.
- **Base de données** — Stockage des questions et des réponses participants via **SQLite**.

---

## 🚀 Installation

### Prérequis

- Python **3.8+**

### Étapes

**1. Configurer l'environnement virtuel**

```bash
# Création
python3 -m venv .venv

# Activation
source .venv/bin/activate
```

**2. Installer les dépendances**

```bash
pip install flask
```

**3. Initialiser la base de données**

```bash
# Créer le dossier et la base de données
mkdir -p bdd
python3 -c "
import sqlite3
conn = sqlite3.connect('bdd/Question.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Question (ID INTEGER PRIMARY KEY, question TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT)')
conn.commit()
conn.close()
print('Base de données créée.')
"
```

**4. Ajouter les questions**

Les questions sont dans `Question.txt`, une par ligne. Pour les importer :

```bash
python3 -c "
import sqlite3
with open('Question.txt', 'r') as f:
    questions = [l.strip() for l in f if l.strip()]
conn = sqlite3.connect('bdd/Question.db')
cur = conn.cursor()
for i, q in enumerate(questions, 1):
    cur.execute('INSERT OR IGNORE INTO Question (ID, question) VALUES (?, ?)', (i, q))
conn.commit()
conn.close()
print(f'{len(questions)} questions importées.')
"
```

**5. Lancer le serveur**

```bash
python3 Projet.py
```

L'application est accessible sur `http://localhost:1664`.

---

## 💡 Choix Techniques

| Technologie | Justification |
|---|---|
| **Flask** | Framework léger et simple, idéal pour une application web de taille réduite |
| **SQLite** | Base de données embarquée, sans serveur à configurer |
| **Jinja2** | Moteur de templates intégré à Flask pour le rendu dynamique des pages |
| **`.gitignore`** | Protection de la base de données (données personnelles) hors du dépôt |

---

## 🔒 Sécurité

- La base de données SQLite (`*.db`) est exclue du contrôle de version via `.gitignore` — elle contient des données personnelles (noms et prénoms des participants).
- Chaque déploiement génère sa propre base de données locale.

---

## 📋 Changelog

### v1.1.0
- **Repo** — Suppression de la base de données SQLite du contrôle de version (données personnelles)
- **Repo** — Suppression de l'archive `.rar` du dépôt
- **Doc** — Ajout d'un README complet avec instructions d'installation

### v1.0.0
- Version initiale : application Flask de sondage avec stockage SQLite et interface Jinja2

---

> Projet scolaire développé avec une approche centrée sur la **simplicité** et la **séparation des responsabilités**.
