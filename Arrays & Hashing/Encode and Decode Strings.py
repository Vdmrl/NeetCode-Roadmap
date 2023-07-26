import re

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        coded = ""
        for i in strs:
            coded += i
            coded += 'ЗаЛуПа_ИвАнЫчА'
        return coded

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        pattern = re.compile("ЗаЛуПа_ИвАнЫчА")
        return pattern.split(str)[0:-1]