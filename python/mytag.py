#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mytag.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-01 18:14:57
# @Last Modified: 2018-10-01 18:14:57
#

def tag(name, *content, cls=None, **args):
  if cls:
    args['class'] = cls
  else:
    pass

  attribute_str = ''.join([' %s=%r' % (k,v)for k,v in args.items()])
  if content:
    return '\n'.join('<%s%s>%s</%s>' % (name, attribute_str, v, name) for v in content)
  else:
    return '<%s%s />' % (name, attribute_str)

assert tag('br') == '<br />'
assert tag('p', 'hello') == '<p>hello</p>'
assert tag('p', 'hello', 'world') == '<p>hello</p>\n<p>world</p>'
assert tag('p', 'hello', id = 33) == "<p id=33>hello</p>"

assert tag('p', 'hello', 'world', cls='sidbar') == "<p class='sidbar'>hello</p>\n<p class='sidbar'>world</p>"
assert tag(content = 'testing', name = 'img') == "<img content='testing' />"
mytag = dict(name='img',title='Sunset Bufe', src='sum.jpg', cls = 'frame')
print(mytag)
print(tag(**mytag))

print('函数的特有方法')
class C:pass
c = C()
print(set(dir(tag)) - set(dir(c)))


print(tag.__defaults__)
