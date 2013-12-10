from dropbox.client import DropboxClient, DropboxOAuth2Flow, DropboxOAuth2FlowNoRedirect
from dropbox.rest import ErrorResponse, RESTSocketError
#from dropbox.datastore import DatastoreError, DatastoreManager, Date, Bytes
from dropbox import rest as dbrest

class GCDropbox(DropboxClient):
    def __init__(self, app_key, app_secret, locale='UTF-8'):
        oauth_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        authorize_url = oauth_flow.start()
        print("1, Go to: " + authorize_url + "\n",\
              "2, Click \"Allow\" (log in if necessary)\n",\
              "3, Copy the authorization code\n")
        access_token, user_id = oauth_flow.finish(input("Enter the authorization code here:").strip())
        DropboxClient.__init__(self, access_token, locale)
    def upload(self, fp):
        pass
    def get_list(self, path):
        pass

if __name__ == "__main__":
    from config import *
    gcd = GCDropbox(app_key, app_secret)
    metadata = gcd.metadata('/dt2')
    print(metadata)
