import streamlit as st
import random

st.title('欢迎来到“今天吃什么”程序！')

# 菜单选项
st.write('请选择您要吃的类型')
st.write('1.一荤 2.两荤 3.三荤 4.一素 5.两素 6.三素')
st.write('组合：7.一荤一素 8.一荤两素 9.一荤三素')
st.write('10.两荤一素 11.两荤两素 12.两荤三素')
st.write('13.三荤一素 14.三荤两素 15.三荤三素')

# 初始化变量
lst1 = ['炒青菜', "麻婆豆腐", "清炒西兰花", "蒜蓉空心菜", "红烧茄子", "香菇炒青菜", "鱼香茄子", "清炒豆芽", "凉拌黄瓜", "干煸四季豆", "番茄炒蛋", "凉拌木耳", "地三鲜", "麻辣土豆丝", "红烧冬瓜", "腐竹烧冬瓜", "凉拌海带丝", "菠菜豆腐汤", "香椿炒鸡蛋", "凉拌金针菇", "南瓜粥", "素炒三丝", "家常豆腐", "白灼芥兰", "凉拌菠菜", "麻辣凉粉", "芹菜炒香干", "凉拌海带结", "蒜蓉油麦菜", "菜心炒香菇"]
lst2 = ["红烧肉", "宫保鸡丁", "鱼香肉丝", "麻辣香锅", "糖醋排骨", "辣子鸡丁", "水煮鱼", "清蒸鲈鱼", "香酥鸭", "孜然羊肉", "回锅肉", "烤鸭", "酱牛肉", "红烧鱼", "东坡肉", "香辣蟹", "盐焗鸡", "叉烧肉", "椒盐虾", "黄焖鸡", "溜肉段", "干锅牛蛙", "红烧狮子头", "黄焖排骨", "蒜香排骨", "炖牛肉", "猪蹄炖花生", "干煸肥肠", "酸菜鱼", "毛血旺"]
# 价格变量
# 10元左右荤菜,素菜
lst3 = ["肉末茄子", "土豆炖牛肉", "豆腐烧肉", "蒜苔炒肉", "青椒肉丝", "香干炒肉", "鱼香肉丝", "木耳炒肉片", "土豆烧排骨",  "小炒牛肉", "辣子鸡丁", "香菇炖鸡", "青椒炒鸡蛋","黄瓜炒肉片", "红烧鸡块", "豆角炖肉", "西葫芦炒肉片", "芹菜炒肉丝", "韭菜炒蛋", "酸辣土豆丝", "洋葱炒肉片", "黄豆炖猪蹄", "冬瓜烧排骨", "胡萝卜炖牛肉", "香菇炒鸡片", "西红柿牛腩"]
lst4 = ["炒青菜", "凉拌黄瓜", "清炒西兰花", "蒜蓉空心菜", "红烧茄子", "清炒豆芽", "凉拌木耳", "麻婆豆腐", "清炒油麦菜", "凉拌菠菜", "凉拌海带丝", "香菇炒青菜", "番茄炒蛋","蒜蓉油麦菜", "地三鲜", "豆腐皮炒青椒", "干煸四季豆", "凉拌豆皮", "香椿炒鸡蛋", "凉拌金针菇", "清炒南瓜", "香菇炒豆腐", "白灼芥兰", "凉拌茄子", "蒜香豇豆", "炒菠菜", "炝拌土豆丝", "红烧冬瓜", "清炒苦瓜", "豆腐脑"]
# 25元左右荤菜，素菜
lst5 = ["红烧肉", "宫保鸡丁", "鱼香肉丝", "麻辣香锅", "糖醋排骨", "辣子鸡丁", "水煮鱼", "清蒸鲈鱼", "香酥鸭", "孜然羊肉", "回锅肉", "烤鸭", "酱牛肉", "红烧鱼", "东坡肉","香辣蟹", "盐焗鸡", "叉烧肉", "椒盐虾", "黄焖鸡", "溜肉段", "干锅牛蛙", "红烧狮子头", "黄焖排骨", "蒜香排骨", "炖牛肉", "猪蹄炖花生", "干煸肥肠", "酸菜鱼", "毛血旺"]
lst6 = ["鱼香茄子", "蒜蓉空心菜", "红烧茄子", "香菇炒青菜", "凉拌黄瓜", "干煸四季豆", "凉拌木耳", "地三鲜", "麻辣土豆丝", "红烧冬瓜", "腐竹烧冬瓜", "菠菜豆腐汤", "香椿炒鸡蛋", "凉拌金针菇", "南瓜粥", "素炒三丝", "家常豆腐", "白灼芥兰", "凉拌菠菜", "麻辣凉粉", "芹菜炒香干", "凉拌海带结", "蒜蓉油麦菜", "菜心炒香菇"]
# 50元左右及以上价格荤菜，素菜
lst7 = ["龙井虾仁", "佛跳墙", "清蒸大闸蟹", "香煎鲍鱼", "蒜蓉蒸龙虾", "红烧甲鱼", "清蒸石斑鱼", "鹅肝酱配牛排", "金牌烧鹅", "蚝油鲍片", "酱焖鲍鱼", "海参炖鸡", "鲍汁扣鹅掌", "烤全羊", "生蚝烤牛排", "黑椒牛柳", "蜜汁叉烧", "冬阴功汤", "蒜香小龙虾", "芙蓉蟹", "红酒焖牛尾", "清蒸鲈鱼", "黄焖大虾", "干煎带鱼", "盐焗海螺", "烤乳猪", "香煎银鳕鱼", "日式照烧鸡", "咖喱大虾", "烤羊排", "炭烧肥牛", "姜葱龙虾", "水晶蹄筋", "粤式烧乳鸽", "酱爆鱿鱼", "风味烤鱼", "铁板黑椒牛肉", "海鲜蒸锅", "法式煎鹅肝"]
lst8 = ["松露炒饭", "金银蒜蒸丝瓜", "鲍汁花菇", "龙井芙蓉豆腐", "鲜菇扒菜心", "百花酿豆腐", "红烧狮子头（素）", "上素小炒皇", "秘制豆腐皮", "荷香糯米素鸡", "松茸炖豆腐", "鲜百合炒芦笋", "山珍炖猴头菇", "金瓜盅", "竹荪豆腐羹", "杏鲍菇炒甜豆", "凉拌珍珠菌", "翡翠豆腐", "金汤鲜蔬", "椰香南瓜盅", "葱油素鲍鱼", "脆皮豆腐", "芝士焗蘑菇", "松茸烧南瓜", "红烧豆腐脑", "蚝皇扒生菜", "鲍汁冬瓜条", "野菌煲", "羊肚菌扒翡翠", "酥炸金针菇", "红烧榆耳", "秘制罗汉斋", "上汤娃娃菜", "姜汁白玉菇", "素蟹粉豆腐", "辣炒鲜菌", "素烧狮子头", "京酱素肉丝", "秘制松茸羹", "红烧莲藕"]

