"""Arma data/lexicon.json y data/a1.json ... c2.json para el curso de portugués de Brasil."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from course_upper import D, L, Q, bind  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# Palabra, español, ejemplo, traducción (la pronunciación sale de pt_pron.py).
A1_SPECS = [
    L(
        "Sonidos del portugués",
        "Vocales nasales, lh, nh, ç, ch y la t y la d que se suavizan.",
        [
            "El portugués se escribe casi como se lee, pero tiene sonidos que el español no tiene. Las vocales nasales llevan tilde: pão, mãe, limão, coração. No pronuncies una «n» completa: dejá salir el aire también por la nariz.",
            "Lh suena como una «ly»: filho. Nh es nuestra ñ: manhã. La ç suena como una s: abraço. Ch suena como la «sh» rioplatense de «calle»: chuva. La j y la g delante de e o i suenan como la «y» de «yo». La r inicial y la rr suenan como una j española: Rio, carro.",
            "En casi todo Brasil, la t y la d delante de i (o de una e final) se suavizan: dia suena «dyia» y noite suena «noichi». La l al final de sílaba suena como una u: Brasil es «braziu».",
            "Las vocales e y o pueden ser abiertas (é, ó) o cerradas (ê, ô). Avó, con ó abierta, es la abuela; avô, con ô cerrada, es el abuelo. La o final sin acento suena casi u, y la e final suena casi i: obrigado es «obrigadu».",
            "En este curso la guía de pronunciación usa estas marcas: y = «y» de «yo», j = j española, sh = «sh» rioplatense, ch = «ch» de «chico», dy = d suave delante de i, ly = lh, ñ = nh y z = s entre vocales.",
        ],
        [
            ("pão", "pan", "Eu como pão com manteiga.", "Como pan con manteca."),
            ("mãe", "madre; mamá", "Minha mãe cozinha muito bem.", "Mi mamá cocina muy bien."),
            ("limão", "limón", "Um suco de limão, por favor.", "Un jugo de limón, por favor."),
            ("coração", "corazón", "Meu coração está feliz.", "Mi corazón está feliz."),
            ("filho", "hijo", "Meu filho tem dez anos.", "Mi hijo tiene diez años."),
            ("manhã", "mañana (parte del día)", "Eu estudo de manhã.", "Estudio por la mañana."),
            ("abraço", "abrazo", "Um abraço para você.", "Un abrazo para vos."),
            ("chuva", "lluvia", "A chuva já passou.", "La lluvia ya pasó."),
            ("dia", "día", "Hoje é um bom dia.", "Hoy es un buen día."),
            ("noite", "noche", "Boa noite e bons sonhos.", "Buenas noches y felices sueños."),
            ("Brasil", "Brasil", "Eu moro no Brasil.", "Vivo en Brasil."),
            ("avó", "abuela", "Minha avó faz bolo.", "Mi abuela hace torta."),
            ("avô", "abuelo", "Meu avô mora no Rio.", "Mi abuelo vive en Río."),
        ],
        quiz=[
            Q("¿Cómo suena la «lh» de filho?", "Como una «ly»", "Como una «k»", "Como una «s»", "Como una «u»"),
            Q("¿Qué marca la tilde en pão?", "Que la vocal es nasal", "Que es una pregunta", "Que la sílaba no se lee", "Que la palabra es plural"),
            Q("Brasil suena casi como…", "braziu", "brasir", "brasik", "brasich"),
            Q("¿Qué diferencia a avó de avô?", "La vocal abierta (abuela) y la cerrada (abuelo)", "Que una es plural", "Que una es de usted", "Nada, son iguales"),
            Q("La ç de abraço suena como…", "una s", "una k", "una ch", "una j"),
        ],
    ),
    L(
        "Saludos",
        "Oi, olá, gracias, perdón y los saludos del día.",
        [
            "Oi es el saludo de todos los días, con cualquiera. Olá es un poco más formal. Bom dia se usa hasta el mediodía, boa tarde hasta que anochece y boa noite sirve para saludar de noche y también para despedirse.",
            "Tchau y até logo cierran la charla. Obrigado lo dice un hombre y obrigada lo dice una mujer: concuerda con quien habla. Se responde con de nada.",
            "Por favor acompaña cada pedido. Desculpa es para pedir perdón con confianza. Com licença es el «permiso» para pasar o para interrumpir. Tudo bem es a la vez pregunta y respuesta: «¿todo bien?» «todo bien».",
        ],
        [
            ("oi", "hola", "Oi, tudo bem?", "Hola, ¿todo bien?"),
            ("olá", "hola (más formal)", "Olá, seja bem-vindo.", "Hola, bienvenido."),
            ("bom dia", "buen día", "Bom dia, dona Ana.", "Buen día, doña Ana."),
            ("boa tarde", "buenas tardes", "Boa tarde a todos.", "Buenas tardes a todos."),
            ("boa noite", "buenas noches", "Boa noite, até amanhã.", "Buenas noches, hasta mañana."),
            ("tchau", "chau", "Tchau, até logo!", "¡Chau, hasta luego!"),
            ("até logo", "hasta luego", "Até logo, Pedro.", "Hasta luego, Pedro."),
            ("obrigado", "gracias (lo dice un hombre)", "Muito obrigado pela ajuda.", "Muchas gracias por la ayuda."),
            ("de nada", "de nada", "De nada, foi um prazer.", "De nada, fue un placer."),
            ("por favor", "por favor", "Um café, por favor.", "Un café, por favor."),
            ("desculpa", "perdón (con confianza)", "Desculpa, eu não entendi.", "Perdón, no entendí."),
            ("com licença", "permiso; disculpe", "Com licença, onde fica o banheiro?", "Permiso, ¿dónde queda el baño?"),
            ("tudo bem", "todo bien; ¿cómo va?", "Tudo bem, e você?", "Todo bien, ¿y vos?"),
        ],
        dialogue=D(
            ("Oi, bom dia! Tudo bem?", "¡Hola, buen día! ¿Todo bien?"),
            ("Tudo bem, e você?", "Todo bien, ¿y vos?"),
            ("Tudo ótimo, obrigado.", "Todo excelente, gracias."),
            ("Com licença, preciso ir. Tchau!", "Permiso, tengo que irme. ¡Chau!"),
            ("Até logo!", "¡Hasta luego!"),
        ),
        quiz=[
            Q("¿Cómo saludás con confianza?", "Oi", "Conta", "Passagem", "Cardápio"),
            Q("¿Qué se responde a obrigado?", "De nada", "Tudo bem, sim", "Boa noite", "Pão"),
            Q("Com licença se usa para…", "pedir permiso o pasar", "pedir la cuenta", "decir el nombre", "contar hasta diez"),
            Q("Una mujer agradece diciendo…", "obrigada", "obrigado", "desculpa", "tchau"),
            Q("Até logo significa…", "hasta luego", "por favor", "tengo frío", "a la izquierda"),
        ],
    ),
    L(
        "Presentarse",
        "Yo, vos, él y las primeras frases con ser y chamar.",
        [
            "Eu, você, ele, ela, nós, eles son los pronombres que más vas a usar. En Brasil você sirve tanto para «vos» como para «usted». Vocês es «ustedes». El «vos» argentino no existe en Brasil, así que decí você.",
            "Ser en presente: eu sou, você é, ele é, nós somos, eles são. Eu sou argentino. Ela é professora. Para decir cómo te llamás se usa chamar: eu me chamo Lucas.",
            "Qual é o seu nome? pregunta el nombre. Onde você mora? pregunta dónde vivís. Eu moro em Buenos Aires. Falo espanhol e um pouco de português.",
        ],
        [
            ("eu", "yo", "Eu sou argentino.", "Yo soy argentino."),
            ("você", "vos; usted", "Você é brasileiro?", "¿Vos sos brasileño?"),
            ("ele", "él", "Ele é meu irmão.", "Él es mi hermano."),
            ("ela", "ella", "Ela é professora.", "Ella es profesora."),
            ("nós", "nosotros", "Nós moramos em Buenos Aires.", "Vivimos en Buenos Aires."),
            ("eles", "ellos", "Eles falam português.", "Ellos hablan portugués."),
            ("ser", "ser", "Eu sou estudante.", "Soy estudiante."),
            ("chamar", "llamar; llamarse (me chamo)", "Eu me chamo Lucas.", "Me llamo Lucas."),
            ("nome", "nombre", "Qual é o seu nome?", "¿Cuál es tu nombre?"),
            ("onde", "dónde", "Onde você mora?", "¿Dónde vivís?"),
            ("morar", "vivir (en un lugar)", "Eu moro em Córdoba.", "Vivo en Córdoba."),
            ("português", "portugués", "Eu falo um pouco de português.", "Hablo un poco de portugués."),
            ("espanhol", "español", "O espanhol é minha língua.", "El español es mi lengua."),
        ],
        dialogue=D(
            ("Oi, eu sou o Lucas. E você?", "Hola, yo soy Lucas. ¿Y vos?"),
            ("Eu me chamo Ana. Muito prazer.", "Me llamo Ana. Mucho gusto."),
            ("De onde você é?", "¿De dónde sos?"),
            ("Sou argentina. Moro em Buenos Aires.", "Soy argentina. Vivo en Buenos Aires."),
            ("Você fala português?", "¿Hablás portugués?"),
            ("Falo um pouco. Estou estudando.", "Hablo un poco. Estoy estudiando."),
        ),
    ),
    L(
        "Números",
        "Del uno al diez, las decenas útiles y las horas.",
        [
            "Um y dois cambian de género: um café, uma pizza, dois cafés, duas pizzas. Del tres al diez no cambian: três, quatro, cinco, seis, sete, oito, nove, dez.",
            "Vinte, cem y mil cubren las cantidades del día. Cem se usa para cien justo; si hay algo más, es cento: cento e dez. La moneda es el real, plural reais, y se dice quanto custa para preguntar el precio.",
            "Para la hora se dice são três horas, são seis horas. Con la una se dice é uma hora. Que horas são? pregunta la hora. Un detalle curioso: al dictar un teléfono, muchos brasileños dicen «meia» para el seis.",
        ],
        [
            ("um", "uno; un", "Eu tenho um irmão.", "Tengo un hermano."),
            ("dois", "dos", "Dois cafés, por favor.", "Dos cafés, por favor."),
            ("três", "tres", "São três horas.", "Son las tres."),
            ("quatro", "cuatro", "Quatro passagens, por favor.", "Cuatro boletos, por favor."),
            ("cinco", "cinco", "Faltam cinco minutos.", "Faltan cinco minutos."),
            ("seis", "seis", "Eu acordo às seis.", "Me levanto a las seis."),
            ("sete", "siete", "Às sete da noite.", "A las siete de la noche."),
            ("oito", "ocho", "O ônibus sai às oito.", "El colectivo sale a las ocho."),
            ("nove", "nueve", "São nove e meia.", "Son las nueve y media."),
            ("dez", "diez", "Eu tenho dez anos de estudo.", "Tengo diez años de estudio."),
            ("vinte", "veinte", "Eu tenho vinte anos.", "Tengo veinte años."),
            ("cem", "cien", "Cem gramas de queijo.", "Cien gramos de queso."),
            ("mil", "mil", "Custa mil reais.", "Cuesta mil reales."),
        ],
    ),
    L(
        "La familia",
        "Madre, padre, hermanos y los posesivos meu y minha.",
        [
            "Família junta a todos. Mãe y pai, irmão e irmã, filho e filha, avô e avó, tio e tia, marido e esposa, criança. Amigo y amiga son los de confianza; primo, el de la familia grande.",
            "El posesivo concuerda con lo que se posee, no con quien habla: meu pai, minha mãe, meus irmãos, minhas irmãs. En portugués se usa casi siempre el artículo: a minha mãe, o meu pai.",
            "Para contar cuántos son se dice eu tenho um irmão y eu tenho duas irmãs. Tenho viene de ter, que ya vas a ver en una clase siguiente.",
        ],
        [
            ("família", "familia", "Minha família é grande.", "Mi familia es grande."),
            ("pai", "padre; papá", "Meu pai trabalha muito.", "Mi papá trabaja mucho."),
            ("irmão", "hermano", "Eu tenho um irmão.", "Tengo un hermano."),
            ("irmã", "hermana", "Minha irmã estuda medicina.", "Mi hermana estudia medicina."),
            ("filha", "hija", "Minha filha se chama Ana.", "Mi hija se llama Ana."),
            ("tio", "tío", "Meu tio chega amanhã.", "Mi tío llega mañana."),
            ("tia", "tía", "Minha tia é muito simpática.", "Mi tía es muy simpática."),
            ("marido", "esposo; marido", "Meu marido é médico.", "Mi esposo es médico."),
            ("esposa", "esposa", "Minha esposa fala inglês.", "Mi esposa habla inglés."),
            ("criança", "niño; niña", "A criança dorme.", "El niño duerme."),
            ("amigo", "amigo", "Ele é meu melhor amigo.", "Él es mi mejor amigo."),
            ("amiga", "amiga", "Ela é minha amiga.", "Ella es mi amiga."),
            ("primo", "primo", "Meu primo mora em Lisboa.", "Mi primo vive en Lisboa."),
        ],
        reuse=["mãe", "filho", "avó", "avô"],
    ),
    L(
        "Comer y beber",
        "Arroz, porotos, carne y lo que pedís en la mesa.",
        [
            "En Brasil el plato de todos los días es arroz e feijão. El feijão son los porotos negros. Se acompaña con carne, frango o peixe, y de postre, fruta.",
            "Para tomar: água, suco, leite y café. Suco es el jugo de fruta. Café en Brasil es chico y fuerte, a menos que pidas café com leite.",
            "Comer y beber son los dos verbos de la mesa. Eu como pão. Eu bebo água. El queijo se come en pão de queijo, una masa de queso muy típica. Beber también es «tomar»: eu tomo café.",
        ],
        [
            ("água", "agua", "Um copo de água, por favor.", "Un vaso de agua, por favor."),
            ("arroz", "arroz", "Arroz e feijão todos os dias.", "Arroz y porotos todos los días."),
            ("feijão", "porotos negros", "O feijão está pronto.", "Los porotos están listos."),
            ("carne", "carne", "Eu gosto de carne.", "Me gusta la carne."),
            ("frango", "pollo", "Frango com arroz.", "Pollo con arroz."),
            ("peixe", "pescado", "O peixe está fresco.", "El pescado está fresco."),
            ("queijo", "queso", "Pão de queijo é delicioso.", "El pan de queso es riquísimo."),
            ("leite", "leche", "Um copo de leite frio.", "Un vaso de leche fría."),
            ("café", "café", "Eu tomo café de manhã.", "Tomo café por la mañana."),
            ("suco", "jugo", "Um suco de laranja, por favor.", "Un jugo de naranja, por favor."),
            ("fruta", "fruta", "Eu como fruta todos os dias.", "Como fruta todos los días."),
            ("comer", "comer", "Vamos comer juntos.", "Vamos a comer juntos."),
            ("beber", "beber; tomar", "Eu quero beber água.", "Quiero tomar agua."),
        ],
    ),
    L(
        "En el restaurante",
        "Menú, cuenta, precios y el verbo querer.",
        [
            "Al llegar a un restaurante se pide o cardápio. El garçom lo trae. Querer sirve para pedir: eu quero um suco. Más cortés: eu queria um suco, queria uma água.",
            "Gostoso es rico, sabroso, y se usa para la comida: o bolo está gostoso. Quanto custa pregunta el precio. Caro y barato dan la opinión sobre ese precio.",
            "Para cerrar se pide a conta. Pagar, comprar y dinheiro son el resto del vocabulario del gasto. Se paga en reais; el real se divide en centavos. Muchos lugares aceptan cartão y pix.",
        ],
        [
            ("restaurante", "restaurante", "Esse restaurante é muito bom.", "Este restaurante es muy bueno."),
            ("cardápio", "menú; carta", "Pode trazer o cardápio?", "¿Podés traer el menú?"),
            ("conta", "cuenta", "A conta, por favor.", "La cuenta, por favor."),
            ("garçom", "mozo", "O garçom é muito simpático.", "El mozo es muy simpático."),
            ("quanto", "cuánto", "Quanto custa?", "¿Cuánto cuesta?"),
            ("caro", "caro", "Este vinho é caro.", "Este vino es caro."),
            ("barato", "barato", "O almoço é barato.", "El almuerzo es barato."),
            ("real", "real (moneda de Brasil)", "Um café custa cinco reais.", "Un café cuesta cinco reales."),
            ("dinheiro", "dinero; plata", "Eu não tenho dinheiro.", "No tengo plata."),
            ("comprar", "comprar", "Eu quero comprar pão.", "Quiero comprar pan."),
            ("pagar", "pagar", "Posso pagar com cartão?", "¿Puedo pagar con tarjeta?"),
            ("gostoso", "rico; sabroso", "O bolo está muito gostoso.", "La torta está muy rica."),
            ("querer", "querer", "Eu quero um suco.", "Quiero un jugo."),
        ],
        dialogue=D(
            ("Boa noite. O cardápio, por favor.", "Buenas noches. El menú, por favor."),
            ("Claro. O que você quer beber?", "Claro. ¿Qué querés tomar?"),
            ("Um suco de laranja e uma água.", "Un jugo de naranja y un agua."),
            ("E para comer?", "¿Y para comer?"),
            ("Frango com arroz e feijão.", "Pollo con arroz y porotos."),
            ("A conta, por favor. Quanto é?", "La cuenta, por favor. ¿Cuánto es?"),
        ),
    ),
    L(
        "Días y horas",
        "Hoy, mañana, ayer y los días de la semana.",
        [
            "Hoje es hoy, amanhã es mañana (el día siguiente) y ontem es ayer. De manhã, de tarde y de noite dicen la parte del día.",
            "Los días de la semana en el habla común se acortan: segunda, terça, quarta, quinta, sexta. Se agrega -feira en lo formal: segunda-feira. Sábado y domingo no llevan -feira. No se escriben con mayúscula.",
            "Semana y hora cierran la clase. Que horas são? pregunta la hora. A que horas pregunta a qué hora pasa algo: o ônibus sai às oito.",
        ],
        [
            ("hoje", "hoy", "Hoje é segunda.", "Hoy es lunes."),
            ("amanhã", "mañana (día siguiente)", "Até amanhã!", "¡Hasta mañana!"),
            ("ontem", "ayer", "Ontem eu estudei muito.", "Ayer estudié mucho."),
            ("segunda", "lunes", "Na segunda eu trabalho.", "El lunes trabajo."),
            ("terça", "martes", "Na terça tenho aula.", "El martes tengo clase."),
            ("quarta", "miércoles", "Na quarta eu descanso.", "El miércoles descanso."),
            ("quinta", "jueves", "Quinta à noite tem cinema.", "El jueves a la noche hay cine."),
            ("sexta", "viernes", "Sexta a gente sai.", "El viernes salimos."),
            ("sábado", "sábado", "No sábado não trabalho.", "El sábado no trabajo."),
            ("domingo", "domingo", "Domingo é dia de família.", "El domingo es día de familia."),
            ("semana", "semana", "Esta semana estou ocupado.", "Esta semana estoy ocupado."),
            ("hora", "hora", "Que horas são?", "¿Qué hora es?"),
            ("tarde", "tarde (parte del día)", "À tarde eu estudo.", "A la tarde estudio."),
        ],
    ),
    L(
        "En la ciudad",
        "Calles, colectivos, boletos y cómo preguntar dónde queda algo.",
        [
            "Rua es la calle y praça es la plaza. A estação es la estación. El ônibus es el colectivo; el trem, el tren. La passagem es el boleto.",
            "Para orientarte: esquerda y direita, aqui y ali, perto y longe. Vire à esquerda es «doblá a la izquierda». Onde fica...? pregunta dónde queda algo.",
            "Ir es el verbo del movimiento: eu vou, você vai, nós vamos, eles vão. Vou para casa. Vou de ônibus. Vamos? es la invitación más corta.",
        ],
        [
            ("rua", "calle", "Eu moro na rua Augusta.", "Vivo en la calle Augusta."),
            ("praça", "plaza", "Vamos nos encontrar na praça.", "Nos encontramos en la plaza."),
            ("estação", "estación", "A estação fica perto.", "La estación queda cerca."),
            ("ônibus", "colectivo", "Eu pego o ônibus.", "Tomo el colectivo."),
            ("trem", "tren", "O trem sai às nove.", "El tren sale a las nueve."),
            ("passagem", "boleto; pasaje", "Uma passagem para o Rio.", "Un boleto para Río."),
            ("esquerda", "izquierda", "Vire à esquerda.", "Doblá a la izquierda."),
            ("direita", "derecha", "O banco fica à direita.", "El banco queda a la derecha."),
            ("aqui", "acá; aquí", "Eu estou aqui.", "Estoy acá."),
            ("ali", "ahí; allá", "O banheiro é ali.", "El baño está ahí."),
            ("perto", "cerca", "Fica perto da praça.", "Queda cerca de la plaza."),
            ("longe", "lejos", "A estação é longe.", "La estación queda lejos."),
            ("ir", "ir", "Eu vou para casa.", "Voy a casa."),
        ],
        dialogue=D(
            ("Com licença, onde fica a estação?", "Permiso, ¿dónde queda la estación?"),
            ("Fica perto. Vire à direita.", "Queda cerca. Doblá a la derecha."),
            ("É longe daqui?", "¿Queda lejos de acá?"),
            ("Não, é só uma rua.", "No, es solo una calle."),
            ("Obrigado! Tchau.", "¡Gracias! Chau."),
        ),
    ),
    L(
        "Colores y adjetivos",
        "Vermelho, azul, grande, pequeno y cómo concuerdan.",
        [
            "Los adjetivos van después del sustantivo y concuerdan: carro vermelho, casa vermelha. Los que terminan en -e no cambian: cidade grande, carro grande.",
            "Vermelho, verde, branco, preto, azul y amarelo son los colores básicos. Preto es negro: café preto, feijão preto.",
            "Grande y pequeno miden el tamaño. Bonito es lindo. Novo y velho dicen la edad, y quente y frio, la temperatura: o café está quente. Hoje faz frio.",
        ],
        [
            ("vermelho", "rojo", "O semáforo está vermelho.", "El semáforo está en rojo."),
            ("verde", "verde", "A maçã é verde.", "La manzana es verde."),
            ("branco", "blanco", "O vinho branco é gelado.", "El vino blanco está helado."),
            ("preto", "negro", "Eu gosto de café preto.", "Me gusta el café negro."),
            ("azul", "azul", "O mar é azul.", "El mar es azul."),
            ("amarelo", "amarillo", "O ônibus é amarelo.", "El colectivo es amarillo."),
            ("grande", "grande", "É uma cidade grande.", "Es una ciudad grande."),
            ("pequeno", "pequeño", "Um café pequeno, por favor.", "Un café chico, por favor."),
            ("bonito", "lindo", "Que casa bonita!", "¡Qué casa linda!"),
            ("novo", "nuevo", "Eu tenho um carro novo.", "Tengo un auto nuevo."),
            ("velho", "viejo", "Esta casa é velha.", "Esta casa es vieja."),
            ("quente", "caliente; caluroso", "O café está quente.", "El café está caliente."),
            ("frio", "frío", "Hoje faz frio.", "Hoy hace frío."),
        ],
    ),
    L(
        "Verbos básicos",
        "Estar, ter, fazer, poder y los verbos para sobrevivir.",
        [
            "Estar dice cómo o dónde estás ahora: eu estou em casa, ela está feliz. Ser es para lo permanente: eu sou argentino. Esa diferencia se parece a la del español.",
            "Ter es tener: eu tenho, você tem, nós temos. Con ter se dice la edad, el hambre, el frío: tenho fome, tenho frio. Fazer es hacer: o que você faz? Poder y precisar van con otro verbo: posso entrar? Preciso estudar.",
            "Falar, entender, saber, ver, vir, gostar, trabalhar y estudar completan el kit. Gostar lleva de: eu gosto de café. Vir es venir: você vem amanhã?",
        ],
        [
            ("estar", "estar", "Eu estou em casa.", "Estoy en casa."),
            ("ter", "tener", "Eu tenho fome.", "Tengo hambre."),
            ("fazer", "hacer", "O que você faz?", "¿Qué hacés?"),
            ("poder", "poder", "Posso entrar?", "¿Puedo entrar?"),
            ("precisar", "necesitar", "Eu preciso estudar.", "Necesito estudiar."),
            ("falar", "hablar", "Você fala português?", "¿Hablás portugués?"),
            ("entender", "entender", "Eu não entendi.", "No entendí."),
            ("saber", "saber", "Eu não sei.", "No sé."),
            ("ver", "ver", "Eu vejo o mar.", "Veo el mar."),
            ("vir", "venir", "Você vem amanhã?", "¿Venís mañana?"),
            ("gostar", "gustar; querer (gostar de)", "Eu gosto de café.", "Me gusta el café."),
            ("trabalhar", "trabajar", "Eu trabalho de segunda a sexta.", "Trabajo de lunes a viernes."),
            ("estudar", "estudiar", "Eu estudo português.", "Estudio portugués."),
        ],
    ),
    L(
        "Casa y salidas",
        "Casa, ciudad, mascotas, clima y planes juntos.",
        [
            "Casa, cozinha, quarto y banheiro nombran la vivienda. Cidade es la ciudad. Gato y cachorro son las mascotas. Sim y não son las dos respuestas más cortas.",
            "El clima: tempo es tanto «tiempo» como «clima». Que tempo faz? pregunta cómo está el día. Faz sol, faz calor, faz frio, vai chover.",
            "Para proponer un plan se dice vamos ao cinema? y se responde vamos! o não posso. Juntos es «juntos» y siempre en plural.",
        ],
        [
            ("casa", "casa", "A casa é pequena.", "La casa es chica."),
            ("cidade", "ciudad", "São Paulo é uma cidade enorme.", "San Pablo es una ciudad enorme."),
            ("cozinha", "cocina", "A cozinha é grande.", "La cocina es grande."),
            ("quarto", "cuarto; dormitorio", "Meu quarto é pequeno.", "Mi cuarto es chico."),
            ("banheiro", "baño", "Onde fica o banheiro?", "¿Dónde queda el baño?"),
            ("sim", "sí", "Sim, eu quero.", "Sí, quiero."),
            ("não", "no", "Não, obrigado.", "No, gracias."),
            ("gato", "gato", "O gato dorme no sofá.", "El gato duerme en el sillón."),
            ("cachorro", "perro", "O cachorro é meu amigo.", "El perro es mi amigo."),
            ("tempo", "tiempo; clima", "Que tempo faz hoje?", "¿Qué tiempo hace hoy?"),
            ("chover", "llover", "Hoje vai chover.", "Hoy va a llover."),
            ("cinema", "cine", "Vamos ao cinema?", "¿Vamos al cine?"),
            ("juntos", "juntos", "Nós moramos juntos.", "Vivimos juntos."),
        ],
        dialogue=D(
            ("Vamos ao cinema hoje?", "¿Vamos al cine hoy?"),
            ("Hoje não posso. Vai chover.", "Hoy no puedo. Va a llover."),
            ("Então vamos amanhã?", "¿Entonces vamos mañana?"),
            ("Amanhã eu posso. A que horas?", "Mañana puedo. ¿A qué hora?"),
            ("Às oito. Vamos juntos de ônibus.", "A las ocho. Vamos juntos en colectivo."),
        ),
        quiz=[
            Q("Vai chover significa…", "va a llover", "hace sol", "hay viento", "es de noche"),
            Q("Vamos ao cinema é…", "vamos al cine", "pago la cuenta", "me llamo Lucas", "a la izquierda"),
            Q("Juntos quiere decir…", "juntos", "lejos", "caro", "ayer"),
            Q("Que tempo faz? pregunta por…", "el clima", "el precio", "el nombre", "la hora"),
            Q("Cachorro es…", "perro", "lluvia", "boleto", "queso"),
        ],
    ),
]


def main():
    from course_bind import extra_lessons, extra_words

    lexicon, a1_lessons = bind(A1_SPECS, 1)
    for level, rows in extra_words().items():
        lexicon += rows

    seen = set()
    for item in lexicon:
        if item["hanzi"] in seen:
            raise SystemExit("repetida: " + item["hanzi"])
        seen.add(item["hanzi"])

    courses = {1: a1_lessons, **extra_lessons()}

    missing = []
    for classes in courses.values():
        for item in classes:
            for pin in item["pins"]:
                if pin not in seen:
                    missing.append(pin)
    if missing:
        raise SystemExit("pins fuera del léxico: " + ", ".join(missing))

    by_level = {}
    for item in lexicon:
        by_level.setdefault(item["level"], set()).add(item["hanzi"])
    names = {1: "a1", 2: "a2", 3: "b1", 4: "b2", 5: "c1", 6: "c2"}
    for level, classes in courses.items():
        if len(classes) != 12:
            raise SystemExit(f"{names[level]} tiene {len(classes)} clases")
        pinned = [pin for item in classes for pin in item["pins"]]
        unknown = sorted({pin for pin in pinned if pin not in by_level[level]})
        if unknown:
            raise SystemExit(f"{names[level]} pins ajenos: " + ", ".join(unknown))
        uncovered = sorted(by_level[level] - set(pinned))
        if uncovered:
            raise SystemExit(f"{names[level]} sin clase: " + ", ".join(uncovered))

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "lexicon.json").write_text(
        json.dumps(lexicon, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    counts = []
    for level, classes in courses.items():
        path = ROOT / "data" / f"{names[level]}.json"
        path.write_text(json.dumps(classes, ensure_ascii=False, indent=2), encoding="utf-8")
        counts.append(f"{names[level].upper()} {len(classes)}")
    per_level = " ".join(f"{names[level].upper()}={len(words)}" for level, words in sorted(by_level.items()))
    print(f"lexico {len(lexicon)} ({per_level}) " + " ".join(counts))


if __name__ == "__main__":
    main()
