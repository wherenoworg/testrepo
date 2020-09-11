def getTrigger(){
    print(currentBuild.getBuildCauses()[0]._class)
    switch (currentBuild.getBuildCauses()[0]._class){
        case 'hudson.model.Cause$UserIdCause':
            return "User"
            break;
        case 'hudson.triggers.TimerTrigger$TimerTriggerCause':
            return "Timer"
            break;
        case ['hudson.triggers.SCMTrigger.SCMTriggerCause',
              'jenkins.branch.BranchEventCause',
              'jenkins.branch.BranchIndexingCause']:
            if (env.CHANGE_ID != null){
                return 'pr'
            } else if (env.TAG_NAME != null){
                return 'tag'
            } else {
                return 'push'
            }
            break;
    }
}

pipeline {
    agent any
    stages {
        stage('a stage'){
            steps {
                sh 'ls'
                script {
                    print("CHANGE_ID: ${env.CHANGE_ID}")
                    print(getTrigger())
                }
            }
        }
    }
}
