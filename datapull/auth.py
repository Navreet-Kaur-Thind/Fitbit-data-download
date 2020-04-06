import fitbit
from . import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime

def authorize(client_id, client_secret):
    server = Oauth2.OAuth2Server(client_id, client_secret)
    
    # Note that I've modified this method to print out the auth URL, which we need to follow by hand since the window.open command doesn't seem to be working properly
    server.browser_authorize()
    
    access_token = str(server.fitbit.client.session.token['access_token'])
    refresh_token = str(server.fitbit.client.session.token['refresh_token'])

    return fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token=access_token, refresh_token=refresh_token)