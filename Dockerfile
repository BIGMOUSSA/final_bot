# Utilisation de l'image de base Python
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
COPY . .

# Installer les dépendances Python
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install rasa
#RUN    python3 -m spacy download fr_core_news_md
#RUN         pip3 install transformers

USER 1001

ENTRYPOINT ["rasa"]
# Exposer le port pour l'API Rasa
EXPOSE 5005

# Entraîner le modèle Rasa
RUN  train --config config/config_regex.yml

# Commande par défaut pour exécuter les actions Rasa
CMD ["run", "actions"]
