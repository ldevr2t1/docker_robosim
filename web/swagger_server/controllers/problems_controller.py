from . import utilities

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
db = client.path_db

def add_problem(problem):
    """
    Creates a new problem and returns a problemID with default version 0
    
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    #find largest pid
    try:
        str_body = str(problem).replace('\'', '\"')
        problem = Problem.from_dict(connexion.request.get_json())
        pid = db.posts.find({}, {'problem_id': 1}).sort({'problem_id': -1}).limit(1)

        if pid is not None:
            pid = int(pid) + 1
        else:
            pid = 0

        insert_json(pid, 0, problem)
        return jsonify({"problem_id": pid}), status.HTTP_201_CREATED  
    except ValueError:
        return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE



def get_problems():
    """
    Problems
    Returns a list of all of the Problems generated. This can be an empty list. 

    :rtype: List[int]
    """
    array = []
    for post in db.posts.find({},{"problem_id":1}):
        array.append(post)
    if (len(array) == 0):
        return jsonify(Error(404, "No problems in database")), status.HTTP_404_NOT_FOUND
    return jsonify(array)
