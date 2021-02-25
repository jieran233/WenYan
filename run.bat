:: 该批处理脚本用于在Windows平台的服务器上运行闻言并输出日志到run.log
:: 请使用任务计划程序定期运行本批处理脚本
echo [%date% %time%] >> run.log
python main.py >> run.log
echo. >> run.log