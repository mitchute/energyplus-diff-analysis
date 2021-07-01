import sys
from shutil import make_archive


def zip_plots(dir_to_zip):
    make_archive(dir_to_zip, "zip")


if __name__ == "__main__":
    zip_plots(sys.argv[1])
