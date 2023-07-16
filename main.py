
import re
from packaging import version

class Updater():

    def get_version(self):
        VERSIONFILE = "_version.py"
        verstrline = open(VERSIONFILE, "rt").read()
        VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
        mo = re.search(VSRE, verstrline, re.M)
        if mo:
            verstr = mo.group(1)
            return verstr
        else:
            raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

    def compare_versions(self, local_version, repo_version):
        return version.parse(local_version) < version.parse(repo_version)

    def __init__(self):
        version = self.get_version()
        print(version)



if __name__ == '__main__':
    Updater()
