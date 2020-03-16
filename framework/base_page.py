#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 0006 下午 15:18
# @Author : ShaoMingJin
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os.path
from framework.logger import Logger

'定义页面基类'
class BasePage(object):
    # 创建一个日志实例
    logger = Logger()
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
    """
    def __init__(self, driver):
        self.driver=driver

    '''
    打开指定的网址
    '''
    def open(self, url):
        self.driver.get(url)

    '''
    窗口最大化
    '''
    def maxWindows(self):
        self.driver.maximize_window()

    '''
    浏览器前进操作
    '''
    def forward(self):
        self.driver.forward()
        self.logger.info("在当前页面点击向前.")

    '''
    浏览器后退操作
    '''
    def back(self):
        self.driver.back()
        self.logger.info("点击浏览器上返回按钮.")

    '''
    刷新当前页面
    '''
    def refresh(self):
        self.driver.refresh()

    '''
     显示等待
    '''
    def wait(self, element, seconds):
        try:
            wait_ = WebDriverWait(self.driver, seconds)
            wait_.until(lambda driver: element)
            self.logger.info("等待了%d秒." %seconds)
        except NameError as e:
           self.logger.error("Failed to load the element with %s" % e)

    '''
    保存图片
    '''
    def get_windows_img(self):
        """
        把file_path保存到项目根目录的一个文件夹.\screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '\\screenshots\\'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.logger.info("Had take screenshot and save to folder : \screenshots")
        except NameError as e:
            self.logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    '''
    根据指定的字符串定位元素
    '''
    def getElementObject(self,strValue):
        try:
            '分割字符串'
            locatorType=strValue.split("->")[0]
            locatorValue=strValue.split("->")[1]
            '判断'
            if locatorType.lower()=='id':
                return self.driver.find_element_by_id(locatorValue)
            elif locatorType.lower()=='name':
                return self.driver.find_element_by_name(locatorValue)
            elif locatorType.lower()=='classname' or locatorType.lower()=='class':
                return self.driver.find_element_by_class_name(locatorValue)
            elif locatorType.lower()=='tagname' or locatorType.lower()=='tag':
                return self.driver.find_element_by_tag_name(locatorValue)
            elif locatorType.lower()=='linktext' or locatorType.lower()=='link':
                return self.driver.find_element_by_link_text(locatorValue)
            elif locatorType.lower()=='partiallinktext':
                return self.driver.find_element_by_partial_link_text(locatorValue)
            elif locatorType.lower()=='xpath':
                return self.driver.find_element_by_xpath(locatorValue)
        except:
            self.logger.info("定位元素失败！")

    '''
    文本框中输入
    '''
    def send_keys(self, element, text):
        self.wait(element, 10)
        self.clear(element)
        #element.clear()
        try:
            element.send_keys(text)
            self.logger.info("在输入框中输入' %s \'成功" % text)
        except NameError as e:
            self.logger.error("Failed to select in input box with %s" % e)
            self.get_windows_img()

    '''
    获取指定元素的文本内容
    '''
    def getText(self, element):
        self.wait(element,20)
        return element.text

    '''
    清除文本框中内容
    '''
    def clear(self, element):
        try:
            element.clear()
            self.logger.info("输入内容之前清空输入框")
        except NameError as e:
            self.logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    '''
    判断元素是否可见
    '''
    def isDisplay(self, element):
        try:
            self.wait(element,20)
            return element.is_displayed()
        except:
            self.logger.info("%s元素在20秒内不显示"%element)

    '''
    判断元素是否启用
    '''
    def isEnabled(self, element):
        self.wait(element,20)
        return element.is_enabled()

    '''
    获取当前页面的title
    '''
    def getTitle(self):
        return self.driver.title

    '''
    获取当前页面的url
    '''
    def getCurrentUrl(self):
        return self.driver.current_url

    '''
    全局等待,Implicitly wait.All elements on the page.
    '''
    def waitAllElementDisplay(self, secs):
        self.driver.implicitly_wait(secs)

    '''
    点击元素
    '''
    def click(self, element):
        '等待10秒钟'
        self.wait(element,10)
        try:
            element.click()
            self.logger.info("当前元素 %s 被点击." % element.text)
        except NameError as e:
            print(e)
            self.logger.error("Failed to click the element with %s" % e)

    '''
    鼠标左键点击链接文本
    '''
    def clickLinkText(self, text):
        self.driver.find_element_by_partial_link_text(text).click()

    '''
    根据指定的值选中相应的下拉列表中的选项
    --如果没有指定的值则抛出异常
    '''
    def selectByValue(self, element, value):
        self.wait(element,20)
        Select(element.select_by_value(value))

    '''
    #操作select下拉框，通过下标选择
    :param xpath:xpath
    :param index:下标
    '''
    def select_by_index(self,  element, index):
        self.wait(element,20)
        Select(element).select_by_index(index)

    '''
    操作select下拉框，通过可视文本值选择
    param xpath:xpath
    param text:可视文本
    '''
    def select_by_visible_text(self, element,text):
        self.wait(element, 20)
        Select(element).select_by_visible_text(text)

    '''
    判断元素是否选中,一般用于验证checkbox和radio
    '''
    def isSelected(self, element):
        self.wait(element,20)
        return element.is_selected()

    '''
    弹框警告-确认
    '''
    def alertAccept(self):
        self.driver.switch_to.alert.accept()

    '''
    弹框警告-取消
    '''
    def alertDismiss(self):
        self.driver.switch_to.alert.dismiss()

    '''
    切换到指定的iframe
    '''
    def switchFrame(self, element):
        self.wait(element,20)
        self.driver.switch_to.frame(element)

    '''
    切换到上一级(iframe)
    '''
    def switchFrameOut(self):
        self.driver.switch_to.default_content()

    '''
    打开新页面,并切换当前句柄为新页面的句柄
    (每个页面对应一个句柄handle,可以通过self.driver.window_handles查看所有句柄)
    --当前方法可能存在问题
    '''
    def openNewWindow(self):
        original_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)
        return self.driver

    '''
    #切换到名字为title的窗口
    :param title: 窗口标题
    :return: 返回值：当前窗口的句柄
    '''
    def switch_to_windows_by_title(self,title):
        current = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if (self.driver.title.__contains__(title)):
                break
        return current
    '''
    鼠标右键元素菜单
    '''
    def rightClick(self, element):
        self.wait(element,20)
        ActionChains(self.driver).context_click(element).perform()

    '''
    移动鼠标到指定元素(默认在元素的中间位置)
    '''
    def moveToTargetElement(self, element):
        self.wait(element,20)
        ActionChains(self.driver).move_to_element(element).perform()

    '''
    鼠标左键双击
    '''
    def doubleClick(self, element):
        self.wait(element,20)
        ActionChains(self.driver).double_click(element).perform()

    '''
    #xpath 定位 输入文件路径 上传文件
    :param Keys:操作步骤,xpath定位 输入文件路径
    '''
    def upload_files(self, step, Xpath, file_path):
        self.driver.find_element_by_xpath(Xpath).send_keys(file_path)

    '执行JS脚本'
    def execute_script(self, js):
        self.driver.execute_script(js)

    '''
    滚动窗口，滚到底
    param step:操作步骤
    '''
    def scroll_screen_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    '''
    向下滑动滚动条，跳转到目标元素处
    '''
    def scroll_screen_element(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();",element)

    '''
    向上滑动滚动条，跳转到目标元素处
    '''
    def scroll_screen_up(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(false);",element)