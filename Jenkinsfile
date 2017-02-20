def commit_status(context, message, state="SUCCESS"){
  step([$class: 'GitHubCommitStatusSetter',
  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: context],
  statusResultSource: [$class: 'ConditionalStatusResultSource',
    results: [[$class: 'AnyBuildResult', message: message, state: state]]],
  backrefSource: [$class: 'ManuallyEnteredBackrefSource', backref: "http://google.com"]
  ])
}

/* Args:
 * repo: the repo
 * org: Github organisation or user that owwns the repo
 * sha: commit sha to update
 * pat: Github personall access token
 * state: success pending error failure
 * target_url: Url this status links to
 * description: Short description
 * context: Name of the status
 */
def github_commit_status(Map args){
  
  sha = httpRequest(args.pr_url).head.sha
  url= "https://api.github.com/repos/${args.org}/${args.repo}/statuses/${sha}?access_token=${args.pat}"
  requestBody = """
  {
    "state": "${args.state}",
    "target_url": "${args.target_url}",
    "description": "${args.description}",
    "context": "${args.context}"
  }"""
  echo("Github Status update:")
  echo(url)
  echo(requestBody)
  httpRequest(
    httpMode: 'POST',
    url: url,
    requestBody: requestBody
  )
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
      github_commit_status("ceph", "Build Complete")
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
