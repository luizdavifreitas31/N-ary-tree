"""
Testes automatizados para a implementação de FileSystemTree
Execute com: pytest test_file_system.py -v
"""

import pytest
from file_system import FileSystemTree


@pytest.fixture
def empty_tree():
    """Árvore vazia para testes."""
    return FileSystemTree()


@pytest.fixture
def populated_tree():
    """Árvore populada com dados de teste."""
    tree = FileSystemTree()

    files = [
        "/home/user/Documentos/trabalho.pdf",
        "/home/user/Documentos/notas.txt",
        "/home/user/Documentos/AED1/main.py",
        "/home/user/Documentos/AED1/utils.py",
        "/home/user/Documentos/AED1/testes/test_main.py",
        "/home/user/Documentos/BD/schema.sql",
        "/home/user/Imagens/foto.jpg",
        "/home/user/Imagens/2024/viagem.jpg",
        "/home/user/Imagens/2024/praia.png",
        "/home/user/Imagens/2025/selfie.jpg",
        "/home/user/Vídeos/aula.mp4",
        "/var/log/system.log",
        "/var/log/error.log",
        "/var/log/2024/app.log",
        "/etc/config.conf",
    ]

    for file in files:
        tree.add_file(file)

    return tree


# ============================================================
# TESTES: add_file() e file_exists()
# ============================================================

def test_add_file_simple(empty_tree):
    """Testa adição de arquivo simples."""
    result = empty_tree.add_file("/home/file.txt")
    assert result == True, "Deve retornar True ao adicionar arquivo novo"
    assert empty_tree.file_exists("/home/file.txt") == True


def test_add_file_with_nested_path(empty_tree):
    """Testa adição de arquivo com caminho profundo."""
    result = empty_tree.add_file("/home/user/docs/file.txt")
    assert result == True
    assert empty_tree.file_exists("/home/user/docs/file.txt") == True


def test_add_duplicate_file(empty_tree):
    """Testa que não pode adicionar arquivo duplicado."""
    empty_tree.add_file("/home/file.txt")
    result = empty_tree.add_file("/home/file.txt")
    assert result == False, "Deve retornar False ao adicionar duplicata"


def test_file_not_exists(empty_tree):
    """Testa verificação de arquivo inexistente."""
    assert empty_tree.file_exists("/nonexistent/path.txt") == False


def test_add_multiple_files(empty_tree):
    """Testa adição de múltiplos arquivos."""
    files = ["/a/b/c.txt", "/a/b/d.txt", "/a/e.txt", "/f.txt"]
    for f in files:
        assert empty_tree.add_file(f) == True

    for f in files:
        assert empty_tree.file_exists(f) == True


# ============================================================
# TESTES: get_directory_contents()
# ============================================================

def test_get_directory_contents_root(populated_tree):
    """Testa listagem do diretório raiz."""
    contents = populated_tree.get_directory_contents("/")
    assert contents is not None
    assert "home" in contents
    assert "var" in contents
    assert "etc" in contents


def test_get_directory_contents_nested(populated_tree):
    """Testa listagem de diretório aninhado."""
    contents = populated_tree.get_directory_contents("/home/user/Documentos/")
    assert contents is not None
    assert "AED1" in contents or "AED1" in [c.strip("/") for c in contents]
    assert "BD" in contents or "BD" in [c.strip("/") for c in contents]


def test_get_directory_contents_nonexistent(populated_tree):
    """Testa listagem de diretório que não existe."""
    contents = populated_tree.get_directory_contents("/nonexistent/")
    assert contents is None


def test_get_directory_contents_file(populated_tree):
    """Testa tentativa de listar conteúdo de um arquivo (não diretório)."""
    contents = populated_tree.get_directory_contents(
        "/home/user/Documentos/trabalho.pdf")
    # Pode retornar None ou lista vazia, depende da implementação
    assert contents is None or contents == []


# ============================================================
# TESTES: get_files_by_extension()
# ============================================================

def test_get_files_by_extension_py(populated_tree):
    """Testa busca por arquivos .py."""
    py_files = populated_tree.get_files_by_extension(".py")
    assert py_files is not None
    assert len(py_files) >= 2
    assert "/home/user/Documentos/AED1/main.py" in py_files
    assert "/home/user/Documentos/AED1/utils.py" in py_files
    assert "/home/user/Documentos/AED1/testes/test_main.py" in py_files


def test_get_files_by_extension_jpg(populated_tree):
    """Testa busca por arquivos .jpg."""
    jpg_files = populated_tree.get_files_by_extension(".jpg")
    assert jpg_files is not None
    assert "/home/user/Imagens/foto.jpg" in jpg_files
    assert "/home/user/Imagens/2024/viagem.jpg" in jpg_files


