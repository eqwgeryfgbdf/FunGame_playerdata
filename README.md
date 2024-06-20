# FunGame 玩家資料分析

## 目錄
- [簡介](#簡介)
- [專案結構](#專案結構)
- [檔案說明](#檔案說明)
- [安裝與使用](#安裝與使用)
- [使用字體](#使用字體)
- [注意事項](#注意事項)

## 簡介
這是一個用於分析 FunGame 遊戲玩家數據的專案。該專案包含數據分析腳本、玩家數據以及字體文件。本專案旨在提供對遊戲玩家行為和數據的深入分析，從而幫助改善遊戲體驗。

## 專案結構

```
FunGame_playerdata/
├── font/
│   └── chinese.simhei.ttf
├── img/
│   └── Counter-StrikeSource_Homepage_icon.webp
├── all_player_data.csv
├── all_player_data.csv 應該是程式執行後的產物，如果爬蟲程式無法正常抓取，才會需要
├── chromedriver.exe
├── FunGame_playerdata.py
├── LICENSE.chromedriver
├── Python期末考影片封面.png
├── README.md
└── streamlit_app.py
```

## 檔案說明
- `FunGame_playerdata.py`：使用 Selenium 抓取玩家數據的腳本，將數據存儲在 CSV 檔案中。
- `streamlit_app.py`：使用 Streamlit 來建立的網頁應用程式，用於可視化和分析玩家數據。
- `font/`：包含專案中使用的字體檔案。
  - `chinese.simhei.ttf`：中文字體檔案。
- `img/`：包含專案中使用的圖像檔案。
  - `Counter-StrikeSource_Homepage_icon.webp`：WebP 格式的圖像檔案。
- `all_player_data.csv`：玩家數據的 CSV 檔案，包含玩家的詳細數據。
- `chromedriver.exe`：用於網頁抓取的 ChromeDriver 可執行檔案。
- `LICENSE.chromedriver`：ChromeDriver 的授權檔案。
- `Python期末考影片封面.png`：期末考影片的封面圖像。
- `README.md`：本自述檔案。

## 安裝與使用

### 環境要求
- Python 3.x
- pandas 庫
- matplotlib 庫
- selenium 庫
- streamlit 庫

### 安裝步驟
1. 克隆或下載此專案到本地：
    ```bash
    git clone https://your-repo-url.git
    cd your-repo-directory
    ```

2. 安裝所需的 Python 庫：
    ```bash
    pip install pandas matplotlib selenium streamlit
    ```

3. 下載並將 `chromedriver.exe` 放置在專案目錄中。

### 使用方法

#### 抓取玩家數據
1. 執行抓取數據的腳本：
    ```bash
    python FunGame_playerdata.py
    ```

#### 可視化玩家數據
1. 啟動 Streamlit 應用程式：
    ```bash
    streamlit run streamlit_app.py
    ```

2. 打開瀏覽器並進入 `http://localhost:8501` 查看應用程式。

## 使用字體
本專案中使用了 SimHei 字體來生成包含中文字符的圖表。字體文件已包含在項目中，並且來源於 sharefonts.net。

## 注意事項
- `all_player_data.csv` 文件中包含了大量的玩家數據，請確保在使用該數據時遵守相關的隱私政策和數據保護規定。
- 在生成圖表時，如果遇到字體顯示問題，請確保已安裝 SimHei 字體並在腳本中正確引用。

