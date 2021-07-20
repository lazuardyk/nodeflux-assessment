import subprocess
import platform
import sys

class Setup:
    
    def run(self):
        self.installDependencies()
        self.createDatabase()

    def installDependencies(self):
        if platform.system() == "Windows":
            subprocess.call("pip install -r requirements.txt")
        else:
            if sys.version_info[0] < 3:
                subprocess.call("pip install -r requirements.txt")
            else:
                subprocess.call("pip3 install -r requirements.txt")
    
    def createDatabase(self):
        from app.database.migrate import Migrate
        m = Migrate()

if __name__ == "__main__":
    s = Setup()
    s.run()