def test_get_files_by_extension_no_matches(populated_tree):
    """Testa busca por extensão que não existe."""
    files = populated_tree.get_files_by_extension(".xyz")
    assert files is not None
    assert len(files) == 0


def test_get_files_by_extension_multiple(populated_tree):
    """Testa busca que retorna múltiplos resultados."""
    txt_files = populated_tree.get_files_by_extension(".txt")
    assert len(txt_files) >= 1


# ============================================================
# TESTES: get_max_depth()
# ============================================================

def test_get_max_depth_empty(empty_tree):
    """Testa profundidade de árvore vazia."""
    assert empty_tree.get_max_depth() == 0


def test_get_max_depth_single_file(empty_tree):
    """Testa profundidade com um arquivo."""
    empty_tree.add_file("/file.txt")
    assert empty_tree.get_max_depth() == 1


def test_get_max_depth_nested(empty_tree):
    """Testa profundidade com arquivos aninhados."""
    empty_tree.add_file("/a/b/c/d/e.txt")
    assert empty_tree.get_max_depth() == 5  # a, b, c, d, e


def test_get_max_depth_populated(populated_tree):
    """Testa profundidade da árvore populada."""
    depth = populated_tree.get_max_depth()
    assert depth >= 5  # Pelo menos /home/user/Documentos/AED1/testes/test_main.py = 5 níveis
    assert depth <= 6  # Máximo especificado (conforme dados fornecidos)


# ============================================================
# TESTES: count_files_by_level()
# ============================================================

def test_count_files_by_level_empty(empty_tree):
    """Testa contagem em árvore vazia."""
    counts = empty_tree.count_files_by_level()
    assert counts == {} or counts == {0: 0}


def test_count_files_by_level_single(empty_tree):
    """Testa contagem com um arquivo."""
    empty_tree.add_file("/file.txt")
    counts = empty_tree.count_files_by_level()
    assert 1 in counts.values()


def test_count_files_by_level_populated(populated_tree):
    """Testa contagem em árvore populada."""
    counts = populated_tree.count_files_by_level()

    # Verificações básicas
    assert isinstance(counts, dict)
    assert len(counts) > 0

    # Soma de todos os níveis deve ser total de arquivos
    total = sum(counts.values())
    assert total == populated_tree.get_total_files()


# ============================================================
# TESTES: get_total_files()
# ============================================================

def test_get_total_files_empty(empty_tree):
    """Testa contagem em árvore vazia."""
    assert empty_tree.get_total_files() == 0


def test_get_total_files_single(empty_tree):
    """Testa contagem com um arquivo."""
    empty_tree.add_file("/file.txt")
    assert empty_tree.get_total_files() == 1


def test_get_total_files_multiple(empty_tree):
    """Testa contagem com múltiplos arquivos."""
    empty_tree.add_file("/a/b.txt")
    empty_tree.add_file("/a/c.txt")
    empty_tree.add_file("/d.txt")
    assert empty_tree.get_total_files() == 3


def test_get_total_files_populated(populated_tree):
    """Testa contagem em árvore populada."""
    total = populated_tree.get_total_files()
    assert total == 15  # Conforme arquivos.txt


# ============================================================
# TESTES: is_valid()
# ============================================================

def test_is_valid_empty(empty_tree):
    """Testa validação de árvore vazia."""
    assert empty_tree.is_valid() == True


def test_is_valid_populated(populated_tree):
    """Testa validação de árvore populada."""
    assert populated_tree.is_valid() == True


def test_is_valid_single_file(empty_tree):
    """Testa validação com um arquivo."""
    empty_tree.add_file("/file.txt")
    assert empty_tree.is_valid() == True


# ============================================================
# TESTES INTEGRADOS
# ============================================================

def test_integration_full_workflow(empty_tree):
    """Testa fluxo completo de operações."""
    # Adicionar arquivos
    assert empty_tree.add_file("/project/src/main.py") == True
    assert empty_tree.add_file("/project/src/utils.py") == True
    assert empty_tree.add_file("/project/docs/readme.txt") == True

    # Verificar existência
    assert empty_tree.file_exists("/project/src/main.py") == True
    assert empty_tree.file_exists("/project/test.py") == False

    # Listar diretório
    contents = empty_tree.get_directory_contents("/project/src/")
    assert contents is not None

    # Buscar por extensão
    py_files = empty_tree.get_files_by_extension(".py")
    assert len(py_files) == 2

    # Verificar profundidade
    assert empty_tree.get_max_depth() == 3

    # Verificar total
    assert empty_tree.get_total_files() == 3

    # Validar
    assert empty_tree.is_valid() == True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