# 模式选择
mode = st.radio(
    "选择您的用餐模式",
    ("普通模式", "经济模式", "丰盛模式")
)

# 根据模式选择显示内容
if mode == "普通模式":
    st.write("请选择您要吃的类型：")
    st.write("1. 一荤 2. 两荤 3. 三荤 4. 一素 5. 两素 6. 三素")
    st.write("组合：7. 一荤一素 8. 一荤两素 9. 一荤三素")
    st.write("10. 两荤一素 11. 两荤两素 12. 两荤三素")
    st.write("13. 三荤一素 14. 三荤两素 15. 三荤三素")
    menu_type = st.number_input("输入菜单类型编号", min_value=1, max_value=15, step=1)

    if st.button('生成菜单'):
        if menu_type == 1:
            st.write(random.choice(lst2))
        elif menu_type == 2:
            st.write(random.choice(lst2) + " " + random.choice(lst2))
        elif menu_type == 3:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst2))
        elif menu_type == 4:
            st.write(random.choice(lst1))
        elif menu_type == 5:
            st.write(random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 6:
            st.write(random.choice(lst1) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 7:
            st.write(random.choice(lst2) + " " + random.choice(lst1))
        elif menu_type == 8:
            st.write(random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 9:
            st.write(random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 10:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1))
        elif menu_type == 11:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 12:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 13:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1))
        elif menu_type == 14:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1))
        elif menu_type == 15:
            st.write(random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst2) + " " + random.choice(lst1) + " " + random.choice(lst1) + " " + random.choice(lst1))

elif mode == "经济模式":
    st.write("请选择您要吃的类型：")
    st.write("1. 一荤 2. 两荤 3. 三荤 4. 一素 5. 两素 6. 三素")
    st.write("组合：7. 一荤一素 8. 一荤两素 9. 一荤三素")
    st.write("10. 两荤一素 11. 两荤两素 12. 两荤三素")
    st.write("13. 三荤一素 14. 三荤两素 15. 三荤三素")
    menu_type = st.number_input("输入菜单类型编号", min_value=1, max_value=15, step=1)

    if st.button('生成菜单'):
        if menu_type == 1:
            st.write(random.choice(lst3))
        elif menu_type == 2:
            st.write(random.choice(lst3) + " " + random.choice(lst3))
        elif menu_type == 3:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst3))
        elif menu_type == 4:
            st.write(random.choice(lst4))
        elif menu_type == 5:
            st.write(random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 6:
            st.write(random.choice(lst4) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 7:
            st.write(random.choice(lst3) + " " + random.choice(lst4))
        elif menu_type == 8:
            st.write(random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 9:
            st.write(random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 10:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4))
        elif menu_type == 11:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 12:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 13:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4))
        elif menu_type == 14:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4))
        elif menu_type == 15:
            st.write(random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst3) + " " + random.choice(lst4) + " " + random.choice(lst4) + " " + random.choice(lst4))

elif mode == "丰盛模式":
    st.write("请选择您要吃的类型：")
    st.write("1. 一荤 2. 两荤 3. 三荤 4. 一素 5. 两素 6. 三素")
    st.write("组合：7. 一荤一素 8. 一荤两素 9. 一荤三素")
    st.write("10. 两荤一素 11. 两荤两素 12. 两荤三素")
    st.write("13. 三荤一素 14. 三荤两素 15. 三荤三素")
    menu_type = st.number_input("输入菜单类型编号", min_value=1, max_value=15, step=1)

    if st.button('生成菜单'):
        if menu_type == 1:
            st.write(random.choice(lst5))
        elif menu_type == 2:
            st.write(random.choice(lst5) + " " + random.choice(lst5))
        elif menu_type == 3:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst5))
        elif menu_type == 4:
            st.write(random.choice(lst6))
        elif menu_type == 5:
            st.write(random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 6:
            st.write(random.choice(lst6) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 7:
            st.write(random.choice(lst5) + " " + random.choice(lst6))
        elif menu_type == 8:
            st.write(random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 9:
            st.write(random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 10:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6))
        elif menu_type == 11:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 12:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 13:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6))
        elif menu_type == 14:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6))
        elif menu_type == 15:
            st.write(random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst5) + " " + random.choice(lst6) + " " + random.choice(lst6) + " " + random.choice(lst6))
