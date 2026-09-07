import streamlit as st

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор Обаяния и Близости")
st.caption("Точный расчет по игровым механикам")

tab1, tab2 = st.tabs(["✨ Расчет Обаяния", "❤️ Расчет Близости"])

with tab1:
    st.header("Расчет минимального количества Обаяния")
    
    st.subheader("👥 Ваши данные")
    kol_nalozhnic = st.number_input("Текущее количество наложниц:", min_value=1, value=10, help="Крайне важно для массовых предметов вроде Хадаков!")
    
    st.subheader("📦 Ресурсы со склада")
    duhi = st.number_input("Духи (+1 очко):", min_value=0, value=0)
    
    # Логика для случайных предметов
    mode_ob = st.radio("Как калькулировать случайные предметы Обаяния (2-5 ед. / 1-3 ед.)?", 
                       ["По гарантированному минимуму", "По среднему значению"], 
                       horizontal=True, key="mode_ob")
    
    val_ser_shp = 2 if "минимуму" in mode_ob else 3.5
    val_sin_hadak = 1 if "минимуму" in mode_ob else 2
    
    ser_shpilka = st.number_input("Серебряная шпилька (дает 2–5):", min_value=0, value=0)
    zol_shpilka = st.number_input("Золотая шпилька (+5 стабильно):", min_value=0, value=0)
    
    hadak = st.number_input("Белый хадак (+1 ВСЕМ наложницам):", min_value=0, value=0)
    sin_hadak = st.number_input("Синий хадак (1–3 ВСЕМ наложницам):", min_value=0, value=0)
    
    st.subheader("🎁 Сундуки и Фураж")
    red_sunduki = st.number_input("Красные сундуки (шт.):", min_value=0, value=0)
    ob_za_100_sun = st.number_input("Сколько обаяния принесли 100 красных сундуков?:", min_value=0, value=0)
    furazh = st.number_input("Фураж (обаяние):", min_value=0, value=0)
    
    st.subheader("💃 Наложницы для призыва")
    st.info("Впишите очки обаяния, если планируете призывать наложниц в рейтинг.")
    
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

    # МАТЕМАТИКА ОБАЯНИЯ
    avg_sunduk_val = (ob_za_100_sun / 100) if ob_za_100_sun > 0 else 0
    sunduki_total = red_sunduki * avg_sunduk_val
    
    # Массовый эффект хадаков
    hadak_total = hadak * kol_nalozhnic
    sin_hadak_total = sin_hadak * val_sin_hadak * kol_nalozhnic

    total_ob = (
        (duhi * 1) + 
        (ser_shpilka * val_ser_shp) + 
        (zol_shpilka * 5) + 
        hadak_total + 
        sin_hadak_total + 
        sunduki_total + 
        furazh + 
        sum_girls_ob
    )
    
    st.metric(label="✨ Итоговый прирост Обаяния:", value=f"{int(total_ob)}")

with tab2:
    st.header("Расчет количества Близости")
    
    st.subheader("👥 Ваши данные")
    kol_nalozhnic_bl = st.number_input("Количество наложниц (для расчета Близости):", min_value=1, value=10)
    
    st.subheader("📦 Ресурсы со склада")
    kolca = st.number_input("Самоцветное кольцо (+1 очко):", min_value=0, value=0)
    sergi = st.number_input("Золотые серьги (+2 очка):", min_value=0, value=0)
    
    mode_bl = st.radio("Как калькулировать Сандаловый браслет (2-5 ед.)?", 
                       ["По гарантированному минимуму (2 очка)", "По среднему значению (3.5 очка)"], 
                       horizontal=True, key="mode_bl")
    val_sandal = 2 if "минимуму" in mode_bl else 3.5
    
    sandal = st.number_input("Сандаловый браслет (дает 2–5):", min_value=0, value=0)
    nefrit = st.number_input("Нефритовый браслет (+5 стабильно):", min_value=0, value=0)
    
    takya = st.number_input("Такъя (+1 Близости ВСЕМ наложницам):", min_value=0, value=0)
    ordos = st.number_input("Ордос (+50 очков):", min_value=0, value=0)
    
    st.subheader("🌾 Дополнительно")
    furazh_bl = st.number_input("Фураж (близость):", min_value=0, value=0)
    
    # МАТЕМАТИКА БЛИЗОСТИ
    takya_total = takya * kol_nalozhnic_bl
    
    total_bl = (
        (kolca * 1) +
        (sergi * 2) +
        (sandal * val_sandal) +
        (nefrit * 5) +
        takya_total +
        (ordos * 50) +
        furazh_bl
    )
    
    st.metric(label="❤️ Итоговый прирост Близости:", value=f"{int(total_bl)}")
