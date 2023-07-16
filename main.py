
import re
from packaging import version

from github import Github
from github import Auth # Authentication is defined via github.Auth



class Updater():
    authentication = Auth.Token("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")
    github = Github(auth=authentication)
    repo = github.get_repo("lawrence-matei/git-update-tester")


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

    def get_latest_release(self):
        release = self.repo.get_latest_release()

        return release

    def get_tags(self): # this is a label that contains info of the version
        tags = self.repo.get_tags()

        return list(tags)

    def __init__(self):
        version = self.get_version()
        print("version file: ", version)

        release = self.get_latest_release()
        print("latest release: ", release)

        tags = self.get_tags()
        latest_tag = tags[-1]
        print("latest tags: ", latest_tag)
        print("latest tag name: ", latest_tag.name)



if __name__ == '__main__':
    Updater()
