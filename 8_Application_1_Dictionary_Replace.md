# Dictionary_Replace
This section will show a example how to use dictionary, and how to replace content for duplicated work
We use module json, re, codecs (check [module information](1_Module.md))

```
import json, re, codecs

emails = {}

def trash_mail(mail_list, mail_template): # 定义函数
    f_addr = codecs.open(mail_list,encoding='utf-8') # 打开邮件地址文件
    dict_addr = json.load(f_addr) # 将json解析为字典结构

    f_temp = codecs.open(mail_template,encoding='utf-8').read() # 打开并读取邮件模板

    for i in dict_addr: # 对收件人列表循环

        to_replace = re.sub('\[address]', dict_addr[i], f_temp) # 替换[address]为收件人地址

        # 请继续替换收件人姓名
        # 代码补完
        to_replace = re.sub('\[name]', i, f_temp) 

        # 代码补完

        emails[i] = to_replace

mail_list = "address.json" # 邮件群发地址的json文件
mail_template = "email.txt" # 邮件模板txt文件

trash_mail(mail_list, mail_template) # 执行函数，传入参数

# 查看邮件内容（重点是[address]和[name]是否替换成功）
print(emails['Kobe Bryant'])
```
