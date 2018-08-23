 # coding=utf-8

import psycopg2

from config import config

def routine():
    """ Connexion avec le serveur postgresql """
    conn = None
    try:
    # On lit les informations de connection
        params = config()
                
    # On établit la connexion avec le serveur Postgres
        print('Connection à la database PostgreSQL')
        conn = psycopg2.connect(**params)
                                                      
    # On créé un curseur
        cur = conn.cursor()
                                                                                  
    # On exécute une query SQL
        print('Execution de la requète')
        cur.execute('select version()')
        print('Requête terminée')
                                                                                                        
    # On récupère le résultat de la query SQL
        query_result = cur.fetchone()
                                                                                                                                        
    # On ferme le curseur PostgreSQL
        cur.close()
        print('Interruption de la communication avec la base de donnée réussie')
        return(query_result)
    except (Exception, psycopg2.DatabaseError) as error:
        return('''Erreur - Impossible d\'exécuter la requête.\n
        Contactez l\'administrateur système''')
    finally:
    # On se déconnecte du serveur 
        if conn is not None:
            conn.close()
            print('Déconnexion effectuée')
                                                                                                                                                                                                                  
                                                                                                                                                                                                                   
if __name__ == '__main__':
    connect()
