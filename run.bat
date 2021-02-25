:: 该批处理脚本用于在Windows平台的服务器上运行闻言并输出日志到run.log
:: 请使用任务计划程序定期运行本批处理脚本
:: 请把相对路径替换为绝对路径，以确保任务计划能够万无一失顺利执行
echo [%date% %time%] >> run.log && python main.py >> run.log