# export files for import into Aleph
#
import os.path

from engels.common import get_project_path
from engels.db import get_db_engine


def export_all():
    engine = get_db_engine()
    with engine.connect() as conn:
        with conn.begin():
            path = os.path.join(get_project_path(), "aleph_lt/import/aleph_real_property_account.csv")
            sql = f"COPY aleph_real_property_account TO '{path}' WITH DELIMITER ',' CSV HEADER"
            conn.execute(sql)

            path = os.path.join(get_project_path(), "aleph_lt/import/aleph_apartment_complex.csv")
            sql = f"COPY stg_apartment_complex TO '{path}' WITH DELIMITER ',' CSV HEADER"
            conn.execute(sql)

if __name__ == "__main__":
    print("Exporting tables")
    export_all()
