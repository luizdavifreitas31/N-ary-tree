"""
Script principal para testar a Arvore interativamente via terminal.
Permite executar todos os 8 métodos implementados na árvore.
"""

import os
from Metodos.main import FileSystemTree


def exibir_menu():
    print("\n" + "=" * 50)
    print("      MENU INTERATIVO - FILE SYSTEM TREE")
    print("=" * 50)
    print("1. Adicionar Arquivo/Diretório (add_file)")
    print("2. Verificar se Existe (file_exists)")
    print("3. Listar Conteúdo de Diretório (get_directory_contents)")
    print("4. Buscar por Extensão (get_files_by_extension)")
    print("5. Ver Profundidade Máxima (get_max_depth)")
    print("6. Contar Itens por Nível (count_files_by_level)")
    print("7. Ver Total de Arquivos (get_total_files)")
    print("8. Validar Estrutura da Árvore (is_valid)")
    print("9. Carregar Carga de Teste Padrão (arquivos.txt)")
    print("0. Sair")
    print("=" * 50)


def carregar_carga_padrao(tree):
    nome_arquivo = "arquivos.txt"
    if not os.path.exists(nome_arquivo):
        print(
            f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado nesta pasta.")
        return

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        cont_sucesso = 0
        for linha in linhas:
            caminho = linha.strip()
            if not caminho or caminho.startswith("#"):
                continue
            if tree.add_file(caminho):
                cont_sucesso += 1

        print(
            f"✓ Sucesso! {cont_sucesso} caminhos carregados de '{nome_arquivo}'.")
    except Exception as e:
        print(f"❌ Erro ao ler arquivo de carga: {e}")


def main():
    tree = FileSystemTree()
    print("🌳 Árvore de Sistema de Arquivos Inicializada com Sucesso!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-9): ").strip()

        if opcao == "1":
            path = input(
                "Digite o caminho completo (ex: /home/user/doc.txt): ").strip()
            if not path.startswith("/"):
                print("⚠️ Aviso: O caminho deve começar com '/'")
                continue
            sucesso = tree.add_file(path)
            if sucesso:
                print(f"✓ Item '{path}' adicionado com sucesso!")
            else:
                print(
                    f"❌ Falha ao adicionar '{path}' (Pode ser uma duplicata ou caminho inválido).")

        elif opcao == "2":
            path = input(
                "Digite o caminho para verificar (ex: /home/user): ").strip()
            if tree.file_exists(path):
                print(f"🔍 O caminho '{path}' EXISTE na árvore.")
            else:
                print(f"❌ O caminho '{path}' NÃO existe na árvore.")

        elif opcao == "3":
            path = input(
                "Digite o caminho do diretório (ex: /home/user/): ").strip()
            contents = tree.get_directory_contents(path)
            if contents is None:
                print(
                    f"❌ Diretório '{path}' não encontrado ou é um arquivo final.")
            elif len(contents) == 0:
                print(f"📁 O diretório '{path}' está vazio.")
            else:
                print(f"📁 Conteúdo de '{path}':")
                for item in contents:
                    print(f"   └── {item}")

        elif opcao == "4":
            ext = input(
                "Digite a extensão desejada (ex: .py ou .txt): ").strip()
            if not ext.startswith("."):
                ext = "." + ext
            files = tree.get_files_by_extension(ext)
            if files:
                print(f"📄 Arquivos com a extensão '{ext}':")
                for f in files:
                    print(f"   • {f}")
            else:
                print(
                    f"🔍 Nenhum arquivo com a extensão '{ext}' foi encontrado.")

        elif opcao == "5":
            depth = tree.get_max_depth()
            print(f"📊 Profundidade máxima atual da árvore: {depth} níveis.")

        elif opcao == "6":
            counts = tree.count_files_by_level()
            if counts:
                print("📈 Quantidade de arquivos por nível:")
                for nivel, qtd in sorted(counts.items()):
                    print(f"   Nível {nivel}: {qtd} item(ns)")
            else:
                print("📊 Árvore não possui arquivos mapeados por nível.")

        elif opcao == "7":
            total = tree.get_total_files()
            print(f"🔢 Total de arquivos mapeados (is_file=True): {total}")

        elif opcao == "8":
            if tree.is_valid():
                print(
                    "✅ Árvore VÁLIDA! Todos os ponteiros de pais e regras de duplicatas estão corretos.")
            else:
                print(
                    "❌ Árvore INVÁLIDA! Existe alguma inconsistência estrutural nos ponteiros ou nós.")

        elif opcao == "9":
            carregar_carga_padrao(tree)

        elif opcao == "0":
            print("Encerrando o programa de testes. Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Por favor, escolha um número de 0 a 9.")


if __name__ == "__main__":
    main()
