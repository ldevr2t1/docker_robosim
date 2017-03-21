from utilities import *

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
db = client.path_db

def delete_problem(problem_id, version):
    """
    Delete Problem
    This removes the problem by the given ID and version
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the problem being manipulated
    :type version: int

    :rtype: None
    """
    if db.posts.delete_many({"problem_id": str(uid), "version": str(version)}).deleted_count == 0:
        return get_status(404, "Problem not found"), status.HTTP_404_NOT_FOUND
    else:
        return get_status(200, "Successfully Deleted")


def get_problem(problem_id, version):
    """
    Problems
    Returns a specific problem given its pid and version 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the problem being manipulated
    :type version: int

    :rtype: Problem
    """
    problem = db.posts.find_one({'problem_id':problem_id, 'version': version}, {'body':1})
    if (not problem):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    else:
        return jsonify(problem)


def get_problem_all_versions(problem_id):
    """
    Problems
    Returns all problem versions for a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    array = []
    for post in db.posts.find({'problem_id': str(problem_id)}, {'version': 1, 'body': 1})
        array.append(post)
    if (len(array) == 0):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    else:
        return jsonify(array)


def update_problem(problem_id, problem):
    """
    Update the existing problem
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the problem being manipulated
    :type version: int
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    #if the problem exists, generate a new object and submit the values under a new version
    try:
        if connexion.request.is_json:
            body = GenericObject.from_dict(connexion.request.get_json())

            if db.posts.find_one({'problem_id':problem_id, 'version': version}, {'body':1}) is None:
                return get_status(404, "Problem not found"), status.HTTP_404_NOT_FOUND
            else:
                version = db.posts.find({}, {'version': 1}).sort({'version': -1}).limit(1)

                if version is not None:
                    version = int(version) + 1
                else:
                    version = 0

                str_body = str(problem).replace('\'', '\"')
                problem = Problem.from_dict(connexion.request.get_json())

                insert_json(problem_id, version, problem)
                return jsonify({"version": version})   
        else:
            return get_status(405, "Validation Error - Invalid JSON")
    except ValueError:
        return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE