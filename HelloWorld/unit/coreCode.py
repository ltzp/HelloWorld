#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2017/9/27 下午7:39
# @Author  : Letao@zingfront.com
# @Site    : 
# @File    : coreCode.py.py
# @Software: SocialPeta

import jieba
import jieba.analyse

class Launge(object):

    @staticmethod
    def statistics(str):
        tags = jieba.analyse.extract_tags(str, topK=5, withWeight=False)
        text = " ".join(tags)
        #text = unicode(text)
        return text