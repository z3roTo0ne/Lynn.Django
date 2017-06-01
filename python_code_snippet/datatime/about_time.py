# coding=utf-8
import datetime
import time
import types


class DateTimeOpt(object):
    """
    日期时间管理类
    """

    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.today = datetime.datetime.today()

    def days_before(self, days):
        # 获取n天前的日期
        n_days_before = self.today - datetime.timedelta(days=days)
        return n_days_before.strftime('%Y-%m-%d')

    def days_after(self, days):
        n_days_after = self.today + datetime.timedelta(days=days)
        return n_days_after.strftime('%Y-%m-%d')

    @staticmethod
    def to_timestamp(time_str):
        assert type(time_str) == types.StringType
        time_arr = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        return time.mktime(time_arr)

    @staticmethod
    def format_date():
        # 获取并格式化当前时间
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    d = DateTimeOpt()
    print d.to_timestamp(d.format_date())