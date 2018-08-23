# Bot de Monitoring Telegram

## Quelles sont les fonctionnalités de ce bot ? 

Ce bot permet a pour vocation de permettre de faire de checkup sur une base de ddonnées PostgreSQL. Il est à la fois capable de résoudre des requètes à la demande via des commandes sur un channel, et de réaliser des routines de checkup automatiques et régulières. 

## Comment lancer ce bot 

### Requirements 

Dans un premier temps, il s'agit de cloner le repo git. 
Cela se fait à l'aide de la commande 

<pre><code> git clone https://github.com/unchartech/telegram_bots.git </pre></code>

Si vous êtes sur debian, ubuntu ou Kali, git peut s'installer en tapant la ligne suivante dans un terminal : 

<pre><code> sudo apt install git </pre></code>

Sur Windows, il existe des utilitaires comme gitkraken, mais vous pouvez tout simplement le télécharger en format \.zip sur https://github.com/unchartech/telegram_bots.git\.
Cette solution fonctionne aussi sur linux mais est moins rapide. 

### Lancer ce bot

Si vous voulez faire les choses proprement, je vous conseille de lancer 

<pre><code>cd telegram_bot
sudo apt install virtualenv
virtualenv -p python3 tgbot_virtualenv
source tgbot_virtualenv/bin/activate</pre></code>

C'est plus propre que d'installer les librairies en global. On peut ensuite lancer

<pre><code>pip3 -r install requirements.txt </pre></code>

Qui installe les paquets nécessaires au bon fonctionnement du bot.

Enfin, il vous faut prendre le template "database_template.ini", le renommer "database.ini", et remplacer les informations de connexion par celles que vous désirez mettre en place. 

Une fois ceci fait, vous pouvez lancer la commande 

<pre><code>chmod +x tgbot.py
 nohup /path/to/tgbot.py &  </pre></code>

Qui lance le bot à proprement parler.
chmod +x donne l'autorisation d'exécuter le code, nohup ... & permet de faire tourner le programme en arière plan (sans ça, le programme s'arrêterait de tourner dès que le terminal est fermé, ce qui est assez moyen d'un point de vue uptime).

On pourra vérifier que le programme est bien en train de fonctionner en lançant <pre><code>ps aux | grep tgbot.py </pre></code>.

Afin d'interrompre l'exécution, on pourra lancer la commande ci-dessus, relever l'identifiant unique du programme et lancer <pre><code>kill id_du_programme </pre></code>

## Quelques considérations sur la structure du code

### Config.py

config.py contient la fonction qui initie la connexion avec la base de données distante. Il utilise les identifiants de connexion de database.ini, que je n'ai pas commités pour des raisons évidentes.
Ce fichier n'a pas vocation à être édité.

### Queries_template.py

Ce fichier .py contient le template de requête SQL. Il contient une unique fonction, sql_query, qui prend une query SQL en argument, ouvre la connexion avec le serveur, exécute la query, récupère le résultat, ferme la connexion et renvoie le résultat. Ce fichier n'a pas vocation à être changé.

La fonction est appelée par tgbot.py, les arguments sont directement fournis dans tgbot.py. 

### Routine.py

Ce fichier contient le programme permettant de checker la base de donnée toutes les 15 minutes. Il est appelé par tgbot.py toutes les 15 minutes et renvoie une exception chaque fois que certaines statiques varient dans certaines proportionsprédéterminées. Un changement des seuils ou des ratios à considérer devra être fait directement dans ce fichier ; un changement de la fréquence devra être fait dans tgbot.py.  

### tgbot.py

C'est la foinction principale du bot, qui initie la connexion avec telegram et lance les routines. Il contient entre autres le token unique d'identification du bot (qu'il faut donc récupérer) ainsi que l'identifiant de la conversation, qui permetttent au bot de communiquer avec l'API telegram. Afin de récupérer l'administration du bot, il faut créer un nouveau bot et remplacer 'insert-bot-token-here' et 'insert-conversation-identifier-here' (cette seconde étape n'est pas obligatoire). Pour ça, ça se passe ici : https://telegram.org/blog/bot-revolution. 

En outre, il contient l'indentifiant unique de la conversation Unchartech Monitoring - qu'il faudra éventuellement remplacer - qui lui permet d'envoyer des messages sur cette conversation. 

### Database_template.ini

Il s'agit d'un template de database. Le parser de config utilise les infos contenues dans ce fichier pour s'authentifier. Evidemment la version originale du fichier contient des identifiants et mots de passe, et n'est donc pas comitée. Il faut remplacer les identifiants et IP que j'ai mis par ceux désirés, et renommer le fichier database.ini.

### Requirements.txt

Ce fichier contient les librairies python utilisées par le projet et qu'il faudra installer afin de faire tourner le projet   

### README.md

Il s'agit du fichier en format markdown que vous lisez en ce moment, la documentation.

### Botfather.txt

En envoyant la commande /setcommands au botfather et en lui envoyant ensuite le contenu de botfather.txt, vous activez les suggestions de commande pour le bot de monitoring 
