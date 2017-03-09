currentBuild.result == "SUCCESS"
node(){
  checkout scm
  print "the end.."
  //key = jiraIssueSelector()
  //print("issue key: ${key}")
  //jiraComment issueKey: key, body: "Jenkins Build [${JOB_NAME}|${JOB_URL}] #[${BUILD_NUMBER}|${BUILD_URL}] ${currentBuild.result}"
  
  
  step([$class: 'hudson.plugins.jira.JiraIssueUpdater', 
    issueSelector: [$class: 'hudson.plugins.jira.selector.DefaultIssueSelector'], 
  ]) 
}
