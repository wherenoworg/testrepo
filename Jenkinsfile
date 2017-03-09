currentBuild.result == "SUCCESS"
node(){
  checkout scm
  print "the end."
  jiraComment issueKey: jiraIssueSelector(), body: "Jenkins Build [${JOB_NAME}|${JOB_URL}] #[${BUILD_NUMBER}|${BUILD_URL}] ${currentBuild.result}"
}
