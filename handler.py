from events import county_data, illinois_results, ohio_results
import logging


log = logging.getLogger(__name__)

def entry(event, context):
    """
    Distributes events triggering the lambda
    """
    log.info(f"Event Recieved! {event}")
    event_types = {
        'ohio': ohio_results, # Ohio State results
        'illinois': illinois_results, # IL State results
        'county': county_data, # county level calls
    }
    for event_type in event:
        if event_type in event_types:
            event_types[event_type](event)