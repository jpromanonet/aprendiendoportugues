"""Clases temáticas del portugués de Brasil. Doce por nivel; aquí van A1 (base), A2, B1 y B2.

Cada clase trae sus propias palabras: el léxico del nivel sale de ahí, así que
cada palabra queda anclada (pin) en la clase donde se enseña.
"""

from pt_pron import pron


def w(pt, es, ex, ex_es, pr=None):
    """Palabra, español, ejemplo, traducción y (opcional) pronunciación a mano."""
    return (pt, es, ex, ex_es, pr)


def L(title, summary, body, words, dialogue=None, quiz=None, reuse=()):
    return {
        "title": title,
        "summary": summary,
        "body": body,
        "words": words,
        "reuse": list(reuse),
        "dialogue": dialogue,
        "quiz": quiz,
    }


def D(*pairs):
    """Diálogo: pares (portugués, español). La guía de pronunciación sale sola."""
    return [{"zh": pt, "py": pron(pt), "es": es} for pt, es in pairs]


def Q(prompt, right, *wrong):
    """Pregunta de opción múltiple; la correcta va primera (el sitio mezcla las opciones)."""
    return {"prompt": prompt, "options": [right, *wrong], "correct": 0}


def row(item, level):
    pt, es, ex, ex_es = item[:4]
    pr = item[4] if len(item) > 4 and item[4] else pron(pt)
    return {
        "hanzi": pt,
        "pinyin": pr,
        "es": es,
        "level": level,
        "ex_zh": ex,
        "ex_py": pron(ex),
        "ex_es": ex_es,
    }


def bind(specs, level):
    """Devuelve (filas de léxico, clases numeradas) a partir de las clases de un nivel."""
    rows, lessons = [], []
    for number, spec in enumerate(specs, 1):
        rows += [row(item, level) for item in spec["words"]]
        pins = [item[0] for item in spec["words"]] + spec["reuse"]
        lesson = {
            "number": number,
            "title": spec["title"],
            "summary": spec["summary"],
            "body": spec["body"],
            "pins": pins,
        }
        if spec["dialogue"]:
            lesson["dialogue"] = spec["dialogue"]
        if spec["quiz"]:
            lesson["quiz"] = spec["quiz"]
        lessons.append(lesson)
    return rows, lessons


# --- A2 ---------------------------------------------------------------------

