import COVID19Py
import logging

log = logging.getLogger(__name__)

class Covid(object):
    """
    Class to pull information from COVIDPy
    """
    def __init__(self, state=None, active=True):
        self.active = active
        self.state = state
        self.resources = {}

    def get_us_locations(self):
        """
        Get all US data from csbs
        Set a resource UnitedStates
        """
        covid19 = COVID19Py.COVID19(data_source="csbs")
        locations = covid19.getLocations()
        return locations

    def get_state_data(self):
        """
        Given a state name
        Fetch counts of confirmed cases, deaths and recoverd
        Return them
        """
        self.resources[self.state] = {}
        state_list = []
        for county in self.get_us_locations():
            if county["province"] == self.state:
                log.info(f'{self.state} found')
                state_list.append(county)
            else:
                pass
        confirmed_cases = []
        confirmed_deaths = []
        confirmed_recoveries = []
        log.info('Doing math on latest case counts')
        for latest in state_list:
            confirmed_cases.append(latest['latest']['confirmed'])
            confirmed_deaths.append(latest['latest']['deaths'])
            confirmed_recoveries.append(latest['latest']['recovered'])

        self.resources[self.state]["ConfirmedCases"] = sum(confirmed_cases)
        self.resources[self.state]["ConfirmedDeaths"] = sum(confirmed_deaths)
        self.resources[self.state]["ConfirmedRecoveries"] = sum(confirmed_recoveries)

        return self.resources[self.state]

    def get_county_data(self, county):
        """
        Given a state and county
        Fetch counts of confirmed cases, deaths and recoverd
        Return them
        """
        self.resources[self.state] = {}
        self.resources[self.state][county] = {}
        for province in self.get_us_locations():
            if province["province"] == self.state:
                if province["county"] == county:
                    target = province

        self.resources[self.state][county] = target['latest']

        return self.resources[self.state][county]

    def get_resources(self):
        """
        Return resources dictionary
        """
        return self.resources