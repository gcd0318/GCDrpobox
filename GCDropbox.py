from dropbox.client import DropboxClient, DropboxOAuth2Flow, DropboxOAuth2FlowNoRedirect
from dropbox.rest import ErrorResponse, RESTSocketError
#from dropbox.datastore import DatastoreError, DatastoreManager, Date, Bytes
from dropbox import rest as dbrest

class GCDropbox(DropboxClient):
    def __init__(self, app_key, app_secret, locale='UTF-8'):
        oauth_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        authorize_url = oauth_flow.start()
        print(authorize_url)
        access_token, user_id = oauth_flow.finish(input("code: ").strip())
        print(access_token)
        DropboxClient.__init__(self, access_token, locale)
    def upload(self, fp):
        pass
    def get_list(self, path):
        pass

def parse(client, root='/'):
    cont = client.metadata(root)['contents']
    print(root, len(cont))
    res = []
    for item in cont:
        if(item['is_dir']):
            res = res + parse(client, item['path'])
        else:
            res.append(item)
    return res

if __name__ == "__main__":
    save_path = '/mnt/share/dropbox/'
    app_key = '1lso43s8iv08kv2'
    app_secret = 'pnt9p61hg42vpwq'
    access_token = None

    for i in parse(GCDropbox(app_key, app_secret)):
        print(i['path'], i['bytes'])

