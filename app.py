import streamlit as st

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор Обаяния и Близости")
st.caption("by ТаЙга | Мобильная версия")

# Создаем вкладки для удобства, чтобы не перегружать экран
tab1, tab2 = st.tabs(["✨ Расчет Обаяния", "❤️ Расчет Близости"])

with tab1:
    st.header("Расчет минимального количества Обаяния")
    
    # Константы для расчета предметов (весов/ценностей предметов)
    # ПРИМЕЧАНИЕ: Впишите сюда реальные значения очков из игры, если они фиксированные!
    # Сейчас стоят базовые множители (1 предмет = 1 очко), замените цифры на игровые.
    VAL_DUHI = 1
    VAL_SER_SHP = 2
    VAL_ZOL_SHP = 5
    VAL_HADAK = 10
    VAL_SIN_HADAK = 20
    
    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic = st.number_input("Количество наложниц:", min_value=0, value=0, help="<-Задания-Достижения-Монарх-романтик")
    duhi = st.number_input("Духи:", min_value=0, value=0)
    ser_shpilka = st.number_input("Серебряная шпилька:", min_value=0, value=0)
    zol_shpilka = st.number_input("Золотая шпилька:", min_value=0, value=0)
    hadak = st.number_input("Хадак:", min_value=0, value=0)
    sin_hadak = st.number_input("Синий Хадак:", min_value=0, value=0)
    
    st.subheader("🎁 Сундуки и Фураж")
    red_sunduki = st.number_input("Красные сундуки (кол-во):", min_value=0, value=0)
    ob_za_100_sun = st.number_input("Сколько обаяния дало 100 красных сундуков?:", min_value=0, value=0, help="Посмотреть значения в рейтинге ДО, открыть 100 сундуков, посмотреть значение после, вписать разницу")
    furazh = st.number_input("Фураж (обаяние):", min_value=0, value=0)
    
    st.subheader("💃 Наложницы для призыва")
    st.info("Впишите кол-во обаяния, если планируете призывать наложницу в рейтинг. Если не призываете — оставьте 0.")
    
    # Список наложниц из вашего файла
    girls = [
        "Бадра", "Маша", "Байлина", "Медея", "Бастет", "Милана", "Ильза", "Ника", 
        "Ипполита", "Паулина", "Кармилла", "Родия", "Каталин", "Сигрид", "Киара", 
        "Тамара", "Кларисса", "Табити", "Корэна", "Ува", "Кунегурда", "Улана", 
        "Людмила", "Фазара", "Марика", "Фрейя", "Марико", "Юлия", 
        "Анар (Дочь вечности)", "Земея (Дочь вечности)", "Айрис (Дочь вечности)", 
        "Амар (Дочь вечности)", "Иветт (Дочь вечности)", "Вилма (Дочь вечности)"
    ]
    
    sum_girls_ob = 0
    # Разделим наложниц на 2 колонки, чтобы на телефоне это выглядело компактно
    col1, col2 = st.columns(2)
    for i, girl in enumerate(girls):
        with col1 if i % 2 == 0 else col2:
            val = st.number_input(f"{girl}:", min_value=0, value=0, key=f"ob_{girl}")
            sum_girls_ob += val

    # Математика расчета Обаяния
    # Считаем сундуки (если введено значение за 100 сундуков)
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
    st.caption("⚠️ Данное значение минимальное, т.к. красные сундуки и фураж дают рандомное количество очков.")

with tab2:
    st.header("Расчет минимального количества Близости")
    
    # Константы для расчета предметов Близости
    # Замените 1, 2, 5 и т.д. на реальные очки, которые дает предмет в игре Великий Хан
    VAL_KOLCO = 1
    VAL_SERGI = 2
    VAL_SANDAL = 5
    VAL_NEFRIT = 10
    VAL_TAKYA = 20
    VAL_ORDOS = 50

    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic_bl = st.number_input("Количество наложниц (Близость):", min_value=0, value=0)
    kolca = st.number_input("Кольца:", min_value=0, value=0)
    sergi = st.number_input("Серьги:", min_value=0, value=0)
    sandal = st.number_input("Сандаловый браслет:", min_value=0, value=0)
    nefrit = st.number_input("Нефритовый браслет:", min_value=0, value=0)
    takya = st.number_input("Такъя:", min_value=0, value=0)
    ordos = st.number_input("Ордос:", min_value=0, value=0)
    
    st.subheader("🌾 Дополнительно")
    furazh_bl = st.number_input("Фураж (близость):", min_value=0, value=0)
    
    # Математика расчета Близости
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
import streamlit as st

