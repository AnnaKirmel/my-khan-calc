import streamlit as st
import pandas as pd

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор Ресурсов")
st.caption("Мобильная версия")


tab1, tab2, tab3, tab4 = st.tabs([
    "✨ Обаяние", 
    "❤️ Близость", 
    "🏡 Процветание", 
    "⚔️ Таланты и Прокачка"
])

# --- ВКЛАДКА 1: ОБАЯНИЕ ---
with tab1:
    st.header("Расчет минимального количества Обаяния")
    VAL_DUHI, VAL_SER_SHP, VAL_ZOL_SHP, VAL_HADAK, VAL_SIN_HADAK = 1, 2, 5, 10, 20
    
    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic = st.number_input("Количество наложниц:", min_value=0, value=0)
    duhi = st.number_input("Духи:", min_value=0, value=0, key="duhi")
    ser_shpilka = st.number_input("Серебряная шпилька:", min_value=0, value=0, key="ser_shp")
    zol_shpilka = st.number_input("Золотая шпилька:", min_value=0, value=0, key="zol_shp")
    hadak = st.number_input("Хадак:", min_value=0, value=0, key="hadak")
    sin_hadak = st.number_input("Синий Хадак:", min_value=0, value=0, key="sin_hadak")
    
    st.subheader("🎁 Сундуки и Фураж")
    red_sunduki = st.number_input("Красные сундуки (кол-во):", min_value=0, value=0, key="sunduki")
    ob_za_100_sun = st.number_input("Сколько обаяния дало 100 красных сундуков?:", min_value=0, value=0, key="sun_100")
    furazh = st.number_input("Фураж (обаяние):", min_value=0, value=0, key="furazh_ob")
    
    st.subheader("💃 Наложницы для призыва")
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
    total_ob = (duhi*VAL_DUHI) + (ser_shpilka*VAL_SER_SHP) + (zol_shpilka*VAL_ZOL_SHP) + (hadak*VAL_HADAK) + (sin_hadak*VAL_SIN_HADAK) + (red_sunduki*avg_sunduk_val) + furazh + sum_girls_ob
    st.metric(label="✨ Итого минимальное количество обаяния:", value=f"{int(total_ob)}")

# --- ВКЛАДКА 2: БЛИЗОСТЬ ---
with tab2:
    st.header("Расчет минимального количества Близости")
    VAL_KOLCO, VAL_SERGI, VAL_SANDAL, VAL_NEFRIT, VAL_TAKYA, VAL_ORDOS = 1, 2, 5, 10, 20, 50
    kolca = st.number_input("Кольца:", min_value=0, value=0, key="kolca")
    sergi = st.number_input("Серьги:", min_value=0, value=0, key="sergi")
    sandal = st.number_input("Сандаловый браслет:", min_value=0, value=0, key="sandal")
    nefrit = st.number_input("Нефритовый браслет:", min_value=0, value=0, key="nefrit")
    takya = st.number_input("Такъя:", min_value=0, value=0, key="takya")
    ordos = st.number_input("Ордос:", min_value=0, value=0, key="ordos")
    furazh_bl = st.number_input("Фураж (близость):", min_value=0, value=0, key="furazh_bl")
    total_bl = (kolca*VAL_KOLCO) + (sergi*VAL_SERGI) + (sandal*VAL_SANDAL) + (nefrit*VAL_NEFRIT) + (takya*VAL_TAKYA) + (ordos*VAL_ORDOS) + furazh_bl
    st.metric(label="❤️ Итого минимальное количество близости:", value=f"{int(total_bl)}")

# --- ВКЛАДКА 3: ПРОЦВЕТАНИЕ ---
with tab3:
    st.header("Расчет минимального количества Процветания")
    agat = st.number_input("Чёрный агат (300 очков):", min_value=0, value=0, key="agat")
    kedr = st.number_input("Зимний кeдр (100 очков):", min_value=0, value=0, key="kedr")
    lenty = st.number_input("Цветные ленты (50 очков):", min_value=0, value=0, key="lenty")
    total_procvetanie = (agat * 300) + (kedr * 100) + (lenty * 50)
    st.metric(label="🏡 Итого количество процветания:", value=f"{total_procvetanie}")

