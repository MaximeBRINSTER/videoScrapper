Je n'ai pas réussi à mettre les commentaires comme demandé dans l'exercice. 

J'ai aussi dû mettre en commentaire le nombre de likes, alors que cela fonctionnait sur des liens choisis. 
Il a cependant cessé de fonctionner lorsque j'ai utilisé le fichier json. 

Pour le output.json, je n'ai pas réussi à mettre bien en forme le fichier. 
Toutes les données se retrouvent dans un seul indice du dictionnaire

Le scrapper.py contient une classe videoScraper qui initialise un BeautifulSoup à partir d'un lien hypertexte d'une vidéo youtube. 
Il récupère ensuite le titre de la vidéo, le nom de la chaine, la date de publication, le nombre de vues, la description et les liens dans la description et les écrit sur un fichier json "output.json". 

Les tests marqués dans le fichier test_.py dans le dossier tests sont essetiellement des tests de type ou de taille de la donnée. 
En effet, une donnée marquée dans le mauvais type ou trop petite peut affecter le résultat et souvent amène à une erreur.
