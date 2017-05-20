#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/23 13:00
# @Version : python 3.4
# @Author  : KingDow

import glob
import os
import smtplib
import threading
import zipfile
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import readConfig
from common.logConfig import GetLog

localReadConfig = readConfig.ReadConfig()


class EmailConfig(object):
    def __init__(self):
        self.log = GetLog().log()
        self.host = localReadConfig.conf_email("mail_host")
        self.user = localReadConfig.conf_email("mail_user")
        self.password = localReadConfig.conf_email("mail_pass")
        self.port = localReadConfig.conf_email("mail_port")
        self.sender = localReadConfig.conf_email("sender")
        self.content = localReadConfig.conf_email("content")
        self.value = localReadConfig.conf_email("receiver")
        self.receiver = []
        # 获取收件人邮箱地址列表
        for n in str(self.value).split("/"):
            self.receiver.append(n)
        # 邮件主题 = title + date
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = localReadConfig.conf_email("subject")
        self.subject = title + " " + date
        self.msg = MIMEMultipart('mixed')
        self.reportpath = readConfig.os.getcwd()  # self.log.get_result_path()
        self.zippath = os.path.join(readConfig.os.getcwd(), "test.zip")

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = self.sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(self.content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def config_image(self):  # 待调试
        msg_alter_native = MIMEMultipart('alternative')
        self.msg.attach(msg_alter_native)
        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """
        msg_alter_native.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        fp = open('test.png', 'rb')
        msg_image = MIMEImage(fp.read())
        fp.close()
        msg_image.add_header('Content-ID', '<image1>')
        self.msg.attach(msg_image)

    def config_file(self):
        if not self.check_file():
            files = glob.glob(self.reportpath + '\*')  # 遍历文件夹下所有文件写入列表
            f = zipfile.ZipFile(self.zippath, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                f.write(file)
            f.close()
            reportfile = open(self.zippath, 'rb').read()
            file_html = MIMEText(reportfile, 'base64', 'utf-8')
            file_html['Content-Type'] = 'application/octet-stream'
            file_html['Content-Disposition'] = 'attachment; filename="testReport.zip"'
            self.msg.attach(file_html)

    def check_file(self):
        if os.path.isfile(self.reportpath) and not os.stat(self.reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        # self.config_image()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.host)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.log.info("The test report has send to developer by email.")
        except Exception as e:
            self.log.error(str(e))


class SendEmail(object):
    def __init__(self):
        self.email = None
        self.mutex = threading.Lock()

    def get_email(self):
        if self.email is None:
            self.mutex.acquire()
            self.email = EmailConfig()
            self.mutex.release()
        return self.email
