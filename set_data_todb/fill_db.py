import pandas as pd

from models.connectionsPools import MongoPoolConnection


def read_data_from_excel(path: str) -> list[dict]:
    data = pd.read_excel(path, sheet_name="roles",
                         usecols="A:K", header=0)
    list_of_dict = data.to_dict(orient="records")
    return list_of_dict


def connect_and_fill_data(records: list[dict]):
    try:
        pool = MongoPoolConnection()
        conn = pool.get_connection()
        session = conn.start_session()

        with session.start_transaction():
            db = conn.divideRules
            collection = db.mycollection
            unique_records = []

            for record in records:
                existing_record = collection.find_one(record)
                if existing_record is None:
                    unique_records.append(record)

            if unique_records:
                result = collection.insert_many(unique_records)
                print(f"Added {len(result.inserted_ids)} documents")
            else:
                print(f"All records are exist")

            session.commit_transaction()
            session.end_session()
    except Exception as e:
        print(f"Error while executing transaction : {e}")
    finally:
        pool.return_connection(conn)
        pool.close_all_connections()


if __name__ == "__main__":
    path = r"C:\Users\Maksim\PycharmProjects\divideRules\set_data_todb\Roles and TIERS.xlsx"
    data = read_data_from_excel(path)
    connect_and_fill_data(data)
