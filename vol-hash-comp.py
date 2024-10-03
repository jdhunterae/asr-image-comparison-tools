import os
import hashlib
import sqlite3
import argparse
import time


def calculate_hashes(file_path: str) -> tuple[str, str]:
    """
    Calculates the MD5 and SHA1 hash of a given file.

    Parameters:
    file_path (str): The path to the file for which to calculate the hashes.

    Returns:
    tuple[str, str]: A tuple containing the MD5 and SHA1 hash of the file
                    as hexadecimal strings. If an error occurs while reading
                    the file, returns (None, None).
    """
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                md5.update(chunk)
                sha1.update(chunk)
        return md5.hexdigest(), sha1.hexdigest()
    except Exception as e:
        print(f"Error reading file: {file_path}: {e}")
        return None, None


def create_hash_db(db_path: str) -> sqlite3.Connection:
    """
    Creates a SQLite database to store file hashes.

    Parameters:
    db_path (str): The path to the SQLite database file.

    Returns:
    sqlite3.Connection: A connection object to the SQLite database.

    This function creates a SQLite database with a table named 'file_hashes'.
    The table has columns for the file path and the MD5 and SHA1 hashes of two
    images associated with the file. The function returns a connection object
    to the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS file_hashes (
                    file_path TEXT,
                    image_1_md5 TEXT, image_1_sha1 TEXT,
                    image_2_md5 TEXT, image_2_sha1 TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS mismatched_hashes (
                    file_path TEXT,
                    image_1_md5 TEXT, image_1_sha1 TEXT,
                    image_2_md5 TEXT, image_2_sha1 TEXT)''')
    conn.commit()

    return conn


def fill_diff_table(db_conn: sqlite3.Connection) -> None:
    """
    This function fills the 'mismatched_hashes' table in the SQLite database with
    records of files that have different MD5 or SHA1 hashes for their two images.

    Parameters:
    db_conn (sqlite3.Connection): A connection object to the SQLite database.

    Returns:
    None: This function does not return any value. It modifies the database by
          inserting records into the 'mismatched_hashes' table.

    The function first retrieves all records from the 'file_hashes' table where
    the MD5 or SHA1 hashes of the two images are different. For each such record,
    it inserts a new record into the 'mismatched_hashes' table with the same
    file path and image hashes.
    """
    hash_cursor = db_conn.cursor()
    diff_cursor = db_conn.cursor()
    hash_cursor.execute('''SELECT * FROM file_hashes WHERE
                      image_1_md5!= image_2_md5 OR
                      image_1_sha1!= image_2_sha1''')

    for row in hash_cursor.fetchall():
        diff_cursor.execute('''INSERT INTO mismatched_hashes (
                        file_path, image_1_md5, image_1_sha1,
                        image_2_md5, image_2_sha1) VALUES (?,?,?,?,?)''',
                            row)

    db_conn.commit()


def main():
    print("Running...")
    print("          done.")


if __name__ == "__main__":
    main()
