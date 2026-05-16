# %%
import pandas as pd
df =pd.read_csv('train.csv')
df.head(20)
# %%
df['Order Date']
# %%
df.shape
# %%
df.info()
# %%
df.isnull().sum()
# %%
df['Sales'].describe()
# %%
df['Sales'].sum()
# %%
df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
# %% [markdown]
# Technology 类别销售额最高,是核心收入来源.
# %%
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    dayfirst=True
)
# %%
df['Order Date'].head(10)
# %%
df['Month'] = df['Order Date'].dt.to_period('M')
# %%
df.groupby('Month')['Sales'].sum()
# %% [markdown]
# 保存月销售额
# %%
monthly_sales= df.groupby('Month')['Sales'].sum()
monthly_sales
# %% [markdown]
# 第二部分：可视化分析
# %%
import matplotlib.pyplot as plt
monthly_sales.plot(figsize=(12,6))

plt.title('Monthly Sales Trend')

plt.xlabel('Month')

plt.ylabel('Sales')

plt.show()
# %% [markdown]
# 销售趋势：月销售额整体呈增长趋势，部分月份出现明显销售高峰，说明业务存在季节性销售特征。
# %%
city_sales = (
    df.groupby('City')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
city_sales
# %%
city_sales.plot(
    kind='bar',
    figsize=(12,6)
)

plt.title('Top 10 Cities by Sales')

plt.xlabel('City')

plt.ylabel('Sales')

plt.show()
# %% [markdown]
# 城市分析： New YorK 和 Los Angeles贡献了大部分销售额。建议简历区域化运营策略。
# %%
category_sales = (
    df.groupby('Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

category_sales
# %% [markdown]
# 第三部分：发货效率分析
# %%
df['Ship Date'] = pd.to_datetime(
    df['Ship Date'],
    dayfirst=True
)
# %%
df['Shipping Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days
# %%
df['Shipping Days'].mean()
# %%
ship_mode_speed = (
    df.groupby('Ship Mode')['Shipping Days']
    .mean()
    .sort_values()
)

ship_mode_speed
# %%
ship_mode_speed.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title('Average Shipping Days by Ship Mode')

plt.xlabel('Ship Mode')

plt.ylabel('Average Days')

plt.show()
# %% [markdown]
# 第四部分：用户类型分析
# %%
segment_sales = (
    df.groupby('Segment')['Sales']
    .sum()
    .sort_values(ascending=False)
)

segment_sales
# %%
segment_avg = (
    df.groupby('Segment')['Sales']
    .mean()
    .sort_values(ascending=False)
)

segment_avg
# %% [markdown]
# Consumer 用户贡献最高销售额。
# Home office 用户平均订单金额更高。
# %% [markdown]
# 第五部分：top商品分析
# %%
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products
# %%
top_products.plot(
    kind='barh',
    figsize=(10,8)
)

plt.title('Top 10 Products by Sales')

plt.xlabel('Sales')

plt.ylabel('Product')

plt.show()
# %% [markdown]
# Canon imageCLASS 2200 Advanced Copier的销售额显著领先，说明存在“头部商品集中”现象
# %% [markdown]
# 
# %%
Restart