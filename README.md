
简介
-----------
这个模块是将Perl中著名的 Template Toolkit (TT) 模块用 python 实现一遍

更多信息请参考：
  http://template-toolkit.org/


文档
-------------

使用示范：

```python
from template import Template
from template.util import TemplateException
TEMPLATE_TEXT = "Hello [% thing %]!"
t = Template()
try:
    print t.processString(TEMPLATE_TEXT, { "thing": "world" })
except TemplateException, e:
    print "ERROR: %s" % e
```

语法
-------

IF / UNLESS / ELSIF / ELSE:
```
[% IF frames %]
   [% INCLUDE frameset %]
[% END %]

[% UNLESS text_mode %]
   [% INCLUDE biglogo %]
[% END %]

```
在上述流程控制中，这些 “== != < <= > >= && || ! and or not” 逻辑表达式都是可以使用的


FOREACH：
```
[% foo   = 'Foo'
   items = [ 'one', 'two', 'three' ]
%]

Things:
[% FOREACH thing IN [ foo 'Bar' "$foo Baz" ] %]
   * [% thing %]
[% END %]

Items:
[% FOREACH i IN items %]
   * [% i %]
[% END %]

Stuff:
[% stuff = [ foo "$foo Bar" ] %]
[% FOREACH s IN stuff %]
   * [% s %]
[% END %]
```
输出：

```
Things:
  * Foo
  * Bar
  * Foo Baz

Items:
  * one
  * two
  * three

Stuff:
  * Foo
  * Foo Bar
```

当然 Template tookit所支持的控制语法远不止这些，更多控制语法请参考：
  http://template-toolkit.org/docs/manual/Directives.html

安装
---------------
sudo python setup.py install


