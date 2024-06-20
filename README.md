FunGame Data Analysis
目錄
簡介
檔案說明
安裝與使用
使用字體
注意事項
簡介
這是一個用於分析FunGame遊戲玩家數據的專案。該專案包含數據分析腳本、玩家數據以及字體文件。本專案旨在提供對遊戲玩家行為和數據的深入分析，從而幫助改善遊戲體驗。

檔案說明
app.py: 主要的數據分析腳本，負責讀取玩家數據並生成報告。
FunGame_playerdata.py: 玩家數據的處理腳本，包含數據清洗和格式化的函數。
chinese.simhei.ttf 和 SimHei.ttf: 字體文件，用於生成包含中文的圖表和報告。
sharefonts.net.txt: 字體來源資訊文件。
all_player_data.csv: 玩家數據的CSV文件，包含玩家的詳細數據。
安裝與使用
環境要求

Python 3.x
pandas 庫
matplotlib 庫
安裝步驟

克隆或下載此專案到本地：
bash
複製程式碼
git clone https://your-repo-url.git
cd your-repo-directory
安裝所需的Python庫：
bash
複製程式碼
pip install pandas matplotlib
使用方法

執行主腳本進行數據分析：
bash
複製程式碼
python app.py
使用字體
本專案中使用了SimHei字體來生成包含中文字符的圖表。字體文件已包含在項目中，並且來源於sharefonts.net​​。

注意事項
all_player_data.csv 文件中包含了大量的玩家數據，請確保在使用該數據時遵守相關的隱私政策和數據保護規定。
在生成圖表時，如果遇到字體顯示問題，請確保已安裝SimHei字體並在腳本中正確引用。
