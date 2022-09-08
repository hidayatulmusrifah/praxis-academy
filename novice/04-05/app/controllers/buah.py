import psycopg2
from flask import request, render_template

def index():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="yasayatau18"
        )
    except Exception as e:
        print(e)
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()
        

    print(request.method)
    query = f"select * from buah order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["anggur", "jeruk", "apel"]
    return render_template("index.html", context=data)

