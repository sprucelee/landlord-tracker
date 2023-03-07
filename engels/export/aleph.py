# export files for import into Aleph
#
import os.path

from engels.common import get_project_path
from engels.db import get_db_engine

def copy_to(conn, path, sql):
    with open(path, "w") as f:
        cursor = conn.connection.cursor()
        # see https://www.psycopg.org/docs/cursor.html#cursor.copy_expert
        cursor.copy_expert(sql, f, size=1024*1024)

def export_all():
    engine = get_db_engine()
    with engine.connect() as conn:
        with conn.begin():
            path = os.path.join(get_project_path(), "aleph_lt/import/aleph_real_property_account.csv")
            sql = f"COPY aleph_real_property_account TO STDOUT WITH DELIMITER ',' CSV HEADER"
            copy_to(conn, path, sql)

            path = os.path.join(get_project_path(), "aleph_lt/import/aleph_apartment_complex.csv")
            sql = f"COPY stg_apartment_complex TO STDOUT WITH DELIMITER ',' CSV HEADER"
            copy_to(conn, path, sql)

if __name__ == "__main__":
    print("Exporting tables")
    export_all()
