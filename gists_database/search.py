from .models import Gist

def search_gists(db_connection, **kwargs):
    #Check if there are keyword args
    if not kwargs:
        query = "SELECT * FROM gists"
    #Check if github_id in kwargs
    elif 'github_id' in kwargs:
        query = "SELECT * FROM gists WHERE github_id = :github_id"
    #Check if created_at in kwargs
    elif 'created_at' in kwargs:
        query = "SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)"
    
    cursor = db_connection.execute(query,kwargs)
    result = []
    for gist in cursor:
        result.append(Gist(gist))
    
    return result