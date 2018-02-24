# -*- coding: utf-8 -*-
from collections import OrderedDict
from urllib import urlencode

from constants import (
    SearchArticleType,
    SearchArticleTime,
    HotArticleType
)

_search_gzh = 1
_search_article = 2


class SogouRequest:

    def __init__(self):
        pass

    @classmethod
    def generate_search_article_url(cls, keyword, page,
                                    time=SearchArticleTime.ANYTIME, article_type=SearchArticleType.ALL):
        assert isinstance(page, int) and page > 0
        assert time in SearchArticleTime.__dict__.values()
        query = OrderedDict()
        query['type'] = _search_article
        query['page'] = page
        query['ie'] = 'utf-8'
        query['tsn'] = time
        query['query'] = keyword
        if article_type == SearchArticleType.ALL:
            query['interation'] = '%s,%s' % (SearchArticleType.IMAGE, SearchArticleType.VIDEO)
        else:
            query['interation'] = article_type

        return 'http://weixin.sogou.com/weixin?%s' % urlencode(query)

    @classmethod
    def generate_search_gzh_url(cls, keyword, page=1):
        assert isinstance(page, int) and page > 0 #不符合的时候让程序停止

        query = OrderedDict()
        query['type'] = _search_gzh
        query['page'] = page
        query['ie'] = 'utf8'
        query['query'] = keyword

        return 'http://weixin.sogou.com/weixin?%s' % urlencode(query)

    @staticmethod
    def generate_hot_url(hot_type, page=1):
        assert isinstance(page, int) and page > 0

        return 'http://weixin.sogou.com/wapindex/wap/0612/wap_%s/%s.html' % (hot_type, page - 1)


if __name__ == '__main__':
    url = SogouRequest.generate_search_gzh_url('九章算法')
    print url