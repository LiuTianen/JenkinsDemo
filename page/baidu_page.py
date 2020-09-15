from poium import Page, PageElement, PageElements
import time

class BaiduPage(Page):
    search_input = PageElement(id_="kw", describe="搜索框")
    search_button = PageElement(id_="su", describe="搜索按钮")
    settings = PageElement(xpath='//*[@id="s-usersetting-top"]', describe="设置下拉框")
    search_setting = PageElement(css=".setpref", describe="搜索设置选项")
    save_setting = PageElement(css=".prefpanelgo", describe="保存设置")

    # 定位一组元素
    search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")

    def search_succes(self, values):
        self.search_input = values
        self.search_button.click()

    def baidu_seeting(self):
        self.settings.click()
        self.search_setting.click()
        time.sleep(2)
        self.save_setting.click()
