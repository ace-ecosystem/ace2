from ace2 import *

def run(event:dict, context:dict) -> dict:
    ''' Lambda handler for running analysis

    Args:
        event (dict): the analysis state object to run
        context (dict): the context of the lambda function (we dont use this for anything)

    Returns:
        dict: the new analysis state object
    '''

    # load the analysis, run it and return the new state
    return Analysis(**event).run()