A2_SPECS = [
    L(
        "La casa",
        "Living, muebles, llaves y el alquiler.",
        [
            "En A1 viste casa, cozinha y quarto. Acá entrás: sala es el living, sofá el sillón, mesa y cadeira lo que usás para comer, cama donde dormís, armário el placard y geladeira la heladera.",
            "El fogão es la cocina con hornallas. Janela y porta se abren y se cierran: abra a janela, feche a porta. Chave abre la puerta. En Brasil el alquiler se paga todos los meses: o aluguel vence no dia cinco.",
        ],
        [
            ("sala", "living; sala de estar", "A sala é ampla e clara.", "El living es amplio y luminoso."),
            ("sofá", "sillón", "O sofá é muito confortável.", "El sillón es muy cómodo."),
            ("mesa", "mesa", "A mesa está posta.", "La mesa está puesta."),
            ("cadeira", "silla", "Puxe uma cadeira.", "Acercá una silla."),
            ("cama", "cama", "A cama é de casal.", "La cama es matrimonial."),
            ("armário", "placard; armario", "O armário está cheio.", "El placard está lleno."),
            ("geladeira", "heladera", "A geladeira está vazia.", "La heladera está vacía."),
            ("fogão", "cocina (artefacto); hornallas", "O fogão é a gás.", "La cocina es a gas."),
            ("janela", "ventana", "Abra a janela, por favor.", "Abrí la ventana, por favor."),
            ("porta", "puerta", "Feche a porta.", "Cerrá la puerta."),
            ("chave", "llave", "Onde está a chave?", "¿Dónde está la llave?"),
            ("aluguel", "alquiler", "O aluguel é caro.", "El alquiler es caro."),
        ],
    ),
    L(
        "El edificio y el barrio",
        "Piso, ascensor, expensas y el ruido de los vecinos.",
        [
            "Un prédio tiene andares, elevador, varanda e interfone. Andar significa piso, y también caminar: moro no terceiro andar, gosto de andar.",
            "O vizinho vive al lado. O síndico administra el edificio y el condomínio son las expensas. Si algo se rompe hace falta un conserto. El barulho molesta y un bairro silencioso se valora.",
        ],
        [
            ("prédio", "edificio", "O prédio tem dez andares.", "El edificio tiene diez pisos."),
            ("andar", "piso; caminar", "Moro no terceiro andar.", "Vivo en el tercer piso."),
            ("elevador", "ascensor", "O elevador está quebrado.", "El ascensor está roto."),
            ("vizinho", "vecino", "Meu vizinho é muito simpático.", "Mi vecino es muy simpático."),
            ("condomínio", "consorcio; expensas", "O condomínio vence hoje.", "Las expensas vencen hoy."),
            ("síndico", "administrador del edificio", "O síndico resolve o problema.", "El administrador resuelve el problema."),
            ("varanda", "balcón; terraza", "A varanda tem vista para o mar.", "El balcón tiene vista al mar."),
            ("interfone", "portero eléctrico", "O interfone está tocando.", "Está sonando el portero."),
            ("barulho", "ruido", "Tem muito barulho na rua.", "Hay mucho ruido en la calle."),
            ("silencioso", "silencioso; tranquilo", "O bairro é silencioso.", "El barrio es tranquilo."),
            ("conserto", "arreglo", "O conserto leva uma semana.", "El arreglo lleva una semana."),
            ("bairro", "barrio", "Gosto do meu bairro.", "Me gusta mi barrio."),
        ],
    ),
    L(
        "La rutina",
        "Del despertador a la cena, con siempre, nunca y a veces.",
        [
            "O despertador abre el día. Acordar es despertarse. Se toma banho, se toma café da manhã y más tarde viene el almoço. Por la noche se janta.",
            "Cedo y depois ubican el momento. Sempre, nunca y às vezes miden la frecuencia: eu sempre tomo café, eu nunca como carne, às vezes eu caminho. La palabra rotina resume todo.",
            "Fijate que en portugués los verbos de rutina van en presente: eu acordo, você acorda, nós acordamos. Para el almuerzo se usa a la hora: o almoço é ao meio-dia.",
        ],
        [
            ("despertador", "despertador", "O despertador toca às seis.", "El despertador suena a las seis."),
            ("acordar", "despertarse", "Eu acordo muito cedo.", "Me despierto muy temprano."),
            ("café da manhã", "desayuno", "Eu tomo café da manhã em casa.", "Desayuno en casa."),
            ("almoço", "almuerzo", "O almoço é ao meio-dia.", "El almuerzo es al mediodía."),
            ("jantar", "cena; cenar", "Nós jantamos às oito.", "Cenamos a las ocho."),
            ("banho", "baño; ducha", "Eu tomo banho de manhã.", "Me baño a la mañana."),
            ("cedo", "temprano", "Hoje acordei cedo.", "Hoy me desperté temprano."),
            ("depois", "después", "Depois eu ligo para você.", "Después te llamo."),
            ("sempre", "siempre", "Eu sempre tomo café.", "Siempre tomo café."),
            ("nunca", "nunca", "Eu nunca como carne.", "Nunca como carne."),
            ("às vezes", "a veces", "Às vezes eu caminho.", "A veces camino."),
            ("rotina", "rutina", "Minha rotina é simples.", "Mi rutina es simple."),
        ],
        dialogue=D(
            ("A que horas você acorda?", "¿A qué hora te despertás?"),
            ("Eu acordo às seis. E você?", "Me despierto a las seis. ¿Y vos?"),
            ("Eu sempre acordo cedo, mas nunca tomo café da manhã.", "Yo siempre me despierto temprano, pero nunca desayuno."),
            ("Às vezes eu tomo só um suco.", "A veces tomo solo un jugo."),
            ("Depois do almoço eu descanso um pouco.", "Después del almuerzo descanso un rato."),
        ),
    ),
    L(
        "El trabajo",
        "Oficina, jefe, sueldo y vacaciones.",
        [
            "Escritório, colega, chefe y empresa arman el mundo laboral. El salário llega a fin de mes y las férias se piden con tiempo. La reunião ordena el día.",
            "Una tarefa se termina, el computador sirve para hacerla y la mensagem es el canal con los demás. Ocupado avisa que no tenés tiempo. El horário es el rango en que se trabaja.",
        ],
        [
            ("escritório", "oficina; escritorio", "Eu trabalho no escritório.", "Trabajo en la oficina."),
            ("colega", "compañero de trabajo", "Meu colega me ajuda.", "Mi compañero me ayuda."),
            ("salário", "sueldo", "O salário cai no dia cinco.", "El sueldo cae el día cinco."),
            ("férias", "vacaciones", "Estou de férias em julho.", "Estoy de vacaciones en julio."),
            ("chefe", "jefe", "O chefe está em reunião.", "El jefe está en una reunión."),
            ("reunião", "reunión", "A reunião é às três.", "La reunión es a las tres."),
            ("tarefa", "tarea", "Terminei a tarefa.", "Terminé la tarea."),
            ("computador", "computadora", "O computador está lento.", "La computadora está lenta."),
            ("ocupado", "ocupado", "Hoje estou muito ocupado.", "Hoy estoy muy ocupado."),
            ("mensagem", "mensaje", "Mande uma mensagem.", "Mandá un mensaje."),
            ("empresa", "empresa", "A empresa é grande.", "La empresa es grande."),
            ("horário", "horario", "O horário é flexível.", "El horario es flexible."),
        ],
    ),
    L(
        "La ropa",
        "Lo que te ponés, de la remera a los anteojos.",
        [
            "Camiseta, calça, camisa y sapato alcanzan para vestirte. Sumá vestido, saia y casaco para el frío, tênis para hacer deporte y meia para los pies.",
            "Chapéu, óculos y bolsa cierran el look. Fijate que óculos siempre va en plural: meus óculos. Para decir «usar ropa» se usa el verbo usar: eu uso camiseta no verão.",
        ],
        [
            ("camiseta", "remera", "Eu uso camiseta no verão.", "Uso remera en verano."),
            ("calça", "pantalón", "Esta calça é nova.", "Este pantalón es nuevo."),
            ("camisa", "camisa", "A camisa é branca.", "La camisa es blanca."),
            ("vestido", "vestido", "Ela comprou um vestido.", "Ella compró un vestido."),
            ("saia", "pollera", "A saia é curta.", "La pollera es corta."),
            ("casaco", "abrigo; campera", "Leve um casaco.", "Llevá un abrigo."),
            ("sapato", "zapato", "O sapato é confortável.", "El zapato es cómodo."),
            ("tênis", "zapatillas", "Eu uso tênis para correr.", "Uso zapatillas para correr."),
            ("meia", "media; calcetín", "Eu perdi uma meia.", "Perdí una media."),
            ("chapéu", "sombrero", "O chapéu é de palha.", "El sombrero es de paja."),
            ("óculos", "anteojos", "Onde estão meus óculos?", "¿Dónde están mis anteojos?"),
            ("bolsa", "bolso; cartera", "A bolsa é de couro.", "La cartera es de cuero."),
        ],
    ),
    L(
        "El cuerpo y la salud",
        "Dónde duele y a quién se lo decís.",
        [
            "Cabeça, olho, mão, boca, dente, barriga, costas y garganta nombran el cuerpo. Dor es dolor y se usa con estar com: estou com dor de cabeça, estou com dor de barriga.",
            "El médico receta un remédio y lo comprás en la farmácia. Para decir que algo duele se puede decir também meu dente dói, minhas costas doem: el verbo doer concuerda con lo que duele.",
        ],
        [
            ("cabeça", "cabeza", "Estou com dor de cabeça.", "Tengo dolor de cabeza."),
            ("olho", "ojo", "Meu olho está vermelho.", "Mi ojo está rojo."),
            ("mão", "mano", "Eu machuquei a mão.", "Me lastimé la mano."),
            ("boca", "boca", "Abra a boca.", "Abrí la boca."),
            ("dente", "diente", "Meu dente dói.", "Me duele un diente."),
            ("barriga", "panza; barriga", "Estou com dor de barriga.", "Me duele la panza."),
            ("costas", "espalda", "Minhas costas doem.", "Me duele la espalda."),
            ("garganta", "garganta", "Estou com a garganta inflamada.", "Tengo la garganta inflamada."),
            ("dor", "dolor", "Eu sinto uma dor forte.", "Siento un dolor fuerte."),
            ("médico", "médico", "Preciso ir ao médico.", "Tengo que ir al médico."),
            ("remédio", "medicamento", "Tome o remédio agora.", "Tomá el remedio ahora."),
            ("farmácia", "farmacia", "A farmácia fica na esquina.", "La farmacia queda en la esquina."),
        ],
        quiz=[
            Q("Estou com dor de cabeça significa…", "me duele la cabeza", "tengo hambre", "estoy en casa", "me llamo Ana"),
            Q("Remédio es…", "medicamento", "jefe", "reunión", "puente"),
            Q("¿Dónde comprás un remédio?", "en la farmácia", "en la praça", "en la padaria", "en el ônibus"),
            Q("Costas es…", "la espalda", "el precio", "el sabor", "la llave"),
            Q("Barriga es…", "la panza", "el zapato", "la ventana", "el lago"),
        ],
    ),
    L(
        "El pasado",
        "Pretérito perfeito: fui, comi, fiz, vi.",
        [
            "Para hablar de lo que ya pasó, el portugués usa el pretérito perfeito. Eu fui, eu comi, eu fiz, eu vi. Fui sirve tanto para ir como para ser: ontem eu fui ao mercado.",
            "Las terminaciones para eu: -ei en los verbos en -ar (falei, cheguei, voltei) y -i en los verbos en -er e -ir (comi, saí). Los irregulares se aprenden de memoria: fiz, disse, tive, estive, pude.",
            "Otro detalle: para ele, ela y você los verbos en -ar terminan en -ou: ele falou, ela chegou. Los irregulares cambian de forma: ela disse, ela fez.",
        ],
        [
            ("fui", "fui (de ir o ser)", "Ontem eu fui ao mercado.", "Ayer fui al mercado."),
            ("comi", "comí", "Eu comi arroz e feijão.", "Comí arroz y porotos."),
            ("fiz", "hice", "O que você fez ontem?", "¿Qué hiciste ayer?"),
            ("vi", "vi", "Eu vi um filme ontem.", "Ayer vi una película."),
            ("disse", "dije; dijo", "Ela disse que sim.", "Ella dijo que sí."),
            ("tive", "tuve", "Eu tive uma ideia.", "Tuve una idea."),
            ("estive", "estuve", "Eu estive em São Paulo.", "Estuve en San Pablo."),
            ("pude", "pude", "Eu não pude ir.", "No pude ir."),
            ("cheguei", "llegué", "Eu cheguei cedo.", "Llegué temprano."),
            ("saí", "salí", "Eu saí de casa às oito.", "Salí de casa a las ocho."),
            ("voltei", "volví", "Eu voltei tarde.", "Volví tarde."),
            ("falei", "hablé", "Eu falei com o chefe.", "Hablé con el jefe."),
        ],
        dialogue=D(
            ("O que você fez ontem?", "¿Qué hiciste ayer?"),
            ("Eu fui ao centro e vi um filme.", "Fui al centro y vi una película."),
            ("Com quem você foi?", "¿Con quién fuiste?"),
            ("Fui com minha irmã. Depois comi pizza.", "Fui con mi hermana. Después comí pizza."),
            ("Que legal! Eu fiquei em casa.", "¡Qué bueno! Yo me quedé en casa."),
        ),
    ),
    L(
        "Moverse por la ciudad",
        "Subte, aeropuerto, trasbordo y demoras.",
        [
            "Metrô, aeroporto y mala cubren el viaje largo. Táxi, ponto de ônibus y plataforma cubren el viaje corto. El colectivo se espera en el ponto; el tren, en la plataforma.",
            "Un atraso y una baldeação explican por qué llegás tarde. Mapa, ponte, centro y museu te ubican cuando ya bajaste. Para pedir indicaciones se dice como chego ao centro?",
        ],
        [
            ("metrô", "subte; metro", "Eu vou de metrô.", "Voy en subte."),
            ("aeroporto", "aeropuerto", "O aeroporto é longe.", "El aeropuerto queda lejos."),
            ("mala", "valija", "Minha mala é pesada.", "Mi valija es pesada."),
            ("táxi", "taxi", "Vamos de táxi?", "¿Vamos en taxi?"),
            ("ponto de ônibus", "parada de colectivo", "O ponto de ônibus fica ali.", "La parada de colectivo está ahí."),
            ("plataforma", "andén", "O trem sai da plataforma dois.", "El tren sale del andén dos."),
            ("atraso", "demora; retraso", "O voo teve atraso.", "El vuelo tuvo demora."),
            ("baldeação", "combinación; trasbordo", "Preciso fazer baldeação.", "Tengo que hacer combinación."),
            ("mapa", "mapa", "Olhe no mapa.", "Mirá en el mapa."),
            ("ponte", "puente", "A ponte está fechada.", "El puente está cerrado."),
            ("centro", "centro", "Vou ao centro.", "Voy al centro."),
            ("museu", "museo", "O museu abre às dez.", "El museo abre a las diez."),
        ],
    ),
    L(
        "El mercado",
        "Feria, kilo, caja y el vuelto.",
        [
            "O mercado es el supermercado y la feira es el mercado callejero que abre algunos días a la semana. Para el pan se va a la padaria, que es mucho más que una panadería: se desayuna ahí.",
            "Pedís un quilo y lo pesan en la balança. Pagás no caixa y te dan el troco y el recibo. Una promoção baja el preço. Con cartão pagás sin efectivo. Pedí una sacola si no llevás bolsa. Fresco elogia lo que está recién traído.",
        ],
        [
            ("mercado", "mercado; supermercado", "Vou ao mercado.", "Voy al supermercado."),
            ("feira", "feria; mercado callejero", "A feira é aos domingos.", "La feria es los domingos."),
            ("padaria", "panadería", "Compro pão na padaria.", "Compro pan en la panadería."),
            ("quilo", "kilo", "Dois quilos de arroz.", "Dos kilos de arroz."),
            ("caixa", "caja; cajero", "Pague no caixa.", "Pagá en la caja."),
            ("troco", "vuelto", "O senhor esqueceu o troco.", "Se olvidó el vuelto."),
            ("recibo", "recibo; ticket", "Guarde o recibo.", "Guardá el ticket."),
            ("sacola", "bolsa (de compras)", "Preciso de uma sacola.", "Necesito una bolsa."),
            ("promoção", "oferta", "Hoje tem promoção de frutas.", "Hoy hay oferta de frutas."),
            ("fresco", "fresco", "O peixe está fresco.", "El pescado está fresco."),
            ("balança", "balanza", "Ponha na balança.", "Ponelo en la balanza."),
            ("preço", "precio", "O preço subiu.", "El precio subió."),
            ("cartão", "tarjeta", "Aceita cartão?", "¿Aceptan tarjeta?"),
        ],
    ),
    L(
        "Gustos",
        "Me encanta, lo detesto, demasiado y bastante.",
        [
            "Preferir arma la elección. Adorar sube la intensidad y detestar la baja. Bastante, demais, pouco y muito gradúan la cantidad: é bastante caro, está quente demais, falo pouco inglês.",
            "Sabor, salgado, doce, amargo y picante describen el plato. Doce sirve para todo lo dulce: bolo doce, café doce. Si querés más azúcar decí mais açúcar.",
        ],
        [
            ("preferir", "preferir", "Eu prefiro chá.", "Prefiero té."),
            ("adorar", "adorar; encantar", "Eu adoro chocolate.", "Me encanta el chocolate."),
            ("detestar", "detestar", "Eu detesto filas.", "Detesto las colas."),
            ("bastante", "bastante", "É bastante caro.", "Es bastante caro."),
            ("demais", "demasiado; muchísimo", "Está quente demais.", "Hace demasiado calor."),
            ("pouco", "poco", "Falo pouco inglês.", "Hablo poco inglés."),
            ("muito", "mucho", "Eu gosto muito de música.", "Me gusta mucho la música."),
            ("sabor", "sabor", "Que sabor você prefere?", "¿Qué sabor preferís?"),
            ("salgado", "salado", "O pastel é salgado.", "El pastel es salado."),
            ("doce", "dulce", "O bolo é muito doce.", "La torta es muy dulce."),
            ("amargo", "amargo", "O café está amargo.", "El café está amargo."),
            ("picante", "picante", "A pimenta é picante.", "El ají es picante."),
        ],
    ),
    L(
        "Tiempo libre",
        "Deporte, música y una salida.",
        [
            "Esporte y academia son el cuerpo. Nadar y dançar son hacer. Tocar sirve para instrumentos: tocar violão.",
            "Filme y show son la salida. El convite llega, el jogo tiene time. El passatempo es lo que hacés por gusto y música lo acompaña todo.",
        ],
        [
            ("esporte", "deporte", "Eu gosto de esporte.", "Me gusta el deporte."),
            ("academia", "gimnasio", "Vou à academia hoje.", "Voy al gimnasio hoy."),
            ("nadar", "nadar", "Eu nado na piscina.", "Nado en la pileta."),
            ("dançar", "bailar", "Nós dançamos samba.", "Bailamos samba."),
            ("tocar", "tocar (un instrumento)", "Ele toca violão.", "Él toca la guitarra."),
            ("filme", "película", "Este filme é ótimo.", "Esta película es excelente."),
            ("show", "recital; show", "O show é sábado.", "El recital es el sábado."),
            ("convite", "invitación", "Recebi um convite.", "Recibí una invitación."),
            ("jogo", "juego; partido", "O jogo começa às nove.", "El partido empieza a las nueve."),
            ("time", "equipo", "Meu time ganhou.", "Mi equipo ganó."),
            ("passatempo", "pasatiempo", "Meu passatempo é ler.", "Mi pasatiempo es leer."),
            ("música", "música", "Eu escuto música.", "Escucho música."),
        ],
    ),
    L(
        "El fin de semana",
        "Playa, montaña y una excursión en auto.",
        [
            "O passeio sale el domingo. Campo, praia y montanha son el destino. El piquenique va en la mochila.",
            "La trilha sube hasta la vista. Pôr do sol y amanhecer marcan la luz. El carro pide gasolina. Proponé con vamos y cerrá con a gente se vê, que es muy brasileño.",
        ],
        [
            ("passeio", "paseo", "Domingo vamos fazer um passeio.", "El domingo vamos a dar un paseo."),
            ("campo", "campo", "Eu moro no campo.", "Vivo en el campo."),
            ("praia", "playa", "Eu amo a praia.", "Amo la playa."),
            ("montanha", "montaña", "A montanha é linda.", "La montaña es hermosa."),
            ("piquenique", "picnic", "O piquenique é no parque.", "El picnic es en el parque."),
            ("trilha", "sendero", "A trilha é longa.", "El sendero es largo."),
            ("mochila", "mochila", "Eu levo a mochila.", "Llevo la mochila."),
            ("pôr do sol", "atardecer", "O pôr do sol é lindo.", "El atardecer es lindo."),
            ("amanhecer", "amanecer", "Vamos sair ao amanhecer.", "Vamos a salir al amanecer."),
            ("carro", "auto", "O carro está na garagem.", "El auto está en el garaje."),
            ("gasolina", "nafta", "Falta gasolina.", "Falta nafta."),
            ("lago", "lago", "Vamos até o lago.", "Vamos hasta el lago."),
            ("vista", "vista", "A vista é incrível.", "La vista es increíble."),
        ],
        dialogue=D(
            ("No domingo a gente faz um passeio?", "¿El domingo hacemos un paseo?"),
            ("Vamos! Para a praia ou para a montanha?", "¡Vamos! ¿A la playa o a la montaña?"),
            ("Montanha. Eu levo a mochila e o piquenique.", "Montaña. Yo llevo la mochila y el picnic."),
            ("Vamos de carro. Falta gasolina.", "Vamos en auto. Falta nafta."),
            ("Eu passo aí ao amanhecer.", "Paso por tu casa al amanecer."),
        ),
        quiz=[
            Q("Mochila es…", "la mochila", "el ascensor", "el sueldo", "el vuelto"),
            Q("Falta gasolina quiere decir…", "falta nafta", "falta pan", "está cerrado", "llegué tarde"),
            Q("Passeio es…", "un paseo", "una factura", "un dolor", "un permiso"),
            Q("Pôr do sol es…", "el atardecer", "el desayuno", "el andén", "el jefe"),
            Q("Amanhecer significa…", "amanecer", "anochecer", "almorzar", "bailar"),
        ],
    ),
]

