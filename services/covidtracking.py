import requests
import logging

log = logging.getLogger(__name__)

class Tracking(object):
    """
    Class to call the covidtracking project
    https://covidtracking.com
    """
    def __init__(self, state=None, active=True):
        self.active = active
        self.state = state
        self.url = 'http://covidtracking.com/api/states?state=%s' % state
        self.resources = {}

    def get_case_date(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            log.error(f'{response.status_code} returned')
            return
        data = response.json()
        if data['state'] != self.state:
            log.error(f'Provided state: {self.state} does not match response data')
            return
        self.resources[self.state] = {}
        self.resources[self.state]["TotalTested"] = data['totalTestResults']
        self.resources[self.state]["ConfirmedCases"] = data['positive']
        self.resources[self.state]["ConfirmedDeaths"] = data['death']
        self.resources[self.state]["Hopsitizations"] = data['hospitalizedCurrently']
        self.resources[self.state]["InIcu"] = data['inIcuCurrently']

        return self.resources