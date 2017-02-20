def commit_status(context, message, state="SUCCESS"){
  step([$class: 'GitHubCommitStatusSetter',
  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: context],
  statusResultSource: [$class: 'ConditionalStatusResultSource',
    results: [[$class: 'AnyBuildResult', message: message, state: state]]],
  backrefSource: [$class: 'ManuallyEnteredBackrefSource', backref: "http://google.com"]
  ])
}

node(){
  sh "env"
  stage("Swift"){
    echo("I'm the swift steage")
    commit_status("swfit", "Build Complete")
  }
  
  stage("Ceph"){
    echo("I'm the ceph stage")
    commit_status("ceph", "Build Complete")
    
  }

}
