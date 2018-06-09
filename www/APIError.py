import json, logging, inspect, functools


class Page(object):
    def __init__(self,item_count,page_index=1,page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size>0 else 0)
        if (item_count==0 ) or (page_index>self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index -1)
            self.limit = self.page_size
        self.has_next = self.page_index<self.page_count
        self.has_previous = self.page_index > 1


    def __str__(self):
        return 'item_count:%s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)

    __repr__ = __str__



class APIError(Exception):
    """
    基础的APIError,包含错误类型（必要），数据（可选），信息（可选）
    """
    def __init__(self, error, data='', message= ' ' ):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """
    表明输入数据有问题，data 说明输入的错误字段
    """
    def __init__(self, field, message = ''):
        super(APIValueError,self).__init__('value:invalid', field, message)


class APIResourceNotfoundError(APIError):
    def __init__(self, field, message = ''):
        super(APIResourceNotfoundError, self).__init__('value: Notfound', field, message)


class APIPermissionError(APIError):
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('PERMISSION: forbidden', 'permission', message)
