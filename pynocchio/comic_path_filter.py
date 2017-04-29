# -*- coding: utf-8 -*-

import glob
from .utility import Utility
from .exception import NoDataFindException


class ComicPathFilter:

    def __init__(self, extension_list):
        self.file_list = []
        self.current_path = None
        self.extension_list = extension_list
        self.current_index = None

    def parse(self, path):

        self.current_path = path
        self.file_list = []

        for ext in self.extension_list:
            self.file_list.extend(glob.glob1(path, ext))

        # sort list
        self.file_list.sort()

    def is_first_comic(self, filename):
        try:
            return True if self.file_list[0] == filename else False
        except IndexError as exc:
            raise NoDataFindException(
                'ComicPathFilter file list is empty!') from exc

    def is_last_comic(self, filename):
        try:
            return True if self.file_list[-1] == filename else False
        except IndexError as exc:
            raise NoDataFindException(
                'ComicPathFilter file list is empty!') from exc

    def get_previous_comic(self, filename):

        if not self.is_first_comic(filename):
            name = self.file_list[self.file_list.index(filename) - 1]
            return Utility.join_path(self.current_path, '', name)
        else:
            raise NoDataFindException('ComicPathFilter reach first file!')

    def get_next_comic(self, filename):

        if not self.is_last_comic(filename):
            name = self.file_list[self.file_list.index(filename) + 1]
            return Utility.join_path(self.current_path, '', name)
        else:
            raise NoDataFindException('ComicPathFilter reach last file!')
