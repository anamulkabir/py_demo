pipeline {
  agent any
  stages {
    stage ('Code pull'){
        steps{
              checkout scm
        }
    }
    stage('build') {
      steps {
        echo 'building'
      }
    }
    stage('Test build') {
      steps {
        sh pythoun -m unittest -v
      }
    }

  }
}
