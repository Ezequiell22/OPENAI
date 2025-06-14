import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE "a323tre21" (
    "a001" TEXT,
    "a002" TEXT,
    "a003" TEXT,
    "a004" TEXT,
    "a005" TEXT,
    "a006" TEXT,
    "a007" TEXT,
    "a008" TEXT,
    "a009" TEXT,
    "a010" TEXT,
    "a011" TEXT,
    "a012" TEXT,
    "a013" TEXT,
    "a014" TEXT,
    "a015" TEXT,
    "a016" TEXT,
    "a017" TEXT,
    "a018" TEXT,
    "a019" TEXT,
    "a020" TEXT
)
""")


cursor.execute("""
CREATE TABLE "b412421re412" (
    "a01321301" TEXT,
    "a002" TEXT,
    "a0203" TEXT,
    "a004" TEXT,
    "a0035" TEXT,
    "a006" TEXT,
    "a007" TEXT,
    "a0108" TEXT,
    "a009" TEXT,
    "a010" TEXT,
    "a013221" TEXT,
    "a012" TEXT,
    "a013" TEXT,
    "a0fd14" TEXT,
    "a015" TEXT,
    "a016" TEXT,
    "a03232117" TEXT,
    "a032118" TEXT,
    "a019" TEXT,
    "a0321320" TEXT
)
""")

conn.commit()
conn.close()
