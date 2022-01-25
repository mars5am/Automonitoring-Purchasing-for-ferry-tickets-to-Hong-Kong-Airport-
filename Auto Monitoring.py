from splinter.browser import Browser
from time import sleep
import smtplib
import email
import traceback
# 负责构造文本	
from email.mime.text import MIMEText	
# 负责构造图片	
from email.mime.image import MIMEImage	
# 负责将多个对象集合起来	
from email.mime.multipart import MIMEMultipart	
from email.header import Header
import traceback

class Buy_Tickets(object):
    def __init__(self,username,passwd,siteResJson,toDate,airline,flightNo,flightDate,realName,passport,Surname,familyName,birthday,order):
        self.username=username
        self.passwd=passwd
        self.siteResJson=siteResJson
        self.toDate=toDate
        self.airline=airline
        self.flightNo=flightNo
        self.flightDate=flightDate
        self.realName=realName
        self.passport=passport
        self.Surname=Surname
        self.familyName=familyName
        self.birthday=birthday
        self.order=order
        self.login_url='https://www.cmskchp.com/'
        self.initMy_url = 'https://www.cmskchp.com/personCenter'
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.ticket_url='https://www.cmskchp.com/sailings'

    # 登录
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.find_by_text('登录').click()
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/input').fill(self.username)
        #填写用户名
        sleep(1)
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/input').fill(self.passwd)
        #填写密码
        sleep(1)
        print('请输入验证码')
        while True:
            if self.driver.url!=self.initMy_url:
                sleep(1)
            else:
                break
    # 买票
    def start_buy(self):
        self.driver=Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.login()
        self.driver.visit(self.ticket_url)
        print('开始买票')
        #加载查询信息
        self.driver.cookies.add({"siteResJson": self.siteResJson})
        self.driver.reload()
        self.driver.find_by_text('展开航空选择').click()
        #填写出发时间
        js1 = 'document.getElementById("to_date").removeAttribute("readonly");'
        self.driver.execute_script(js1)
        to_date=self.driver.find_by_id('to_date')[0]
        to_date.clear()
        js2= 'document.getElementById("to_date").value = "2021-09-14"'
        self.driver.execute_script(js2)
        self.driver.find_by_text('搜索').click()
        self.driver.find_by_text('确定').click()
        #填写航空公司
        autocomplete=self.driver.find_by_id('autocomplete')
        autocomplete.click()
        self.driver.find_by_text('荷兰航空').click()
        #填写航班号
        self.driver.find_by_id('flightNo').fill(self.flightNo)
        #填写起飞日期
        #js2 = 'document.getElementById("flightDate").removeAttribute("readonly");'
        #self.driver.execute_script(js2)
        #flightDate = self.driver.find_by_id('flightDate')
        #flightDate.clear()
        #flightDate.fill(self.flightDate)
        #填写起飞整点
        self.driver.find_by_id('flightHours').click()
        self.driver.find_by_text('20').click()
        #填写起飞分钟
        sleep(1)
        #self.driver.find_by_id('flightMinute').click()
        #self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div/div[7]/div[2]/dl[2]/dd/p[16]').click()

        sleep(1)
        #self.driver.find_by_text('搜索').click()
        


        while True:
            if self.driver.url!=self.ticket_url:
                sleep(1)
            else:
                break

            # 处理alert弹窗
        #try:
           # self.driver.find_by_text('确定').click()
        #except Exception as e:
           # print(e)
           # print('没有出现弹窗')
            # 接受弹窗信息

        

        count=0
        if self.order!=0:
            while self.driver.url==self.ticket_url:
                try:
                    self.driver.find_by_text('订票')
                    self.driver.find_by_text('购票')[self.order-1].click()
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    print('预订失败')
                    continue
        else:
            while self.driver.url==self.ticket_url:
                count+=1
                print('第%d次点击查询...' % count)


                try:
                    self.driver.reload()
                    sleep(1)
                    #try:
                     #  js='document.querySelector("#all_sailing > div > div.sk_lttr_top > ul > li.fl.sk_lw125.air_line_hide").style.display="block";'
                     #  self.driver.execute_script(js)
                     #  left=self.driver.find_by_xpath('//*[@id="all_sailing"]/div/div[1]/ul/li[4]').text
                     #  print(left)
                    #except Exception as e:
                     #  print(e)
                      # print('也许是网速问题...')

                    #try:
                      # self.driver.find_by_text('确定').click()
                    #except Exception as e:
                       # print(e)
                       # print('没有出现弹窗')
                        
                    #self.driver.find_by_text('订票').click()
                    #for i in self.driver.find_by_text('购票'):
                    #    i.click()
                    #    sleep(1)
                    
                    for i in self.driver.find_by_text('订票'):
                        i.click()
                    for i in self.driver.find_by_text('购票'):
                        i.click()
                    sleep(1)

                except Exception as e:
                    print(e)
                    print('预定又失败了')
                    continue

        print('开始预订...')
        self.driver.find_by_text('添加乘客').first.click()
            # 点击添加成人乘客
        try:
            # SMTP服务器,这里使用163邮箱	
            mail_host = "smtp.163.com"	
        # 发件人邮箱	
            mail_sender = "miumiumilkyway@163.com"	
        # 邮箱授权码
            mail_license = "CDQHBAEQZCGGHRYK"	
        # 收件人邮箱，可以为多个收件人	
            mail_receivers = ["1244673092@qq.com","616585987@qq.com"]

            mm = MIMEMultipart('related')

            # 邮件主题	
            subject_content = """抢票成功！"""	
            # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱	
            mm["From"] = "sender_name<miumiumilkyway@163.com>"	
            # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱	
            mm["To"] = "receiver_1_name<1244673092@qq.com>,receiver_2_name<616585987@qq.com>"	
            # 设置邮件主题	
            mm["Subject"] = Header(subject_content,'utf-8')

            
            # 邮件正文内容	
            body_content = """你好，抢票成功！"""	
            # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式	
            message_text = MIMEText(body_content,"plain","utf-8")	
            # 向MIMEMultipart对象中添加文本对象
            mm.attach(message_text)

            # 创建SMTP对象	
            stp = smtplib.SMTP()	
            # 设置发件人邮箱的域名和端口，端口地址为25	
            stp.connect(mail_host, 25)  	
            # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息	
            stp.set_debuglevel(1)	
            # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码	
            stp.login(mail_sender,mail_license)	
            # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str	
            stp.sendmail(mail_sender, mail_receivers, mm.as_string())	
            print("邮件发送成功")	
            # 关闭SMTP对象	
            stp.quit()

        except Exception as e:
            print(e)
            print('邮件发送失败')

        sleep(1)
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div[1]/div/input').fill(self.realName)
            # 填写姓名 debug的时候要看一下
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div[1]/input').fill(self.passport)
            # 护照号码
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div[2]/input[1]').fill(self.Surname)
            # 姓
        self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div[2]/input[2]').fill(self.familyName)
            # 名
        js3 = 'document.querySelector("#URT001-certInfo-1 > input").removeAttribute("readonly");'
        self.driver.execute_script(js3)
        choosebirthday=self.driver.find_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div[3]/input')
        choosebirthday.clear()
        js4= 'document.querySelector("#URT001-certInfo-1 > input").value = "1997-04-24"'
        self.driver.execute_script(js4)
            # 填写生日
        self.driver.find_by_id('read').click()
        self.driver.find_by_text('已阅读并同意条款').click()
            # 点击勾选确认
        self.driver.find_by_id('submit').click()
            # 提交订单
        self.driver.find_by_text('去支付').click()
        print('请支付')



