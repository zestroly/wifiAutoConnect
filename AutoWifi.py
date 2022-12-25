import pywifi
from pywifi import const
import time
import os
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import *
from PySide6.QtCore import QSettings

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem)
from ui_form import Ui_Home


def is_connected(wifi_inter):
    if wifi_inter.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
        return True
    else:
        return False


def connet_wifi(wifi_inter, wifi_profile):
    wifi_inter.remove_all_network_profiles()  # 删除其它配置文件
    tmp_profile = wifi_inter.add_network_profile(wifi_profile)  # 加载配置文件
    wifi_inter.connect(tmp_profile)
    time.sleep(2)
    if wifi_inter.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False


def set_profile(ssid, password):
    wifi_profile = pywifi.Profile()  # 配置文件
    wifi_profile.ssid = ssid  # wifi名称
    wifi_profile.auth = const.AUTH_ALG_OPEN  # 需要密码
    wifi_profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
    wifi_profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    wifi_profile.key = password  # wifi密码
    return wifi_profile


class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QSettings('config.ini', QSettings.IniFormat)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.wifi = pywifi.PyWiFi()
        self.interface = self.wifi.interfaces()[0]
        self.connectCount = 0
        self.ui.connect.clicked.connect(self.buttonClicked)
        self.timerId = 0
        self.ssid = self.settings.value('ssid', 'HelKitty')
        self.password = self.settings.value('password', 'HelKitty')
        self.profile = set_profile(self.ssid, self.password)
        self.ui.ssid.setText(self.ssid)
        self.ui.password.setText(self.password)

        if self.settings.value('isRun', False, type=bool):
            self.ui.connect.click()

    def wifiCheck(self):
        self.log('检查网络')
        if not is_connected(self.interface):
            self.log('网络已断开，重新连接中……')
            con = connet_wifi(self.interface, self.profile)
            self.connectCount += 1
            if not con and self.connectCount <= 3:
                self.log(f'连接{self.connectCount}次，连接失败!')
            else:
                res = '成功' if con else '失败'
                self.log(f'尝试连接{self.connectCount}次，连接{res}!')
                self.connectCount = 0
        else:
            self.log('网络已连接')

    def timerEvent(self, evt):
        self.wifiCheck()

    def log(self, txt):
        self.ui.Log.append(txt)

    def buttonClicked(self, enable):
        if enable:
            self.ui.connect.setText(u'暂停')
            self.timerId = self.startTimer(5000)
            self.ui.ssid.setEnabled(False)
            self.ui.password.setEnabled(False)
            self.password = self.ui.password.text()
            self.settings.setValue('ssid', self.ssid)
            self.settings.setValue('password', self.password)
            self.settings.setValue('isRun', True)
            self.settings.sync()
            self.ssid = self.ui.ssid.text()
            self.profile = set_profile(self.ssid, self.password)
            self.process_auto_run(True)
        else:
            self.ui.connect.setText(u'开始')
            self.killTimer(self.timerId)
            self.ui.ssid.setEnabled(True)
            self.ui.password.setEnabled(True)
            self.process_auto_run(False)
            self.settings.setValue('isRun', False)
            self.settings.sync()

    def process_auto_run(self, flag):
        settings = QSettings('HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', QSettings.NativeFormat)
        exeName = os.path.realpath(sys.argv[0])  # 获取当前运行的文件名称
        exePath = os.path.dirname(exeName)  # 获取当前运行文件所在的目录
        if flag:
            self.log(f'{exeName},目录：{exePath}')
            settings.setValue(exeName, exePath)
        else:
            self.log(f'删除自启动：{exeName}')
            settings.remove(exeName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Home()
    widget.show()
    sys.exit(app.exec())

#pyinstaller -F 文件.py