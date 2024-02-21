import sqlite3
from contextlib import contextmanager


@contextmanager
def open_database(database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        connection.commit()
        connection.close()


class MemberModel:

    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score

    def __repr__(self):
        return f"MemberModel({self.name}, {self.email}, {self.score})"

    @classmethod
    def from_tuple(cls, data):
        return cls(data[1], data[2], data[3])


def create_table():
    with open_database("member.db") as cursor:
        res = cursor.execute(
            """CREATE TABLE IF NOT EXISTS member
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             email TEXT,
                score INTEGER)"""
        )
        res.fetchone()


def insert(name, email, score):
    with open_database("member.db") as cursor:
        res = cursor.execute(
            "INSERT INTO member (name, email, score) VALUES (?, ?, ?)",
            (name, email, score),
        )
        res.fetchone()
    print(f"Member {name} added to the database.")


def delete_all_members():
    with open_database("member.db") as cursor:
        res = cursor.execute("DELETE FROM member")
        res.fetchone()


def get_all_members():
    with open_database("member.db") as cursor:
        res = cursor.execute("SELECT * FROM member")
        member_on_tuple = res.fetchall()

        members = [MemberModel.from_tuple(member) for member in member_on_tuple]

        return members


if __name__ == "__main__":

    create_table()
    members = get_all_members()

    print(members)
