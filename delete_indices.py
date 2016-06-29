import urllib2

# run to delete elasticsearch indices whose name contains
# MATCH_STR as a substring. elasticsearch must be running
# on HOST

HOST = 'localhost'
MATCH_STR = '2016.02'

def get_indices():
    url = 'http://'+HOST+':9201/_cat/indices'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    indices = [f.split(' ')[2] for f in response]
    return indices

def matches(index):
    return MATCH_STR in index

def delete_indices(indices):
    base_url = 'http://'+HOST+':9201/'
    for index in indices:
        url = base_url + index
        req = urllib2.Request(url)
        req.get_method = lambda: 'DELETE'
        response = urllib2.urlopen(req)
        print response

if __name__ == '__main__':
    matching_indices = filter(matches, get_indices())
    delete_indices(matching_indices)
    
    