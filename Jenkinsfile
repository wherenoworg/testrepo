def commit_status(context, message, state="SUCCESS"){
  step([$class: 'GitHubCommitStatusSetter',
  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: context],
  statusResultSource: [$class: 'ConditionalStatusResultSource',
    results: [[$class: 'AnyBuildResult', message: message, state: state]]],
  backrefSource: [$class: 'ManuallyEnteredBackrefSource', backref: "http://google.com"]
  ])
}



/* Args:
 * pat: Github personall access token
 * state: success pending error failure
 * target_url: Url this status links to
 * description: Short description
 * context: Name of the status
 */
def github_commit_status(Map args){
  sh """
    python <<EOF
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
body={
    "state": "${args.state}",
    "target_url": "${args.target_url}",
    "description": "${args.description}",
    "context": "${args.context}"
  }
url=add_token(pr_info["statuses_url"])
print "Update status request, url: {url}, body: {body}".format(url=url, body=body)
response = requests.post(url=url, data=body)
print "update status response: ", response, response.content

EOF
"""
}

node(){
  checkout scm
  withCredentials([
    string(
      credentialsId: "hughsaunders_github_pat",
      variable: "github_pat"
   )
  ]){
    sha = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
    stage("Swift"){
      echo("I'm the swift steage")
      github_commit_status(
        repo: "testrepo",
        org: "wherenoworg",
        pr_url: env.CHANGE_URL,
        pat: env.github_pat,
        state: "success",
        target_url: "http://google.com",
        description: "um ok.",
        context: "swift"
     )
    }

    stage("Ceph"){
      echo("I'm the ceph stage")
      github_commit_status(
        repo: "testrepo",
        org: "wherenoworg",
        pr_url: env.CHANGE_URL,
        pat: env.github_pat,
        state: "success",
        target_url: "http://google.com",
        description: "where am I?",
        context: "ceph"
     )

    }//stage
  }//creds
}//node
