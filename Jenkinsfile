def getTrigger(){
    print(currentBuild.getBuildCauses()[0]._class)
    switch (currentBuild.getBuildCauses()[0]._class){
        case 'hudson.model.Cause$UserIdCause':
            return "User"
            break;
        case 'hudson.triggers.TimerTrigger$TimerTriggerCause':
            return "Timer"
            break;
        case 'hudson.triggers.SCMTrigger.SCMTriggerCause':
            return "SCM"
            break;
        case 'jenkins.branch.BranchEventCause':
            return 'git'
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
                    print(getTrigger())
                }
            }
        }
    }
}
