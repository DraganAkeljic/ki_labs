import connexion

import main


def add_candidate():
    req = connexion.request.json
    name, time = get_name_time(req)


def get_candidate_time(id):
    pass


def add_interviewer():
    req = connexion.request.json
    name, time = get_name_time(req)


def get_interviewer_time(id):
    pass


def arrange():
    """
    Find a match for specific candidate and interviewer/s

    interviewers_id is list of interviewer id's
    :return:
    """
    req = connexion.request.json
    candidate_id = req["candidate_id"]
    interviewers_id = req["interviewers_id"]
    return main.arrange_interview(candidate_id, interviewers_id)


def get_name_time(req):
    """
    Extract name and time dict from request
    :param req: request sent
    :return: tuple of name and time dict
    """
    name = req["name"]
    time = req["time"]
    return name, time
