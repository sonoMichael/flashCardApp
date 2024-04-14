from flask import Flask, render_template
from flashcard import app

words = [
    {
        "it": "macchina",
        "ch": "车辆"
    },
    {
        "it": "frenare",
        "ch": "刹车"
    },
    {
        "it": "frizione",
        "ch": "离合器"
    },
    {
        "it": "gas",
        "ch": "油门"
    },
    {
        "it": "accellerare",
        "ch": "油门"
    },
    {
        "it": "volante",
        "ch": "方向盘"
    },
    {
        "it": "clacson",
        "ch": "喇叭"
    },
    {
        "it": "suona",
        "ch": "喇叭"
    },
    {
        "it": "freccia",
        "ch": "转向灯"
    },
    {
        "it": "freno a mano",
        "ch": "手刹"
    },
    {
        "it": "marcia",
        "ch": "档位"
    },
    {
        "it": "cambia la marcia",
        "ch": "换档"
    },
    {
        "it": "prima marcia",
        "ch": "—档"
    },
    {
        "it": "seconda marcia",
        "ch": "二档"
    },
    {
        "it": "terza marcia",
        "ch": "三档"
    },
    {
        "it": "quartta marcia",
        "ch": "四档"
    },
    {
        "it": "quinta marcia",
        "ch": "五档"
    },
    {
        "it": "specchio",
        "ch": "后祝鏡"
    },
    {
        "it": "spia",
        "ch": "指示灯"
    },
    {
        "it": "luce anabbagliante",
        "ch": "近光灯"
    },
    {
        "it": "luce abbagliante",
        "ch": "远光灯"
    },
    {
        "it": "cintura",
        "ch": "安全带"
    },
    {
        "it": "sedile",
        "ch": "座椅"
    },
    {
        "it": "gira",
        "ch": "转弯"
    },
    {
        "it": "svolta",
        "ch": "转弯"
    },
    {
        "it": "davanti",
        "ch": "前"
    },
    {
        "it": "dietro",
        "ch": "后"
    },
    {
        "it": "sinistra",
        "ch": "左"
    },
    {
        "it": "destra",
        "ch": "右"
    },
    {
        "it": "su",
        "ch": "上"
    },
    {
        "it": "giu",
        "ch": "下"
    },
    {
        "it": "centro",
        "ch": "中间"
    },
    {
        "it": "in mezzo",
        "ch": "中间"
    },
    {
        "it": "diritto",
        "ch": "直走"
    },
    {
        "it": "tenere",
        "ch": "保持"
    },
    {
        "it": "attento",
        "ch": "小心"
    },
    {
        "it": "inversione",
        "ch": "调头"
    },
    {
        "it": "sorpasso",
        "ch": "超车"
    },
    {
        "it": "dare la precedenza",
        "ch": "让行"
    },
    {
        "it": "parcheggia",
        "ch": "停车"
    },
    {
        "it": "calma",
        "ch": "慢一点"
    },
    {
        "it": "piano",
        "ch": "慢一点"
    },
    {
        "it": "forza",
        "ch": "快一点"
    },
    {
        "it": "veloce",
        "ch": "快一点"
    },
    {
        "it": "retromarcia",
        "ch": "倒车"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                           words = words,
                           num_words = len(words))

@app.route("/translation/<int:link_id>")
def translation(link_id):
    if 0 <= link_id < len(words):
        return render_template("translation.html",
                               id = link_id,
                               words = words,
                               num_words = len(words),
                               next = link_id + 1,
                               prev = link_id - 1)
    else:
        return "INVALID LINK ID"
