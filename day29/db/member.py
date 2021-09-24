# member 테이블 생성 및 관리
from day28.libs.dbconn import getconn
import sqlite3

def create_table():
    # conn = sqlite3.connect("c:/webdb/webdb.db") # db 연결 객체 생성
    conn = getconn()
    cur = conn.cursor() # db 작업객체 생성
    spl = """
        CREATE TABLE member(
            memberId char(5) PRIMARY KEY,
            passwd   char(8) NOT NULL,
            name     TEXT NOT NULL,
            age      INTEGER,
            reg_Date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    cur.execute(spl)
    conn.commit()
    conn.close()

# 자료 추가
def insert_member():
    # conn = sqlite3.connect("c:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(memberId, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10003', 'c1234567', '콩쥐', 17))
    conn.commit()
    conn.close()

# 전체 자료 검색
def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()  # 전체 자료 반환
    for i in rs:
        print(i)
    conn.close()

# 특정한 1개 검색 - 아이디와 비밀번호 가져오기
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT memberId, passwd FROM member WHERE memberId = ?"
    cur.execute(sql, ('10002', ))   # 1개 매핑할 때 콤머 찍음.
    rs = cur.fetchone()    # 1개의 정보를 반환 받음
    print(rs)
    conn.commit()
    conn.close()

def update_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET age = ? WHERE memberId = ?"
    cur.execute(sql, (37, '10001'))  # ? 순서대로 매핑
    conn.commit()
    conn.close()

def delete_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberId = ?"
    cur.execute(sql, ('10002', ))   # 튜플은 1개 추가,삭제할 때 뒤에 콤머 붙임 : 주의!
    conn.commit()
    conn.close()


# create_table()
# insert_member()
# update_member()
delete_member()
# select_one()
select_member()