st.set_page_config(page_title="Калькулятор Великого Хана", layout="centered")
st.title("🏆 Калькулятор Обаяния и Близости")
st.caption("by ТаЙга | Мобильная версия")

# Создаем вкладки для удобства, чтобы не перегружать экран
tab1, tab2 = st.tabs(["✨ Расчет Обаяния", "❤️ Расчет Близости"])

with tab1:
    st.header("Расчет минимального количества Обаяния")
    
    # Константы для расчета предметов (весов/ценностей предметов)
    # ПРИМЕЧАНИЕ: Впишите сюда реальные значения очков из игры, если они фиксированные!
    # Сейчас стоят базовые множители (1 предмет = 1 очко), замените цифры на игровые.
    VAL_DUHI = 1
    VAL_SER_SHP = 2
    VAL_ZOL_SHP = 5
    VAL_HADAK = 10
    VAL_SIN_HADAK = 20
    
    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic = st.number_input("Количество наложниц:", min_value=0, value=0, help="<-Задания-Достижения-Монарх-романтик")
    duhi = st.number_input("Духи:", min_value=0, value=0)
    ser_shpilka = st.number_input("Серебряная шпилька:", min_value=0, value=0)
    zol_shpilka = st.number_input("Золотая шпилька:", min_value=0, value=0)
    hadak = st.number_input("Хадак:", min_value=0, value=0)
    sin_hadak = st.number_input("Синий Хадак:", min_value=0, value=0)
    
    st.subheader("🎁 Сундуки и Фураж")
    red_sunduki = st.number_input("Красные сундуки (кол-во):", min_value=0, value=0)
    ob_za_100_sun = st.number_input("Сколько обаяния дало 100 красных сундуков?:", min_value=0, value=0, help="Посмотреть значения в рейтинге ДО, открыть 100 сундуков, посмотреть значение после, вписать разницу")
    furazh = st.number_input("Фураж (обаяние):", min_value=0, value=0)
    
    st.subheader("💃 Наложницы для призыва")
    st.info("Впишите кол-во обаяния, если планируете призывать наложницу в рейтинг. Если не призываете — оставьте 0.")
    
    # Список наложниц из вашего файла
    girls = [
        "Бадра", "Маша", "Байлина", "Медея", "Бастет", "Милана", "Ильза", "Ника", 
        "Ипполита", "Паулина", "Кармилла", "Родия", "Каталин", "Сигрид", "Киара", 
        "Тамара", "Кларисса", "Табити", "Корэна", "Ува", "Кунегурда", "Улана", 
        "Людмила", "Фазара", "Марика", "Фрейя", "Марико", "Юлия", 
        "Анар (Дочь вечности)", "Земея (Дочь вечности)", "Айрис (Дочь вечности)", 
        "Амар (Дочь вечности)", "Иветт (Дочь вечности)", "Вилма (Дочь вечности)"
    ]
    
    sum_girls_ob = 0
    # Разделим наложниц на 2 колонки, чтобы на телефоне это выглядело компактно
    col1, col2 = st.columns(2)
    for i, girl in enumerate(girls):
        with col1 if i % 2 == 0 else col2:
            val = st.number_input(f"{girl}:", min_value=0, value=0, key=f"ob_{girl}")
            sum_girls_ob += val

    # Математика расчета Обаяния
    # Считаем сундуки (если введено значение за 100 сундуков)
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
    st.caption("⚠️ Данное значение минимальное, т.к. красные сундуки и фураж дают рандомное количество очков.")

with tab2:
    st.header("Расчет минимального количества Близости")
    
    # Константы для расчета предметов Близости
    # Замените 1, 2, 5 и т.д. на реальные очки, которые дает предмет в игре Великий Хан
    VAL_KOLCO = 1
    VAL_SERGI = 2
    VAL_SANDAL = 5
    VAL_NEFRIT = 10
    VAL_TAKYA = 20
    VAL_ORDOS = 50

    st.subheader("📦 Ресурсы со склада")
    kol_nalozhnic_bl = st.number_input("Количество наложниц (Близость):", min_value=0, value=0)
    kolca = st.number_input("Кольца:", min_value=0, value=0)
    sergi = st.number_input("Серьги:", min_value=0, value=0)
    sandal = st.number_input("Сандаловый браслет:", min_value=0, value=0)
    nefrit = st.number_input("Нефритовый браслет:", min_value=0, value=0)
    takya = st.number_input("Такъя:", min_value=0, value=0)
    ordos = st.number_input("Ордос:", min_value=0, value=0)
    
    st.subheader("🌾 Дополнительно")
    furazh_bl = st.number_input("Фураж (близость):", min_value=0, value=0)
    
    # Математика расчета Близости
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
