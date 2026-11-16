"""Pronunciación orientativa del portugués de Brasil para hispanohablantes.

Convención de la guía (la misma que se explica en la clase 1 de A1):
  y   = j / g suave del portugués (como la «y» rioplatense de «yo»)
  j   = como la j española (la r inicial y la rr del portugués)
  sh  = ch / x del portugués (como la «sh» rioplatense de «calle»)
  ch  = t delante de i (como la «ch» de «chico»)
  dy  = d delante de i (como «dy» de «dyi»)
  ly  = lh;  ñ = nh;  z = s entre vocales;  ã õ = vocales nasales
  n final tras vocal = nasalización suave (bon, un, bein)
"""

import re

VOW = set("aeiouáéíóúâêôãõàĩũ")
SOFT = set("eiéêíĩ")
IS = set("iíĩ")

# Palabras cuya pronunciación se corrige a mano (vocales abiertas, x, préstamos).
OVR = {
    "tchau": "chau",
    "nove": "nóvi",
    "dez": "dés",
    "futebol": "futchibou",
    "ritmo": "jítchimu",
    "bossa": "bósa",
    "cara": "kara",
    "dor": "dór",
    "meia": "meia",
    "mil": "miu",
    "pois": "pois",
    "tá": "tá",
    "sete": "sétchi",
    "ela": "éla",
    "ele": "éli",
    "eles": "élis",
    "elas": "élas",
    "perto": "pértu",
    "terra": "téja",
    "festa": "fésta",
    "porta": "pórta",
    "forte": "fórchi",
    "morte": "mórchi",
    "corpo": "kórpu",
    "novo": "novu",
    "nova": "nóva",
    "novos": "nóvus",
    "novas": "nóvas",
    "táxi": "taksi",
    "próximo": "prósimu",
    "máximo": "másimu",
    "sexta": "sesta",
    "sexta-feira": "sesta feira",
    "texto": "testu",
    "explicar": "esplikar",
    "exemplo": "ezemplu",
    "exame": "ezami",
    "existir": "ezistchir",
    "trouxe": "trosi",
    "auxílio": "ausílyu",
    "mexer": "mesher",
    "taxa": "tasha",
    "fixo": "fiksu",
    "complexo": "kompleksu",
    "sexo": "seksu",
    "tóxico": "tóksiku",
    "boxe": "boksi",
    "fax": "faks",
    "xadrez": "shadres",
    "e": "i",
    "o": "u",
    "os": "us",
    "um": "un",
    "é": "é",
    "são": "sãu",
    "você": "vose",
    "vocês": "voses",
    "wi-fi": "uai fai",
    "internet": "internéchi",
    "e-mail": "imeiu",
    "shopping": "shopin",
    "show": "shou",
    "mouse": "mausi",
    "design": "dizain",
    "feedback": "fidbék",
    "marketing": "markechin",
    "stress": "estres",
    "ok": "oquei",
    "jazz": "yaz",
    "hobby": "róbi",
    "chef": "shéf",
    "pub": "pab",
    "pizza": "pitsa",
    "hambúrguer": "hambúrguer",
}