# --- ВКЛАДКА 4: ТАЛАНТЫ (ПОЛНАЯ СБОРКА) ---
with tab4:
    st.header("⚔️ Распределитель Опыта и Талантов")
    
    # --- БЛОК 1: МЕШКИ (Пакетами по 100) ---
    st.subheader("💰 1. Мешки талантов (вероятностные)")
    total_bags_pool = st.number_input("Количество мешков талантов на складе:", min_value=0, value=0, step=100, key="pool_bags")
    target_talent = st.selectbox(
        "Куда сливаем паки мешков?",
        ["Не вливать мешки", "В Серый (1★)", "В Зелёный (2★)", "В Синий (3★)", "В Фиолетовый (4★)", "В Оранжевый (5★)", "В Красный (6★)"]
    )
    
    bags_points = 0
    full_hundreds = total_bags_pool // 100
    leftover_bags = total_bags_pool % 100
    
    if total_bags_pool > 0:
        st.info(f"Мешки разделены на: {full_hundreds} паков по 100 шт. Остаток: {leftover_bags} шт.")

    if target_talent == "В Серый (1★)": bags_points = full_hundreds * 100
    elif target_talent == "В Зелёный (2★)": bags_points = full_hundreds * 100
    elif target_talent == "В Синий (3★)": bags_points = full_hundreds * 102
    elif target_talent == "В Фиолетовый (4★)": bags_points = full_hundreds * 100
    elif target_talent == "В Оранжевый (5★)": bags_points = full_hundreds * 100
    elif target_talent == "В Красный (6★)": bags_points = full_hundreds * 102

    st.divider()

    # --- БЛОК 2: ЖЕТОНЫ (100% успех, прокачка по звездам) ---
    st.subheader("🎟️ 2. Жетоны талантов (100% успех)")
    st.caption("Впишите количество ваших жетонов поштучно:")
    
    col_j1, col_j2 = st.columns(2)
    with col_j1:
        zh_grey = st.number_input("Жетоны в Серый (1★ — 200 очков):", min_value=0, value=0, key="zh_grey")
        zh_blue = st.number_input("Жетоны в Синий (3★ — 600 очков):", min_value=0, value=0, key="zh_blue")
        zh_orange = st.number_input("Жетоны в Оранжевый (5★ — 1000 очков):", min_value=0, value=0, key="zh_orange")
    with col_j2:
        zh_green = st.number_input("Жетоны в Зелёный (2★ — 400 очков):", min_value=0, value=0, key="zh_green")
        zh_purple = st.number_input("Жетоны в Фиолетовый (4★ — 800 очков):", min_value=0, value=0, key="zh_purple")
        zh_red = st.number_input("Жетоны в Красный (6★ — 1200 очков):", min_value=0, value=0, key="zh_red")

    tokens_points = (
        (zh_grey * 200) +
        (zh_green * 400) +
        (zh_blue * 600) +
        (zh_purple * 800) +
        (zh_orange * 1000) +
        (zh_red * 1200)
    )

    st.divider()

    # --- БЛОК 3: ИНТЕРАКТИВНЫЕ СВИТКИ ОПЫТА ---
    st.subheader("📜 3. Распределение Свитков Опыта")
    
    if "spent_points" not in st.session_state:
        st.session_state.spent_points = 0
    if "earned_rating" not in st.session_state:
        st.session_state.earned_rating = 0

    input_svitki = st.number_input("Количество ваших свитков опыта советника (1 шт = 50 оп):", min_value=0, value=0, step=1)
    total_experience_pool = input_svitki * 50
    current_balance = total_experience_pool - st.session_state.spent_points

    if current_balance < 0:
        st.session_state.spent_points = 0
        st.session_state.earned_rating = 0
        current_balance = total_experience_pool

    st.info(f"💡 Всего опыта от свитков: {total_experience_pool} | ОСТАТОК БАЛАНСА: {current_balance} очков")
    st.write("Нажмите кнопку, чтобы потратить накопленный опыт и прокачать звезду:")
    
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        if st.button("🌟 Закрыть Серую (1★) [-200 оп.]"):
            if current_balance >= 200:
                st.session_state.spent_points += 200
                st.session_state.earned_rating += 200
                st.rerun()
            else: st.error("Недостаточно опыта!")
        if st.button("🌟 Закрыть Фиолет (4★) [-800 оп.]"):
            if current_balance >= 800:
                st.session_state.spent_points += 800
                st.session_state.earned_rating += 800
                st.rerun()
            else: st.error("Недостаточно опыта!")
    with col_b2:
        if st.button("🌟 Закрыть Зеленую (2★) [-400 оп.]"):
            if current_balance >= 400:
                st.session_state.spent_points += 400
                st.session_state.earned_rating += 400
                st.rerun()
            else: st.error("Недостаточно опыта!")
        if st.button("🌟 Закрыть Оранж (5★) [-1000 оп.]"):
            if current_balance >= 1000:
                st.session_state.spent_points += 1000
                st.session_state.earned_rating += 1000
                st.rerun()
            else: st.error("Недостаточно опыта!")
    with col_b3:
        if st.button("🌟 Закрыть Синюю (3★) [-600 оп.]"):
            if current_balance >= 600:
                st.session_state.spent_points += 600
                st.session_state.earned_rating += 600
                st.rerun()
            else: st.error("Недостаточно опыта!")
        if st.button("🌟 Закрыть Красную (6★) [-1200 оп.]"):
            if current_balance >= 1200:
                st.session_state.spent_points += 1200
                st.session_state.earned_rating += 1200
                st.rerun()
            else: st.error("Недостаточно опыта!")

    if st.button("🔄 Сбросить распределение опыта свитков"):
        st.session_state.spent_points = 0
        st.session_state.earned_rating = 0
        st.rerun()

    st.divider()

    # --- ИТОГОВЫЙ БЛОК РЕЙТИНГА ТАЛАНТОВ ---
    st.subheader("📊 Итог по рейтингу")
    final_talent_rating = bags_points + tokens_points + st.session_state.earned_rating
    
    st.metric(label="⚔️ Всего гарантированных ОЧКОВ ТАЛАНТА в рейтинг:", value=f"{int(final_talent_rating)}")
    
