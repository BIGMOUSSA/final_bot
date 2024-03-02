# Utilisation de l'image de base Python
FROM rasa/rasa:3.6.18-full


WORKDIR /myvol

#VOLUME .
# Copier les fichiers nécessaires dans le conteneur

COPY . .

# Installer les dépendances Python
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip3 install rasa
#RUN    python3 -m spacy download fr_core_news_md
#RUN         pip3 install transformers
RUN rasa train

USER 1001

#ENTRYPOINT ["rasa"]
# Exposer le port pour l'API Rasa
EXPOSE 5005

# Entraîner le modèle Rasa
#RUN  train --config config/config_regex.yml

# Commande par défaut pour exécuter les actions Rasa
#CMD ["run", "actions"]
CMD ["rasa", "run", "-m", "models", "--enable-api"]

