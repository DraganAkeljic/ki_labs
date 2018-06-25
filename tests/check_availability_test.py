import pytest

import main

interviewer_1 = [{
    "dateStart": "01.05.2018",
    "dateEnd": "05.05.2018",
    "timeStart": "9",
    "timeEnd": "16"
}]

interviewer_2 = [
    {
        "dateStart": "01.05.2018",
        "dateEnd": "01.05.2018",
        "timeStart": "12",
        "timeEnd": "18"
    },
    {
        "dateStart": "02.05.2018",
        "dateEnd": "02.05.2018",
        "timeStart": "9",
        "timeEnd": "12"
    },
    {
        "dateStart": "03.05.2018",
        "dateEnd": "03.05.2018",
        "timeStart": "12",
        "timeEnd": "18"
    },
    {
        "dateStart": "04.05.2018",
        "dateEnd": "05.05.2018",
        "timeStart": "9",
        "timeEnd": "12"
    }
]

candidate = [
    {
        "dateStart": "02.05.2018",
        "dateEnd": "02.05.2018",
        "timeStart": "9",
        "timeEnd": "10"
    },
    {
        "dateStart": "03.05.2018",
        "dateEnd": "04.05.2018",
        "timeStart": "9",
        "timeEnd": "11"
    }
]

interviewers = {
    "interviewer_1": interviewer_1,
    "interviewer_2": interviewer_2
}


def test_check_availability():
    res = main.check_availability(candidate, interviewers)
    assert res is not None
    assert res == {'04.05.2018. - (10, 11)', '04.05.2018. - (9, 10)', '02.05.2018. - (9, 10)'}


def test_check_availability_fail():
    res = main.check_availability(candidate, interviewers)
    assert res is not None
    assert res != {'04.05.2018. - (10, 11)', '04.05.2018. - (9, 10)', '02.05.2018. - (9, 11)'}