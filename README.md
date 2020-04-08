# COVID19 State Tracker

Lambda to pull state and county level information on a set interval and return those to an sns topic.

## About

Small extendable application to get COVID-19 case information from a variety of states and counties.

Currently evaluating 2 states and 3 counties within them. Lambda executes different covid data retrievals following a matching cloudwatch event.

Special thanks to the folks who put together [COVID19py](https://github.com/Kamaropoulos/COVID19Py), [Corona Virus Tracker](https://github.com/ExpDev07/coronavirus-tracker-api) and the [Covid Tracking Project](https://github.com/COVID19Tracking/covid-tracking-api)for their projects which made this so much easier than scraping html myself :)

## Entending Usage

If you would like to evaluate additional states or counties simply add a new event to the events file, specifiy what you're triggering json key will be and then add the corresponding cloudwatch event.