if __name__ == '__main__':
    # 用户名
    username = '111111'
    # 密码
    passwd = '111111'
    siteResJson='%7B%22userType%22%3A%22LTP001%22%2C%22sailingType%22%3A%220%22%2C%22toDate%22%3A%222021-09-14%22%2C%22startSiteName%22%3A%22%E6%B7%B1%E5%9C%B3%E8%9B%87%E5%8F%A3%22%2C%22endSiteName%22%3A%22%E9%A6%99%E6%B8%AF%E6%9C%BA%E5%9C%BA%22%2C%22backDate%22%3A%22%22%2C%22lineId%22%3A%22SK-HKA%22%2C%22startSite%22%3A%22SK%22%2C%22endSite%22%3A%22HKA%22%2C%22flightId%22%3A%2245%22%2C%22flightName%22%3A%22%E8%8D%B7%E5%85%B0%E8%88%AA%E7%A9%BA%22%2C%22flightNo%22%3A%22KL820%22%2C%22flightDate%22%3A%222021-09-14%22%2C%22flightHours%22%3A%2220%22%2C%22flightMinute%22%3A%2215%22%2C%22code%22%3A%22KL%22%2C%22flightCode%22%3A%22KL%22%7D'
    toDate='2000-01-01'  #船票日期
    airline='XX'    #航司名
    flightNo='XX111'   #航班号
    flightDate='2000-01-01'  #起飞日期
    realName='XXX'
    passport='AA111111'   #护照号
    Surname='X'            #姓名
    familyName='XX'
    birthday='1990-01-01'    #生日
    order=0
    Buy_Tickets(username, passwd,siteResJson,toDate,airline,flightNo,flightDate,realName,passport,Surname,familyName,birthday,order).start_buy()
