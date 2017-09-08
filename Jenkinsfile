node(){
  stage("checkout"){
    checkout scm
  }
  stage("Execute Reno"){
    sh "./reno.sh"
  }
  stage("Bashate Reno"){
    sh """
      virtualenv venv
      . venv/bin/activate
      pip install bashate
      bashate -v reno.sh
    """
  }
}//node
