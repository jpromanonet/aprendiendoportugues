"""Clases de C1 y C2 y el ensamblado de los niveles A2 a C2 del curso de portugués."""

from course_upper import A2_SPECS, B1_SPECS, B2_SPECS, D, L, Q, bind

# --- C1 ---------------------------------------------------------------------

C1_SPECS = [
    L(
        "Matices del discurso",
        "Conectores formales para argumentar con precisión.",
        [
            "En el registro escrito y en el debate, mas y então se quedan cortos. Contudo, todavia y entretanto marcan oposición con distinto peso. Portanto y ademais encadenan: uno concluye, el otro suma.",
            "Conquanto introduce una concesión y pide subjuntivo: conquanto seja caro, vale a pena. Mediante es «a cambio de» o «por medio de». Visto que da la razón de lo que sigue.",
        ],
        [
            ("contudo", "sin embargo", "Contudo, o plano falhou.", "Sin embargo, el plan falló."),
            ("todavia", "no obstante", "Todavia, ele insistiu.", "No obstante, él insistió."),
            ("entretanto", "mientras tanto; sin embargo", "Entretanto, a obra continua.", "Mientras tanto, la obra continúa."),
            ("portanto", "por lo tanto", "Choveu; portanto, adiamos.", "Llovió; por lo tanto, postergamos."),
            ("ademais", "además", "Ademais, o preço é justo.", "Además, el precio es justo."),
            ("conquanto", "aunque; si bien", "Conquanto seja caro, vale a pena.", "Si bien es caro, vale la pena."),
            ("mediante", "mediante", "Mediante pagamento, entregamos.", "Mediante pago, entregamos."),
            ("visto que", "dado que", "Visto que chove, ficamos.", "Dado que llueve, nos quedamos."),
        ],
        quiz=[
            Q("Portanto equivale a…", "por lo tanto", "sin embargo", "además", "mientras"),
            Q("Conquanto pide…", "subjuntivo", "imperativo", "gerundio", "participio"),
            Q("Ademais significa…", "además", "demasiado", "adelante", "ayer"),
            Q("Visto que introduce…", "una causa", "una pregunta", "un saludo", "un precio"),
            Q("Todavia en este uso significa…", "no obstante", "todavía", "toda vía", "todos"),
        ],
    ),
    L(
        "Lenguaje jurídico",
        "Contrato, cláusula, juicio y sentencia.",
        [
            "Un contrato tiene cláusulas y se firma ante un advogado. Si hay conflicto, se va al tribunal, donde el juiz dicta la sentença.",
            "Todo ese camino es un processo, que también significa «proceso». Una multa es una sanción económica. En portugués los textos jurídicos conservan fórmulas largas y ritmo solemne.",
        ],
        [
            ("contrato", "contrato", "Assinei o contrato ontem.", "Firmé el contrato ayer."),
            ("cláusula", "cláusula", "Leia a cláusula cinco.", "Leé la cláusula cinco."),
            ("tribunal", "tribunal", "O tribunal decide hoje.", "El tribunal decide hoy."),
            ("sentença", "sentencia", "A sentença saiu cedo.", "La sentencia salió temprano."),
            ("advogado", "abogado", "O advogado pediu provas.", "El abogado pidió pruebas."),
            ("juiz", "juez", "O juiz ouviu as partes.", "El juez escuchó a las partes."),
            ("processo", "juicio; proceso", "O processo durou anos.", "El juicio duró años."),
            ("multa", "multa", "Levei uma multa.", "Me hicieron una multa."),
        ],
    ),
    L(
        "Economía avanzada",
        "Superávit, balance, accionistas y recesión.",
        [
            "Un país o una empresa pueden tener superávit o déficit. El balanço resume las cuentas y el patrimônio dice cuánto se posee.",
            "Los acionistas cobran dividendo. Una recessão frena la economía. El tributo es el término jurídico para el impuesto y suena más formal que imposto.",
        ],
        [
            ("superávit", "superávit", "O país teve superávit.", "El país tuvo superávit."),
            ("déficit", "déficit", "Há um déficit fiscal.", "Hay un déficit fiscal."),
            ("patrimônio", "patrimonio", "O patrimônio cresceu.", "El patrimonio creció."),
            ("balanço", "balance", "O balanço sai em março.", "El balance sale en marzo."),
            ("acionista", "accionista", "Os acionistas votaram.", "Los accionistas votaron."),
            ("dividendo", "dividendo", "O dividendo foi pago.", "El dividendo fue pagado."),
            ("recessão", "recesión", "A recessão afetou todos.", "La recesión afectó a todos."),
            ("tributo", "tributo", "O tributo é pago ao Estado.", "El tributo se paga al Estado."),
        ],
    ),
    L(
        "Ideas y filosofía",
        "Ética, libertad, justicia y virtud.",
        [
            "La ética orienta la decisión. La liberdade y la justiça son valores que se discuten sin fin. La consciência es lo que sabe que algo está bien o mal.",
            "Un conceito es una idea abstracta. La essência es lo que no cambia. La virtude es un rasgo positivo. Consciência significa tanto «conciencia moral» como «saber algo».",
        ],
        [
            ("ética", "ética", "A ética guia a decisão.", "La ética guía la decisión."),
            ("liberdade", "libertad", "A liberdade tem limites.", "La libertad tiene límites."),
            ("justiça", "justicia", "A justiça deve ser igual.", "La justicia debe ser igual."),
            ("consciência", "conciencia", "Tenho a consciência tranquila.", "Tengo la conciencia tranquila."),
            ("conceito", "concepto", "O conceito é abstrato.", "El concepto es abstracto."),
            ("essência", "esencia", "A essência não muda.", "La esencia no cambia."),
            ("virtude", "virtud", "A paciência é uma virtude.", "La paciencia es una virtud."),
        ],
    ),
    L(
        "Ciencia avanzada",
        "Teoría, método, muestra y variable.",
        [
            "Una teoria explica un fenómeno. El método dice cómo se llega a la conclusión. La amostra es la parte que se estudia y la variável es lo que cambia.",
            "El pesquisador trabaja en el laboratório y escribe una fórmula. En un paper brasileño vas a encontrar todos estos términos casi idénticos al español.",
        ],
        [
            ("teoria", "teoría", "A teoria explica o fenômeno.", "La teoría explica el fenómeno."),
            ("método", "método", "O método é rigoroso.", "El método es riguroso."),
            ("amostra", "muestra", "A amostra é pequena.", "La muestra es pequeña."),
            ("variável", "variable", "Cada variável importa.", "Cada variable importa."),
            ("laboratório", "laboratorio", "O laboratório abre às sete.", "El laboratorio abre a las siete."),
            ("fórmula", "fórmula", "Escreva a fórmula no quadro.", "Escribí la fórmula en el pizarrón."),
            ("pesquisador", "investigador", "O pesquisador publicou o artigo.", "El investigador publicó el artículo."),
        ],
    ),
    L(
        "Literatura y estilo",
        "Metáfora, narrador, trama e ironía.",
        [
            "Un texto literario tiene narrador, enredo y personagem. La metáfora y la ironia son recursos de estilo. La prosa y el verso son las dos formas básicas.",
            "Personagem es femenino o masculino según quien sea: a personagem principal, o personagem principal. La palabra sirve para ambos géneros.",
        ],
        [
            ("metáfora", "metáfora", "Essa metáfora é bonita.", "Esa metáfora es linda."),
            ("narrador", "narrador", "O narrador conta em primeira pessoa.", "El narrador cuenta en primera persona."),
            ("enredo", "trama", "O enredo é complexo.", "La trama es compleja."),
            ("personagem", "personaje", "A personagem principal morre.", "La protagonista muere."),
            ("ironia", "ironía", "Há ironia no texto.", "Hay ironía en el texto."),
            ("prosa", "prosa", "A prosa dele é limpa.", "Su prosa es limpia."),
            ("verso", "verso", "O último verso é lindo.", "El último verso es hermoso."),
        ],
    ),
    L(
        "Retórica y medios",
        "Discurso, debate, prensa y censura.",
        [
            "La retórica es el arte de persuadir. Un discurso se pronuncia y un debate se discute entre varios. La propaganda es publicidad y también propaganda política.",
            "La censura limita lo que se puede decir. La imprensa investiga y publica. La narrativa es el relato con el que se cuenta un hecho.",
        ],
        [
            ("retórica", "retórica", "A retórica convence.", "La retórica convence."),
            ("discurso", "discurso", "O discurso foi longo.", "El discurso fue largo."),
            ("debate", "debate", "O debate começa às oito.", "El debate empieza a las ocho."),
            ("propaganda", "publicidad; propaganda", "A propaganda é enganosa.", "La publicidad es engañosa."),
            ("censura", "censura", "A censura limita a arte.", "La censura limita el arte."),
            ("imprensa", "prensa", "A imprensa investiga o caso.", "La prensa investiga el caso."),
            ("narrativa", "narrativa; relato", "A narrativa mudou.", "El relato cambió."),
        ],
        dialogue=D(
            ("O debate de ontem foi tenso.", "El debate de ayer fue tenso."),
            ("Pois é. O candidato mudou o discurso.", "Y sí. El candidato cambió el discurso."),
            ("A imprensa vai investigar.", "La prensa va a investigar."),
            ("Tomara que sim. A narrativa dele não fecha.", "Ojalá. Su relato no cierra."),
        ),
    ),
    L(
        "Psicología",
        "Conducta, personalidad, memoria y empatía.",
        [
            "El comportamento se observa. La personalidade es el conjunto de rasgos. La memória guarda lo vivido y el trauma deja marcas.",
            "La empatia permite ponerse en el lugar del otro y la motivação empuja a actuar. La mente es la palabra general. Ojo: ele mente también significa «él miente».",
        ],
        [
            ("comportamento", "comportamiento", "O comportamento mudou.", "El comportamiento cambió."),
            ("personalidade", "personalidad", "Ela tem muita personalidade.", "Ella tiene mucha personalidad."),
            ("memória", "memoria", "Tenho boa memória.", "Tengo buena memoria."),
            ("trauma", "trauma", "O trauma deixa marcas.", "El trauma deja marcas."),
            ("empatia", "empatía", "A empatia aproxima as pessoas.", "La empatía acerca a las personas."),
            ("motivação", "motivación", "Falta motivação.", "Falta motivación."),
            ("mente", "mente", "A mente precisa descansar.", "La mente necesita descansar."),
        ],
    ),
    L(
        "Historia",
        "Colonia, imperio, independencia y república.",
        [
            "La história de Brasil empieza con la colônia de Portugal. Después viene el império y la independência, que ocurrió en el siglo diecinueve.",
            "La escravidão marcó siglos y todavía se discute. La república nació a fines de ese mismo siglo. Una revolução cambia el rumbo de un país.",
        ],
        [
            ("história", "historia; cuento", "A história do Brasil é longa.", "La historia de Brasil es larga."),
            ("império", "imperio", "O império durou décadas.", "El imperio duró décadas."),
            ("colônia", "colonia", "O Brasil foi colônia de Portugal.", "Brasil fue colonia de Portugal."),
            ("independência", "independencia", "A independência foi no século dezenove.", "La independencia fue en el siglo diecinueve."),
            ("escravidão", "esclavitud", "A escravidão deixou marcas.", "La esclavitud dejó marcas."),
            ("república", "república", "A república nasceu no fim do século.", "La república nació a fines del siglo."),
            ("revolução", "revolución", "A revolução mudou o país.", "La revolución cambió el país."),
        ],
    ),
    L(
        "Sociedad",
        "Igualdad, prejuicio, migración y diversidad.",
        [
            "La igualdade es un principio. El preconceito lo rompe. La migração mueve a las personas y la minoria necesita voz propia.",
            "La diversidade enriquece y la tolerância permite convivir. La cidadania reúne derechos y deberes. Son palabras muy parecidas al español, pero el sonido cambia.",
        ],
        [
            ("igualdade", "igualdad", "A igualdade é um princípio.", "La igualdad es un principio."),
            ("preconceito", "prejuicio", "O preconceito machuca.", "El prejuicio lastima."),
            ("migração", "migración", "A migração mudou a cidade.", "La migración cambió la ciudad."),
            ("minoria", "minoría", "A minoria também tem voz.", "La minoría también tiene voz."),
            ("diversidade", "diversidad", "A diversidade enriquece.", "La diversidad enriquece."),
            ("tolerância", "tolerancia", "A tolerância é essencial.", "La tolerancia es esencial."),
            ("cidadania", "ciudadanía", "Aprendemos cidadania na escola.", "Aprendemos ciudadanía en la escuela."),
        ],
    ),
    L(
        "Lengua y variación",
        "Acento, dialecto, jerga y traducción.",
        [
            "Cada región tiene su sotaque: el carioca, el paulista, el gaúcho, el nordestino. El dialeto y la gíria cambian de un lugar a otro.",
            "El idioma oficial es el portugués. La tradução pasa un texto de una lengua a otra. El vocabulário se amplía leyendo y la gramática ordena todo.",
        ],
        [
            ("sotaque", "acento", "Ele tem sotaque carioca.", "Él tiene acento carioca."),
            ("dialeto", "dialecto", "Cada região tem um dialeto.", "Cada región tiene un dialecto."),
            ("gíria", "jerga", "A gíria muda rápido.", "La jerga cambia rápido."),
            ("idioma", "idioma", "O idioma oficial é o português.", "El idioma oficial es el portugués."),
            ("tradução", "traducción", "A tradução ficou ótima.", "La traducción quedó excelente."),
            ("vocabulário", "vocabulario", "Ampliei meu vocabulário.", "Amplié mi vocabulario."),
            ("gramática", "gramática", "A gramática é difícil.", "La gramática es difícil."),
        ],
        quiz=[
            Q("Sotaque es…", "acento al hablar", "tipo de café", "golpe", "sombrero"),
            Q("Gíria significa…", "jerga", "regla", "libro", "cuaderno"),
            Q("Tradução es…", "traducción", "tradición", "tráfico", "trato"),
            Q("Idioma es…", "idioma", "ídolo", "idiota", "idea"),
            Q("Gramática es…", "gramática", "gramo", "grama", "gran"),
        ],
    ),
    L(
        "Precisión y matices",
        "Sutil, ambiguo, explícito, implícito.",
        [
            "Un matiz es una diferencia leve. Lo sutil casi no se nota. Lo ambíguo admite dos lecturas. Lo explícito está dicho; lo implícito se entiende sin decirlo.",
            "Preciso es «exacto» (no confundir con precisar) y vago es lo contrario. En un buen texto escrito, la precisión importa tanto como el estilo.",
        ],
        [
            ("matiz", "matiz", "Há um matiz de ironia.", "Hay un matiz de ironía."),
            ("sutil", "sutil", "A diferença é sutil.", "La diferencia es sutil."),
            ("ambíguo", "ambiguo", "O texto é ambíguo.", "El texto es ambiguo."),
            ("explícito", "explícito", "O pedido foi explícito.", "El pedido fue explícito."),
            ("implícito", "implícito", "Há um sentido implícito.", "Hay un sentido implícito."),
            ("preciso", "preciso; exacto", "Seja preciso no relato.", "Sé preciso en el relato."),
            ("vago", "vago", "A resposta foi vaga.", "La respuesta fue vaga."),
        ],
    ),
]

