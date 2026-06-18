"""
Dizionario comuni ilMeteo (estratto dal PDF ufficiale).
Contiene i principali comuni italiani con ID, nome, provincia e regione.
Il config flow usa questo dizionario per la ricerca locale + fallback API.
Totale: 533 comuni indicizzati.
"""

COMUNI: dict[str, dict] = {
    "1": {
        "nome": "Abano Terme",
        "prov": "PD",
        "regione": "Veneto"
    },
    "2": {
        "nome": "Abbadia Cerreto",
        "prov": "LO",
        "regione": "Lombardia"
    },
    "3": {
        "nome": "Abbadia Lariana",
        "prov": "LC",
        "regione": "Lombardia"
    },
    "4": {
        "nome": "Abbadia San Salvatore",
        "prov": "SI",
        "regione": "Toscana"
    },
    "5": {
        "nome": "Abbasanta",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "6": {
        "nome": "Abbateggio",
        "prov": "PE",
        "regione": "Abruzzo"
    },
    "7": {
        "nome": "Abbiategrasso",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "8": {
        "nome": "Abetone",
        "prov": "PT",
        "regione": "Toscana"
    },
    "9": {
        "nome": "Abriola",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "10": {
        "nome": "Acate",
        "prov": "RG",
        "regione": "Sicilia"
    },
    "11": {
        "nome": "Accadia",
        "prov": "FG",
        "regione": "Puglia"
    },
    "12": {
        "nome": "Acceglio",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "13": {
        "nome": "Accettura",
        "prov": "MT",
        "regione": "Basilicata"
    },
    "14": {
        "nome": "Acciano",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "15": {
        "nome": "Accumoli",
        "prov": "RI",
        "regione": "Lazio"
    },
    "16": {
        "nome": "Acerenza",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "17": {
        "nome": "Acerno",
        "prov": "SA",
        "regione": "Campania"
    },
    "18": {
        "nome": "Acerra",
        "prov": "NA",
        "regione": "Campania"
    },
    "19": {
        "nome": "Aci Bonaccorsi",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "20": {
        "nome": "Aci Castello",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "21": {
        "nome": "Aci Catena",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "22": {
        "nome": "Aci Sant Antonio",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "23": {
        "nome": "Acireale",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "24": {
        "nome": "Acquacanina",
        "prov": "MC",
        "regione": "Marche"
    },
    "25": {
        "nome": "Acquafondata",
        "prov": "FR",
        "regione": "Lazio"
    },
    "26": {
        "nome": "Acquaformosa",
        "prov": "CS",
        "regione": "Calabria"
    },
    "27": {
        "nome": "Acquafredda",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "28": {
        "nome": "Acqualagna",
        "prov": "PU",
        "regione": "Marche"
    },
    "29": {
        "nome": "Acquanegra Cremonese",
        "prov": "CR",
        "regione": "Lombardia"
    },
    "30": {
        "nome": "Acquanegra sul Chiese",
        "prov": "MN",
        "regione": "Lombardia"
    },
    "31": {
        "nome": "Acquapendente",
        "prov": "VT",
        "regione": "Lazio"
    },
    "32": {
        "nome": "Acquappesa",
        "prov": "CS",
        "regione": "Calabria"
    },
    "33": {
        "nome": "Acquarica del Capo",
        "prov": "LE",
        "regione": "Puglia"
    },
    "34": {
        "nome": "Acquaro",
        "prov": "VV",
        "regione": "Calabria"
    },
    "35": {
        "nome": "Acquasanta Terme",
        "prov": "AP",
        "regione": "Marche"
    },
    "36": {
        "nome": "Acquasparta",
        "prov": "TR",
        "regione": "Umbria"
    },
    "37": {
        "nome": "Acquaviva Collecroce",
        "prov": "CB",
        "regione": "Molise"
    },
    "38": {
        "nome": "Acquaviva D Isernia",
        "prov": "IS",
        "regione": "Molise"
    },
    "39": {
        "nome": "Acquaviva delle Fonti",
        "prov": "BA",
        "regione": "Puglia"
    },
    "40": {
        "nome": "Acquaviva Picena",
        "prov": "AP",
        "regione": "Marche"
    },
    "41": {
        "nome": "Acquaviva Platani",
        "prov": "CL",
        "regione": "Sicilia"
    },
    "42": {
        "nome": "Acquedolci",
        "prov": "ME",
        "regione": "Sicilia"
    },
    "43": {
        "nome": "Acqui Terme",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "44": {
        "nome": "Acri",
        "prov": "CS",
        "regione": "Calabria"
    },
    "45": {
        "nome": "Acuto",
        "prov": "FR",
        "regione": "Lazio"
    },
    "46": {
        "nome": "Adelfia",
        "prov": "BA",
        "regione": "Puglia"
    },
    "47": {
        "nome": "Adrano",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "48": {
        "nome": "Adrara San Martino",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "49": {
        "nome": "Adrara San Rocco",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "50": {
        "nome": "Adria",
        "prov": "RO",
        "regione": "Veneto"
    },
    "51": {
        "nome": "Adro",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "52": {
        "nome": "Affi",
        "prov": "VR",
        "regione": "Veneto"
    },
    "53": {
        "nome": "Affile",
        "prov": "RM",
        "regione": "Lazio"
    },
    "54": {
        "nome": "Afragola",
        "prov": "NA",
        "regione": "Campania"
    },
    "55": {
        "nome": "Africo",
        "prov": "RC",
        "regione": "Calabria"
    },
    "56": {
        "nome": "Agazzano",
        "prov": "PC",
        "regione": "Emilia Romagna"
    },
    "57": {
        "nome": "Agerola",
        "prov": "NA",
        "regione": "Campania"
    },
    "58": {
        "nome": "Aggius",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "59": {
        "nome": "Agira",
        "prov": "EN",
        "regione": "Sicilia"
    },
    "60": {
        "nome": "Agliana",
        "prov": "PT",
        "regione": "Toscana"
    },
    "61": {
        "nome": "Agliano Terme",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "62": {
        "nome": "Aglie",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "63": {
        "nome": "Aglientu",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "64": {
        "nome": "Agna",
        "prov": "PD",
        "regione": "Veneto"
    },
    "65": {
        "nome": "Agnadello",
        "prov": "CR",
        "regione": "Lombardia"
    },
    "66": {
        "nome": "Agnana Calabra",
        "prov": "RC",
        "regione": "Calabria"
    },
    "67": {
        "nome": "Agnone",
        "prov": "IS",
        "regione": "Molise"
    },
    "68": {
        "nome": "Agnosine",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "69": {
        "nome": "Agordo",
        "prov": "BL",
        "regione": "Veneto"
    },
    "70": {
        "nome": "Agosta",
        "prov": "RM",
        "regione": "Lazio"
    },
    "71": {
        "nome": "Agra",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "72": {
        "nome": "Agrate Brianza",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "73": {
        "nome": "Agrate Conturbia",
        "prov": "NO",
        "regione": "Piemonte"
    },
    "74": {
        "nome": "Agrigento",
        "prov": "AG",
        "regione": "Sicilia"
    },
    "75": {
        "nome": "Agropoli",
        "prov": "SA",
        "regione": "Campania"
    },
    "76": {
        "nome": "Agugliano",
        "prov": "AN",
        "regione": "Marche"
    },
    "77": {
        "nome": "Agugliaro",
        "prov": "VI",
        "regione": "Veneto"
    },
    "78": {
        "nome": "Aicurzio",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "79": {
        "nome": "Aidmaggiore",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "80": {
        "nome": "Aidone",
        "prov": "EN",
        "regione": "Sicilia"
    },
    "81": {
        "nome": "Aielli",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "82": {
        "nome": "Aiello Calabro",
        "prov": "CS",
        "regione": "Calabria"
    },
    "83": {
        "nome": "Aiello del Friuli",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "84": {
        "nome": "Aiello del Sabato",
        "prov": "AV",
        "regione": "Campania"
    },
    "85": {
        "nome": "Aieta",
        "prov": "CS",
        "regione": "Calabria"
    },
    "86": {
        "nome": "Ailano",
        "prov": "CE",
        "regione": "Campania"
    },
    "87": {
        "nome": "Ailoche",
        "prov": "BI",
        "regione": "Piemonte"
    },
    "88": {
        "nome": "Airasca",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "89": {
        "nome": "Airola",
        "prov": "BN",
        "regione": "Campania"
    },
    "90": {
        "nome": "Airole",
        "prov": "IM",
        "regione": "Liguria"
    },
    "91": {
        "nome": "Airuno",
        "prov": "LC",
        "regione": "Lombardia"
    },
    "92": {
        "nome": "Aisone",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "93": {
        "nome": "Ala",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "94": {
        "nome": "Ala dei Sardi",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "95": {
        "nome": "Ala di Stura",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "96": {
        "nome": "Alagna",
        "prov": "PV",
        "regione": "Lombardia"
    },
    "97": {
        "nome": "Alagna Valsesia",
        "prov": "VC",
        "regione": "Piemonte"
    },
    "98": {
        "nome": "Alanno",
        "prov": "PE",
        "regione": "Abruzzo"
    },
    "99": {
        "nome": "Alano di Piave",
        "prov": "BL",
        "regione": "Veneto"
    },
    "100": {
        "nome": "Alassio",
        "prov": "SV",
        "regione": "Liguria"
    },
    "101": {
        "nome": "Alatri",
        "prov": "FR",
        "regione": "Lazio"
    },
    "102": {
        "nome": "Alba",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "103": {
        "nome": "Alba Adriatica",
        "prov": "TE",
        "regione": "Abruzzo"
    },
    "104": {
        "nome": "Albagiara",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "105": {
        "nome": "Albarate",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "106": {
        "nome": "Albanella",
        "prov": "SA",
        "regione": "Campania"
    },
    "107": {
        "nome": "Albano di Lucania",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "108": {
        "nome": "Albano Laziale",
        "prov": "RM",
        "regione": "Lazio"
    },
    "109": {
        "nome": "Albano Sant Alessandro",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "110": {
        "nome": "Albano Vercellese",
        "prov": "VC",
        "regione": "Piemonte"
    },
    "111": {
        "nome": "Albaredo Arnaboldi",
        "prov": "PV",
        "regione": "Lombardia"
    },
    "112": {
        "nome": "Albaredo d Adige",
        "prov": "VR",
        "regione": "Veneto"
    },
    "113": {
        "nome": "Albaredo per San Marco",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "114": {
        "nome": "Albareto",
        "prov": "MO",
        "regione": "Emilia Romagna"
    },
    "115": {
        "nome": "Albaretto della Torre",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "116": {
        "nome": "Albavilla",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "117": {
        "nome": "Albenga",
        "prov": "SV",
        "regione": "Liguria"
    },
    "118": {
        "nome": "Albera Ligure",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "119": {
        "nome": "Alberobello",
        "prov": "BA",
        "regione": "Puglia"
    },
    "120": {
        "nome": "Alberona",
        "prov": "FG",
        "regione": "Puglia"
    },
    "121": {
        "nome": "Albese con Cassano",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "122": {
        "nome": "Albettone",
        "prov": "VI",
        "regione": "Veneto"
    },
    "123": {
        "nome": "Albi",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "124": {
        "nome": "Albiano",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "125": {
        "nome": "Albiano d Ivrea",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "126": {
        "nome": "Albiate",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "127": {
        "nome": "Albidona",
        "prov": "CS",
        "regione": "Calabria"
    },
    "128": {
        "nome": "Albignasego",
        "prov": "PD",
        "regione": "Veneto"
    },
    "129": {
        "nome": "Albinea",
        "prov": "RE",
        "regione": "Emilia Romagna"
    },
    "130": {
        "nome": "Albino",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "131": {
        "nome": "Albiolo",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "132": {
        "nome": "Albissola Superiore",
        "prov": "SV",
        "regione": "Liguria"
    },
    "133": {
        "nome": "Albisola Marina",
        "prov": "SV",
        "regione": "Liguria"
    },
    "134": {
        "nome": "Albizzate",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "135": {
        "nome": "Albonese",
        "prov": "PV",
        "regione": "Lombardia"
    },
    "136": {
        "nome": "Albosaggia",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "137": {
        "nome": "Albugnano",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "138": {
        "nome": "Albuzzano",
        "prov": "PV",
        "regione": "Lombardia"
    },
    "139": {
        "nome": "Alcamo",
        "prov": "TP",
        "regione": "Sicilia"
    },
    "140": {
        "nome": "Alcara Li Fusi",
        "prov": "ME",
        "regione": "Sicilia"
    },
    "141": {
        "nome": "Aldeno",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "142": {
        "nome": "Aldino",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "143": {
        "nome": "Ales",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "144": {
        "nome": "Alessandria",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "145": {
        "nome": "Alessandria del Carretto",
        "prov": "CS",
        "regione": "Calabria"
    },
    "146": {
        "nome": "Alessandria della Rocca",
        "prov": "AG",
        "regione": "Sicilia"
    },
    "147": {
        "nome": "Alessano",
        "prov": "LE",
        "regione": "Puglia"
    },
    "148": {
        "nome": "Alezio",
        "prov": "LE",
        "regione": "Puglia"
    },
    "149": {
        "nome": "Alfano",
        "prov": "SA",
        "regione": "Campania"
    },
    "150": {
        "nome": "Alfedena",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "151": {
        "nome": "Alfianello",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "152": {
        "nome": "Alfiano Natta",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "153": {
        "nome": "Alfonsine",
        "prov": "RA",
        "regione": "Emilia Romagna"
    },
    "154": {
        "nome": "Alghero",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "155": {
        "nome": "Algua",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "156": {
        "nome": "Ali",
        "prov": "ME",
        "regione": "Sicilia"
    },
    "157": {
        "nome": "Ali Terme",
        "prov": "ME",
        "regione": "Sicilia"
    },
    "158": {
        "nome": "Alia",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "159": {
        "nome": "Aliano",
        "prov": "MT",
        "regione": "Basilicata"
    },
    "160": {
        "nome": "Alice Bel Colle",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "161": {
        "nome": "Alice Castello",
        "prov": "VC",
        "regione": "Piemonte"
    },
    "162": {
        "nome": "Alice Superiore",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "163": {
        "nome": "Alife",
        "prov": "CE",
        "regione": "Campania"
    },
    "164": {
        "nome": "Alimena",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "165": {
        "nome": "Aliminusa",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "166": {
        "nome": "Allai",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "167": {
        "nome": "Alleghe",
        "prov": "BL",
        "regione": "Veneto"
    },
    "168": {
        "nome": "Allein",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "169": {
        "nome": "Allerona",
        "prov": "TR",
        "regione": "Umbria"
    },
    "170": {
        "nome": "Alliste",
        "prov": "LE",
        "regione": "Puglia"
    },
    "171": {
        "nome": "Allumiere",
        "prov": "RM",
        "regione": "Lazio"
    },
    "172": {
        "nome": "Alluvioni Cambi",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "173": {
        "nome": "Alme",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "174": {
        "nome": "Almeno San Bartolomeo",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "175": {
        "nome": "Almeno San Salvatore",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "176": {
        "nome": "Almese",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "177": {
        "nome": "Alonte",
        "prov": "VI",
        "regione": "Veneto"
    },
    "178": {
        "nome": "Alpette",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "179": {
        "nome": "Alpignano",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "180": {
        "nome": "Alseno",
        "prov": "PC",
        "regione": "Emilia Romagna"
    },
    "181": {
        "nome": "Alserio",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "182": {
        "nome": "Altamura",
        "prov": "BA",
        "regione": "Puglia"
    },
    "183": {
        "nome": "Altare",
        "prov": "SV",
        "regione": "Liguria"
    },
    "184": {
        "nome": "Altavilla Irpina",
        "prov": "AV",
        "regione": "Campania"
    },
    "185": {
        "nome": "Altavilla Milicia",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "186": {
        "nome": "Altavilla Monferrato",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "187": {
        "nome": "Altavilla Silentina",
        "prov": "SA",
        "regione": "Campania"
    },
    "188": {
        "nome": "Altavilla Vicentina",
        "prov": "VI",
        "regione": "Veneto"
    },
    "189": {
        "nome": "Altidona",
        "prov": "AP",
        "regione": "Marche"
    },
    "190": {
        "nome": "Altilia",
        "prov": "CS",
        "regione": "Calabria"
    },
    "191": {
        "nome": "Altino",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "192": {
        "nome": "Altissimo",
        "prov": "VI",
        "regione": "Veneto"
    },
    "193": {
        "nome": "Altivole",
        "prov": "TV",
        "regione": "Veneto"
    },
    "194": {
        "nome": "Alto",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "195": {
        "nome": "Altofonte",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "196": {
        "nome": "Altomonte",
        "prov": "CS",
        "regione": "Calabria"
    },
    "197": {
        "nome": "Altopascio",
        "prov": "LU",
        "regione": "Toscana"
    },
    "198": {
        "nome": "Alviano",
        "prov": "TR",
        "regione": "Umbria"
    },
    "199": {
        "nome": "Alvignano",
        "prov": "CE",
        "regione": "Campania"
    },
    "200": {
        "nome": "Alvito",
        "prov": "FR",
        "regione": "Lazio"
    },
    "201": {
        "nome": "Alzano Lombardo",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "202": {
        "nome": "Alzano Scrivia",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "203": {
        "nome": "Alzate Brianza",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "204": {
        "nome": "Amalfi",
        "prov": "SA",
        "regione": "Campania"
    },
    "205": {
        "nome": "Amandola",
        "prov": "AP",
        "regione": "Marche"
    },
    "206": {
        "nome": "Amantea",
        "prov": "CS",
        "regione": "Calabria"
    },
    "207": {
        "nome": "Amaro",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "208": {
        "nome": "Amaroni",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "209": {
        "nome": "Amaseno",
        "prov": "FR",
        "regione": "Lazio"
    },
    "210": {
        "nome": "Amato",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "211": {
        "nome": "Amatrice",
        "prov": "RI",
        "regione": "Lazio"
    },
    "212": {
        "nome": "Ambivere",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "213": {
        "nome": "Amblar",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "214": {
        "nome": "Ameglia",
        "prov": "SP",
        "regione": "Liguria"
    },
    "215": {
        "nome": "Amelia",
        "prov": "TR",
        "regione": "Umbria"
    },
    "216": {
        "nome": "Amendolara",
        "prov": "CS",
        "regione": "Calabria"
    },
    "217": {
        "nome": "Ameno",
        "prov": "NO",
        "regione": "Piemonte"
    },
    "218": {
        "nome": "Amorosi",
        "prov": "BN",
        "regione": "Campania"
    },
    "219": {
        "nome": "Ampezzo",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "220": {
        "nome": "Anacapri",
        "prov": "NA",
        "regione": "Campania"
    },
    "221": {
        "nome": "Anagni",
        "prov": "FR",
        "regione": "Lazio"
    },
    "222": {
        "nome": "Ancarano",
        "prov": "TE",
        "regione": "Abruzzo"
    },
    "223": {
        "nome": "Ancona",
        "prov": "AN",
        "regione": "Marche"
    },
    "224": {
        "nome": "Andali",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "225": {
        "nome": "Andalo",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "226": {
        "nome": "Andalo Valtellino",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "227": {
        "nome": "Andezeno",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "228": {
        "nome": "Andora",
        "prov": "SV",
        "regione": "Liguria"
    },
    "229": {
        "nome": "Andorno Micca",
        "prov": "BI",
        "regione": "Piemonte"
    },
    "230": {
        "nome": "Andrano",
        "prov": "LE",
        "regione": "Puglia"
    },
    "231": {
        "nome": "Andrate",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "232": {
        "nome": "Andreis",
        "prov": "PN",
        "regione": "Friuli Venezia Giulia"
    },
    "233": {
        "nome": "Andretta",
        "prov": "AV",
        "regione": "Campania"
    },
    "234": {
        "nome": "Andria",
        "prov": "BA",
        "regione": "Puglia"
    },
    "235": {
        "nome": "Andriano",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "236": {
        "nome": "Anela",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "237": {
        "nome": "Anfo",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "238": {
        "nome": "Angera",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "239": {
        "nome": "Anghiari",
        "prov": "AR",
        "regione": "Toscana"
    },
    "240": {
        "nome": "Angiari",
        "prov": "VR",
        "regione": "Veneto"
    },
    "241": {
        "nome": "Angolo Terme",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "242": {
        "nome": "Angri",
        "prov": "SA",
        "regione": "Campania"
    },
    "243": {
        "nome": "Angrogna",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "244": {
        "nome": "Anguillara Sabazia",
        "prov": "RM",
        "regione": "Lazio"
    },
    "245": {
        "nome": "Anguillara Veneta",
        "prov": "PD",
        "regione": "Veneto"
    },
    "246": {
        "nome": "Annicco",
        "prov": "CR",
        "regione": "Lombardia"
    },
    "247": {
        "nome": "Annone di Brianza",
        "prov": "LC",
        "regione": "Lombardia"
    },
    "248": {
        "nome": "Annone Veneto",
        "prov": "VE",
        "regione": "Veneto"
    },
    "249": {
        "nome": "Anoia",
        "prov": "RC",
        "regione": "Calabria"
    },
    "250": {
        "nome": "Antegnate",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "251": {
        "nome": "Anterivo",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "252": {
        "nome": "Antey-Saint-Andre",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "253": {
        "nome": "Anticoli Corrado",
        "prov": "RM",
        "regione": "Lazio"
    },
    "254": {
        "nome": "Antignano",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "255": {
        "nome": "Antillo",
        "prov": "ME",
        "regione": "Sicilia"
    },
    "256": {
        "nome": "Antonimina",
        "prov": "RC",
        "regione": "Calabria"
    },
    "257": {
        "nome": "Antrodoco",
        "prov": "RI",
        "regione": "Lazio"
    },
    "258": {
        "nome": "Antrona Schieranco",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "259": {
        "nome": "Anversa degli Abruzzi",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "260": {
        "nome": "Anzano del Parco",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "261": {
        "nome": "Anzano di Puglia",
        "prov": "FG",
        "regione": "Puglia"
    },
    "262": {
        "nome": "Anzi",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "263": {
        "nome": "Anzio",
        "prov": "RM",
        "regione": "Lazio"
    },
    "264": {
        "nome": "Anzola d Ossola",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "265": {
        "nome": "Anzola dell Emilia",
        "prov": "BO",
        "regione": "Emilia Romagna"
    },
    "266": {
        "nome": "Aosta",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "267": {
        "nome": "Apecchio",
        "prov": "PU",
        "regione": "Marche"
    },
    "268": {
        "nome": "Apice",
        "prov": "BN",
        "regione": "Campania"
    },
    "269": {
        "nome": "Apiro",
        "prov": "MC",
        "regione": "Marche"
    },
    "270": {
        "nome": "Apollosa",
        "prov": "BN",
        "regione": "Campania"
    },
    "271": {
        "nome": "Appiano Gentile",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "272": {
        "nome": "Appiano sulla Strada del Vino",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "273": {
        "nome": "Appignano",
        "prov": "MC",
        "regione": "Marche"
    },
    "274": {
        "nome": "Appignano del Tronto",
        "prov": "AP",
        "regione": "Marche"
    },
    "275": {
        "nome": "Aprica",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "276": {
        "nome": "Apricale",
        "prov": "IM",
        "regione": "Liguria"
    },
    "277": {
        "nome": "Apricena",
        "prov": "FG",
        "regione": "Puglia"
    },
    "278": {
        "nome": "Aprigliano",
        "prov": "CS",
        "regione": "Calabria"
    },
    "279": {
        "nome": "Aprilia",
        "prov": "LT",
        "regione": "Lazio"
    },
    "280": {
        "nome": "Aquara",
        "prov": "SA",
        "regione": "Campania"
    },
    "281": {
        "nome": "Aquila di Arroscia",
        "prov": "IM",
        "regione": "Liguria"
    },
    "282": {
        "nome": "Aquileia",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "283": {
        "nome": "Aquilonia",
        "prov": "AV",
        "regione": "Campania"
    },
    "284": {
        "nome": "Aquino",
        "prov": "FR",
        "regione": "Lazio"
    },
    "285": {
        "nome": "Aradeo",
        "prov": "LE",
        "regione": "Puglia"
    },
    "286": {
        "nome": "Aragona",
        "prov": "AG",
        "regione": "Sicilia"
    },
    "287": {
        "nome": "Aramengo",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "288": {
        "nome": "Arba",
        "prov": "PN",
        "regione": "Friuli Venezia Giulia"
    },
    "289": {
        "nome": "Arborea",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "290": {
        "nome": "Arborio",
        "prov": "VC",
        "regione": "Piemonte"
    },
    "291": {
        "nome": "Arbus",
        "prov": "CA",
        "regione": "Sardegna"
    },
    "292": {
        "nome": "Arcade",
        "prov": "TV",
        "regione": "Veneto"
    },
    "293": {
        "nome": "Arce",
        "prov": "FR",
        "regione": "Lazio"
    },
    "294": {
        "nome": "Arcene",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "295": {
        "nome": "Arcevia",
        "prov": "AN",
        "regione": "Marche"
    },
    "296": {
        "nome": "Archi",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "297": {
        "nome": "Arcidosso",
        "prov": "GR",
        "regione": "Toscana"
    },
    "298": {
        "nome": "Arcinazzo Romano",
        "prov": "RM",
        "regione": "Lazio"
    },
    "299": {
        "nome": "Arcisate",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "300": {
        "nome": "Arco",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "301": {
        "nome": "Arcola",
        "prov": "SP",
        "regione": "Liguria"
    },
    "302": {
        "nome": "Arcole",
        "prov": "VR",
        "regione": "Veneto"
    },
    "303": {
        "nome": "Arconate",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "304": {
        "nome": "Arcore",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "305": {
        "nome": "Arcugnano",
        "prov": "VI",
        "regione": "Veneto"
    },
    "306": {
        "nome": "Ardara",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "307": {
        "nome": "Ardauli",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "308": {
        "nome": "Ardea",
        "prov": "RM",
        "regione": "Lazio"
    },
    "309": {
        "nome": "Ardenno",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "310": {
        "nome": "Ardesio",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "311": {
        "nome": "Ardore",
        "prov": "RC",
        "regione": "Calabria"
    },
    "312": {
        "nome": "Arena",
        "prov": "VV",
        "regione": "Calabria"
    },
    "313": {
        "nome": "Arena Po",
        "prov": "PV",
        "regione": "Lombardia"
    },
    "314": {
        "nome": "Arenzano",
        "prov": "GE",
        "regione": "Liguria"
    },
    "315": {
        "nome": "Arese",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "316": {
        "nome": "Arezzo",
        "prov": "AR",
        "regione": "Toscana"
    },
    "317": {
        "nome": "Argegno",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "318": {
        "nome": "Argelato",
        "prov": "BO",
        "regione": "Emilia Romagna"
    },
    "319": {
        "nome": "Argenta",
        "prov": "FE",
        "regione": "Emilia Romagna"
    },
    "320": {
        "nome": "Argentera",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "321": {
        "nome": "Arguello",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "322": {
        "nome": "Argusto",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "323": {
        "nome": "Ari",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "324": {
        "nome": "Ariano Irpino",
        "prov": "AV",
        "regione": "Campania"
    },
    "325": {
        "nome": "Ariano nel Polesine",
        "prov": "RO",
        "regione": "Veneto"
    },
    "326": {
        "nome": "Ariccia",
        "prov": "RM",
        "regione": "Lazio"
    },
    "327": {
        "nome": "Arielli",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "328": {
        "nome": "Arienzo",
        "prov": "CE",
        "regione": "Campania"
    },
    "329": {
        "nome": "Arignano",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "330": {
        "nome": "Aritzo",
        "prov": "NU",
        "regione": "Sardegna"
    },
    "331": {
        "nome": "Arizzano",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "332": {
        "nome": "Arlena di Castro",
        "prov": "VT",
        "regione": "Lazio"
    },
    "333": {
        "nome": "Arluno",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "334": {
        "nome": "Armeno",
        "prov": "NO",
        "regione": "Piemonte"
    },
    "335": {
        "nome": "Armento",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "336": {
        "nome": "Armo",
        "prov": "IM",
        "regione": "Liguria"
    },
    "337": {
        "nome": "Armungia",
        "prov": "CA",
        "regione": "Sardegna"
    },
    "338": {
        "nome": "Arnad",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "339": {
        "nome": "Arnara",
        "prov": "FR",
        "regione": "Lazio"
    },
    "340": {
        "nome": "Arnasco",
        "prov": "SV",
        "regione": "Liguria"
    },
    "341": {
        "nome": "Arnesano",
        "prov": "LE",
        "regione": "Puglia"
    },
    "342": {
        "nome": "Arola",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "343": {
        "nome": "Arona",
        "prov": "NO",
        "regione": "Piemonte"
    },
    "344": {
        "nome": "Arosio",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "345": {
        "nome": "Arpaia",
        "prov": "BN",
        "regione": "Campania"
    },
    "346": {
        "nome": "Arpaise",
        "prov": "BN",
        "regione": "Campania"
    },
    "347": {
        "nome": "Arpino",
        "prov": "FR",
        "regione": "Lazio"
    },
    "348": {
        "nome": "Arqua Petrarca",
        "prov": "PD",
        "regione": "Veneto"
    },
    "349": {
        "nome": "Arqua Polesine",
        "prov": "RO",
        "regione": "Veneto"
    },
    "350": {
        "nome": "Arquata del Tronto",
        "prov": "AP",
        "regione": "Marche"
    },
    "351": {
        "nome": "Arquata Scrivia",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "352": {
        "nome": "Arre",
        "prov": "PD",
        "regione": "Veneto"
    },
    "353": {
        "nome": "Arrone",
        "prov": "TR",
        "regione": "Umbria"
    },
    "354": {
        "nome": "Arsago Seprio",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "355": {
        "nome": "Arsie",
        "prov": "BL",
        "regione": "Veneto"
    },
    "356": {
        "nome": "Arsiero",
        "prov": "VI",
        "regione": "Veneto"
    },
    "357": {
        "nome": "Arsita",
        "prov": "TE",
        "regione": "Abruzzo"
    },
    "358": {
        "nome": "Arsoli",
        "prov": "RM",
        "regione": "Lazio"
    },
    "359": {
        "nome": "Arta Terme",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "360": {
        "nome": "Artegna",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "361": {
        "nome": "Artena",
        "prov": "RM",
        "regione": "Lazio"
    },
    "362": {
        "nome": "Artogne",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "363": {
        "nome": "Arvier",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "364": {
        "nome": "Arzachena",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "365": {
        "nome": "Arzago d Adda",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "366": {
        "nome": "Arzana",
        "prov": "NU",
        "regione": "Sardegna"
    },
    "367": {
        "nome": "Arzano",
        "prov": "NA",
        "regione": "Campania"
    },
    "368": {
        "nome": "Arzene",
        "prov": "PN",
        "regione": "Friuli Venezia Giulia"
    },
    "369": {
        "nome": "Arzergrande",
        "prov": "PD",
        "regione": "Veneto"
    },
    "370": {
        "nome": "Arzignano",
        "prov": "VI",
        "regione": "Veneto"
    },
    "371": {
        "nome": "Ascea",
        "prov": "SA",
        "regione": "Campania"
    },
    "372": {
        "nome": "Asciano",
        "prov": "SI",
        "regione": "Toscana"
    },
    "373": {
        "nome": "Ascoli Piceno",
        "prov": "AP",
        "regione": "Marche"
    },
    "374": {
        "nome": "Ascoli Satriano",
        "prov": "FG",
        "regione": "Puglia"
    },
    "375": {
        "nome": "Ascrea",
        "prov": "RI",
        "regione": "Lazio"
    },
    "376": {
        "nome": "Asiago",
        "prov": "VI",
        "regione": "Veneto"
    },
    "377": {
        "nome": "Asigliano Veneto",
        "prov": "VI",
        "regione": "Veneto"
    },
    "378": {
        "nome": "Asigliano Vercellese",
        "prov": "VC",
        "regione": "Piemonte"
    },
    "379": {
        "nome": "Asola",
        "prov": "MN",
        "regione": "Lombardia"
    },
    "380": {
        "nome": "Asolo",
        "prov": "TV",
        "regione": "Veneto"
    },
    "381": {
        "nome": "Assago",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "382": {
        "nome": "Assemini",
        "prov": "CA",
        "regione": "Sardegna"
    },
    "383": {
        "nome": "Assisi",
        "prov": "PG",
        "regione": "Umbria"
    },
    "384": {
        "nome": "Asso",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "385": {
        "nome": "Assolo",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "386": {
        "nome": "Assoro",
        "prov": "EN",
        "regione": "Sicilia"
    },
    "387": {
        "nome": "Asti",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "388": {
        "nome": "Asuni",
        "prov": "OR",
        "regione": "Sardegna"
    },
    "389": {
        "nome": "Ateleta",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "390": {
        "nome": "Atella",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "391": {
        "nome": "Atena Lucana",
        "prov": "SA",
        "regione": "Campania"
    },
    "392": {
        "nome": "Atessa",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "393": {
        "nome": "Atina",
        "prov": "FR",
        "regione": "Lazio"
    },
    "394": {
        "nome": "Atrani",
        "prov": "SA",
        "regione": "Campania"
    },
    "395": {
        "nome": "Atri",
        "prov": "TE",
        "regione": "Abruzzo"
    },
    "396": {
        "nome": "Atripalda",
        "prov": "AV",
        "regione": "Campania"
    },
    "397": {
        "nome": "Attigliano",
        "prov": "TR",
        "regione": "Umbria"
    },
    "398": {
        "nome": "Attimis",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "399": {
        "nome": "Atzara",
        "prov": "NU",
        "regione": "Sardegna"
    },
    "400": {
        "nome": "Auditore",
        "prov": "PU",
        "regione": "Marche"
    },
    "401": {
        "nome": "Augusta",
        "prov": "SR",
        "regione": "Sicilia"
    },
    "402": {
        "nome": "Auletta",
        "prov": "SA",
        "regione": "Campania"
    },
    "403": {
        "nome": "Aulla",
        "prov": "MS",
        "regione": "Toscana"
    },
    "404": {
        "nome": "Aurano",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "405": {
        "nome": "Aurigo",
        "prov": "IM",
        "regione": "Liguria"
    },
    "406": {
        "nome": "Auronzo di Cadore",
        "prov": "BL",
        "regione": "Veneto"
    },
    "407": {
        "nome": "Ausonia",
        "prov": "FR",
        "regione": "Lazio"
    },
    "408": {
        "nome": "Austis",
        "prov": "NU",
        "regione": "Sardegna"
    },
    "409": {
        "nome": "Avegno",
        "prov": "GE",
        "regione": "Liguria"
    },
    "410": {
        "nome": "Avelengo",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "411": {
        "nome": "Avella",
        "prov": "AV",
        "regione": "Campania"
    },
    "412": {
        "nome": "Avellino",
        "prov": "AV",
        "regione": "Campania"
    },
    "413": {
        "nome": "Averara",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "414": {
        "nome": "Aversa",
        "prov": "CE",
        "regione": "Campania"
    },
    "415": {
        "nome": "Avetrana",
        "prov": "TA",
        "regione": "Puglia"
    },
    "416": {
        "nome": "Avezzano",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "417": {
        "nome": "Aviano",
        "prov": "PN",
        "regione": "Friuli Venezia Giulia"
    },
    "418": {
        "nome": "Aviatico",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "419": {
        "nome": "Avigliana",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "420": {
        "nome": "Avigliano",
        "prov": "PZ",
        "regione": "Basilicata"
    },
    "421": {
        "nome": "Avigliano Umbro",
        "prov": "TR",
        "regione": "Umbria"
    },
    "422": {
        "nome": "Avio",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "423": {
        "nome": "Avise",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "424": {
        "nome": "Avola",
        "prov": "SR",
        "regione": "Sicilia"
    },
    "425": {
        "nome": "Avolasca",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "426": {
        "nome": "Ayas",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "427": {
        "nome": "Aymavilles",
        "prov": "AO",
        "regione": "Valle d Aosta"
    },
    "428": {
        "nome": "Azeglio",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "429": {
        "nome": "Azzanello",
        "prov": "CR",
        "regione": "Lombardia"
    },
    "430": {
        "nome": "Azzano d Asti",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "431": {
        "nome": "Azzano Decimo",
        "prov": "PN",
        "regione": "Friuli Venezia Giulia"
    },
    "432": {
        "nome": "Azzano Mella",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "433": {
        "nome": "Azzano San Paolo",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "434": {
        "nome": "Azzate",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "435": {
        "nome": "Azzio",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "436": {
        "nome": "Azzone",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "532": {
        "nome": "Bari",
        "prov": "BA",
        "regione": "Puglia"
    },
    "563": {
        "nome": "Bassano del Grappa",
        "prov": "VI",
        "regione": "Veneto"
    },
    "609": {
        "nome": "Belluno",
        "prov": "BL",
        "regione": "Veneto"
    },
    "641": {
        "nome": "Bergamo",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "691": {
        "nome": "Biella",
        "prov": "BI",
        "regione": "Piemonte"
    },
    "745": {
        "nome": "Bologna",
        "prov": "BO",
        "regione": "Emilia Romagna"
    },
    "752": {
        "nome": "Bolzano",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "780": {
        "nome": "Bordighera",
        "prov": "IM",
        "regione": "Liguria"
    },
    "830": {
        "nome": "Bormio",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "875": {
        "nome": "Bra",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "907": {
        "nome": "Brescia",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "910": {
        "nome": "Bressanone",
        "prov": "BZ",
        "regione": "Trentino Alto Adige"
    },
    "924": {
        "nome": "Brindisi",
        "prov": "BR",
        "regione": "Puglia"
    },
    "1014": {
        "nome": "Busto Arsizio",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "1039": {
        "nome": "Cagliari",
        "prov": "CA",
        "regione": "Sardegna"
    },
    "1084": {
        "nome": "Calenzano",
        "prov": "FI",
        "regione": "Toscana"
    },
    "1099": {
        "nome": "Caltagirone",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "1100": {
        "nome": "Caltanissetta",
        "prov": "CL",
        "regione": "Sicilia"
    },
    "1148": {
        "nome": "Camogli",
        "prov": "GE",
        "regione": "Liguria"
    },
    "1176": {
        "nome": "Campobasso",
        "prov": "CB",
        "regione": "Molise"
    },
    "1217": {
        "nome": "Canale",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "1221": {
        "nome": "Canazei",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "1234": {
        "nome": "Canelli",
        "prov": "AT",
        "regione": "Piemonte"
    },
    "1238": {
        "nome": "Canicatti",
        "prov": "AG",
        "regione": "Sicilia"
    },
    "1249": {
        "nome": "Cannobio",
        "prov": "VB",
        "regione": "Piemonte"
    },
    "1254": {
        "nome": "Canosa di Puglia",
        "prov": "BA",
        "regione": "Puglia"
    },
    "1269": {
        "nome": "Cantu",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "1272": {
        "nome": "Caorle",
        "prov": "VE",
        "regione": "Veneto"
    },
    "1278": {
        "nome": "Capannori",
        "prov": "LU",
        "regione": "Toscana"
    },
    "1315": {
        "nome": "Capri",
        "prov": "NA",
        "regione": "Campania"
    },
    "1330": {
        "nome": "Capua",
        "prov": "CE",
        "regione": "Campania"
    },
    "1334": {
        "nome": "Caraglio",
        "prov": "CN",
        "regione": "Piemonte"
    },
    "1344": {
        "nome": "Caravaggio",
        "prov": "BG",
        "regione": "Lombardia"
    },
    "1356": {
        "nome": "Carbonia",
        "prov": "CA",
        "regione": "Sardegna"
    },
    "1378": {
        "nome": "Carignano",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "1391": {
        "nome": "Carmagnola",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "1401": {
        "nome": "Caronno Pertusella",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "1404": {
        "nome": "Carovigno",
        "prov": "BR",
        "regione": "Puglia"
    },
    "1412": {
        "nome": "Carpi",
        "prov": "MO",
        "regione": "Emilia Romagna"
    },
    "1422": {
        "nome": "Carrara",
        "prov": "MS",
        "regione": "Toscana"
    },
    "1429": {
        "nome": "Carsoli",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "1462": {
        "nome": "Casale Monferrato",
        "prov": "AL",
        "regione": "Piemonte"
    },
    "1530": {
        "nome": "Caserta",
        "prov": "CE",
        "regione": "Campania"
    },
    "1569": {
        "nome": "Cassino",
        "prov": "FR",
        "regione": "Lazio"
    },
    "1603": {
        "nome": "Castel di Sangro",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "1609": {
        "nome": "Castel Gandolfo",
        "prov": "RM",
        "regione": "Lazio"
    },
    "1631": {
        "nome": "Castel Volturno",
        "prov": "CE",
        "regione": "Campania"
    },
    "1638": {
        "nome": "Castelbuono",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "1647": {
        "nome": "Castelfiorentino",
        "prov": "FI",
        "regione": "Toscana"
    },
    "1655": {
        "nome": "Castelfranco Veneto",
        "prov": "TV",
        "regione": "Veneto"
    },
    "1664": {
        "nome": "Castellabate",
        "prov": "SA",
        "regione": "Campania"
    },
    "1667": {
        "nome": "Castellammare del Golfo",
        "prov": "TP",
        "regione": "Sicilia"
    },
    "1668": {
        "nome": "Castellammare di Stabia",
        "prov": "NA",
        "regione": "Campania"
    },
    "1670": {
        "nome": "Castellana Grotte",
        "prov": "BA",
        "regione": "Puglia"
    },
    "1674": {
        "nome": "Castellanza",
        "prov": "VA",
        "regione": "Lombardia"
    },
    "1697": {
        "nome": "Castellina in Chianti",
        "prov": "SI",
        "regione": "Toscana"
    },
    "1744": {
        "nome": "Castelnuovo di Garfagnana",
        "prov": "LU",
        "regione": "Toscana"
    },
    "1762": {
        "nome": "Castelsardo",
        "prov": "SS",
        "regione": "Sardegna"
    },
    "1776": {
        "nome": "Castelvetrano",
        "prov": "TP",
        "regione": "Sicilia"
    },
    "1832": {
        "nome": "Catania",
        "prov": "CT",
        "regione": "Sicilia"
    },
    "1833": {
        "nome": "Catanzaro",
        "prov": "CZ",
        "regione": "Calabria"
    },
    "1836": {
        "nome": "Cattolica",
        "prov": "RN",
        "regione": "Emilia Romagna"
    },
    "1840": {
        "nome": "Cava de Tirreni",
        "prov": "SA",
        "regione": "Campania"
    },
    "1849": {
        "nome": "Cavalese",
        "prov": "TN",
        "regione": "Trentino Alto Adige"
    },
    "1873": {
        "nome": "Cavriago",
        "prov": "RE",
        "regione": "Emilia Romagna"
    },
    "1880": {
        "nome": "Ceccano",
        "prov": "FR",
        "regione": "Lazio"
    },
    "1882": {
        "nome": "Cecina",
        "prov": "LI",
        "regione": "Toscana"
    },
    "1886": {
        "nome": "Cefalu",
        "prov": "PA",
        "regione": "Sicilia"
    },
    "1889": {
        "nome": "Celano",
        "prov": "AQ",
        "regione": "Abruzzo"
    },
    "1920": {
        "nome": "Cento",
        "prov": "FE",
        "regione": "Emilia Romagna"
    },
    "1943": {
        "nome": "Cerea",
        "prov": "VR",
        "regione": "Veneto"
    },
    "1958": {
        "nome": "Cerignola",
        "prov": "FG",
        "regione": "Puglia"
    },
    "1963": {
        "nome": "Cernobbio",
        "prov": "CO",
        "regione": "Lombardia"
    },
    "1965": {
        "nome": "Cernusco sul Naviglio",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "1974": {
        "nome": "Cerreto Sannita",
        "prov": "BN",
        "regione": "Campania"
    },
    "1983": {
        "nome": "Certaldo",
        "prov": "FI",
        "regione": "Toscana"
    },
    "1994": {
        "nome": "Cerveteri",
        "prov": "RM",
        "regione": "Lazio"
    },
    "1995": {
        "nome": "Cervia",
        "prov": "RA",
        "regione": "Emilia Romagna"
    },
    "1998": {
        "nome": "Cervignano del Friuli",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "2011": {
        "nome": "Cesena",
        "prov": "FC",
        "regione": "Emilia Romagna"
    },
    "2012": {
        "nome": "Cesenatico",
        "prov": "FC",
        "regione": "Emilia Romagna"
    },
    "2039": {
        "nome": "Chianciano Terme",
        "prov": "SI",
        "regione": "Toscana"
    },
    "2045": {
        "nome": "Chiaravalle",
        "prov": "AN",
        "regione": "Marche"
    },
    "2047": {
        "nome": "Chiari",
        "prov": "BS",
        "regione": "Lombardia"
    },
    "2050": {
        "nome": "Chiavari",
        "prov": "GE",
        "regione": "Liguria"
    },
    "2051": {
        "nome": "Chiavenna",
        "prov": "SO",
        "regione": "Lombardia"
    },
    "2054": {
        "nome": "Chieri",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "2059": {
        "nome": "Chieti",
        "prov": "CH",
        "regione": "Abruzzo"
    },
    "2064": {
        "nome": "Chioggia",
        "prov": "VE",
        "regione": "Veneto"
    },
    "2084": {
        "nome": "Chivasso",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "2085": {
        "nome": "Ciampino",
        "prov": "RM",
        "regione": "Lazio"
    },
    "2113": {
        "nome": "Cinisello Balsamo",
        "prov": "MI",
        "regione": "Lombardia"
    },
    "2125": {
        "nome": "Cirie",
        "prov": "TO",
        "regione": "Piemonte"
    },
    "2156": {
        "nome": "Cividale del Friuli",
        "prov": "UD",
        "regione": "Friuli Venezia Giulia"
    },
    "2160": {
        "nome": "Civita Castellana",
        "prov": "VT",
        "regione": "Lazio"
    },
    "2165": {
        "nome": "Civitanova Marche",
        "prov": "MC",
        "regione": "Marche"
    },
    "2167": {
        "nome": "Civitavecchia",
        "prov": "RM",
        "regione": "Lazio"
    }
}
