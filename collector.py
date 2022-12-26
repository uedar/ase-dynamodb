import os
from ase.db import connect
import subprocess


def main(target: str) -> None:
    paths = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(f"./database/contribution_files/{target}")
        for file in files
    ]

    print(paths)

    # remove db
    main_db = f"./database/{target}.json"
    if os.path.isfile(main_db) == True:
        os.remove(main_db)

    db_main = connect(main_db)
    for db_to_combine in paths:
        combine = subprocess.run(["ase", "db", db_to_combine, "-i", main_db])


if __name__ == "__main__":
    for target in ["atom", "bulk", "molecule"]:
        main(target)
