import shutil
import sys
from pathlib import Path


def make_archive(source, destination):
    """https://stackoverflow.com/a/50381223"""

    source = Path(source)
    destination = Path(destination)
    base = destination.name
    name = destination.stem
    archive_format = base.split(".")[1]
    archive_from = str(source.parent)  # /Users/.../PlotVars
    archive_to = name  # plots
    shutil.make_archive(name, archive_format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, archive_format), destination)


if __name__ == "__main__":
    make_archive(sys.argv[1], sys.argv[2])
