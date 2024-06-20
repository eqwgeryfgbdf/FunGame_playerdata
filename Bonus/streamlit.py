import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image
from io import BytesIO
import base64

# 讀取 CSV 檔案，考慮到中文編碼問題
df = pd.read_csv('all_player_data.csv', encoding='utf-8')

# 設置中文字體
font_path = 'font/chinese.simHei.ttf'  # 替換成實際字體路徑，注意使用正斜杠或雙反斜杠
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [font_prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False  # 解決座標軸負號顯示問題

# 加載圖片並轉換為 base64 編碼
image = Image.open('img/Counter-StrikeSource_Homepage_icon.webp')
buffered = BytesIO()
image.save(buffered, format="WEBP")
img_str = base64.b64encode(buffered.getvalue()).decode()

# 定義圓形圖片的 CSS 樣式
circle_image_style = f"""
<style>
    .circle-image {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 500px;
        height: 500px;
    }}
</style>
"""

# 在應用程式中顯示圓形圖片
st.markdown(circle_image_style, unsafe_allow_html=True)
st.markdown(f'<img src="data:image/webp;base64,{img_str}" class="circle-image">', unsafe_allow_html=True)

# Streamlit 應用程式標題
st.title('玩家數據分析')

# 選擇要顯示的數值標題
columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
if len(columns) < 2:
    st.error("數據中需要至少有兩個數值型欄位進行分析")
else:
    # 創建並排顯示的列
    col1, col2, col3 = st.columns(3)

    with col1:
        x_axis = st.selectbox('選擇X軸的數值標題', columns, key='x_axis')

    with col2:
        # 避免 x_axis 與 y_axis 相同
        y_axis_options = [col for col in columns if col != x_axis]
        y_axis = st.selectbox('選擇Y軸的數值標題', y_axis_options, key='y_axis')

    with col3:
        # 玩家選擇
        players = df['Name'].unique()
        selected_player = st.selectbox('選擇玩家', players)

    # 繪製分佈圖
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis], label='所有玩家')

        # 標記選中的玩家
        selected_player_data = df[df['Name'] == selected_player]
        ax.scatter(selected_player_data[x_axis], selected_player_data[y_axis], color='yellow', s=100,
                   label=selected_player, edgecolors='black')

        # 添加標籤
        for i, row in selected_player_data.iterrows():
            ax.annotate(row['Name'], (row[x_axis], row[y_axis]), textcoords="offset points", xytext=(0, 10),
                        ha='center', fontsize=8, color='black', backgroundcolor='yellow', fontproperties=font_prop)

        ax.set_xlabel(x_axis, fontproperties=font_prop)
        ax.set_ylabel(y_axis, fontproperties=font_prop)
        ax.set_title(f'{x_axis} vs {y_axis}', fontproperties=font_prop)
        ax.legend(prop=font_prop)
        st.pyplot(fig)

    # 顯示數據表
    st.write("數據表格")
    st.dataframe(df[[x_axis, y_axis]].head())

    # 顯示統計數據
    if st.checkbox('顯示統計數據'):
        st.write(df[[x_axis, y_axis]].describe())

# 顯示國家分佈
st.title('國家分佈')
country_counts = df['Country'].value_counts().sort_values(ascending=True)  # 由小到大排序

# 使用 matplotlib 繪製橫向條形圖
fig, ax = plt.subplots()
country_counts.plot(kind='barh', ax=ax)
ax.set_xlabel('玩家數量', fontproperties=font_prop)
ax.set_ylabel('國家', fontproperties=font_prop)
ax.set_title('國家分佈', fontproperties=font_prop)
st.pyplot(fig)

# 顯示主要國家或地區的玩家統計
st.title('主要國家或地區的玩家統計')
top_n = st.slider('選擇顯示前N個國家或地區', 1, len(country_counts), 10)
top_countries = country_counts.tail(top_n)  # 由小到大排序後取最後N個

# 繪製前N個國家的橫向條形圖
fig, ax = plt.subplots()
top_countries.plot(kind='barh', ax=ax)
ax.set_xlabel('玩家數量', fontproperties=font_prop)
ax.set_ylabel('國家', fontproperties=font_prop)
ax.set_title('主要國家或地區的玩家統計', fontproperties=font_prop)
st.pyplot(fig)
st.write(top_countries)
