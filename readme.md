# 聊天室1.0

## 环境说明

核心：树莓派4B Kali Linux PHP8.1.2

客户端：Windows Python310

## 注意

如果需要在Linux使用，请将main.py的56行的cls更改为clear

本次没有增加编解码，请合法使用，请自行添加方法

## 公开

本程序公开于微信公众号 末心的小圈圈

## 启动服务
参考文章：https://mp.weixin.qq.com/s?__biz=MzI5NzIwNTAyMQ==&mid=2247489186&idx=1&sn=9bea9b4d92eb6bbca16480aaa805e5e7&chksm=ecb9fad0dbce73c6e17f4bfeed7cd163b0840ee00b3afa262d77587532771fcf79aab753b96c&token=1327896414&lang=zh_CN#rd

执行 php -S 0.0.0.0:8880 -t ~/tools/web_pages/chat_room
-t后面的参数记得修改成clone后的路径，访问当前服务器IP的0.0.0.0:8000
并将main.py的url修改于此
亦可使用其他服务来开启http和php服务，如宝塔、lnmp等，如果能启用https则更好
