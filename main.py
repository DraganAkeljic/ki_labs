from datetime import date, timedelta


def arrange_interview(candidate_id, interviewers_id):
    """
    Get the data from the database (candidate_data & interviewers_data)
    :param candidate_id: candidate id sent from the UI
    :param interviewers_id: list of intervbiewers id sent from the UI
    :return: possible date/times for the interview
    """
    cadidate_data = None
    interviewers_data = None
    check_availability(cadidate_data, interviewers_data)


def check_availability(candidate, interviewers):
    """
    Get candidate and interviewers date/time availability
    :param candidate: all the data from the db
    :param interviewers: all the data from the db
    :return: possible interview date/time/s
    """
    candidate_availability = get_availability(candidate)
    interviewers_availability = get_interviewers_availability(interviewers, candidate_availability)
    # flat the list so it would be easier for us to find the duplicates , which are the date/time of possible interview
    flatten_list_of_date_times = [y for x in interviewers_availability.values() for y in x]
    return set([x for x in flatten_list_of_date_times if flatten_list_of_date_times.count(x) > 1])


def get_interviewers_availability(interviewers, candidate_availability):
    """
    Loop over all the interviewers and check possible interview date/time for that candidate
    :param interviewers: interviewers data
    :param candidate_availability: candidate availability data
    :return: dict with all date/times for each interviewer
    """
    interviewers_dict = {}
    for interviewer, availability in interviewers.items():
        interviewer_availability = get_availability(availability)
        interviewers_dict[interviewer] = candidate_interviewer_availability_match(interviewer_availability, candidate_availability)
    return interviewers_dict


def candidate_interviewer_availability_match(interviewer_availability, candidate_availability):
    match = []
    for date_avail, time_avail in candidate_availability.items():
        for time in time_avail:
            if date_avail in interviewer_availability and time in interviewer_availability[date_avail]:
                match.append("{date} - {time}".format(date=date_avail, time=time))
    return match


def get_availability(availability):
    """
    update availability_dict with each date/s
    :param availability:
    :return:
    """
    availability_dict = {}
    for available in availability:
        time_range = get_time_range(available["timeStart"], available["timeEnd"])
        availability_dict.update(get_availability_dict(available["dateStart"], available["dateEnd"], time_range))
    return availability_dict


def get_availability_dict(date_start, date_end, time_range):
    """
    create availability dictionary (keys: dates str, values: list of time tuples)
    :param date_start:
    :param date_end:
    :param time_range:
    :return:
    """
    availability_dict = {}
    start = date_start.split(".")
    start_dt = date(int(start[2]), int(start[1]), int(start[0]))
    end = date_end.split(".")
    end_dt = date(int(end[2]), int(end[1]), int(end[0]))
    for n in range(int((end_dt - start_dt).days) + 1):
        dt = start_dt + timedelta(n)
        availability_dict[dt.strftime("%d.%m.%Y.")] = time_range
    return availability_dict


def get_time_range(start, end):
    """
    create a list of time tuples
    :param start:
    :param end:
    :return:
    """
    time_range = []
    for i in range(int(start), int(end)):
        time_range.append((i, i + 1))
    return time_range
