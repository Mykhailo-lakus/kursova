import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.*
import jenkins.model.*
import hudson.util.Secret
import org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl


// Функція для отримання змінних середовища
def getEnvVariable(String name) {
    return System.getenv(name)
}

def dockerUserName = getEnvVariable('DOCKERHUB_USERNAME')
def dockerPassword = getEnvVariable('DOCKERHUB_PASSWORD')

def tgBotToken = getEnvVariable('MY_TG_BOT_TOKEN')

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

def creds = new UsernamePasswordCredentialsImpl(CredentialsScope.GLOBAL, "dockerhub_token", "Description", dockerUserName, dockerPassword)
def tgBotTokenCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "tg_bot_token", "TG Bot Token", Secret.fromString(tgBotToken))
store.addCredentials(domain, creds)
store.addCredentials(domain, tgBotTokenCreds)