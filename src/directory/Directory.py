import os, errno, shutil

class Directory():
    def __init__(self, path):
        self.path = path

        try:
            os.makedirs(self.path)
        except OSError as e:
            #directory already exist
            if e.errno != errno.EEXIST:
                raise

    def remove(self):
        shutil.rmtree(self.path)
