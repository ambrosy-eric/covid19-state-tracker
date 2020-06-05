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
        self.url = 'http://covidtracking.com/api/states?state=%s' % state.lower()
        self.resources = {}

    def get_case_date(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise (e.response.text)
        data = response.json()
        if data['state'] != self.state:
            log.error(f'Provided state: {self.state} does not match response data')
            raise Exception('Invalid State returned')
        self.resources[self.state] = {}
        self.resources[self.state]["TotalTested"] = data['totalTestResults']
        self.resources[self.state]["ConfirmedCases"] = data['positive']
        self.resources[self.state]["ConfirmedDeaths"] = data['death']
        self.resources[self.state]["Hopsitizations"] = data['hospitalizedCumulative']
        self.resources[self.state]["InIcu"] = data['inIcuCumulative']
        self.resources[self.state]["Recovered"] = data['recovered']

        return self.resources