# --- B1 ---------------------------------------------------------------------

B1_SPECS = [
    L(
        "Unir ideas",
        "Entonces, mientras, sin embargo, quizás.",
        [
            "Então concluye: estou cansado, então vou dormir. Enquanto superpone dos acciones: eu estudo enquanto você cozinha. Porém contrasta y es más formal que mas.",
            "Aliás agrega algo que se acaba de acordar. Ainda indica que algo no cambió y já que algo ya pasó: ainda não terminei, já comi. Talvez abre la duda y pide subjuntivo: talvez eu vá. Logo es «pronto», assim es «así» y mesmo es «mismo» o «de verdad».",
        ],
        [
            ("então", "entonces; así que", "Então vamos embora.", "Entonces vámonos."),
            ("enquanto", "mientras", "Eu estudo enquanto você cozinha.", "Yo estudio mientras vos cocinás."),
            ("porém", "sin embargo; pero", "Gostei, porém achei caro.", "Me gustó, sin embargo me pareció caro."),
            ("aliás", "por cierto; de hecho", "Aliás, você viu a Ana?", "Por cierto, ¿viste a Ana?"),
            ("ainda", "todavía; aún", "Ainda não terminei.", "Todavía no terminé."),
            ("já", "ya", "Já comi, obrigado.", "Ya comí, gracias."),
            ("talvez", "quizás", "Talvez eu vá amanhã.", "Quizás vaya mañana."),
            ("logo", "pronto; enseguida", "Eu volto logo.", "Vuelvo enseguida."),
            ("assim", "así", "Faça assim.", "Hacelo así."),
            ("mesmo", "mismo; de verdad", "É o mesmo preço.", "Es el mismo precio."),
        ],
        quiz=[
            Q("Enquanto significa…", "mientras", "nunca", "debajo", "juntos"),
            Q("Ainda não terminei quiere decir…", "todavía no terminé", "ya terminé", "terminé ayer", "nunca terminé"),
            Q("Talvez expresa…", "duda; quizás", "orden", "gratitud", "precio"),
            Q("Porém equivale a…", "sin embargo", "así que", "mientras", "después"),
            Q("Logo puede significar…", "pronto", "ayer", "mucho", "nunca"),
        ],
    ),
    L(
        "El viaje",
        "Reserva, aduana, cambio y seguro.",
        [
            "La viagem y la reserva se preparan antes. La hospedagem es el alojamiento. El guia acompaña, y la lembrança es lo que traés de regreso.",
            "El câmbio cambia la moneda. Fronteira, embarque y alfândega son el cruce. El seguro cubre lo inesperado. Al viajar preguntá siempre cuánto sale el câmbio del día.",
        ],
        [
            ("viagem", "viaje", "A viagem foi ótima.", "El viaje fue excelente."),
            ("reserva", "reserva", "Fiz a reserva do hotel.", "Hice la reserva del hotel."),
            ("hospedagem", "alojamiento", "A hospedagem é barata.", "El alojamiento es barato."),
            ("guia", "guía", "O guia explicou tudo.", "El guía explicó todo."),
            ("lembrança", "recuerdo; souvenir", "Comprei uma lembrança.", "Compré un souvenir."),
            ("câmbio", "cambio de moneda", "O câmbio está alto.", "El tipo de cambio está alto."),
            ("fronteira", "frontera", "A fronteira fica perto.", "La frontera queda cerca."),
            ("embarque", "embarque", "O embarque é às seis.", "El embarque es a las seis."),
            ("alfândega", "aduana", "Passamos pela alfândega.", "Pasamos por la aduana."),
            ("seguro", "seguro", "Fiz um seguro de viagem.", "Hice un seguro de viaje."),
        ],
    ),
    L(
        "Cuando algo falla",
        "Falla, culpa, reclamo y reembolso.",
        [
            "Un problema pide una solução. Resolver es el verbo que lo cierra. El defeito y el dano nombran el desperfecto.",
            "La culpa no siempre es tuya. La reclamação y el reembolso se piden con paciência. Si es urgente, decilo claro: é urgente.",
        ],
        [
            ("problema", "problema", "Temos um problema.", "Tenemos un problema."),
            ("solução", "solución", "Preciso de uma solução.", "Necesito una solución."),
            ("defeito", "falla; defecto", "O aparelho tem defeito.", "El aparato tiene una falla."),
            ("dano", "daño", "O dano foi grande.", "El daño fue grande."),
            ("culpa", "culpa", "A culpa não é sua.", "La culpa no es tuya."),
            ("reclamação", "queja; reclamo", "Fiz uma reclamação.", "Hice un reclamo."),
            ("reembolso", "reembolso", "Quero o reembolso.", "Quiero el reembolso."),
            ("urgente", "urgente", "É um caso urgente.", "Es un caso urgente."),
            ("paciência", "paciencia", "Tenha paciência.", "Tené paciencia."),
            ("resolver", "resolver", "Vamos resolver isso.", "Vamos a resolver esto."),
        ],
        dialogue=D(
            ("Boa tarde. Tenho um problema com o meu pedido.", "Buenas tardes. Tengo un problema con mi pedido."),
            ("Qual é o problema?", "¿Cuál es el problema?"),
            ("O aparelho chegou com defeito. Quero o reembolso.", "El aparato llegó con una falla. Quiero el reembolso."),
            ("Desculpe. Vamos resolver isso hoje.", "Disculpe. Lo vamos a resolver hoy."),
            ("Obrigado pela paciência.", "Gracias por la paciencia."),
        ),
    ),
    L(
        "El proyecto",
        "Plazo, meta, equipo y resultado.",
        [
            "Projeto, prazo y meta ordenan el trabajo. La equipe cumple, el cargo define el rol. La prioridade dice qué va primero.",
            "El orçamento limita. Delegar alivia. El resultado cierra el ciclo y, si todo va bien, llega el aumento de sueldo.",
        ],
        [
            ("projeto", "proyecto", "O projeto começa hoje.", "El proyecto empieza hoy."),
            ("prazo", "plazo", "O prazo termina sexta.", "El plazo termina el viernes."),
            ("meta", "meta", "Batemos a meta do mês.", "Alcanzamos la meta del mes."),
            ("equipe", "equipo (de trabajo)", "Minha equipe é ótima.", "Mi equipo es excelente."),
            ("cargo", "cargo", "Ele ocupa um cargo importante.", "Él ocupa un cargo importante."),
            ("prioridade", "prioridad", "Qual é a prioridade?", "¿Cuál es la prioridad?"),
            ("resultado", "resultado", "O resultado saiu hoje.", "El resultado salió hoy."),
            ("orçamento", "presupuesto", "O orçamento é limitado.", "El presupuesto es limitado."),
            ("delegar", "delegar", "Preciso delegar tarefas.", "Necesito delegar tareas."),
            ("aumento", "aumento", "Pedi um aumento.", "Pedí un aumento."),
        ],
    ),
    L(
        "En la cocina",
        "Receta, alergia y los verbos del fuego.",
        [
            "Receita, ingrediente y alergia evitan un mal plato. Forno, panela y frigideira son los utensilios.",
            "Ferver, fritar y misturar son los gestos. El tempero es lo que da el sabor final. En Brasil no se dice «receta» solo para cocinar: también es la receta médica.",
        ],
        [
            ("receita", "receta", "A receita é fácil.", "La receta es fácil."),
            ("ingrediente", "ingrediente", "Falta um ingrediente.", "Falta un ingrediente."),
            ("alergia", "alergia", "Tenho alergia a amendoim.", "Tengo alergia al maní."),
            ("forno", "horno", "O forno está quente.", "El horno está caliente."),
            ("panela", "olla", "A panela está no fogo.", "La olla está en el fuego."),
            ("frigideira", "sartén", "Use a frigideira grande.", "Usá la sartén grande."),
            ("ferver", "hervir", "A água começou a ferver.", "El agua empezó a hervir."),
            ("fritar", "freír", "Vou fritar os ovos.", "Voy a freír los huevos."),
            ("misturar", "mezclar", "Misture tudo bem.", "Mezclá todo bien."),
            ("tempero", "condimento; aderezo", "O tempero está perfeito.", "El condimento está perfecto."),
        ],
    ),
    L(
        "Salud",
        "Fiebre, turno, análisis e informe.",
        [
            "Saúde se cuida. Febre y tosse son el aviso. El sintoma se cuenta en la consulta.",
            "Si hace falta llega la ambulância o una internação. El exame y el laudo dan datos. La pressão es una de las primeras cosas que miden.",
        ],
        [
            ("saúde", "salud", "Saúde é o mais importante.", "La salud es lo más importante."),
            ("febre", "fiebre", "Estou com febre.", "Tengo fiebre."),
            ("tosse", "tos", "Tenho tosse há três dias.", "Tengo tos hace tres días."),
            ("consulta", "consulta; turno médico", "Tenho consulta amanhã.", "Tengo turno mañana."),
            ("sintoma", "síntoma", "Qual é o sintoma?", "¿Cuál es el síntoma?"),
            ("internação", "internación", "Foi preciso uma internação.", "Hizo falta una internación."),
            ("ambulância", "ambulancia", "Chame a ambulância!", "¡Llamá a la ambulancia!"),
            ("exame", "análisis; examen", "O exame é de sangue.", "El análisis es de sangre."),
            ("laudo", "informe médico", "O laudo ficou pronto.", "El informe quedó listo."),
            ("pressão", "presión", "Minha pressão está alta.", "Mi presión está alta."),
        ],
        dialogue=D(
            ("Bom dia, doutor. Estou com febre e tosse.", "Buen día, doctor. Tengo fiebre y tos."),
            ("Há quanto tempo?", "¿Hace cuánto?"),
            ("Há três dias.", "Hace tres días."),
            ("Vou pedir um exame de sangue.", "Voy a pedir un análisis de sangre."),
            ("Quando fica pronto o laudo?", "¿Cuándo está listo el informe?"),
        ),
    ),
    L(
        "El ambiente",
        "Basura, plástico y la crecida.",
        [
            "Meio ambiente, poluição, reciclar y economizar arman la base. Lixo, plástico y vidro son el día a día.",
            "Desperdício y energia se miden. La enchente es la inundación cuando llueve de más. Reciclar es separar y economizar es gastar menos.",
        ],
        [
            ("meio ambiente", "medio ambiente", "Cuidar do meio ambiente é urgente.", "Cuidar el medio ambiente es urgente."),
            ("poluição", "contaminación", "A poluição aumentou.", "La contaminación aumentó."),
            ("reciclar", "reciclar", "Eu reciclo papel.", "Reciclo papel."),
            ("economizar", "ahorrar", "Vamos economizar água.", "Vamos a ahorrar agua."),
            ("lixo", "basura", "Jogue no lixo.", "Tirá a la basura."),
            ("plástico", "plástico", "Evite o plástico.", "Evitá el plástico."),
            ("vidro", "vidrio", "O vidro é reciclável.", "El vidrio es reciclable."),
            ("desperdício", "desperdicio", "Que desperdício de comida!", "¡Qué desperdicio de comida!"),
            ("energia", "energía", "Energia solar é o futuro.", "La energía solar es el futuro."),
            ("enchente", "inundación", "A enchente destruiu casas.", "La inundación destruyó casas."),
        ],
    ),
    L(
        "Verbos de decisión",
        "Esperar, parecer, lograr, olvidar.",
        [
            "Esperar sirve para esperar algo y también para tener esperanza. Parecer opina. Virar cambia de estado: ele virou professor.",
            "Conseguir logra. Esquecer pierde y lembrar recupera. Prometer ata. Escolher corta. Evitar esquiva. Aconselhar recomienda. Casi todos van con un infinitivo.",
        ],
        [
            ("esperar", "esperar; tener la esperanza", "Espero que dê certo.", "Espero que salga bien."),
            ("parecer", "parecer", "Parece que vai chover.", "Parece que va a llover."),
            ("virar", "volverse; convertirse", "Ele virou professor.", "Él se hizo profesor."),
            ("conseguir", "lograr", "Consegui o emprego.", "Conseguí el trabajo."),
            ("esquecer", "olvidar", "Esqueci a chave.", "Me olvidé la llave."),
            ("lembrar", "recordar", "Eu me lembro de você.", "Me acuerdo de vos."),
            ("prometer", "prometer", "Eu prometo ligar.", "Prometo llamar."),
            ("escolher", "elegir", "Escolha uma cor.", "Elegí un color."),
            ("evitar", "evitar", "Evite o trânsito.", "Evitá el tránsito."),
            ("aconselhar", "aconsejar", "Eu aconselho esperar.", "Aconsejo esperar."),
        ],
    ),
    L(
        "Opiniones y acuerdos",
        "Estoy de acuerdo, tenés razón, no coincido.",
        [
            "La opinião se da con achar: eu acho que sim. Concordar y discordar marcan el acuerdo o el desacuerdo. Siempre llevan com: concordo com você.",
            "Certo y errado juzgan. Verdade y mentira separan lo cierto de lo falso. Você tem razão es la forma más natural de dar la razón. Sugerir propone.",
        ],
        [
            ("opinião", "opinión", "Na minha opinião, está certo.", "En mi opinión, está bien."),
            ("concordar", "estar de acuerdo", "Eu concordo com você.", "Estoy de acuerdo con vos."),
            ("discordar", "discrepar", "Eu discordo dele.", "No coincido con él."),
            ("achar", "opinar; encontrar", "Eu acho que sim.", "Creo que sí."),
            ("certo", "correcto; cierto", "Está certo.", "Está bien."),
            ("errado", "equivocado; incorrecto", "A resposta está errada.", "La respuesta está mal."),
            ("verdade", "verdad", "É verdade?", "¿Es verdad?"),
            ("mentira", "mentira", "Isso é mentira.", "Eso es mentira."),
            ("razão", "razón", "Você tem razão.", "Tenés razón."),
            ("sugerir", "sugerir", "Eu sugiro um café.", "Sugiero un café."),
        ],
        quiz=[
            Q("Você tem razão significa…", "tenés razón", "estás cansado", "vas tarde", "tenés hambre"),
            Q("Concordar es…", "estar de acuerdo", "discutir", "olvidar", "viajar"),
            Q("Eu acho que sim es…", "creo que sí", "lo encontré", "no sé", "nunca"),
            Q("Mentira es…", "mentira", "verdad", "razón", "opinión"),
            Q("Certo y errado son…", "correcto e incorrecto", "caro y barato", "frío y caliente", "dulce y salado"),
        ],
    ),
    L(
        "Medios y tecnología",
        "Celular, contraseña, pantalla y archivos.",
        [
            "Internet, celular y aplicativo son la vida diaria. La senha protege, la tela se rompe y la bateria se acaba.",
            "Carregar es cargar el celular, y también llevar peso. Baixar es descargar. La rede sostiene todo y el arquivo se guarda. Fijate que en Brasil se dice celular y no móvil.",
        ],
        [
            ("internet", "internet", "A internet caiu.", "Se cayó internet."),
            ("celular", "celular", "Meu celular quebrou.", "Mi celular se rompió."),
            ("aplicativo", "aplicación", "Baixe o aplicativo.", "Bajá la aplicación."),
            ("senha", "contraseña", "Esqueci a senha.", "Me olvidé la contraseña."),
            ("tela", "pantalla", "A tela está rachada.", "La pantalla está rota."),
            ("bateria", "batería", "A bateria acabou.", "Se acabó la batería."),
            ("carregar", "cargar; llevar", "Preciso carregar o celular.", "Tengo que cargar el celular."),
            ("baixar", "bajar; descargar", "Vou baixar o arquivo.", "Voy a descargar el archivo."),
            ("rede", "red", "A rede está instável.", "La red está inestable."),
            ("arquivo", "archivo", "Salve o arquivo.", "Guardá el archivo."),
        ],
    ),
    L(
        "Cultura y fiestas",
        "Carnaval, fútbol, asado y comparsas.",
        [
            "El carnaval y el samba son marca de Brasil. El feriado se espera todo el año. La festa junina es la fiesta de junio con comidas típicas.",
            "El futebol es pasión, y la torcida es la hinchada. El churrasco es el asado brasileño. La cachaça es el aguardiente con el que se hace la caipirinha. Un bloco es una comparsa callejera.",
        ],
        [
            ("carnaval", "carnaval", "O carnaval é em fevereiro.", "El carnaval es en febrero."),
            ("festa", "fiesta", "A festa foi ótima.", "La fiesta estuvo genial."),
            ("feriado", "feriado", "Segunda é feriado.", "El lunes es feriado."),
            ("samba", "samba", "Eu aprendi a dançar samba.", "Aprendí a bailar samba."),
            ("futebol", "fútbol", "O futebol é paixão nacional.", "El fútbol es pasión nacional."),
            ("churrasco", "asado", "Domingo tem churrasco.", "El domingo hay asado."),
            ("cachaça", "cachaça (aguardiente de caña)", "A caipirinha leva cachaça.", "La caipiriña lleva cachaça."),
            ("torcida", "hinchada", "A torcida cantou o jogo todo.", "La hinchada cantó todo el partido."),
            ("bloco", "comparsa; bloque", "O bloco sai às dez.", "La comparsa sale a las diez."),
        ],
        quiz=[
            Q("Churrasco es…", "asado", "ensalada", "postre", "sopa"),
            Q("Torcida significa…", "hinchada", "lluvia", "boleto", "queso"),
            Q("La cachaça se usa en…", "la caipirinha", "el café", "el jugo", "el pan"),
            Q("Feriado es…", "día no laborable", "una fiesta privada", "un viaje", "un examen"),
            Q("Bloco es…", "una comparsa", "un edificio", "una tarea", "un mapa"),
        ],
    ),
    L(
        "Educación",
        "Curso, clase, examen y título.",
        [
            "Curso, aula y matéria forman el estudio. La prova mide y la nota resume el resultado. En Brasil se usa de cero a diez.",
            "La faculdade es la universidad. El professor enseña. El diploma llega al final, y se festeja con la formatura.",
        ],
        [
            ("curso", "curso", "Faço um curso de inglês.", "Hago un curso de inglés."),
            ("aula", "clase", "A aula começa às oito.", "La clase empieza a las ocho."),
            ("prova", "examen; prueba", "Amanhã tenho prova.", "Mañana tengo examen."),
            ("nota", "nota; calificación", "Tirei uma nota boa.", "Saqué una buena nota."),
            ("faculdade", "facultad; universidad", "Estudo na faculdade.", "Estudio en la facultad."),
            ("professor", "profesor", "O professor explicou bem.", "El profesor explicó bien."),
            ("diploma", "título", "O diploma chegou.", "Llegó el título."),
            ("matéria", "materia", "Qual é a sua matéria preferida?", "¿Cuál es tu materia preferida?"),
            ("formatura", "graduación", "A formatura é em dezembro.", "La graduación es en diciembre."),
        ],
    ),
]