# --- C2 ---------------------------------------------------------------------

C2_SPECS = [
    L(
        "Lusofonía",
        "El portugués más allá de Brasil.",
        [
            "La lusofonia reúne a los países que hablan portugués: Portugal, Brasil, Angola, Moçambique, Cabo Verde, Guiné-Bissau, São Tomé y Príncipe y Timor-Leste. Cada uno tiene su acento y su vocabulario.",
            "Lisboa es la capital de Portugal. El português europeu pronuncia menos las vocales átonas y suena más cerrado, por eso el acento lusitano choca al oído brasileño. El crioulo es la lengua de Cabo Verde, basada en el portugués.",
        ],
        [
            ("lusofonia", "lusofonía", "A lusofonia reúne vários países.", "La lusofonía reúne varios países."),
            ("Portugal", "Portugal", "Portugal fica na Europa.", "Portugal queda en Europa."),
            ("Angola", "Angola", "Angola fala português.", "En Angola se habla portugués."),
            ("Moçambique", "Mozambique", "Moçambique tem muitas línguas.", "Mozambique tiene muchas lenguas."),
            ("Lisboa", "Lisboa", "Lisboa é uma cidade de colinas.", "Lisboa es una ciudad de colinas."),
            ("crioulo", "criollo (lengua)", "O crioulo é falado em Cabo Verde.", "El criollo se habla en Cabo Verde."),
            ("lusitano", "lusitano; portugués", "O sotaque lusitano é fechado.", "El acento portugués es cerrado."),
        ],
    ),
    L(
        "Falsos amigos",
        "Palabras que se parecen al español y engañan.",
        [
            "El portuñol es la trampa de todo hispanohablante. Esquisito no es «exquisito», es «raro». Apelido es «apodo», no «apellido» (que es sobrenome). Borracha es la goma de borrar, no la que tomó de más.",
            "Rato es el animal (rata o ratón) y, en um rato, también «un rato» de tiempo. Oficina es «taller». Largo es «ancho» y salsa es «perejil». Memorizalos en pares: así los controlás mejor.",
        ],
        [
            ("esquisito", "raro; extraño", "Ele é um tipo esquisito.", "Es un tipo raro."),
            ("apelido", "apodo", "Meu apelido é Nando.", "Mi apodo es Nando."),
            ("borracha", "goma de borrar", "Empreste a borracha.", "Prestame la goma."),
            ("rato", "rata; ratón; rato", "Há um rato na cozinha.", "Hay una rata en la cocina."),
            ("oficina", "taller", "Levei o carro à oficina.", "Llevé el auto al taller."),
            ("largo", "ancho; amplio", "O corredor é largo.", "El pasillo es ancho."),
            ("salsa", "perejil", "Coloque salsa na sopa.", "Ponele perejil a la sopa."),
        ],
        quiz=[
            Q("Esquisito significa…", "raro", "exquisito", "exquisitamente", "delicioso"),
            Q("Apelido es…", "apodo", "apellido", "apellidos", "apelación"),
            Q("Largo es…", "ancho", "largo", "lejos", "alto"),
            Q("Oficina es…", "taller", "oficina", "escritorio", "empresa"),
            Q("Salsa es…", "perejil", "salsa", "ají", "ensalada"),
        ],
    ),
    L(
        "Verbos engañosos",
        "Pegar, puxar, apagar y los que no significan lo que creés.",
        [
            "Pegar es «agarrar, tomar»: pegar o ônibus es tomar el colectivo. Puxar es «tirar» (hacia vos) y empurrar es «empujar»; en las puertas brasileñas vas a ver empurre y puxe. Cheirar es «oler».",
            "Apagar sirve para apagar la luz y también para borrar un archivo. Tirar es «sacar, quitar»: tire o casaco. Largar es «soltar»: largue isso. Todos parecen verbos conocidos, pero cambian de sentido.",
        ],
        [
            ("pegar", "agarrar; tomar", "Pegue o ônibus ali.", "Tomá el colectivo ahí."),
            ("puxar", "tirar (jalar)", "Puxe a porta.", "Tirá de la puerta."),
            ("empurrar", "empujar", "Empurre a porta.", "Empujá la puerta."),
            ("cheirar", "oler", "Cheire a flor.", "Olé la flor."),
            ("apagar", "apagar; borrar", "Apague a luz.", "Apagá la luz."),
            ("tirar", "sacar; quitar", "Tire o casaco.", "Sacate el abrigo."),
            ("largar", "soltar; dejar", "Largue isso agora.", "Soltá eso ya."),
        ],
    ),
    L(
        "Modismos",
        "Expresiones que no se traducen palabra por palabra.",
        [
            "Quebrar o galho es sacar a alguien de un apuro. Descascar o abacaxi es resolver un problema difícil, porque pelar una piña es una tarea áspera. Pagar o pato es pagar los platos rotos.",
            "Ficar de olho es estar atento. Dar o braço a torcer es admitir que uno se equivocó. Engolir sapo es aguantarse algo desagradable. Tirar o time de campo es retirarse de un asunto.",
        ],
        [
            ("quebrar o galho", "sacar del apuro", "Você quebrou o meu galho.", "Me sacaste del apuro."),
            ("descascar o abacaxi", "resolver un problema difícil", "Vamos descascar esse abacaxi.", "Vamos a resolver este problema difícil."),
            ("pagar o pato", "pagar el pato", "Sobrou para mim pagar o pato.", "Me tocó pagar el pato."),
            ("ficar de olho", "estar atento; vigilar", "Fique de olho na hora.", "Estate atento a la hora."),
            ("dar o braço a torcer", "ceder; admitir un error", "Ele não dá o braço a torcer.", "Él no da el brazo a torcer."),
            ("engolir sapo", "aguantarse; tragar sapos", "Tive que engolir sapo no trabalho.", "Tuve que aguantarme en el trabajo."),
            ("tirar o time de campo", "retirarse; abandonar", "Ele tirou o time de campo.", "Él se retiró del asunto."),
        ],
    ),
    L(
        "Figuras del lenguaje",
        "Eufemismo, hipérbole, elipsis y registros.",
        [
            "Un eufemismo suaviza algo duro: falecer en vez de morrer. La hipérbole exagera y el pleonasmo repite: subir para cima. La elipse omite lo que se sobreentiende.",
            "Cada registro tiene su palabra. Lo coloquial es el habla de todos los días. Lo culto es el habla elevada. Lo vulgar es el habla que se evita en contextos formales.",
        ],
        [
            ("eufemismo", "eufemismo", "Falecer é um eufemismo.", "«Falecer» es un eufemismo."),
            ("hipérbole", "hipérbole", "Isso é pura hipérbole.", "Eso es pura hipérbole."),
            ("elipse", "elipsis", "A elipse omite o sujeito.", "La elipsis omite el sujeto."),
            ("pleonasmo", "pleonasmo", "Subir para cima é pleonasmo.", "«Subir para arriba» es un pleonasmo."),
            ("coloquial", "coloquial", "O tom é coloquial.", "El tono es coloquial."),
            ("culto", "culto; de nivel elevado", "Ele usa um registro culto.", "Él usa un registro culto."),
            ("vulgar", "vulgar; popular", "A palavra é vulgar.", "La palabra es vulgar."),
        ],
    ),
    L(
        "Clásicos de la literatura",
        "Realismo, romanticismo, modernismo y el canon.",
        [
            "La literatura brasileña pasó por el romantismo, el realismo y el modernismo. Machado de Assis, el gran romancista del realismo, escribió novelas, cuentos y crônicas.",
            "El cânone es la lista de obras que una cultura considera esenciales. Una antologia reúne textos de varios autores. La crônica es un texto breve y personal que sale en el diario.",
        ],
        [
            ("realismo", "realismo", "O realismo critica a sociedade.", "El realismo critica la sociedad."),
            ("romantismo", "romanticismo", "O romantismo exalta a emoção.", "El romanticismo exalta la emoción."),
            ("modernismo", "modernismo", "O modernismo renovou a poesia.", "El modernismo renovó la poesía."),
            ("crônica", "crónica (texto breve)", "A crônica sai no domingo.", "La crónica sale el domingo."),
            ("cânone", "canon", "O cânone literário muda.", "El canon literario cambia."),
            ("romancista", "novelista", "Machado de Assis foi um grande romancista.", "Machado de Assis fue un gran novelista."),
            ("antologia", "antología", "Comprei uma antologia de poemas.", "Compré una antología de poemas."),
        ],
    ),
    L(
        "Música de Brasil",
        "Bossa nova, forró, sertanejo y la letra de una canción.",
        [
            "La bossa nova nació en Río en los años cincuenta. El forró es el baile del nordeste. El sertanejo es hoy la música más escuchada en la radio brasileña.",
            "Una canção tiene melodia, ritmo y letra. La palabra letra en música es «letra de la canción»: a letra fala de saudade.",
        ],
        [
            ("bossa nova", "bossa nova", "A bossa nova nasceu no Rio.", "La bossa nova nació en Río."),
            ("forró", "forró (baile del nordeste)", "O forró anima a festa.", "El forró anima la fiesta."),
            ("sertanejo", "sertanejo (country brasileño)", "O sertanejo domina o rádio.", "El sertanejo domina la radio."),
            ("melodia", "melodía", "A melodia é simples.", "La melodía es simple."),
            ("ritmo", "ritmo", "O ritmo é contagiante.", "El ritmo es contagioso."),
            ("letra", "letra (de canción)", "A letra fala de saudade.", "La letra habla de añoranza."),
            ("canção", "canción", "Esta canção é antiga.", "Esta canción es antigua."),
        ],
    ),
    L(
        "Naturaleza",
        "Amazonia, selva, cerrado y ecosistemas.",
        [
            "La Amazônia es la mayor selva tropical del mundo. Un bioma es un gran ecosistema. El cerrado es la sabana brasileña, cada vez más amenazada.",
            "La fauna y la flora describen a los animales y las plantas. El desmatamento es la deforestación y es uno de los grandes temas del país.",
        ],
        [
            ("Amazônia", "Amazonia", "A Amazônia é enorme.", "La Amazonia es enorme."),
            ("floresta", "bosque; selva", "A floresta é densa.", "La selva es densa."),
            ("bioma", "bioma", "Cada bioma tem sua fauna.", "Cada bioma tiene su fauna."),
            ("cerrado", "sabana brasileña (cerrado)", "O cerrado é um bioma.", "El cerrado es un bioma."),
            ("fauna", "fauna", "A fauna é diversa.", "La fauna es diversa."),
            ("flora", "flora", "A flora é protegida.", "La flora está protegida."),
            ("desmatamento", "deforestación", "O desmatamento preocupa.", "La deforestación preocupa."),
        ],
    ),
    L(
        "Cortesía y tono",
        "Educado, rude, gentil y franco.",
        [
            "Educado en portugués es «bien criado, cortés»: ele é muito educado. No significa «con estudios». Rude es «grosero», gentil es «amable» y cortês es «cortés».",
            "Sincero y franco se parecen, pero franco puede ser demasiado directo. Discreto es el que no llama la atención. Dominar el tono es parte del nivel C2.",
        ],
        [
            ("educado", "cortés; bien criado", "Ele é muito educado.", "Él es muy cortés."),
            ("rude", "grosero", "A resposta foi rude.", "La respuesta fue grosera."),
            ("gentil", "gentil; amable", "Foi muito gentil da sua parte.", "Fue muy amable de tu parte."),
            ("sincero", "sincero", "Seja sincero comigo.", "Sé sincero conmigo."),
            ("franco", "franco", "Ele é franco demais.", "Él es demasiado franco."),
            ("discreto", "discreto", "Ela é muito discreta.", "Ella es muy discreta."),
            ("cortês", "cortés", "Um convite cortês.", "Una invitación cortés."),
        ],
    ),
    L(
        "Humor e ironía",
        "Chistes, ironías y bromas.",
        [
            "La piada es el chiste. El sarcasmo hiere con humor. El trocadilho es el juego de palabras. La gozação es la burla entre amigos y zoar es hacer bromas.",
            "La brincadeira es la broma o el juego. Graça es «gracia»: não tem graça es «no tiene gracia». De graça significa «gratis».",
        ],
        [
            ("piada", "chiste", "Ele contou uma piada.", "Él contó un chiste."),
            ("sarcasmo", "sarcasmo", "Detesto sarcasmo.", "Detesto el sarcasmo."),
            ("trocadilho", "juego de palabras", "Que trocadilho horrível!", "¡Qué juego de palabras horrible!"),
            ("gozação", "cargada; burla", "Foi só uma gozação.", "Fue solo una cargada."),
            ("zoar", "hacer bromas; cargar", "Eles vivem zoando o Pedro.", "Siempre le hacen bromas a Pedro."),
            ("brincadeira", "broma; juego", "Foi só brincadeira.", "Fue solo una broma."),
            ("graça", "gracia", "Não tem graça.", "No tiene gracia."),
        ],
        dialogue=D(
            ("Você ouviu a piada do Pedro?", "¿Escuchaste el chiste de Pedro?"),
            ("Ouvi. Não tem graça nenhuma.", "Lo escuché. No tiene ninguna gracia."),
            ("Foi só brincadeira!", "¡Fue solo una broma!"),
            ("Tá bom, mas eu não gosto de gozação.", "Está bien, pero no me gustan las cargadas."),
        ),
    ),
    L(
        "Alma brasileña",
        "Palabras que no tienen traducción exacta.",
        [
            "Cafuné es el gesto de pasar los dedos por el pelo de alguien con cariño. Jeitinho es la forma flexible de resolver algo. El malandro es el pícaro. El sertão es el interior seco del nordeste.",
            "El caipira es el campesino del interior del sudeste, y su fiesta es la festa caipira. El mineiro es el de Minas Gerais, famoso por su hospitalidad y su comida.",
        ],
        [
            ("cafuné", "caricia en el pelo", "Ele fez cafuné nela.", "Él le acarició el pelo."),
            ("jeitinho", "maña; arreglo informal", "O jeitinho brasileiro é famoso.", "El jeitinho brasileño es famoso."),
            ("malandro", "pícaro; vivo", "O malandro enganou todos.", "El pícaro engañó a todos."),
            ("sertão", "interior árido del nordeste", "O sertão é seco.", "El sertão es seco."),
            ("caipira", "campesino; paleto", "A festa caipira é divertida.", "La fiesta campesina es divertida."),
            ("mineiro", "de Minas Gerais", "O mineiro fala devagar.", "El mineiro habla despacio."),
        ],
        quiz=[
            Q("Cafuné es…", "una caricia en el pelo", "un café", "un perro", "una fiesta"),
            Q("Sertão es…", "el interior seco del nordeste", "una playa", "un barrio", "un edificio"),
            Q("Malandro es…", "pícaro", "enfermo", "mala suerte", "mala persona siempre"),
            Q("Mineiro es…", "de Minas Gerais", "de São Paulo", "de Río", "de Bahía"),
            Q("Jeitinho es…", "una forma flexible de resolver", "una forma de bailar", "un plato", "un jugo"),
        ],
    ),
    L(
        "Cierre del curso",
        "Un último repaso y las palabras para seguir.",
        [
            "Llegaste al final. Parabéns! Fue una longa jornada y una conquista que te abre puertas. El caminho sigue: ahora toca leer, escuchar y hablar con brasileños.",
            "Avançar significa seguir adelante. Persistir es no rendirse. Con estas palabras y las que ya sumaste, tenés el nivel para vivir en portugués. Boa sorte!",
        ],
        [
            ("parabéns", "felicitaciones", "Parabéns pela conquista!", "¡Felicitaciones por el logro!"),
            ("conquista", "logro; conquista", "Foi uma grande conquista.", "Fue un gran logro."),
            ("jornada", "jornada; travesía", "Foi uma longa jornada.", "Fue una larga travesía."),
            ("caminho", "camino", "O caminho é longo.", "El camino es largo."),
            ("avançar", "avanzar", "É hora de avançar.", "Es hora de avanzar."),
            ("persistir", "persistir", "É preciso persistir.", "Hay que persistir."),
        ],
    ),
]

_COURSE = None


def _course():
    global _COURSE
    if _COURSE is None:
        _COURSE = {
            2: bind(A2_SPECS, 2),
            3: bind(B1_SPECS, 3),
            4: bind(B2_SPECS, 4),
            5: bind(C1_SPECS, 5),
            6: bind(C2_SPECS, 6),
        }
    return _COURSE


def extra_words():
    """Filas de léxico de A2 a C2, por nivel."""
    return {level: rows for level, (rows, _) in _course().items()}


def extra_lessons():
    """Clases de A2 a C2, por nivel."""
    return {level: lessons for level, (_, lessons) in _course().items()}
