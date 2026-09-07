import streamlit as st

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор ресурсов")
st.caption("Мобильная версия")

tab1, tab2 = st.tabs(["✨ Обаяние", "❤️ Близость"])

with tab1:
    st.header("Расчет Обаяния")
    
    st.subheader("👥 Ваши наложницы")
    b4_val = st.number_input("Дополнительные наложницы (из Заданий / Достижений):", min_value=0, value=0, key="ob_b4")
    
    st.subheader("📦 Предметы со склада")
    b5_duhi = st.number_input("Духи:", min_value=0, value=0)
    b6_ser_shp = st.number_input("Серебряная шпилька:", min_value=0, value=0)
    b7_zol_shp = st.number_input("Золотая шпилька:", min_value=0, value=0)
    b8_bel_hadak = st.number_input("Белый хадак:", min_value=0, value=0)
    b9_sin_hadak = st.number_input("Синий хадак:", min_value=0, value=0)
    
    st.subheader("📊 Сундуки и дополнительно")
    b10_val = st.number_input("Количество красных сундуков:", min_value=0, value=0)
    b11_val = st.number_input("Сколько очков дали 100 сундуков?:", min_value=0, value=0)
    b12_val = st.number_input("Фураж (Обаяние):", min_value=0, value=0)
    
    st.subheader("💃 Текущие очки наложниц")
    st.info("Впишите текущие очки только тех наложниц, которых планируете прокачивать.")
    
    regular_girls = [
        "Бадра", "Маша", "Байлина", "Медея", "Бастет", "Милана", "Ильза", "Ника", 
        "Ипполита", "Паулина", "Кармилла", "Родия", "Каталин", "Сигрид", "Киара", 
        "Тамара", "Кларисса", "Табити", "Корэна", "Ува", "Кунегурда", "Улана", 
        "Людмила", "Фазара", "Марика", "Фрейя", "Марико", "Юлия"
    ]
    
    eternity_girls = [
        "Анар (Дочь вечности)", "Земея (Дочь вечности)", "Айрис (Дочь вечности)", 
        "Амар (Дочь вечности)", "Иветт (Дочь вечности)", "Вилма (Дочь вечности)"
    ]
    
    sum_regular = 0
    count_active_regular = 0
    
    st.write("**Обычные наложницы:**")
    col1, col2 = st.columns(2)
    for i, girl in enumerate(regular_girls):
        with col1 if i % 2 == 0 else col2:
            val_str = st.text_input(f"{girl}:", value="", key=f"app_reg_{girl}")
            if val_str.strip(): 
                count_active_regular += 1
                try:
                    sum_regular += float(val_str)
                except ValueError:
                    pass

    st.write("**Дочерей вечности:**")
    sum_eternity = 0
    col3, col4 = st.columns(2)
    for i, girl in enumerate(eternity_girls):
        with col3 if i % 2 == 0 else col4:
            val_str = st.text_input(f"{girl}:", value="", key=f"app_et_{girl}")
            if val_str.strip():
                try:
                    sum_eternity += float(val_str)
                except ValueError:
                    pass

    # МАТЕМАТИКА ОБАЯНИЯ
    total_concubines_for_hadak = count_active_regular + b4_val
    hadaki_points = (total_concubines_for_hadak * b8_bel_hadak) + (b9_sin_hadak * 2 * total_concubines_for_hadak)
    sunduki_points = (b10_val * b11_val) / 100 if b10_val > 0 else 0
    
    total_ob = (
        sum_regular + 
        sum_eternity + 
        b5_duhi + 
        (b6_ser_shp * 2.5) + 
        (b7_zol_shp * 5) + 
        sunduki_points + 
        hadaki_points + 
        (b12_val * 1.5)
    )
    
    st.metric(label="✨ Итоговый прирост Обаяния:", value=f"{int(total_ob)}")

with tab2:
    st.header("Расчет Близости")
    
    st.subheader("👥 Ваши наложницы")
    bl_b4_val = st.number_input("Общее количество наложниц на аккаунте:", min_value=1, value=10, key="bl_b4")
    
    st.subheader("📦 Предметы со склада")
    b5_kolca = st.number_input("Самоцветное кольцо (+1):", min_value=0, value=0)
    b6_sergi = st.number_input("Золотые серьги (+2):", min_value=0, value=0)
    b7_sandal = st.number_input("Сандаловый браслет (+3.5):", min_value=0, value=0)
    b8_nefrit = st.number_input("Нефритовый браслет (+5):", min_value=0, value=0)
    b9_takya = st.number_input("Такъя (+1 ВСЕМ наложницам):", min_value=0, value=0)
    b10_mass_item = st.number_input("Ордос:", min_value=0, value=0)
    b11_furazh = st.number_input("Фураж (Близость) [+1.5]:", min_value=0, value=0)
    
    # МАТЕМАТИКА БЛИЗОСТИ ИЗ ВАШЕЙ ФОРМУЛЫ EXCEL
    total_bl = (
        b5_kolca +
        (b6_sergi * 2) +
        (b7_sandal * 3.5) +
        (b8_nefrit * 5) +
        (b9_takya * bl_b4_val) +
        (b10_mass_item * bl_b4_val * 2) +
        (b11_furazh * 1.5)
    )
    
    st.metric(label="❤️ Итоговый прирост Близости:", value=f"{int(total_bl)}")
