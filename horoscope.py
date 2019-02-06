import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    i = 0
    while i < total_num:
        j = 0
        forecast = ""
        while j < num_sentences:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = t.capitalize() + " " + a + " " + p + "."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1

        prophecies.append(forecast)
        i = i + 1

    return prophecies
def generate_prophecies_list():
    prophecies_list_=[]
    prophecies_list ="<ol>"

    prophecies_list +="<li>Времена дня</li>"
    prophecies_list +="<ul>"
    for items in times:
        prophecies_list +=f"<li>{items}</li>"
    prophecies_list += "</ul>"

    prophecies_list +="<li>Глаголы</li>"
    prophecies_list +="<ul>"
    for item in advices:
        prophecies_list +=f"<li>{item}</li>"
    prophecies_list +="</ul>"

    prophecies_list += "<li>Предостережение</li>"
    prophecies_list += "<ul>"
    for item in promises:
        prophecies_list += f"<li>{item}</li>"
    prophecies_list += "</ul>"

    prophecies_list +="</ol>"
    print (prophecies_list)
    prophecies_list_.append(prophecies_list)
    return prophecies_list_