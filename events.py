from services.covidtracking import Tracking
from services.covid import Covid
from utilities import send_sns

def county_data(event):
    """
    Given an event from cloudwatch
    Use COVIDPy to return daily and county data
    Return the data to sns
    """
    covid = Covid("Ohio")
    covid.get_county_data("Trumbull")
    send_sns(covid.get_resources())
    covid.get_county_data("Mahoning")
    send_sns(covid.get_resources())
    covid = Covid("Illinois")
    covid.get_county_data("Cook")
    send_sns(covid.get_resources())

def ohio_results(event):
    """
    Given an event from cloudwatch
    Get daily state data from the covidtracking project
    Return the data to sns
    """
    covid = Tracking("OH")
    send_sns(covid.get_case_date())

def illinois_results(event):
    """
    Given an event from cloudwatch
    Get daily state data from the covidtracking project
    Return the data to sns
    """
    covid = Tracking("IL")
    send_sns(covid.get_case_date())