import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys


class TestClass:
    def setup_class(self):
        print('打开浏览器进入登录页面')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://login.duofriend.com/jsp/login/login.jsp')
        # self.driver.get('https://baidu.com')
        self.driver.maximize_window()
        return self.driver

    # def test_A001(self):
    #     def aa(self):
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('酒吧系统')
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath('//*[@id="su"]').click()
    #         original_window = self.driver.current_window_handle
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath('//*[@id="m6006880887_canvas"]/div/div[1]/div[1]/div/h2/a/span').click()
    #         time.sleep(2)
    #         new_window = self.driver.window_handles[-1]  # 获取新打开的标签页句柄
    #         self.driver.switch_to.window(new_window)  # 切换到新标签页
    #         self.driver.close()
    #         self.driver.switch_to.window(original_window)  # 切换回原来的标签页
    #         time.sleep(2)
    #         self.driver.refresh()  # 刷新当前页面
    #         time.sleep(1)
    #         self.driver.find_element_by_xpath('//*[@id="kw"]').clear()
    #
    #     for i in range(100):
    #         aa(self)
    #
    #     return self.driver



    def test_E001(self):
        print('登录账号')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/input').send_keys('dfty')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[5]/input').send_keys('asd8523')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[12]/button').click()
        return self.driver

    def test_E002(self):
        print('进入多粉一级菜单')
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[text()='商城']").click()
        return self.driver

    def test_E003(self):
        print('进入商城二级菜单')
        time.sleep(1)
        self.driver.switch_to.default_content()  # 进入碎片后返回父类
        self.driver.find_element_by_xpath("//li[text()='商品管理']").click()
        self.driver.switch_to.frame('iframeMain')  # 进入碎片
        return self.driver

    def test_E004(self):
        print('循环多次创建新商品')
        time.sleep(1)

        def addstor(self, name):
            self.driver.find_element_by_xpath('//*[@id="tab-product-list"]')
            time.sleep(1)
            bt_primary = self.driver.find_element_by_xpath("//button/span[text()='发布商品']")
            bt_primary.click()

            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="product-layout"]/div[2]/div[6]/div/div[2]/div/div[5]/div[2]').click()

            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/div/div/div').click()

            time.sleep(1)
            # bt_ulstorelist = driver .find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul')
            bt_select_store = self.driver.find_element_by_xpath("//li/span[text()='黄牛票专卖']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", bt_select_store)
            time.sleep(0.5)
            bt_select_store.click()

            time.sleep(0.5)
            self.driver.find_element_by_class_name('el-textarea__inner').send_keys(name)

            time.sleep(0.5)
            self.driver.find_element_by_xpath(
                '//*[@id="pro-info"]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/span/span/i').click()

            time.sleep(1)
            bt_fenzhu = self.driver.find_element_by_xpath(
                "//html/body/div[5]/div[1]/div/div[1]/ul/li[2]/span/preceding-sibling::label/span")  # preceding-sibling:: 定位到同一级
            self.driver.execute_script("arguments[0].scrollIntoView(true);", bt_fenzhu)
            time.sleep(0.5)
            bt_fenzhu.click()

            time.sleep(0.5)
            self.driver.find_element_by_xpath('//*[@id="material-select"]/div[1]/div/i').click()

            time.sleep(1)
            self.driver.switch_to.default_content()  # 切回父类外层的 iframe
            iframe = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/iframe")
            self.driver.switch_to.frame(iframe)

            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/div[1]/span[2]").click()

            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="views"]/div[2]/div[2]/div[2]').click()
            self.driver.find_element_by_xpath(
                '//*[@id="material"]/div[1]/div[2]/div[3]/div[2]/button[2]/span').click()
            self.driver.switch_to.default_content()  # 切回父类外层的 iframe.click()
            self.driver.switch_to.frame('iframeMain')  # 进入碎片

            time.sleep(0.3)
            self.driver.find_element_by_xpath(
                '//*[@id="spec-block"]/form/div/div[2]/div[3]/div[1]/div/div/input').send_keys('1000')

            time.sleep(0.3)
            self.driver.find_element_by_xpath(
                '//*[@id="spec-block"]/form/div/div[2]/div[4]/div/div/div/div[1]/input').send_keys('1000')

            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="spec-block"]/form/div/div[2]/div[5]/div[1]/div/div/div/input').click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//li/div/span[text()='副']").click()

            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/button[1]').click()

            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/button[2]').click()

            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/button[5]').click()

        text = 1
        for i in range(5):
            addstor(self, '23.11.7自动化商品' + str(text))
            text = text + 1

        return self.driver

    def test_E005(self):
        print("搜索商品")
        time.sleep(2)
        input_search = self.driver.find_element_by_xpath(
            '//*[@id="product-layout"]/div[2]/div[1]/div/div[1]/div[5]/input')
        input_search.send_keys('23.11.7自动化商品')
        input_search.send_keys(Keys.RETURN)
        return self.driver

    def test_E006(self):
        print('删除所有相关的商品')

        def dele(self):
            time.sleep(2)
            bt_more = self.driver.find_element_by_xpath(
                '//*[@id="proTable"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/div/div[2]/button')
            ActionChains(self.driver).move_to_element(bt_more).perform()
            time.sleep(1)
            bt_dele = self.driver.find_element_by_xpath('/html/body/ul[1]/li[2]')
            bt_dele.click()
            time.sleep(1)
            bt_ok = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]')
            bt_ok.click()

        while True:
            try:
                element = self.driver.find_element_by_xpath('//span[contains(text(),"23.11.7自动化商品")]')
                if element:
                    dele(self)
                else:
                    break
            except NoSuchElementException:

                break

    def teardown_class(self):
        print('关闭浏览器')
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["-vs", "test_case.py"])
