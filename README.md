# File Comparison and Metadata Analysis Scripts

This project contains three Python scripts for comparing and analyzing files between mounted volumes. Each script focuses on a different type of comparison:

1. **vol-hash-comp-tool.py**: Compares MD5 and SHA1 hashes of files between the two mounted volumes.
2. **vol-mdls-comp-tool.py**: Compares `kMDItemFSContentChangeDate` and `kMDItemFSCreationDate` timestamps using macOS's `mdls` command.
3. **vol-stat-comp-tool.py**: Compares the four POSIX dates (Access, Modify, Change, and Birth) of files using `stat -x`.

## Prerequisites

1. Python 3.8+ must be installed on the system.
2. Install `virtualenv` if not already available with the following command:

Using the `pip` command to install the package.

```bash
python3 -m pip install virtualenv
```

If `pip` returns an error/warning that the environment is externally managed, you can try to install `virtualenv` through `brew` instead.

```bash
brew install virtualenv
```

## Project Setup

1. Clone or copy the project files into your desired working directory.
2. Create and activate the virtual environment.
3. Install the required dependencies.

### Create and activate the virtual environment

From within the project directory, run the following commands:

```bash
python3 -m venv env      # create the virtual environment
source env/bin/activate  # activate the virtual environment
```

### Install the required dependencies

Once the virtual environment is activated, install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

## Running the Scripts

Each script can be run from the terminal with two input volume paths for comparison. Here are examples for each:

### vol-hash-comp-tool.py: File Hash Comparison

Compares the MD5 and SHA1 hashes for each file in two volumes, stores the result in a SQLite database (`file_hashes.db`), and stores the results of a comparison query in a second SQLite database (`mismatched_hashes.db`).

```bash
python vol-hash-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2
```

Optionally, you can also indicate the directory to place the output folder in. By default it will be created on the current user desktop (`~/Desktop/`).

```bash
python vol-hash-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2 --output_dir /path/to/output/directory
```

This will compare the files in `/Volumes/MountedVolume1` and `/Volumes/MountedVolume2`, storing results in `/path/to/output/directory/hash_comparison_case_YYYYMMDD_HHMMSS`.

### mdls-comparison-tool.py: MDLS Metadata Comparison

Compares `kMDItemFSContentChangeDate` and `kMDItemFSCreationDate` timestamps using the macOS `mdls` command, stores the result in a SQLite database (`mdls_timestamps.db`), and stores the results of a comparison query in a second SQLite database (`mismatched_timestamps.db`).

Example:

```bash
python vol-mdls-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2
```

Optionally, you can also indicate the directory to place the output folder in. By default it will be created on the current user desktop (`~/Desktop/`).

```bash
python vol-mdls-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2 --output_dir /path/to/output/directory
```

This will compare the files in `/Volumes/MountedVolume1` and `/Volumes/MountedVolume2`, storing results in `/path/to/output/directory/hash_comparison_case_YYYYMMDD_HHMMSS`.

### stat-comparison-tool.py: File Stat Comparison

Compares Access, Modify, Change, and Birth dates using the `stat -x` command, storing the information for files in both directories in a SQLite database, and storing the results of a comparison query in a second SQLite database (`mismatched_timestamps.db`).

Example:

```bash
python vol-mdls-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2
```

Optionally, you can also indicate the directory to place the output folder in. By default it will be created on the current user desktop (`~/Desktop/`).

```bash
python vol-mdls-comp-tool.py /Volumes/MountedVolume1 /Volumes/MountedVolume2 --output_dir /path/to/output/directory
```

This will compare the files in `/Volumes/MountedVolume1` and `/Volumes/MountedVolume2`, storing results in `/path/to/output/directory/hash_comparison_case_YYYYMMDD_HHMMSS`.

## Output

Each script generates a SQLite database saved in a timestamped folder on the desktop (`~/Desktop`) or a custom output path you specify. The database contains the comparison results for each file between the two input paths.

## Deactivating the Virtual Environment

Once you’re done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```
