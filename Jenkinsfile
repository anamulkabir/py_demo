pipeline {
  agent {
  dockerfile true
  }
  stages {
    stage ('Code pull'){
        steps{
              checkout scm
        }
    }
    stage('build') {
      steps {
        echo 'building python'
      }
    }
    stage('Test build') {
      steps {
        sh 'python -m unittest -v test_unit'
      }
    }
	stage('Clean dangling images') {
	 agent any	
	  steps {
	   sh 'docker system prune -f'
	  }
	}

  }
}
