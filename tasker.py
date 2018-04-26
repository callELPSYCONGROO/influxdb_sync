#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
APScheduler实现定时任务。
"""


from apscheduler.schedulers.blocking import BlockingScheduler


class Tasker(object):

    def __init__(self, wait_time, job_func):
        """
        :param int wait_time: 等待时间，单位秒
        :param function job_func:  执行函数
        """
        self.wait_time = wait_time
        self.job_func = job_func
        self.__sched = BlockingScheduler()

    def start(self):
        self.__sched.add_job(self.job_func, 'interval', seconds=self.wait_time)
        try:
            self.__sched.start()
        except (SystemExit, KeyboardInterrupt):
            print('任务终止！')
        except Exception:
            print('任务异常！')
