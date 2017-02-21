node(){
  checkout scm
  this.binding.variables.each {k,v -> println "$k = $v"}
  sh "env"
  withCredentials([
    string(
      credentialsId: "hughsaunders_github_pat",
      variable: "github_pat"
   )
  ]){
    sha = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
    stage("Swift"){
      echo("I'm the swift steage")
      common.githubStatus(
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
      common.githubStatus(
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
