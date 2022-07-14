<?php
# POST传参数据的方式传入用户名、聊天内容和鉴权因子
# 请求头内容中传入一个自定义值，来进行鉴权
# 鉴权因子判断
$name = $_POST["a"];
$text = $_POST["b"];
$check =$_COOKIE["check"];
date_default_timezone_set("PRC");
$date = date("Y-m-d D h:i:s A");
$texts = $name.":".$text." \n|IP:".$check."|Date:".$date."|\n\n";
print($texts);
# 下面是写文件的方式
$data_file = fopen("data.cht","a+");
fwrite($data_file, $texts);