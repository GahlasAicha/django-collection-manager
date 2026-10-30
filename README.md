# 📚 Django Collection Manager

Application web **Django** de gestion de **collections** et de leurs **éléments**. Chaque utilisateur peut créer ses collections, y ajouter des éléments, et seul le **créateur** d'un objet peut en voir le détail, le modifier ou le supprimer.

> Projet réalisé dans le cadre du module *Framework Web 1* — Master Informatique, Université d'Orléans (2024-2025).

---

## ✨ Fonctionnalités

- 📋 **Liste publique** des collections et éléments
- 🔐 **Authentification** — connexion requise pour accéder aux détails et aux actions
- 👤 **Droits par créateur** — seul l'auteur d'une collection ou d'un élément peut la consulter en détail, la modifier ou la supprimer
- 🗂️ **CRUD complet** sur les collections et les éléments (ajout, détail, suppression)
- 🧩 **Relation** collection → éléments
- 🛠️ **Interface d'administration** Django

---

## 🏗️ Structure du projet

```
django-collection-manager/
├── cc/                         # Configuration du projet Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── collec_management/          # Application principale
│   ├── models.py               # Collec, Element
│   ├── views.py                # Logique métier + contrôle d'accès
│   ├── forms.py                # Formulaires
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── fixtures/examples.json  # Données de démonstration
│   └── templates/              # Pages HTML (liste, détail, ajout, login…)
└── manage.py
```

---

## 🛠️ Stack technique

| | |
|---|---|
| **Framework** | Django (Python) |
| **Base de données** | SQLite |
| **Templates** | Django Templates (HTML) |
| **Auth** | Système d'authentification Django |
| **Conteneurisation** | Docker |

---

## 🚀 Installation & lancement

### Avec Python (local)

```bash
# 1. Environnement virtuel
python -m venv venv
source venv/bin/activate      # Windows : venv\Scripts\activate

# 2. Dépendances
pip install django

# 3. Configurer le SECRET_KEY (voir section ci-dessous)

# 4. Base de données + données de démo
python manage.py migrate
python manage.py loaddata examples

# 5. (optionnel) compte administrateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

Application accessible sur `http://localhost:8000`.

### Avec Docker

```bash
docker build . -f Dockerfile --tag cc
docker run -ti -p 8080:8000 -v $PWD:/home/user/workspace cc
python manage.py runserver 0.0.0.0:8000
```

---

## 🔑 Configuration du SECRET_KEY

Par sécurité, la vraie clé n'est **pas** versionnée. Dans `cc/settings.py`, la valeur est un placeholder (`django-insecure-change-me`). Génère ta propre clé avant usage :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

puis remplace la valeur de `SECRET_KEY` (idéalement via une variable d'environnement en production).

---

## 👥 Auteurs

Projet de groupe — Master Informatique, Université d'Orléans :

- **Gahlas Aicha** — [github.com/GahlasAicha](https://github.com/GahlasAicha)
- **Seffar Nordine**
- **Mimoun Ali**
- **Aissat Fatima**