"""
create a .sig file from .pat files stored in tarballs
optionally excludes tarball paths and includes pat file names

example runs:
  $ python3 create_sig.py -d -e libraries test -i libc msvc --tarballs-root data/ -- outdir/
    -d - debug output
    -e - exclude paths containing string `libraries` or `test`
    -i - include pat files containing `libc` and `msvc`
    --tarballs-root - root path storing tarballs containing .pat files
    --
    data/ - root path of tarballs
    outdir/ - path to output files

  $ python3 create_sig.py --patfiles data/VS6/vc98/lib/libc*.pat -- outdir/
    --patfiles - paths to .pat files
    --
    outdir/ - path to output files
"""

import os
import shutil
import sys
import logging
import tarfile
import argparse
import subprocess


logger = logging.getLogger(__name__)


# the patched sigmake doesn't complain about number of leaves
PATH_SIGMAKE = os.path.abspath("../sigmake_patched.exe")
PATH_ZIPSIG = os.path.abspath("../zipsig.exe")


def collect_tarball_paths(path, exclude=None):
    """
    return all tarballs recursively collected starting from path
    exclude specifies a list of strings used to filter out paths
    """
    tarball_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".tar.gz"):
                continue

            tarball_path = os.path.join(root, file)

            if exclude:
                skip = False
                for exc in exclude:
                    if exc in tarball_path:
                        skip = True
                        break
                if skip:
                    continue

            tarball_paths.append(tarball_path)
    return tarball_paths


def extract_pat_files(outdir, tarball_path, include=None):
    """
    extract all .pat files from a tarball to output directory
    """
    tar = tarfile.open(tarball_path, "r:gz")
    for m in tar.getmembers():
        if not m.name.endswith(".pat"):
            continue

        if include:
            for inc in include:
                if inc in m.name:
                    write_tar_member(outdir, tar, m)
        else:
            write_tar_member(outdir, tar, m)
    return 0


def write_tar_member(outdir, tar, m):
    """
    write file from tarball to output directory
    """
    outpath = os.path.join(outdir, flatten_path(m.name))
    logger.debug(" writing %s", outpath)
    with open(outpath, "wb") as f:
        f.write(tar.extractfile(m).read())


def flatten_path(name):
    # tarballs may store directory structure, e.g. VS6.tar.gz/VS6.tar/VS6/vc98/lib/libc.lib.pat
    name = name.replace("/", "-")
    return name


def create_sig_file_from_pats(outdir, outsigfile, patfiles):
    """
    convenience functionality around IDA's sigmake
    """
    # on Windows need to shorten file names to avoid command line >~ 8100 characters
    created_temp_files = False
    if os.name == "nt":
        logger.debug("creating temporary pat files")
        patfiles = create_temp_pat_files(outdir, patfiles)
        created_temp_files = True

    outsigfile = os.path.join(outdir, outsigfile)

    # use multiple -v for more verbosity, two appears to be max
    args = [PATH_SIGMAKE, "-v", "-v"] + patfiles + [outsigfile]
    logfile = open(os.path.join(outdir, "run1.log"), "wb")
    run(args, stdout=logfile, stderr=logfile)
    logfile.close()

    exc_file = os.path.splitext(outsigfile)[0] + ".exc"
    process_exc_file(exc_file)

    logfile = open(os.path.join(outdir, "run2.log"), "wb")
    run(args, stdout=logfile, stderr=logfile)
    logfile.close()

    if created_temp_files:
        remove_files(patfiles)

    if not os.path.exists(outsigfile):
        raise ValueError(f"did not create {outsigfile}")

    return outsigfile


def create_temp_pat_files(outdir, files):
    temp_pat_files = []
    for i, f in enumerate(files):
        new = os.path.join(outdir, f"{i}.pat")
        shutil.copy(f, new)
        temp_pat_files.append(new)
    return temp_pat_files


def remove_files(pat_files):
    for f in pat_files:
        logger.debug("removing file %s", f)
        os.remove(f)


def get_pat_files(path):
    pat_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pat"):
                pat_path = os.path.join(root, file)
                pat_paths.append(os.path.relpath(pat_path))
    return pat_paths


def run(args, cwd=os.curdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    logger.debug("running %s", " ".join(args))
    p = subprocess.Popen(args, cwd=cwd, stdout=stdout, stderr=stderr)
    # wait
    p.communicate()


def process_exc_file(exc_file):
    """
    for now just delete first 5 lines
    """
    with open(exc_file, "rb") as f:
        d = f.read().splitlines(keepends=True)
    with open(exc_file, "wb") as f:
        f.writelines(d[5:])


def zipsig(outsigfile, save_unzipped_file=True):
    if save_unzipped_file:
        shutil.copy(outsigfile, f"{outsigfile}.bu")

    args = [PATH_ZIPSIG, outsigfile]
    run(args)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "outdir",
        type=str,
        help="path to output directory",
    )
    parser.add_argument("-e", "--exclude", nargs="*", help="exclude paths that contain exclusion string")
    parser.add_argument("-i", "--include_pats", nargs="*", help="include pat files that contain inclusion string")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tarballs-root", help="data path to root of tarballs, use with -e and -i")
    group.add_argument("--patfiles", nargs="+", help="paths to input .pat files")
    parser.add_argument("-s", "--sigfile", default="flare.sig", help="name of output .sig file")
    # logging modes
    parser.add_argument("-d", "--debug", action="store_true", help="enable debugging output on STDERR")
    parser.add_argument("-q", "--quiet", action="store_true", help="disable all output but errors")
    args = parser.parse_args(args=argv)

    if args.quiet:
        logging.basicConfig(level=logging.WARNING)
        logging.getLogger().setLevel(logging.WARNING)
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().setLevel(logging.INFO)

    if args.patfiles and (args.exclude or args.include_pats):
        logger.error("-e and -i arguments can only be used with --tarballs-root")
        return -1

    if os.path.exists(args.outdir):
        logger.error("%s already exists", args.outdir)
        return -1
    else:
        logger.debug("creating output directory %s", args.outdir)
        os.mkdir(args.outdir)

    if args.tarballs_root:
        logger.debug("collecting tarball paths")
        tarball_paths = collect_tarball_paths(args.tarballs_root, exclude=args.exclude)

        for tarball_path in tarball_paths:
            logger.debug("extracting from %s", tarball_path)
            extract_pat_files(args.outdir, tarball_path, include=args.include_pats)

        patfiles = get_pat_files(args.outdir)
    else:
        logger.debug("using provided .pat files")
        patfiles = args.patfiles

    logger.debug("creating sig file %s", args.sigfile)
    try:
        sigpath = create_sig_file_from_pats(args.outdir, args.sigfile, patfiles)
    except ValueError as e:
        logger.error(str(e))
        return -1

    logger.debug("zipping sig file %s", sigpath)
    zipsig(sigpath, save_unzipped_file=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
