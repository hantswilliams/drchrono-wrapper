import json
import iso8601
import tzlocal
import pytz
import itertools
import sys
from requests import request
from requests.exceptions import HTTPError

DRCHRONO_API_URL = "https://drchrono.com/api/"

user_agent = "drchronowrapper-0.0.5"

_credentials = {
    "api_key": None,
}

class DrchronoException(Exception):
    pass

def set_credentials(username, api_key):
    """Set the drchrono api credentials to use."""
    _credentials["user"] = username
    _credentials["api_key"] = api_key

def set_user_agent(agent):
    """Set User-Agent in the HTTP requests.
    :keyword param agent: string
    ex. 'test agent 1'
    """
    global user_agent
    user_agent = agent

def set_timezone(new_tz=None):
    """Set the timezone for datetime fields.
    By default is your machine's time.
    If it's called without parameter sets the
    local time again.
    :keyword param new_tz: timezone string
    ex. 'Europe/Athens',
        'Asia/Seoul',
        'America/Los_Angeles',
        'UTC'
    :return
        None
    """
    global tz
    if new_tz:
        tz = pytz.timezone(new_tz)
    else:
        tz = tzlocal.get_localzone()

def get_credentials():
    """Retrieve the challonge.com credentials set with set_credentials()."""
    return _credentials["api_key"]


def get_timezone():
    """Return currently timezone in use."""
    return tz

def fetch(method, uri, params=None, data=None):
    """Fetch the given uri and return the contents of the response."""
    
    if not _credentials["api_key"]:
        raise DrchronoException("No API key set. Use set_credentials() first.")

    if method == "POST" or method == "PUT":
        r_data = {"data": params}
    else:
        r_data = {"params": params}

    # build the HTTP request and use basic authentication
    url = "https://%s/%s" % (DRCHRONO_API_URL, uri)

    try:
        response = request(
            method, url, headers={"User-Agent": user_agent}, auth=get_credentials(), **r_data
        )
        response.raise_for_status()

    except HTTPError:
        if response.status_code != 422:
            response.raise_for_status()
        # wrap up application-level errors
        doc = response.json()
        if doc.get("errors"):
            raise DrchronoException(*doc["errors"])

    return response