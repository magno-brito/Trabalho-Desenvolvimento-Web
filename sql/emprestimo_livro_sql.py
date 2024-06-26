SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS emprestimo_livros (
    emprestimo_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    PRIMARY KEY (emprestimo_id, livro_id),
    FOREIGN KEY (emprestimo_id) REFERENCES emprestimo (id),
    FOREIGN KEY (livro_id) REFERENCES livro (id)
)
"""


SQL_INSERIR = """
INSERT INTO emprestimo_livros(emprestimo_id, livro_id)
VALUES (?, ?)
"""


SQL_OBTER_QUANTIDADE = """
SELECT COUNT(*) FROM emprestimo_livros
"""

SQL_OBTER_TODOS = """   
SELECT emprestimo_id, livro_id 
FROM emprestimo_livros

"""

SQL_OBTER_UM = """
    SELECT emprestimo_id, livro_id
    FROM emprestimo_livros
    WHERE emprestimo_id=?
"""




SQL_EXCLUIR = """
    DELETE FROM emprestimo_livros
    WHERE emprestimo_id=?

"""