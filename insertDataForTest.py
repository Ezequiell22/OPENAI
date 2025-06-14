import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()


cursor.execute("""
              INSERT INTO "a323tre21" VALUES
("Ana Silva", "12345678901", "ana@email.com", "11999990000", "1990-05-12", "F", "Solteira", "Analista", "Tech Ltda", "Desenvolvedora", "5000", "VIP", "Ativo", "15000", "800", "Boa cliente", "Indicação", "2022-01-01", "2023-12-15", "12"),
("Bruno Souza", "98765432100", "bruno@email.com", "21988887777", "1985-09-23", "M", "Casado", "Gerente", "Bank SA", "Gerente Geral", "12000", "Premium", "Ativo", "20000", "950", "", "Google", "2021-11-20", "2024-01-10", "25"),
("Carlos Lima", "11122233344", "carlos@email.com", "31977776666", "1992-03-10", "M", "Solteiro", "Professor", "Universidade", "Docente", "6000", "Standard", "Ativo", "10000", "720", "", "Instagram", "2020-06-30", "2023-10-20", "8"),
("Daniela Teixeira", "44455566677", "dani@email.com", "47966665555", "1988-07-08", "F", "Casada", "Designer", "Studio Criativo", "UX Designer", "7000", "Premium", "Ativo", "12000", "780", "", "LinkedIn", "2023-03-15", "2024-05-01", "14"),
("Eduardo Ramos", "55566677788", "edu@email.com", "11955554444", "1995-12-01", "M", "Solteiro", "Estudante", "Faculdade", "Estagiário", "2000", "Standard", "Ativo", "5000", "620", "", "Feira", "2022-05-18", "2023-09-05", "4"),
("Fernanda Costa", "66677788899", "fer@email.com", "21944443333", "1980-01-30", "F", "Divorciada", "Médica", "Clínica Saúde", "Pediatra", "15000", "VIP", "Ativo", "30000", "980", "", "Indicação", "2019-09-10", "2024-04-25", "33"),
("Gabriel Almeida", "77788899900", "gab@email.com", "31933332222", "1991-08-17", "M", "Casado", "Engenheiro", "Construtora X", "Civil", "11000", "Premium", "Ativo", "18000", "890", "", "Anúncio", "2020-12-01", "2023-06-11", "19"),
("Helena Borges", "88899900011", "helena@email.com", "47922221111", "1993-02-05", "F", "Solteira", "Advogada", "Escritório Y", "Cível", "9500", "Premium", "Ativo", "15000", "860", "", "Google", "2021-04-07", "2024-02-02", "17"),
("Igor Fernandes", "99900011122", "igor@email.com", "11911110000", "1987-06-21", "M", "Casado", "TI", "Empresa Z", "Suporte", "7000", "Standard", "Ativo", "9000", "700", "", "Instagram", "2018-11-29", "2023-08-18", "10"),
("Julia Martins", "00011122233", "julia@email.com", "21900009999", "1996-10-14", "F", "Solteira", "Arquiteta", "Studio A", "Projetista", "8000", "Standard", "Ativo", "10000", "730", "", "LinkedIn", "2023-06-20", "2024-05-30", "6");

               """)


cursor.execute("""
               INSERT INTO "b412421re412" VALUES
("12345678", "Rua das Flores", "100", "Ap 101", "Centro", "São Paulo", "SP", "Brasil", "Próximo ao parque", "Residencial", "Urbana", "2024-01-01", "Sim", "-23.5505,-46.6333", "Sudeste", "3550308", "1", "1", "Sim", "Nenhuma"),
("23456789", "Av. Brasil", "200", "Bloco B", "Jardins", "Rio de Janeiro", "RJ", "Brasil", "Em frente ao mercado", "Comercial", "Urbana", "2024-01-05", "Não", "-22.9068,-43.1729", "Sudeste", "3304557", "2", "1", "Sim", ""),
("34567890", "Rua A", "300", "", "Vila Nova", "Belo Horizonte", "MG", "Brasil", "Próximo à escola", "Residencial", "Suburbana", "2023-12-20", "Sim", "-19.9167,-43.9345", "Sudeste", "3106200", "3", "2", "Sim", "Fundos"),
("45678901", "Rua B", "400", "Casa 2", "Industrial", "Curitiba", "PR", "Brasil", "Atrás da fábrica", "Comercial", "Urbana", "2023-11-15", "Sim", "-25.4284,-49.2733", "Sul", "4106902", "4", "2", "Sim", ""),
("56789012", "Av. Central", "500", "", "Centro", "Florianópolis", "SC", "Brasil", "Ao lado da prefeitura", "Residencial", "Urbana", "2023-10-10", "Não", "-27.5954,-48.5480", "Sul", "4205407", "5", "3", "Sim", ""),
("67890123", "Rua do Sol", "600", "Apto 22", "Praia", "Fortaleza", "CE", "Brasil", "Vista para o mar", "Residencial", "Litorânea", "2023-09-01", "Sim", "-3.7172,-38.5433", "Nordeste", "2304400", "6", "3", "Sim", ""),
("78901234", "Rua Verde", "700", "", "Parque", "Manaus", "AM", "Brasil", "Próximo à floresta", "Residencial", "Rural", "2023-08-18", "Não", "-3.1190,-60.0217", "Norte", "1302603", "7", "4", "Sim", ""),
("89012345", "Rua Azul", "800", "Casa 1", "Alto", "Porto Alegre", "RS", "Brasil", "Subida íngreme", "Comercial", "Urbana", "2023-07-22", "Sim", "-30.0346,-51.2177", "Sul", "4314902", "8", "4", "Sim", ""),
("90123456", "Av. Norte", "900", "", "Centro", "Recife", "PE", "Brasil", "Ao lado do shopping", "Residencial", "Urbana", "2023-06-30", "Sim", "-8.0476,-34.8770", "Nordeste", "2611606", "9", "5", "Sim", ""),
("01234567", "Rua Oeste", "1000", "Bloco C", "Antigo", "Salvador", "BA", "Brasil", "Perto do pelourinho", "Comercial", "Histórica", "2023-05-15", "Sim", "-12.9714,-38.5014", "Nordeste", "2927408", "10", "5", "Sim", "Sem acesso");

               """)

conn.commit()
conn.close()
