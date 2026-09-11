import streamlit as st
import pandas as pd

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор Ресурсов")
st.caption(" Мобильная версия")

# Создаем 4 вкладки для всех ваших рейтингов
tab1, tab2, tab3, tab4 = st.tabs([
    "✨ Обаяние", 
    "❤️ Близость", 
    "🏡 Процветание", 
    "⚔️ Таланты"
])

with tab1:
    st.header("Расчет минимального количества Обаяния")
    VAL_DUHI = 1
    VAL_SER_SHP = 2
    VAL_ZOL_SHP = 5
    VAL_HADAK = 10
    VAL_SIN_HADAK = 20
    
    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic = st.number_input("Количество наложниц:", min_value=0, value=0, help="<-Задания-Достижения-Монарх-романтик")
    duhi = st.number_input("Духи:", min_value=0, value=0, key="duhi")
    ser_shpilka = st.number_input("Серебряная шпилька:", min_value=0, value=0, key="ser_shp")
    zol_shpilka = st.number_input("Золотая шпилька:", min_value=0, value=0, key="zol_shp")
    hadak = st.number_input("Хадак:", min_value=0, value=0, key="hadak")
    sin_hadak = st.number_input("Синий Хадак:", min_value=0, value=0, key="sin_hadak")
    
    st.subheader("🎁 Сундуки и Фураж")
    red_sunduki = st.number_input("Красные сундуки (кол-во):", min_value=0, value=0, key="sunduki")
    ob_za_100_sun = st.number_input("Сколько обаяния дало 100 красных сундуков?:", min_value=0, value=0, key="sun_100", help="Посмотреть значения в рейтинге ДО, открыть 100 сундуков, посмотреть значение после, вписать разницу")
    furazh = st.number_input("Фураж (обаяние):", min_value=0, value=0, key="furazh_ob")
    
    st.subheader("💃 Наложницы для призыва")
    st.info("Впишите кол-во обаяния, если планируете призывать наложницу в рейтинг. Если не призываете — оставьте 0.")
    
    girls = [
        "Бадра", "Маша", "Байлина", "Медея", "Бастет", "Милана", "Ильза", "Ника", 
        "Ипполита", "Паулина", "Кармилла", "Родия", "Каталин", "Сигрид", "Киара", 
        "Тамара", "Кларисса", "Табити", "Корэна", "Ува", "Кунегурда", "Улана", 
        "Людмила", "Фазара", "Марика", "Фрейя", "Марико", "Юлия", 
        "Анар (Дочь вечности)", "Земея (Дочь вечности)", "Айрис (Дочь вечности)", 
        "Амар (Дочь вечности)", "Иветт (Дочь вечности)", "Вилма (Дочь вечности)"
    ]
    
    sum_girls_ob = 0
    col1, col2 = st.columns(2)
    for i, girl in enumerate(girls):
        with col1 if i % 2 == 0 else col2:
            val = st.number_input(f"{girl}:", min_value=0, value=0, key=f"ob_{girl}")
            sum_girls_ob += val

    avg_sunduk_val = (ob_za_100_sun / 100) if ob_za_100_sun > 0 else 0
    sunduki_total = red_sunduki * avg_sunduk_val

    total_ob = (
        (duhi * VAL_DUHI) + 
        (ser_shpilka * VAL_SER_SHP) + 
        (zol_shpilka * VAL_ZOL_SHP) + 
        (hadak * VAL_HADAK) + 
        (sin_hadak * VAL_SIN_HADAK) + 
        sunduki_total + 
        furazh + 
        sum_girls_ob
    )
    st.metric(label="✨ Итого минимальное количество обаяния:", value=f"{int(total_ob)}")

with tab2:
    st.header("Расчет минимального количества Близости")
    VAL_KOLCO = 1
    VAL_SERGI = 2
    VAL_SANDAL = 5
    VAL_NEFRIT = 10
    VAL_TAKYA = 20
    VAL_ORDOS = 50

    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic_bl = st.number_input("Количество наложниц (Близость):", min_value=0, value=0, key="nal_bl")
    kolca = st.number_input("Кольца:", min_value=0, value=0, key="kolca")
    sergi = st.number_input("Серьги:", min_value=0, value=0, key="sergi")
    sandal = st.number_input("Сандаловый браслет:", min_value=0, value=0, key="sandal")
    nefrit = st.number_input("Нефритовый браслет:", min_value=0, value=0, key="nefrit")
    takya = st.number_input("Такъя:", min_value=0, value=0, key="takya")
    ordos = st.number_input("Ордос:", min_value=0, value=0, key="ordos")
    
    st.subheader("🌾 Дополнительно")
    furazh_bl = st.number_input("Фураж (близость):", min_value=0, value=0, key="furazh_bl")
    
    total_bl = (
        (kolca * VAL_KOLCO) +
        (sergi * VAL_SERGI) +
        (sandal * VAL_SANDAL) +
        (nefrit * VAL_NEFRIT) +
        (takya * VAL_TAKYA) +
        (ordos * VAL_ORDOS) +
        furazh_bl
    )
    st.metric(label="❤️ Итого минимальное количество близости:", value=f"{int(total_bl)}")

