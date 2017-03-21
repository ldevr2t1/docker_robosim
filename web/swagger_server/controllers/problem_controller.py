import connexion, pymongo, json
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from flask_api import status
from pymongo import MongoClient
from flask import jsonify
from flask_api import status


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
    return 'do some magic!'


def delete_problem_all_versions(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID and version
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


def get_problem_all_versions(problem_id):
    """
    Problems
    Returns all problem versions for a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    return 'do some magic!'


def update_problem(problem_id, version, problem):
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
    if connexion.request.is_json:
        problem = Problem.from_dict(connexion.request.get_json())
    return 'do some magic!'
