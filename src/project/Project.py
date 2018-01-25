import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.directory.Directory import Directory
from src.makefile.Makefile import Makefile

class ProjectAlreadyExistsException(Exception):
    def __init__(self, *args, **kwargs):
        super(ProjectAlreadyExistsException, self).__init__(self, *args, **kwargs)


class Project():
    def __init__(self, name, path=None):
        self.name = name
        self.path = path

        try:
            self.root_directory = Directory(self.path or self.name)
            self.bin_directory = Directory("{path}/bin".format(path=self.root_directory.path))
            self.obj_directory = Directory("{path}/obj".format(path=self.root_directory.path))
            self.src_directory = Directory("{path}/src".format(path=self.root_directory.path))
        except:
            self.root_directory.remove()
            raise ProjectAlreadyExistsException("A directory called '{}' exists already!".format(
                self.path or self.name
            ))

        self.makefile = Makefile(self.name, path=self.path or self.name)

        self.makefile.write_makefile()