# --- B2 ---------------------------------------------------------------------

B2_SPECS = [
    L(
        "Argumentar",
        "Defender, criticar, probar y concluir.",
        [
            "Un argumento se defiende y se critica. Para sostenerlo hace falta provar con evidência. Una hipótese todavía no está probada.",
            "Una contradição debilita la posición. Concluir cierra el razonamiento. Do meu ponto de vista abre una opinión personal y suena natural en el debate.",
        ],
        [
            ("argumento", "argumento", "O argumento é convincente.", "El argumento es convincente."),
            ("defender", "defender", "Ele defende a sua ideia.", "Él defiende su idea."),
            ("criticar", "criticar", "É fácil criticar.", "Es fácil criticar."),
            ("provar", "probar; demostrar", "Preciso provar isso.", "Tengo que probar esto."),
            ("concluir", "concluir", "Podemos concluir que sim.", "Podemos concluir que sí."),
            ("hipótese", "hipótesis", "Essa é só uma hipótese.", "Esa es solo una hipótesis."),
            ("evidência", "evidencia", "Não há evidência disso.", "No hay evidencia de eso."),
            ("contradição", "contradicción", "Há uma contradição aqui.", "Hay una contradicción acá."),
            ("ponto de vista", "punto de vista", "Do meu ponto de vista, é injusto.", "Desde mi punto de vista, es injusto."),
        ],
        quiz=[
            Q("Provar significa…", "probar; demostrar", "perder", "pagar", "pedir"),
            Q("Una hipótese es…", "una suposición sin probar", "un precio", "una fiesta", "una ruta"),
            Q("Do meu ponto de vista es…", "desde mi punto de vista", "a mi derecha", "por mi culpa", "en mi casa"),
            Q("Concluir es…", "cerrar un razonamiento", "empezar un viaje", "pedir un préstamo", "bajar un archivo"),
            Q("Evidência es…", "evidencia", "paciencia", "inflación", "ingrediente"),
        ],
    ),
    L(
        "Economía",
        "Inflación, impuestos, préstamos e inversión.",
        [
            "La economia crece o entra en crise. La inflação sube los precios y el imposto sale del bolsillo de todos.",
            "Un empréstimo se paga con juros. Quien tiene una dívida debe plata. Investir implica un riesgo, y el lucro es la ganancia. En Brasil juros es siempre plural.",
        ],
        [
            ("economia", "economía", "A economia está crescendo.", "La economía está creciendo."),
            ("inflação", "inflación", "A inflação subiu.", "La inflación subió."),
            ("imposto", "impuesto", "O imposto é alto.", "El impuesto es alto."),
            ("empréstimo", "préstamo", "Pedi um empréstimo.", "Pedí un préstamo."),
            ("juros", "intereses", "Os juros são altos.", "Los intereses son altos."),
            ("investir", "invertir", "Quero investir em ações.", "Quiero invertir en acciones."),
            ("lucro", "ganancia", "A empresa teve lucro.", "La empresa tuvo ganancias."),
            ("dívida", "deuda", "A dívida cresceu.", "La deuda creció."),
            ("crise", "crisis", "O país vive uma crise.", "El país vive una crisis."),
        ],
    ),
    L(
        "Política y ciudadanía",
        "Gobierno, elección, ley y derechos.",
        [
            "El governo propone y la lei se aprueba. La eleição se vota con un voto, que en Brasil es obligatorio. Un candidato pertenece a un partido.",
            "El cidadão tiene direitos y deveres. El prefeito es el intendente de la ciudad. Direito es «derecho» y también «recto», como en ir direto.",
        ],
        [
            ("governo", "gobierno", "O governo anunciou medidas.", "El gobierno anunció medidas."),
            ("eleição", "elección", "A eleição é em outubro.", "La elección es en octubre."),
            ("voto", "voto", "O voto é obrigatório.", "El voto es obligatorio."),
            ("candidato", "candidato", "O candidato falou na TV.", "El candidato habló en la tele."),
            ("partido", "partido político", "Ele mudou de partido.", "Él cambió de partido."),
            ("lei", "ley", "A lei foi aprovada.", "La ley fue aprobada."),
            ("direito", "derecho", "Todos têm direito à saúde.", "Todos tienen derecho a la salud."),
            ("cidadão", "ciudadano", "Cada cidadão tem deveres.", "Cada ciudadano tiene deberes."),
            ("prefeito", "intendente; alcalde", "O prefeito inaugurou a ponte.", "El intendente inauguró el puente."),
        ],
    ),
    L(
        "Trabajo y carrera",
        "Currículum, entrevista, vacante y jubilación.",
        [
            "Una carreira empieza con un currículo y una entrevista. Hay una vaga y alguien se contrata, o se demite.",
            "La experiência cuenta y cada puesto trae un desafio. Al final de la vida laboral llega la aposentadoria. Fijate que contratar y demitir son verbos del que decide.",
        ],
        [
            ("carreira", "carrera", "Ela tem uma carreira longa.", "Ella tiene una carrera larga."),
            ("currículo", "currículum", "Envie seu currículo.", "Mandá tu currículum."),
            ("entrevista", "entrevista", "A entrevista é amanhã.", "La entrevista es mañana."),
            ("vaga", "vacante; lugar", "Abriram uma vaga.", "Abrieron una vacante."),
            ("contratar", "contratar", "Vamos contratar dois analistas.", "Vamos a contratar a dos analistas."),
            ("demitir", "despedir", "A empresa vai demitir vinte pessoas.", "La empresa va a despedir a veinte personas."),
            ("experiência", "experiencia", "Tenho experiência na área.", "Tengo experiencia en el área."),
            ("desafio", "desafío", "É um grande desafio.", "Es un gran desafío."),
            ("aposentadoria", "jubilación", "A aposentadoria é aos sessenta e cinco.", "La jubilación es a los sesenta y cinco."),
        ],
        dialogue=D(
            ("Boa tarde. Vim para a entrevista da vaga.", "Buenas tardes. Vine para la entrevista por la vacante."),
            ("Boa tarde. Você trouxe o currículo?", "Buenas tardes. ¿Trajiste el currículum?"),
            ("Trouxe. Tenho cinco anos de experiência.", "Lo traje. Tengo cinco años de experiencia."),
            ("Ótimo. Qual é o maior desafio da sua carreira?", "Excelente. ¿Cuál es el mayor desafío de tu carrera?"),
            ("Liderar uma equipe nova.", "Liderar un equipo nuevo."),
        ),
    ),
    L(
        "Ciencia y tecnología",
        "Investigación, descubrimientos y datos.",
        [
            "La ciência avanza con pesquisa. Una descoberta cambia lo que se sabe y la inovação lleva ese conocimiento a la vida diaria.",
            "El cientista diseña un experimento y junta dados. El algoritmo procesa esos datos. Pesquisa también significa «encuesta». Según el contexto vas a entender cuál.",
        ],
        [
            ("ciência", "ciencia", "A ciência avança rápido.", "La ciencia avanza rápido."),
            ("pesquisa", "investigación; encuesta", "A pesquisa durou dois anos.", "La investigación duró dos años."),
            ("descoberta", "descubrimiento", "Foi uma grande descoberta.", "Fue un gran descubrimiento."),
            ("inovação", "innovación", "A inovação gera emprego.", "La innovación genera empleo."),
            ("tecnologia", "tecnología", "A tecnologia mudou tudo.", "La tecnología cambió todo."),
            ("cientista", "científico", "A cientista ganhou um prêmio.", "La científica ganó un premio."),
            ("experimento", "experimento", "O experimento deu certo.", "El experimento salió bien."),
            ("dados", "datos", "Os dados são confiáveis.", "Los datos son confiables."),
            ("algoritmo", "algoritmo", "O algoritmo escolhe o vídeo.", "El algoritmo elige el video."),
        ],
    ),
    L(
        "Salud y bienestar",
        "Sueño, estrés, ejercicio y hábitos.",
        [
            "El bem-estar depende de varios factores: sono, dieta y exercício. El estresse y la ansiedade lo afectan.",
            "La terapia ayuda. Descansar también. Un buen hábito se construye de a poco. Estresse se escribe con doble s y una e final: es la forma portuguesa de «estrés».",
        ],
        [
            ("bem-estar", "bienestar", "O bem-estar vem em primeiro lugar.", "El bienestar va primero."),
            ("sono", "sueño", "Estou com muito sono.", "Tengo mucho sueño."),
            ("estresse", "estrés", "O estresse faz mal.", "El estrés hace mal."),
            ("dieta", "dieta", "Estou fazendo dieta.", "Estoy haciendo dieta."),
            ("exercício", "ejercicio", "Faço exercício toda manhã.", "Hago ejercicio todas las mañanas."),
            ("ansiedade", "ansiedad", "A ansiedade atrapalha o sono.", "La ansiedad arruina el sueño."),
            ("terapia", "terapia", "Faço terapia há um ano.", "Hago terapia hace un año."),
            ("descansar", "descansar", "Você precisa descansar.", "Tenés que descansar."),
            ("hábito", "hábito", "Dormir cedo é um bom hábito.", "Dormir temprano es un buen hábito."),
        ],
    ),
    L(
        "Medios y redes",
        "Noticias, titulares, seguidores y rumores.",
        [
            "La notícia sale en el jornal, en una reportagem o en una manchete. La mídia reúne a todos esos canales.",
            "En las redes se ganan seguidores, se curte y se compartilha. Pero cuidado con el boato, el rumor que corre más rápido que la verdad.",
        ],
        [
            ("notícia", "noticia", "Li uma notícia curiosa.", "Leí una noticia curiosa."),
            ("jornal", "diario; periódico", "O jornal chega cedo.", "El diario llega temprano."),
            ("reportagem", "reportaje", "A reportagem é longa.", "El reportaje es largo."),
            ("manchete", "titular", "A manchete chamou atenção.", "El titular llamó la atención."),
            ("seguidor", "seguidor", "Ela tem mil seguidores.", "Ella tiene mil seguidores."),
            ("curtir", "dar me gusta; disfrutar", "Eu curto esse cantor.", "Me gusta ese cantante."),
            ("compartilhar", "compartir", "Vou compartilhar o link.", "Voy a compartir el link."),
            ("boato", "rumor", "Isso é só um boato.", "Eso es solo un rumor."),
            ("mídia", "medios (de comunicación)", "A mídia cobriu o caso.", "Los medios cubrieron el caso."),
        ],
    ),
    L(
        "Arte y literatura",
        "Novela, poema, pintura y teatro.",
        [
            "El romance es una novela larga. El poema es verso. El autor escribe y el leitor lee. El estilo es la huella de cada uno.",
            "La pintura se muestra en una exposição. El teatro es la obra en vivo. La palabra obra sirve tanto para una obra de arte como para una construcción.",
        ],
        [
            ("romance", "novela", "Este romance é emocionante.", "Esta novela es emocionante."),
            ("poema", "poema", "Ela escreveu um poema.", "Ella escribió un poema."),
            ("autor", "autor", "O autor assinou os livros.", "El autor firmó los libros."),
            ("leitor", "lector", "Sou um leitor curioso.", "Soy un lector curioso."),
            ("pintura", "pintura", "A pintura é a óleo.", "La pintura es al óleo."),
            ("exposição", "exposición", "A exposição abre sábado.", "La exposición abre el sábado."),
            ("teatro", "teatro", "Vamos ao teatro hoje.", "Vamos al teatro hoy."),
            ("obra", "obra", "Esta obra é famosa.", "Esta obra es famosa."),
            ("estilo", "estilo", "Gosto do estilo dele.", "Me gusta su estilo."),
        ],
    ),
    L(
        "Emociones",
        "Saudade, celos, orgullo y alegría.",
        [
            "Saudade es la palabra más famosa del portugués: una mezcla de añoranza y nostalgia. Se usa con ter: tenho saudade de você.",
            "Ciúme, confiança, vergonha, orgulho, alegria, tristeza y raiva completan el repertorio emocional. Con raiva se usa ficar: fiquei com raiva.",
        ],
        [
            ("saudade", "añoranza; nostalgia", "Tenho saudade de casa.", "Extraño mi casa."),
            ("ciúme", "celos", "Ele sente ciúme.", "Él siente celos."),
            ("confiança", "confianza", "A confiança leva tempo.", "La confianza lleva tiempo."),
            ("vergonha", "vergüenza", "Que vergonha!", "¡Qué vergüenza!"),
            ("orgulho", "orgullo", "Tenho orgulho de você.", "Estoy orgulloso de vos."),
            ("alegria", "alegría", "A alegria é contagiosa.", "La alegría es contagiosa."),
            ("tristeza", "tristeza", "Senti muita tristeza.", "Sentí mucha tristeza."),
            ("raiva", "enojo; rabia", "Fiquei com raiva.", "Me enojé."),
        ],
        quiz=[
            Q("Saudade es…", "añoranza", "enojo", "vergüenza", "orgullo"),
            Q("Tenho saudade de você significa…", "te extraño", "te debo", "te escucho", "te llamo"),
            Q("Raiva es…", "enojo", "alegría", "celos", "confianza"),
            Q("Vergonha es…", "vergüenza", "confianza", "tristeza", "paciencia"),
            Q("Orgulho es…", "orgullo", "orden", "oficio", "olvido"),
        ],
    ),
    L(
        "Sociedad y ciudad",
        "Tránsito, vivienda, seguridad y población.",
        [
            "La sociedade cambia y la desigualdade preocupa. El trânsito de las grandes ciudades es famoso. La moradia y la segurança son derechos básicos.",
            "Una comunidade se organiza. La população crece. El saneamento es el agua potable y las cloacas. Son temas que vas a leer todo el tiempo en el diario.",
        ],
        [
            ("sociedade", "sociedad", "A sociedade está mudando.", "La sociedad está cambiando."),
            ("desigualdade", "desigualdad", "A desigualdade preocupa.", "La desigualdad preocupa."),
            ("trânsito", "tránsito", "O trânsito está parado.", "El tránsito está parado."),
            ("moradia", "vivienda", "Moradia é um direito.", "La vivienda es un derecho."),
            ("segurança", "seguridad", "A segurança melhorou.", "La seguridad mejoró."),
            ("comunidade", "comunidad", "A comunidade se organizou.", "La comunidad se organizó."),
            ("população", "población", "A população cresceu.", "La población creció."),
            ("saneamento", "saneamiento", "Falta saneamento básico.", "Falta saneamiento básico."),
        ],
    ),
    L(
        "Expresiones y jerga",
        "Legal, beleza, valeu: el portugués de todos los días.",
        [
            "Legal es «bueno, genial» y no tiene nada que ver con lo legal de la ley. Beleza es un «dale» o un «todo bien». Valeu es el «gracias» de confianza.",
            "Cara es «tipo» o «che». Bacana es «copado». Pois é admite que el otro tiene razón. Tá es la forma corta de está bom. Dar um jeito es arreglarse como se pueda.",
        ],
        [
            ("legal", "genial; bueno; legal", "O filme é muito legal.", "La película es muy buena."),
            ("beleza", "dale; todo bien", "Beleza, a gente se vê amanhã.", "Dale, nos vemos mañana."),
            ("valeu", "gracias (informal)", "Valeu pela ajuda!", "¡Gracias por la ayuda!"),
            ("cara", "che; tipo", "Cara, você viu isso?", "Che, ¿viste esto?"),
            ("bacana", "copado; lindo", "Que lugar bacana!", "¡Qué lugar copado!"),
            ("pois é", "y sí; es así", "Pois é, a vida é assim.", "Y sí, la vida es así."),
            ("tá", "dale; está bien", "Tá bom, eu vou.", "Dale, voy."),
            ("jeito", "manera; maña", "Vou dar um jeito.", "Voy a arreglármelas."),
        ],
        dialogue=D(
            ("Cara, você viu o jogo ontem?", "Che, ¿viste el partido ayer?"),
            ("Vi sim! Foi muito legal.", "¡Lo vi! Estuvo muy bueno."),
            ("Vamos assistir o próximo juntos?", "¿Vemos el próximo juntos?"),
            ("Beleza! Eu dou um jeito de sair cedo.", "¡Dale! Me las arreglo para salir temprano."),
            ("Valeu!", "¡Gracias!"),
        ),
        quiz=[
            Q("Valeu equivale a…", "gracias (informal)", "perdón", "hasta luego", "por favor"),
            Q("Beleza significa…", "dale; todo bien", "tristeza", "cuenta", "mapa"),
            Q("Legal en la calle significa…", "genial", "ilegal", "legal (de la ley)", "caro"),
            Q("Tá bom es…", "está bien", "tengo hambre", "hay frío", "me duele"),
            Q("Jeito es…", "manera", "jefe", "juego", "jugo"),
        ],
    ),
    L(
        "Registro formal e informal",
        "Señor, señora, estimado y cómo cerrar un correo.",
        [
            "Para dirigirte con respeto usás o senhor o a senhora: o senhor aceita café? En el correo formal se abre con prezado y se cierra con atenciosamente.",
            "El tono puede ser formal o informal. El tratamento y la gentileza dependen del contexto. Con amigos se usa você y, en algunas regiones, tu; en el trabajo, você con más cortesía, o senhor y senhora.",
        ],
        [
            ("senhor", "señor; usted (masc.)", "O senhor aceita café?", "¿El señor acepta café?"),
            ("senhora", "señora; usted (fem.)", "A senhora quer sentar?", "¿La señora quiere sentarse?"),
            ("prezado", "estimado", "Prezado cliente, obrigado.", "Estimado cliente, gracias."),
            ("atenciosamente", "atentamente", "Atenciosamente, Ana Souza.", "Atentamente, Ana Souza."),
            ("formal", "formal", "O e-mail é formal.", "El correo es formal."),
            ("informal", "informal", "Em casa o tom é informal.", "En casa el tono es informal."),
            ("tratamento", "trato; tratamiento", "Ele recebeu bom tratamento.", "Él recibió buen trato."),
            ("gentileza", "amabilidad", "Obrigado pela gentileza.", "Gracias por la amabilidad."),
        ],
    ),
]
