import os
import sys
import MySQLdb


class Friend:
    ID = 0
    Name = ''
    URL = ''


def get_list():
    return [
        {
            'ID': 1,
            'Name': '槿呈Goidea',
            'URL': 'https://justgoidea.com/',
            'Intro': '读书｜新知｜生活禅',
            'Owner': '槿呈Goidea',
            'Icon': 'https://cos.justgoidea.com/justgoidea%2Fblog-logo.webp',
            'Email': 'me@hhzz.top',
        }, {
            'ID': 2,
            'Name': '欧雷流',
            'URL': 'https://ourai.ws/',
            'Intro': '我叫欧雷，是一个出生于上世纪 80 年代的理想主义叛逆青年。喜欢日本，热爱咖啡，善于总结。这里有我对技术和语言的研究，也有对世界和生活的思考。',
            'Owner': '欧雷',
            'Icon': 'https://ourai.ws/assets/avatars/ourai-100px-3bcaa1cb0c7fa0547d15622572d74a8bbc98a5f62e4920ecddb72ca95e505d17.jpg',
            'Email': ''
        }, {
            'ID': 3,
            'Name': '浪海导航',
            'URL': 'https://www.langhai.net/',
            'Intro': '收录各种类型的博客',
            'Owner': '浪海导航',
            'Icon': 'https://www.langhai.net/assets/images/langhai-logo.png',
            'Email': '676558206@qq.com'
        }, {
            'ID': 4,
            'Name': '非理勿试',
            'URL': 'https://www.ntiy.com/',
            'Intro': '“Never Try It Yourself”，记录、分享、学习',
            'Owner': 'Soulizer、欧阳桂花、谢让',
            'Icon': '/static/img/2024/ntiy_logo_o.png',
            'Email': 'collect@live.com',
        }, {
            'ID': 5,
            'Name': '印记',
            'URL': 'https://yinji.org/',
            'Intro': '君子可内敛不可懦弱，面不公可起而论之',
            'Owner': 'Bruce，Blogger/摄影爱好者/数码发烧友',
            'Icon': 'https://huhexian.s3.bitiful.net/2023/12/23/3b83cc067b2c3f1e45807dfdeb66e0c0.webp',
            'Email': 'huhexian0206@gmail.com',
        }, {
            'ID': 6,
            'Name': '松易涅的写作分享站',
            'URL': 'https://songyinie.com/',
            'Intro': '回顾历史，审视当下，期盼未来',
            'Owner': '松易涅',
            'Icon': 'https://logo.songyinie.com/logo.png',
            'Email': 'mail@songyinie.com',
        }
    ]
