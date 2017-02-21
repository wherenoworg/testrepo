#!/usr/bin/env python
import json
import os
import re
import requests

def pr_api_url(pr_ui_url):
  match = re.match("https://github.com/(?P<org>[^/]*)/(?P<repo>[^/]*)/pull/(?P<prnum>[\\d]*)",
    pr_ui_url)
  gd = match.groupdict()
  url = "https://api.github.com/repos/{org}/{repo}/pulls/{prnum}".format(
    org=gd["org"],
    repo=gd["repo"],
    prnum=gd["prnum"]
  )
  url = add_token(url)
  print("{pr_ui_url} --> {url}".format(pr_ui_url=pr_ui_url, url=url))
  return url

def add_token(url):
  url = "{url}?access_token={pat}".format(url=url, pat="${args.pat}")
  print(url)
  return url

response = requests.get(pr_api_url(os.environ["CHANGE_URL"]))
print "Get pr info response: ", response
pr_info = response.json()
sha = pr_info["head"]["sha"]
body=json.dumps({
    "state": "${args.state}",
    "target_url": "${args.target_url}",
    "description": "${args.description}",
    "context": "${args.context}"
  })
url=add_token(pr_info["statuses_url"])
print "Update status request, url: {url}, body: {body}".format(url=url, body=body)
response = requests.post(url=url, data=body)
print "update status response: ", response, response.content