def _conv(w):
    # colas nasales y finales átonos
    tail = ""
    for suf, rep in (("ões", "õis"), ("ães", "ãis"), ("ãos", "ãus"), ("ão", "ãu"), ("ãe", "ãi"), ("õe", "õi")):
        if w.endswith(suf):
            w = w[: -len(suf)]
            tail = rep
            break
    else:
        if w.endswith("ens"):
            w = w[:-3]
            tail = "eins"
        elif w.endswith("em"):
            w = w[:-2]
            tail = "ein"
        elif w.endswith("am") and len(w) >= 4:
            w = w[:-2]
            tail = "ãu"
        elif w.endswith("m") and len(w) >= 2 and w[-2] in VOW:
            w = w[:-1]
            tail = "n"
        elif w.endswith("os") and len(w) > 2:
            w = w[:-2]
            tail = "us"
        elif w.endswith("o") and len(w) > 1:
            w = w[:-1]
            tail = "u"
        elif w.endswith("es") and len(w) > 2:
            w = w[:-2]
            tail = "is"
        elif w.endswith("e") and len(w) > 1:
            w = w[:-1]
            tail = "i"
    palatal_tail = tail in ("i", "is")
    tail_soft = tail[:1] in ("i", "e") and bool(tail)
    n = len(w)
    out = []
    i = 0

    def at(k):
        return w[k] if 0 <= k < n else ""

    while i < n:
        c = w[i]
        nx = at(i + 1)
        pv = at(i - 1)
        two = w[i : i + 2]
        soft2 = at(i + 2) in SOFT or (i + 2 == n and tail_soft)
        if two == "ch":
            out.append("sh")
            i += 2
            continue
        if two == "lh":
            out.append("ly")
            i += 2
            continue
        if two == "nh":
            out.append("ñ")
            i += 2
            continue
        if two == "rr":
            out.append("j")
            i += 2
            continue
        if two == "ss":
            out.append("s")
            i += 2
            continue
        if two == "sc" and soft2:
            out.append("s")
            i += 2
            continue
        if two == "sç":
            out.append("s")
            i += 2
            continue
        if two == "xc" and soft2:
            out.append("s")
            i += 2
            continue
        if two == "qu":
            out.append("k" if soft2 else "ku")
            i += 2
            continue
        if two == "gu" and soft2:
            out.append("gu")
            i += 2
            continue
        if c == "g":
            out.append("y" if nx in SOFT or (i + 1 == n and tail_soft) else "g")
        elif c == "j":
            out.append("y")
        elif c == "ç":
            out.append("s")
        elif c == "c":
            out.append("s" if nx in SOFT or (i + 1 == n and tail_soft) else "k")
        elif c == "h":
            pass
        elif c == "x":
            if i == 1 and at(0) == "e":
                out.append("z" if nx in VOW else "s")
            elif nx in ("c", "t", "p"):
                out.append("s")
            else:
                out.append("sh")
        elif c == "s":
            after = nx if nx else tail[:1]
            if pv in VOW and after in VOW:
                out.append("z")
            else:
                out.append("s")
        elif c == "z":
            out.append("s" if i + 1 == n and not tail else "z")
        elif c == "r":
            if i == 0 or pv in ("n", "l", "s"):
                out.append("j")
            else:
                out.append("r")
        elif c == "t" and (nx in IS or (i + 1 == n and palatal_tail)):
            out.append("ch")
        elif c == "d" and (nx in IS or (i + 1 == n and palatal_tail)):
            out.append("dy")
        elif c == "l":
            vowel_next = (nx in VOW) if nx else (tail[:1] in ("a", "e", "i", "o", "u", "ã", "õ") and bool(tail))
            out.append("l" if vowel_next or pv == "u" else "u")
        elif c in "âà":
            out.append("a")
        elif c == "ê":
            out.append("e")
        elif c == "ô":
            out.append("o")
        elif c == "ü":
            out.append("u")
        elif c == "w":
            out.append("u")
        else:
            out.append(c)
        i += 1
    return "".join(out) + tail


_TOKEN = re.compile(r"[A-Za-zÀ-ÿ0-9]+(?:['’-][A-Za-zÀ-ÿ0-9]+)*")


def pron(text):
    """Pronunciación de una palabra o frase, sin signos ni mayúsculas."""
    text = text.strip().lower()
    if text in OVR:
        return OVR[text]
    words = []
    for token in _TOKEN.findall(text):
        if token in OVR:
            words.append(OVR[token])
            continue
        parts = re.split(r"['’-]", token)
        words.append(" ".join(OVR.get(p) or _conv(p) for p in parts))
    return " ".join(words)


if __name__ == "__main__":
    import sys

    for item in sys.argv[1:]:
        print(item, "->", pron(item))
