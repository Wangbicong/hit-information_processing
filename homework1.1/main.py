# -*- coding:utf-8 -*-
import codecs
import re


def parse_record(expr, text):
    return expr.findall(text.decode('utf-8'))


def translate_to_csv(expr, fin, fout, titles):
    with codecs.open(fout, 'w', encoding='utf-8') as fout:
        with open(fin, 'r') as fin:
            fout.write(u','.join(titles) + '\n')
            for line in fin:
                result = parse_record(expr, line)
                for element in result:
                    fout.write(u','.join(element).strip(',') + '\n')


if __name__ == '__main__':

    expr_phone = re.compile(r'<tr>' + r'<td>(.*?)</td>' * 10 + r'</tr>')  # 通话详单
    expr_msg = re.compile(r'<tr>' + r'<td>(.*?)</td>' * 7 + r'</tr>')     # 短信详单

    translate_to_csv(expr_phone, 'phone.data', 'phone.csv',
                     [u'起始时间', u'通信地点', u'通信方式', u'对方号码', u'通信时长', u'通信类型',
                      u'执行套餐', u'实收通信费', u'网络类型'])
    translate_to_csv(expr_msg, 'msg.data', 'msg.csv',
                     [u'起始时间', u'对方号码', u'通信方式', u'业务类型', u'执行套餐', u'通信费'])