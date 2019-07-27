from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含“To-Do"这个词
        self.assertIn( 'To-Do' in browser.title)
        self.fail('finish the test!')

        # 应用邀请她输入一个待办事项

        # 她在一个文本框中输入了“Buy peacock feathers" (购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵料钓鱼

        # 她按回车键后，页面更新了
        # 代办事项表格中显示了“1：Buy peacock feathers"

        # 页面中又显示了一个文本框，可以输入其他的代办事项

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为他生成了一个唯一的URL
        # 而且页面中又一些文字解说这个功能

        # 她访问那个URL，发现她的待办事项还在

        # 她很满意，去睡觉了

if __name__== '__main__':
    unittest.main()

