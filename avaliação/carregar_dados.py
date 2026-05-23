"""
Script para carregar dados de teste do arquivo arquivos.txt
Use este script para testar sua implementação de FileSystemTree
"""

from file_system import FileSystemTree


def carregar_arquivos_de_arquivo(nome_arquivo: str) -> FileSystemTree:
    """
    Carrega uma lista de arquivos de um arquivo de texto.

    Args:
        nome_arquivo: Nome do arquivo (ex: "arquivos.txt")

    Returns:
        FileSystemTree populada com os arquivos
    """
    tree = FileSystemTree()

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        for linha in linhas:
            # Remove espaços em branco
            caminho = linha.strip()

            # Ignora linhas vazias e comentários
            if not caminho or caminho.startswith("#"):
                continue

            # Adiciona o arquivo à árvore
            sucesso = tree.add_file(caminho)
            if not sucesso:
                print(
                    f"⚠️  Aviso: Não foi possível adicionar {caminho} (duplicata?)")

        print(
            f"✓ Carregados {tree.get_total_files()} arquivos de {nome_arquivo}")
        return tree

    except FileNotFoundError:
        print(f"❌ Erro: Arquivo {nome_arquivo} não encontrado")
        return None
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")
        return None


def demonstrar_operacoes(tree: FileSystemTree):
    """
    Demonstra as operações implementadas na árvore.

    Args:
        tree: FileSystemTree para testar
    """
    if tree is None:
        return

    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO DE OPERAÇÕES")
    print("=" * 60)

    # 1. Total de arquivos
    print(f"\n1. Total de arquivos/diretórios: {tree.get_total_files()}")

    # 2. Profundidade máxima
    print(f"2. Profundidade máxima: {tree.get_max_depth()}")

    # 3. Validação
    print(f"3. Árvore válida? {tree.is_valid()}")

    # 4. Conteúdo da raiz
    print(f"\n4. Conteúdo do diretório raiz (/):")
    contents = tree.get_directory_contents("/")
    if contents:
        for item in contents:
            print(f"   - {item}")
    else:
        print("   (vazio ou não existe)")

    # 5. Conteúdo de um diretório específico
    print(f"\n5. Conteúdo de /home/user/Documentos/:")
    contents = tree.get_directory_contents("/home/user/Documentos/")
    if contents:
        for item in contents:
            print(f"   - {item}")
    else:
        print("   (vazio ou não existe)")

    # 6. Busca por extensão
    print(f"\n6. Arquivos com extensão .py:")
    py_files = tree.get_files_by_extension(".py")
    if py_files:
        for file in py_files:
            print(f"   - {file}")
    else:
        print("   (nenhum encontrado)")

    print(f"\n7. Arquivos com extensão .jpg:")
    jpg_files = tree.get_files_by_extension(".jpg")
    if jpg_files:
        for file in jpg_files:
            print(f"   - {file}")
    else:
        print("   (nenhum encontrado)")

    # 8. Contagem por nível
    print(f"\n8. Contagem de arquivos/diretórios por nível:")
    counts = tree.count_files_by_level()
    if counts:
        for nivel, quantidade in sorted(counts.items()):
            print(f"   Nível {nivel}: {quantidade} itens")
    else:
        print("   (sem dados)")


if __name__ == "__main__":
    print("Carregando sistema de arquivos...")
    print("-" * 60)

    # Carrega dados do arquivo
    tree = carregar_arquivos_de_arquivo("arquivos.txt")

    # Demonstra operações
    if tree:
        demonstrar_operacoes(tree)
        print("\n" + "=" * 60)
        print("✓ Teste concluído com sucesso!")
        print("=" * 60)
