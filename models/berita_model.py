import pymysql
from models import db_connection
class BeritaModel:
    @staticmethod
    def get_all():
        conn = db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM berita")
        berita = cursor.fetchall()
        conn.close()
        return berita

    @staticmethod
    def add(judul, tanggal, rincian, gambar):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO berita (judul, tanggal, rincian, gambar) VALUES (%s, %s, %s, %s)",
                    (judul, tanggal, rincian, gambar))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, judul, tanggal, rincian, gambar):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE berita SET judul = %s, tanggal = %s, rincian = %s, gambar = %s WHERE id = %s",
                       (judul, tanggal, rincian, gambar, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM berita WHERE id = %s", (id,))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_by_id(id):
        conn = db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM berita WHERE id = %s", (id,))
        berita = cursor.fetchone()
        conn.close()
        return berita
