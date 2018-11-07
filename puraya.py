# coding=utf-8
import os
import shutil
import subprocess


def fast_copy(source_path, destination_path):
    """Copies file using system copy utilities for faster copy. Falls back to shutil.copyfile on unsupported systems.
    :param str source_path: Absolute path to source file
    :param str destination_path: Absolute path to destination file
    """
    if os.name == 'posix':
        subprocess.call(['cp', source_path, destination_path])
    elif os.name == 'nt':
        # seriously, fuck xcopy
        (open(destination_path, 'w')).close()
        subprocess.call(['xcopy', source_path, destination_path, '/Y/Q'], stdout=subprocess.DEVNULL)
    else:
        shutil.copyfile(source_path, destination_path)


def flat_copy(source_path_list, destination_path, progress_logger=None):
    """Copies nested directories from the sources list to the flat structure in the destination folder.

    Source directory contents:
        sample1
        ├── bar
        │   ├── 1
        │   └── 2
        └── foo
            ├── 3
            └── 4

    Source directory contents:
        sample2
        ├── bad
        │   ├── 5
        │   └── 6
        └── baz
            ├── 7
            └── 8

    Destination directory contents:
        sample-flat
        ├── sample1
        │   ├── bar - 1
        │   ├── bar - 2
        │   ├── foo - 3
        │   └── foo - 4
        └── sample2
            ├── bad - 5
            ├── bad - 6
            ├── baz - 7
            └── baz - 8

    :param list source_path_list:  List of absolute paths to directories
    :param str destination_path: string Absolute path to the destination directory
    :param SysLogger progress_logger:  Progress logger
    :return:
    """
    for source_path in source_path_list:
        destination_subdir_name = os.path.split(os.path.dirname(source_path))[-1]
        destination_subdir_path = os.path.join(destination_path, destination_subdir_name)
        if not os.path.isdir(destination_subdir_path):
            os.makedirs(destination_subdir_path)

        for dir_info in os.walk(source_path):
            if progress_logger is not None and len(dir_info[2]):
                progress_logger.write_iteration_name(dir_info[0])

            for cnt, file in enumerate(dir_info[2]):
                source_file = os.path.join(dir_info[0], file)
                destination_file = os.path.join(
                    destination_subdir_path,
                    source_file.replace(source_path, '').replace(os.sep, ' - ')
                )
                fast_copy(source_file, destination_file)

                if progress_logger is not None:
                    progress_logger.write_progress(cnt + 1, len(dir_info[2]))