with tab3:
    st.header("Расчет минимального количества Процветания")
    VAL_AGAT = 300
    VAL_KEDR = 100
    VAL_LENTY = 50

    st.subheader("📦 Ресурсы со склада")
    agat = st.number_input("Чёрный агат (300 очков):", min_value=0, value=0, key="agat")
    kedr = st.number_input("Зимний кедр (100 очков):", min_value=0, value=0, key="kedr")
    lenty = st.number_input("Цветные ленты (50 очков):", min_value=0, value=0, key="lenty")
    
    total_procvetanie = (agat * VAL_AGAT) + (kedr * VAL_KEDR) + (lenty * VAL_LENTY)
    st.metric(label="🏡 Итого количество процветания:", value=f"{total_procvetanie}")

with tab4:
    st.header("⚔️ Расчет Талантов")
    
    # --- БЛОК 1: МЕШКИ (Пакетами по 100) ---
    st.subheader("💰 1. Мешки талантов (вероятностные)")
    st.caption("Расчет активен при сливе мешков строго паками по 100 штук")
    
    POINTS_PER_100_GREY = 100
    POINTS_PER_100_GREEN = 100
    POINTS_PER_100_BLUE = 102
    POINTS_PER_100_PURPLE = 100
    POINTS_PER_100_ORANGE = 100
    POINTS_PER_100_RED = 102

    total_bags_pool = st.number_input("Введите общее количество мешков талантов:", min_value=0, value=0, step=50, key="pool_bags")
    
    full_hundreds = total_bags_pool // 100
    leftover_bags = total_bags_pool % 100

    if total_bags_pool > 0:
        st.info(f"Мешки разделены на: {full_hundreds} паков по 100 шт. Остаток: {leftover_bags} шт.")

    # Радио-кнопка для выбора, куда игрок хочет залить мешки
    target_talent = st.selectbox(
        "Куда планируете влить полные паки мешков?",
        ["Не вливать мешки", "В Серый талант (1★)", "В Зелёный талант (2★)", "В Синий талант (3★)", "В Фиолетовый талант (4★)", "В Оранжевый талант (5★)", "В Красный талант (6★)"]
    )
    
    # Считаем очки от мешков
    bags_points = 0
    if target_talent == "В Серый талант (1★)": bags_points = full_hundreds * POINTS_PER_100_GREY
    elif target_talent == "В Зелёный талант (2★)": bags_points = full_hundreds * POINTS_PER_100_GREEN
    elif target_talent == "В Синий талант (3★)": bags_points = full_hundreds * POINTS_PER_100_BLUE
    elif target_talent == "В Фиолетовый талант (4★)": bags_points = full_hundreds * POINTS_PER_100_PURPLE
    elif target_talent == "В Оранжевый талант (5★)": bags_points = full_hundreds * POINTS_PER_100_ORANGE
    elif target_talent == "В Красный талант (6★)": bags_points = full_hundreds * POINTS_PER_100_RED

    st.divider()

    # --- БЛОК 2: ЖЕТОНЫ (100% успех) ---
    st.subheader("🎟️ 2. Жетоны талантов (100% успех)")
    st.caption("Впишите количество поштучно под каждый тип таланта:")
    
    col_j1, col_j2 = st.columns(2)
    with col_j1:
        zh_grey = st.number_input("Жетоны в Серый (1★):", min_value=0, value=0, key="zh_grey")
        zh_blue = st.number_input("Жетоны в Синий (3★):", min_value=0, value=0, key="zh_blue")
        zh_orange = st.number_input("Жетоны в Оранжевый (5★):", min_value=0, value=0, key="zh_orange")
    with col_j2:
        zh_green = st.number_input("Жетоны в Зелёный (2★):", min_value=0, value=0, key="zh_green")
        zh_purple = st.number_input("Жетоны в Фиолетовый (4★):", min_value=0, value=0, key="zh_purple")
        zh_red = st.number_input("Жетоны в Красный (6★):", min_value=0, value=0, key="zh_red")

    # Считаем очки от жетонов (кол-во * количество звезд)
    tokens_points = (
        (zh_grey * 1) +
        (zh_green * 2) +
        (zh_blue * 3) +
        (zh_purple * 4) +
        (zh_orange * 5) +
        (zh_red * 6)
    )

    # --- ОБЩИЙ ИТОГ ПО ТАЛАНТАМ ---
    st.divider()
    total_all_talents = bags_points + tokens_points
    
    st.metric(label="⚔️ Всего гарантированных очков таланта:", value=f"{total_all_talents}")
    if leftover_bags > 0 and target_talent != "Не вливать мешки":
        st.caption(f"💡 Примечание: Еще {leftover_bags} мешков осталось вне расчета, так как они не собираются в полный пак по 100 шт.")
