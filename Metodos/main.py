"""
Arquivo com todos os métodos separados em arquivos diferentes
para melhor organização. Teste usando o arquivo teste_arvore.py.
"""
from add_file import add_file
from file_exists import file_exists
from get_directory_contents import get_directory_contents
from get_files_by_extension import get_files_by_extension
from get_max_depth import get_max_depth
from count_files_by_level import count_files_by_level
from get_total_files import get_total_files
from is_valid import is_valid
import no


class FileSystemTree:
    def __init__(self):
        self.raiz = no.no("/")

    def add_file(self, path) -> bool:
        return add_file(self, path)

    def file_exists(self, path) -> bool:
        return file_exists(self, self.raiz, path)

    def get_directory_contents(self, path):
        return get_directory_contents(self, self.raiz, path)

    def get_files_by_extension(self, ext):
        return get_files_by_extension(self, self.raiz, ext)

    def get_max_depth(self) -> int:
        return get_max_depth(self.raiz)

    def count_files_by_level(self):
        return count_files_by_level(self)

    def get_total_files(self) -> int:
        return get_total_files(self.raiz)

    def is_valid(self) -> bool:
        return is_valid(self.raiz)
