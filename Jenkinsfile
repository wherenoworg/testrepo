currentBuild.result = "SUCCESS"
node(){
  checkout scm
  print "the end.."
  //key = jiraIssueSelector() // <-- throws NPE.
  //print("issue key: ${key}")
  
  // test with hard coded issue key. 
  jiraComment(
    issueKey: "IT-18", 
    body: "Jenkins Build [${JOB_NAME}|${JOB_URL}] [#${BUILD_NUMBER}|${BUILD_URL}] ${currentBuild.result}"
  )
  // This gives unsupported run type
  //step([$class: 'hudson.plugins.jira.JiraIssueUpdater', 
  //  issueSelector: [$class: 'hudson.plugins.jira.selector.DefaultIssueSelector'], 
  //]) 
}
