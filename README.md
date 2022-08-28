# rostelecom-interset-prediction
Предсказание интереса покупателей к тарифу "Игровой" Ростелекома =: **@sergak_blog**

## Запуск решения

Перед началом, давайте скачаем проект и установим зависимости

```python
git clone https://github.com/sergak0/rostelecom-intereset-prediction.git
cd rostelecom-intereset-prediction
python -m pip install -r requirements.txt
```

Работа решения может быть продемонстрирована в файле [main.ipynb](https://github.com/sergak0/rostelecom-intereset-prediction/blob/main/main.ipynb)

## Data-Ext

1) Акции и курсы валют - [источник](https://www.finam.ru/profile/moex-akcii/m-video/export/?market=200&em=19737&token=03ANYolqvdH_OCpqOmKHTuwUlhDZGPJnE5jDfayGZllR8LitkREFpwwJ2bDj_kyHDDQzy8sofBMBHo0Lmqlfj7hlkwuiXjog431QHWu_mjDxj2GCOXiWPfhtyZROj4b-hQrUqlIDzjTqpZEviGeAY_7QfjhtXVhDy5iCcOoTFmMwyPoned99OGRSmRHYQoLdKkjea_DSsoKywjBn--1Un1YSr0iYwwef4orGyZ5nZz-5gaDqwHRu_ZkOvFtXGlcpJIghmaNxTIXltOtrtU5pH-ygcPJNKa-If-G9aD1iItLoNe5lt7r00GWFVlak-ZhhmvuxSc3iyiURdZwAtaTcR8uefEpyAkzvHhBELBC16CTf5zxwhn_XcHeuB0v8socMYJgEIYRwLmN8neSPsekpg556u9F2aSLEZcwFkgsYQabcnDlW5Z9E_-qWOVmrq79oWbO61RKhxx6URvT0L0c4Afg0CyeOw7MGqk6DrKPXH3FE_9trF81WKWHM9ZsFK6QvaqDw5akM0GCd8J&code=MVID&apply=0&df=1&mf=0&yf=2020&from=01.01.2020&dt=1&mt=7&yt=2022&to=01.08.2022&p=10&f=MVID_200101_220801&e=.csv&cn=MVID&dtf=3&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1)
2) Короновирус - [источник](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)
3) Города миллионники (население) - [источник](https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B8%D0%BB%D0%BB%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%8B_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B80)
4) Зарплата по городам - [источник](https://bdex.ru/ratings/cities-salary/)
5) Google Trends - [источник](https://trends.google.ru/trends/explore?geo=RU&q=%D0%A0%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC,%D0%BC%D0%B5%D0%B3%D0%B0%D1%84%D0%BE%D0%BD,%D0%BC%D1%82%D1%81)\
● Спросы на игры\
● Жалобы на плохой интернет\
● Анализа запросов по конкурентам\
● Динамика интереса к Ростелекому
