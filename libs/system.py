# -*- coding: utf-8 -*-
import os
import sys
import re
from shell import shell


os_info = {
    "os_info": "Roycom Storage",
    "version": "v1.0"
}


class Common(object):
    @staticmethod
    def shell_exec(cmd, re_type="str"):
        if not isinstance(cmd, str):
            raise TypeError("Type error:must be str.")
        t_str = ""
        t_list = shell(cmd).output()
        if re_type == "list":
            return t_list
        elif re_type == "str":
            for i in t_list:
                t_str = t_str + i + "\n"
            return t_str
        else:
            raise TypeError("Param type error: must be str or list.")

    @staticmethod
    def regex_str_lines(src_str, reg_str):
        pattren = re.compile(reg_str, flags=re.M)
        match = pattren.findall(src_str)
        return match

    @staticmethod
    def regex_list_lines(src_list, reg_str):
        if not isinstance(src_list, list) or not isinstance(reg_str, str):
            raise TypeError("TypeError:src_list and reg_str must be list and str.")
        result_list = []
        for s in src_list:
            if re.match(reg_str, s) is not None:
                result_list.append(s)
        return result_list

    @staticmethod
    def split_str(src_str, split_str=" "):
        if not isinstance(src_str, str):
            raise Exception("src_str type error.")
        else:
            if split_str == " ":
                return src_str.split()
            else:
                return src_str.split(split_str)

    @staticmethod
    def regex_str_line_column(src_str, reg_str, count, split_s=" "):
        t_list = Common.regex_str_lines(src_str, reg_str)
        len_list = []
        column_list = []
        for i in t_list:
            t_list_1 = Common.split_str(i, split_s)
            len_list.append(len(t_list_1))
            if count <= len(t_list_1):
                column_list.append(t_list_1[count - 1])
        return column_list

    @staticmethod
    def regex_list_line_column(src_list, reg_str, count, split_s=" "):
        t_list = Common.regex_list_lines(src_list, reg_str)
        len_list = []
        column_list = []
        for i in t_list:
            t_list_1 = Common.split_str(i, split_s)
            len_list.append(len(t_list_1))
            if count <= len(t_list_1):
                column_list.append(t_list_1[count - 1])
        return column_list

