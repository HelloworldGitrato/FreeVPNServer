"""
このやり方は非常に危険です、やる場合は自己責任でお願いします
また、変更ごとにWi-FIが切れる可能性があります
"""

#↓Windows edition↓
import subprocess
import time

def change_ip():
    try:
        # IPアドレスを再取得します
        subprocess.run(["ipconfig", "/release"], check=True)
        subprocess.run(["ipconfig", "/renew"], check=True)
        print("IPアドレスを変更しました。")
      
    except Exception as e:
        print("IPアドレスの変更中にエラーが発生しました:", e)

# 一分ごとにIPアドレスを変更します
while True:
    change_ip()
    time.sleep(60) 



#Linux edition↓

import subprocess
import time

def change_ip():
    try:
        # IPアドレスを変更するコマンドを実行。
        # 以下はLinuxのみ実行可能です、ほかのプラットフォームでは使用できません。
        subprocess.run(["sudo", "service", "network-manager", "restart"], check=True)

        print("IPアドレスを変更しました。")

    except Exception as e:
        print("IPアドレスの変更中にエラーが発生しました:", e)

# 一分ごとにIPアドレスを変更します。
while True:
    change_ip()
    time.sleep(60) 
