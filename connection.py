import psycopg


class Connection:
    def __init__(self, host, db, usuario, senha):
        self._db = psycopg.connect(
            host=host,
            dbname=db,
            user=usuario,
            password=senha
        )

    def manipular(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            self._db.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            self._db.rollback()
            return False

    def consultar(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            resultado = cur.fetchall()
            cur.close()
            return resultado
        except Exception as e:
            print(f"Erro: {e}")
            return None
    
    def fechar(self):
        self._db.close()