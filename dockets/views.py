from django.shortcuts import render
from django.http import HttpResponse

import json, os

def index(request):
    dirname = os.getcwd() + "/dockets/docket_data"

    docket_data = []
    for filename in os.listdir(dirname):
        with open(os.path.join(dirname, filename), 'r') as f: # open in readonly mode
            data=f.read()

            obj = json.loads(data)
            docket_data.append(data)

    return HttpResponse(f"Hello, world. You're at the dockets index. there are {len(docket_data)} files to display")