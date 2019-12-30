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
        echo 'building python'
      }
    }
    stage('Test build') {
		agent {
			dockerfile true
		}
      steps {
        sh 'python -m unittest -v test_unit'
      }
    }
  }
  post {
	always {
	 sh 'docker system prune -f'
	}
  }
}
