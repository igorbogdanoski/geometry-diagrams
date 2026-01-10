# Професионален водич за Asymptote - Технички дијаграми

Ова е детален водич и збирка на кодови (snippets) наменети за професионални илустратори и инженери кои го користат **Asymptote** за креирање технички дијаграми со висок квалитет. Како технички геометриски илустратор, овие алатки се основа за прецизност, конзистентност и професионален изглед.

---

## 1. Основни конфигурации (The Preamble)
Секој професионален проект започнува со дефинирање на форматот и основните стилови за да се обезбеди униформност.

```asy
// Поставување на излезниот формат во PDF за векторски квалитет
settings.outformat = "pdf";

// Оневозможување на интерактивното 3D за статични документи (постабилно за LaTeX)
settings.prc = false;

// Вклучување на основните математички и графички модули
import graph;
import geometry;
import three; // За 3D работа

// Дефинирање на фонт и големина според стандардите на документот
defaultpen(fontsize(10pt));
```

---

## 2. Манипулација со патеки (Path Mastery)
Патеките се јадрото на секој дијаграм. Разликата меѓу `--` и `..` е клучна за визуелниот впечаток.

*   **Прецизно поврзување:** Користете `cycle` за затворени форми и `^^` за неповрзани патеки кои се цртаат со еден „пен".
*   **Тензија на криви:** Операторот `::` овозможува помазна крива со помалку осцилации (`..tension atleast 1..`).

```asy
// Креирање на сложена крива со специфични насоки (tangents)
path s = (0,0){up} .. (1,1) .. {right}(2,0);

// Илустрација на "Law of Janet": Користете променливи за патеки за лесно менување
path boundary = (0,0) -- (100,0) -- (100,50) -- (0,50) -- cycle;
draw(boundary, linewidth(1pt) + blue);
```

---

## 3. Професионално означување (Labels & Arrows)
Во професионалните дијаграми, стрелките и ознаките мора да бидат јасни и естетски усогласени со LaTeX.

*   **Стил на стрелки:** Се препорачува `TeXHead` за совпаѓање со математичките симболи во текстот.
*   **Позиционирање:** Користете `Relative()` за ознаки кои следат одреден процент од должината на патеката.

```asy
// Стрелка со LaTeX стил и ознака на крајот
draw((0,0)--(2,0), L=Label("$x$", position=EndPoint, align=E), arrow=Arrow(TeXHead));

// Ознака со позадина (Fill) за да не се преклопува со линиите
label("$f(x)$", (1,1), filltype=Fill(white));

// Димензионални линии со бариери (Bars)
draw((0,1)--(2,1), L=Label("$d$", MidPoint, align=N), bar=Bars);
```

---

## 4. Геометриска прецизност (Intersections & Analysis)
Наместо рачно пресметување на точки, користете го вградениот систем за анализа.

```asy
// Наоѓање на пресек меѓу две криви
real[][] t = intersections(path1, path2);
if(t.length > 0) {
    dot(point(path1, t)); // Точка на првиот пресек
}

// Извлекување на дел од патека меѓу две точки (Subpath)
path segment = subpath(s, t, t);
draw(segment, red + linewidth(1.5pt));
```

---

## 5. Напредно 3D моделирање
За 3D дијаграми, клучот е во проекцијата и осветлувањето.

*   **Проекција:** `orthographic` е често подобра за технички цртежи бидејќи ги зачувува паралелните линии.
*   **Осветлување:** Користете `nolight` за графикони каде боите треба да бидат идентични како во 2D.

```asy
// Поставување на поглед (Camera) и "Up" вектор
currentprojection = orthographic(5, 2, 3, up=Y);

// Површина на ротација - исклучително моќна алатка за пресметковна геометрија
surface rev = surface(path3_curve, c=O, axis=X);
draw(rev, white + opacity(0.8), meshpen=gray(0.2));
```

---

## 6. Математичка контрола на пресеци и патеки
Наместо рачно одредување на координати, професионалната работа се потпира на вградените функции за анализа на патеки.

*   **Наоѓање на сите пресеци:** Функцијата `intersections(path, path)` е клучна за сложени дијаграми каде треба да најдете точки на допир помеѓу криви. Таа враќа низа од вредности за „времето" на патеката, кои потоа се користат за цртање под-патеки.
*   **Законот на Жанет (Law of Janet):** Ова е професионално правило кое вели дека откако ќе се креира една патека, таа не треба да се користи на начин кој зависи од тоа како била дефинирана (на пр. рачно внесени точки), туку преку функции како `times()` за вертикални пресеци или `intersect()` за пресеци со други фигури.
*   **Под-патеки (subpath):** Користете `subpath(path, real, real)` за да извлечете специфичен дел од крива, што е неопходно при означување на агли или делови од функции кои се преклопуваат.

---

## 7. Софистицирано 3D моделирање и материјали
Професионалните 3D дијаграми бараат фина контрола на светлината и перспективата за да се постигне јасност.

*   **Физички базирано рендерирање (PBR):** Користете ја структурата `material` за да дефинирате како површините реагираат на светлина преку `diffusepen` (дифузно одбивање), `emissivepen` (внатрешен сјај) и `specularpen` (одрази).
*   **Техничко осветлување:** Честопати за технички цртежи е подобро да се користи `light=nolight` во комбинација со `emissivepen`, за да се избегнат несакани сенки кои можат да ги сокријат важните детали или ознаки.
*   **Ориентација на камерата:** Користете `currentprojection = orthographic(...)` за технички цртежи каде паралелните линии мора да останат паралелни, или `perspective(...)` за реалистични прикази. Поставувањето на векторот `up=Y` (или друг специфичен вектор) е клучно за правилно позиционирање на оските.

---

## 8. Напредни техники за сенчење (Shading)
Сенчењето е најмоќниот начин за визуелизација на податоци во 2D и 3D.

*   **Gouraud и Tensor сенчење:** За мазни премини на бои во триаголни или четириаголни мрежи, користете `gouraudshade()` и `tensorshade()`. Овие функции овозможуваат дефинирање на бои во темињата, што е стандард за научна визуелизација.
*   **Lattice Shading:** Овозможува креирање на градиентна мрежа преку дводимензионална низа од бои (`pen[][]`), што е идеално за комплексни позадини.

---

## 9. Позиционирање на ознаки во 3D простор
Еден од најголемите предизвици е ознаките (Labels) да не бидат „потопени" во 3D објектите.

*   **Функција „кон камерата":** Професионалците користат сопствени функции како `towardcamera(triple, real)` за да ги поместат ознаките малку поблиску до камерата, со што се обезбедува тие секогаш да бидат видливи над површините.
*   **Billboard ефект:** Стандардно, ознаките во 3D користат `Billboard`, што значи дека секогаш се вртат кон гледачот. Доколку сакате ознаката да лежи во одредена рамнина, треба да ја промените во `Embedded`.

---

## 10. Оптимизација на кодот и меморијата
Кога работите на големи проекти, ефикасноста е критична.

*   **Низи vs. Патеки (Efficiency):** Градењето на патека со операторот `--` во циклус е квадратно по време (бавно), додека користењето на `guide` и негово подоцнежно разрешување во `path` е линеарно и многу поефикасно.
*   **Статични променливи:** Користете го модификаторот `static` во внатрешни функции или циклуси за да ја алоцирате меморијата само еднаш, што е корисно кај рекурзивни алгоритми.
*   **Autounravel:** Овој модификатор овозможува автоматско отпакување на полињата на структурата, што го прави кодот многу почист кога работите со библиотеки за специфични геометриски објекти.

---

## 11. Висока резолуција и излезни формати
*   **Квалитет на рендерирање:** За врвен квалитет на растерските слики (PNG/TIFF), секогаш поставувајте `settings.render = 16` или повеќе пред импортирање на `three`.
*   **Скалирање при излез:** Професионален трик за максимална острина кај PDF е да го скалирате целиот цртеж пред испраќање: `shipout(scale(4.0)*currentpicture.fit());` и потоа да го намалите при вметнување во документот.
*   **Конзистентност со LaTeX:** Секогаш користете `defaultpen(fontsize(10pt))` или соодветната големина на вашиот документ за ознаките да изгледаат како природен дел од текстот.

---

## Професионален "Cheat Sheet" за секојдневна работа

| Задача | Код / Функција | Извор |
| :--- | :--- | :--- |
| **Единица мерка** | `unitsize(1cm);` | |
| **Дебелина на линија** | `linewidth(0.8pt);` | |
| **Трансформации** | `shift(v) * rotate(45) * scale(2) * path;` | |
| **Бои** | `mediumgray`, `rgb(r,g,b)`, `cmyk(c,m,y,k)` | |
| **Специјални патеки** | `unitsquare`, `unitcircle`, `unitbox` | |
| **Тангента во точка** | `dir(path, time);` | |
| **Транспарентност** | `opacity(0.5)` (само за PDF/PNG) | |
| **3D проекција** | `currentprojection = orthographic(5,2,3,up=Y);` | |
| **Материјал** | `material(diffusepen=white, emissivepen=gray(0.2));` | |
| **Сенчење** | `gouraudshade(triangle, pens);` | |
| **Под-патека** | `subpath(path, start_time, end_time);` | |
| **Висока резолуција** | `settings.render = 16;` | |

---

## 12. Златни совети за професионално ниво
За да го доведете вашето креирање на математички дијаграми до професионално, „инженерско" ниво, постојат неколку суптилни, но моќни техники кои често се занемаруваат. Овие „златно вредни" совети се извлечени од длабоката логика на Asymptote и искуствата на експертите во областа.

### Применувајте го „Законот на Жанет" за робусност
Најважниот совет за професионален илустратор е никогаш да не се потпира на тоа како патот (path) е внатрешно дефиниран преку неговите јазли (nodes).
*   **Зошто?** Ако додадете точка во дефиницијата на патот за да го промените неговиот облик, сите претходни координати базирани на „path time" ќе се изместат.
*   **Решение:** Секогаш користете функции како `times(path, x)` за да најдете пресеци со вертикални линии или `intersections(path1, path2)` за да одредите точки базирани на геометриски односи, а не на редоследот на цртање.

### Мајсторство со апсолутни и релативни големини
Професионалните дијаграми бараат фиксни димензии за ознаки (како стрелки или ознаки за агли), без разлика на скалирањето на целата слика.
*   **Користете `unitsize()` наместо `size()`:** Додека `size()` ја присилува сликата во одредена рамка, `unitsize(1cm)` му кажува на Asymptote дека една математичка единица е точно 1 сантиметар на хартијата.
*   **Трик за нескалабилни поместувања:** Ако сакате ознаката да биде секогаш 4 милиметри десно од некоја точка, дефинирајте променлива `real truecm = cm / unit;`. Ова ви овозможува да комбинирате математички координати со прецизни офсети за печатење.

### „Маскирање" на ознаки за подобра читливост
Кога линија минува директно низ текст, дијаграмот изгледа аматерски и е тежок за читање.
*   **Златно правило:** Користете го својството `filltype=Fill(white)` при креирање на `Label`. Ова ќе создаде невидлива бела кутија околу текстот која ќе ја „пресече" линијата што поминува под него, правејќи го текстот јасен и истакнат.

### Решавање на 3D преклопувања (The Layering Hack)
Во 3D просторот, честопати ознаките (Labels) делумно „затонуваат" во површините бидејќи се на иста оддалеченост од камерата.
*   **Професионален трик:** Користете сопствена функција `towardcamera(triple point, real distance)` која математички ја поместува точката малку поблиску до окото на гledaчот пред да ја постави ознаката. Ова гарантира дека текстот секогаш ќе биде „над" објектот, без да го изобличи неговото геометриско значење.

### Напредна манипулација со патеки
Професионалците користат `subpath` за да истакнат делови од веќе постоечки функции.
*   **Тангенти:** Користете `dir(path, time)` за да го добиете векторот на тангентата во која било точка. Ова е клучно за цртање на вектори на брзина или сили во физички дијаграми без рачно пресметување изводи.
*   **Специјални конектори:** Операторот `---` е одличен за поврзување на прави сегменти кои треба да останат мазни (smooth) и во три димензии, додека `^^` е есенцијален за групирање на неповрзани патеки во еден објект за побрзо рендерирање.

### Контрола на излезот за научни трудови
Ако дијаграмите се за печатење или за PDF кој нема да се ротира интерактивно:
*   **Исклучете го PRC:** Поставете `settings.prc = false;` за да избегнете проблеми со фонтовите и за да осигурате дека сликата ќе изгледа идентично во сите PDF прегледувачи.
*   **Зголемете ја резолуцијата:** За исклучително остри растерски слики, користете `settings.render = 16;` и трикот со скалирање на сликата при самиот излез: `shipout(scale(4.0)*currentpicture.fit());`.

### Ресурси кои мора да ги консултирате
*   **Asymptote Gallery:** Официјалната галерија содржи примери за речиси секој можен математички концепт, од дијаграми на Фајнман до комплексни аналитички површини.
*   **Philippe Ivaldi's Geometry Module:** Овој модул (кој доаѓа со Asymptote) содржи готови функции за симетрали, впишани кружници и специфични ознаки за прав агол кои штедат часови работа.

---

## 13. Експертски совети (30 совети за врвна прецизност)

Како професионален илустратор на техничка геометрија, мојата работа со Asymptote се заснова на прецизност, математичка логика и способност за комбинирање на скалабилни елементи со фиксни димензии за печатење. Врз основа на детална анализа на официјалната документација и туторијалите на Staats, подготвив збирка на експертски совети и кодови организирани во групи.

### ГРУПА 1: Темели на прецизноста и робусно скалирање

1.  **Користете `unitsize` наместо `size` за апсолутна геометрија:** `unitsize(1cm)` дефинира точно колку изнесува една математичка единица на хартија.
2.  **Дефинирајте `truecm` за фиксни офсети:** `truecm = cm / unit;` за комбинирање на скалабилни координати со нескалабилни маргини.
3.  **Почитувајте го „Законот на Жанет":** Никогаш не ја користите внатрешната структура на патеките - користете пресеци наместо рачни координати.
4.  **Користете `---` за автоматска мазност:** За поврзување на точки со задржување на мазност дури и низ прави сегменти.
5.  **Групирајте со `^^` за ефикасност:** Оператор за „подигнување на пенкалото" за групирање на дисконтинуирани патеки.
6.  **Автоматско центрирање во 3D:** `size3` со `keepAspect=true` за да не се деформираат 3D модели.
7.  **Релативни позиции за ознаки:** `Relative(0.5)` или `MidPoint` наместо рачно пресметани средни точки.
8.  **LaTeX конзистентност:** `defaultpen(fontsize(10pt))` за фонтот да одговара на текстот во документот.
9.  **Конфигурација на излез:** `settings.outformat = "pdf";` на почеток за избегнување проблеми со фонтови.
10. **Затворени патеки со `cycle`:** Клучен збор за правилно спојување на аглите (line join).

**Code Snippet (Robust Scaling):**
```asy
real unit = 1.2cm;
real truecm = cm / unit; // Офсет што не се менува со скалирање
unitsize(unit);
path s = (0,0)..tension 2 ..(2,1);
draw(s, L=Label("$y=f(x)$", EndPoint, align=4*truecm*E)); // Фиксна маргина
```

### ГРУПА 2: Напредна 3D Визуелизација и Осветлување

11. **Статични PDF документи со `prc = false`:** Оневозможете PRC за подобар векторски квалитет во печатени документи.
12. **Векторска 3D графика со `render = 0`:** За едноставни објекти каде острината е поважна од сенчењето.
13. **Контрола на растерска острина:** `settings.render = 16` пред вклучување на модулот `three`.
14. **Користете PBR материјали:** `material` со `diffusepen` за боја и `specularpen` за метален одсјај.
15. **Функцијата `towardcamera`:** Поместување на ознаки кон камерата за да не бидат „потопени".
16. **Ориентација со `up=Y`:** За математички графикони каде $y$ е вертикална оска.
17. **Емисивно осветлување за „рамни" бои:** `emissive(color)` за постојана боја без сенки.
18. **Апсолутни димензии за WebGL:** `settings.absolute = true` за спречување растегнување на HTML излез.
19. **Позиционирање на камерата со `dir()`:** `orthographic(dir(theta, phi))` за прецизен агол на гледање.
20. **Претворање 2D во 3D рамнина:** `path3(path, plane)` за лесно префрлање на 2D конструкции во 3D рамнини.

**Code Snippet (3D Label Hack):**
```asy
import three;
// Поместување на ознаката кон камерата
triple towardcamera(triple pt, real dist=1) {
  return pt + dist*unit(currentprojection.camera - (currentprojection.infinity ? O : pt));
}
label("$z$", towardcamera(2Z), align=N);
```

### ГРУПА 3: Геометриска анализа и математички патеки

21. **Пресеци со вертикални линии:** `times(path, x)` за прецизни точки каде функцијата поминува низ одредена $x$.
22. **Сите пресеци одеднаш:** `intersections(path, path)` враќа низа од времиња за сите допирни точки.
23. **Под-патеки за означување:** `subpath(path, t1, t2)` за исечување дел од патека со друга боја.
24. **Автоматски тангенти:** `dir(path, time)` за вектор на тангентата - есенцијално за нормали и сили.
25. **Градење циклуси со `buildcycle`:** Автоматско наоѓање затворен простор помеѓу патеки.
26. **Делонеова триангулација:** `triangulate(pair[])` за мрежа од неправилно распоредени точки.
27. **Мазни имплицитни површини:** `smoothcontour3` за поголем квалитет од стандардниот `contour3`.
28. **Екструзија на патеки:** `extrude(path, axis)` претвора 2D облик во 3D цилиндар или призма.
29. **Мазни површини со `Spline`:** Додајте `Spline` за избегнување „набрчкани" површини.
30. **Релативно време на патека:** `reltime(path, fraction)` за време базирано на вкупната должина.

**Code Snippet (Intersection Logic):**
```asy
import graph;
path s = graph(sqrt, 0, 2);
real t = times(s, 1.4); // Најди време за x=1.4
pair P = point(s, t);
draw(P -- P + 0.5*dir(s, t), blue, Arrow); // Тангента
```

### ГРУПА 4: Напредна манипулација, структури и стилска конзистентност

31. **Користете го операторот „перо-нагоре" (`^^`) за неповрзани региони:** Есенцијален за групирање на повеќе патеки во еден објект за пополнување на региони со дупки.
32. **Мајсторство со правилата за пополнување (`fillrule`):** Разлика помеѓу `zerowinding` и `evenodd` - `evenodd` е клуч за Венови дијаграми со пресеци.
33. **Хермитова (`Hermite`) интерполација за технички графици:** Избегнува осцилации кај нагли промени на функциите.
34. **Креирање на сопствени шаблони за засенчување (`hatch`):** Користете `patterns` модул за шрафура во научна визуелизација.
35. **Третирање на функциите како променливи:** Asymptote дозволува first-class functions за генератори на криви.
36. **Автоматизација на легендите со `UnFill`:** Креира бела маска околу легендата за читливост.
37. **Контрола на ознаките (`Billboard` vs `Embedded`):** `Billboard` ротира со камерата, `Embedded` лежи на површина.
38. **Напредно мешање на бои со транспарентност:** `opacity(real, string)` со blend режими ("Multiply", "Screen").
39. **Цртање на патеки со физички волумен (`tube`):** Претвора патеки во 3D цилиндри со сенки и перспектива.
40. **Организација на комплексни дијаграми преку структури (`struct`):** Групирање на елементи со методи за цртање.

**Code Snippets for Group 4:**

#### 1. Complex region with hole (evenodd rule)
```asy
import geometry;
unitsize(1cm);

path outer = circle((0,0), 2);
path inner = circle((0,0), 1);

// ^^ connects into one path, evenodd defines the hole
fill(outer ^^ inner, evenodd + lightgray);
draw(outer ^^ inner, linewidth(1pt));

label("$A = \pi(R^2 - r^2)$", (0,0));
```

#### 2. Dynamic function generation (Higher-order functions)
```asy
import graph;
size(8cm, 6cm, IgnoreAspect);

typedef real function(real);

// Function that returns another function
function generate_sin(real n) {
    return new real(real x) { return sin(n * x); };
}

for(int n=1; n <= 3; ++n) {
    draw(graph(generate_sin(n), 0, pi), Pen(n), "$\sin(" + (string)n + "x)$");
}

xaxis("$x$", BottomTop, LeftTicks);
yaxis("$y$", LeftRight, RightTicks);
attach(legend(), (point(S).x, truepoint(S).y), 10S, UnFill); // Legend with UnFill
```

#### 3. 3D labels (Embedded vs Billboard)
```asy
import three;
size(5cm);
currentprojection = orthographic(5,2,3);

// Draw plane
draw(unitplane, surfacepen=lightgray+opacity(0.5));

// Billboard label (always faces us)
label("$B$", (0.5, 0.5, 0.5), red);

// Embedded label (lies in the plane, rotates with object)
label(XY() * "$\text{Plane } XY$", (0.5, 0.1, 0), blue, Embedded);
```

#### 4. 3D "tube" along complex path
```asy
import three;
import tube;

size(5cm);
path3 path = (0,0,0) .. (1,1,1) .. (2,0,1) .. cycle;

// Create tube with radius 0.1
surface tube = tube(path, 0.1).s;
draw(tube, material(gray, emissivepen=0.2*white));

// Add arrow on path (direction indicator)
draw(path, blue+linewidth(0.5pt), Arrow3);
```

### ГРУПА 5: Моќта на `geometry.asy` за училишна геометрија

41. **Автоматски центар на триаголник:** `incenter(t)`, `orthocenter(t)`, `circumcenter(t)` за апсолутна точност на симетрали.
42. **Означување на еднакви страни:** `StickIntervalMarker` за визуелен стандард на складност во учебници.
43. **Ознака за прав агол:** `perpendicularmark` автоматски го црта симболот со правилна ротација.
44. **Тангенти на кружница:** `tangents(circle, point)` за автоматско наоѓање допирни точки.
45. **Симетрала на агол како објект:** `bisector(line, line)` креира права за понатамошни пресеци.
46. **Масовни точки:** `mass` за Чевината теорема или центар на маса.
47. **Наоѓање подножје на висина:** `foot(vertex)` за моментално наоѓање точка на спротивната страна.
48. **Радикална оска:** `radicalline(c1, c2)` за радикалната оска на две кружници.
49. **Автоматско именување темиња:** `label(triangle)` поставува $A, B, C$ со бисекторна ориентација.
50. **Конверзија помеѓу објекти:** Кружницата автоматски станува патека при цртање.

**Code Snippet (Congruence and vertices):**
```asy
import geometry;
unitsize(1cm);
triangle t = triangleabc(4, 5, 6); // Triangle with sides 4, 5, 6
draw(t, linewidth(1pt));

// Congruence marking on two sides (e.g., AC and BC)
marker congruent = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.AC), congruent);
draw(segment(t.BC), congruent);

// Altitude mark and right angle symbol
point H = foot(t.VA);
draw(t.A--H, dashed);
perpendicularmark(line(t.BC), line(t.A,H), size=0.2cm);

label(t, alignFactor=3); // Automatic A, B, C
```

### ГРУПА 6: Дидактичка јасност и технички стандарди

51. **Маскирање линии зад ознаки:** `UnFill(1mm)` создава бел простор околу текстот.
52. **Скалабилни координати, фиксни фонтови:** `unitsize()` за цртеж, апсолутни поени (bp) за текст.
53. **Конзистентни стрелки:** `Arrow(TeXHead)` имитира LaTeX математички симболи.
54. **Координатен систем за ротирана фигура:** `coordsys` за „природни" координати (0,0), (1,0).
55. **Форматирање броеви:** `format("$%.2f$", x)` за ознаки со правилни децимали.
56. **Димензионирање со `Bars`:** `bar=Bars` за должина надвор од фигурата.
57. **Релативно позиционирање:** `Relative(0.5)` за точен центар на хипотенуза.
58. **Преклопување бои:** `opacity(0.3)` за внатрешност без сокривање елементи.
59. **Глобален хедер:** `asydef` блок во LaTeX за заеднички стилови.
60. **Автоматизација со `latexmk`:** Сам препознава промени и рекомпајлира.

**Code Snippet (Text masks and dimensions):**
```asy
import graph;
unitsize(2cm);
path s = (0,0)..(1,1.5)..(2,0);
draw(s, linewidth(1pt));

// Dimension line with masked text
pair p1 = (0, -0.2), p2 = (2, -0.2);
draw(p1--p2, L=Label("$d=10\,cm$", MidPoint, filltype=UnFill(1mm)), bar=Bars);

// Point label that doesn't overlap line
dot((1,1.5));
label("$M_{max}$", (1,1.5), N, filltype=UnFill);
```

### ГРУПА 7: Стереометрија и 3D визуелизација

61. **Triple Aliases:** Вградените `O, X, Y, Z` за брзо дефинирање точки во простор.
62. **Ортографска проекција:** `orthographic` за технички цртежи каде паралелни линии остануваат паралелни.
63. **3D површини од 2D патеки:** `surface(path3)` претвора 2D нацрт во 3D рамнина.
64. **Ротациони тела:** `solids.asy` за конуси и цилиндри: `cylinder(O, r, h, axis)`.
65. **Транспарентност тела:** `material(white+opacity(0.5))` за видливи „скриени" рабови.
66. **Означување во 3D:** `towardcamera` за ознаки да не бидат пресечени од објекти.
67. **BillboardLabels:** Ознаките секогаш го гледаат ученикот, без разлика на аголот.
68. **3D агли и лакови:** `arc(triple c, triple v1, triple v2)` за агли меѓу рамнини.
69. **Слоеви во 3D:** `shift(dist*unit(camera-pt))` за „извлекување" точки напред.
70. **Висока резолуција за принт:** `settings.render=16` за мазни слики во печат.

**Code Snippet (Cylinder with transparency):**
```asy
import solids;
settings.render=16;
settings.prc=false;
size(5cm,0);
currentprojection=orthographic(5,2,3,up=Z);

// Create and draw cylinder
revolution r = cylinder(O, 1, 2, Z);
draw(r, white+opacity(0.5)); // Transparent body
draw(r.silhouette(), linewidth(1pt)); // Emphasized outer edges

// Cylinder axis
draw(O--2.5Z, blue+dashed, L=Label("$h$", EndPoint, align=N));
dot(O);
```

### ГРУПА 8: Дизајн на функции, дисконтинуитети и аналитичка прецизност

71. **Користете го `graph` модулот за аналитичка точност:** Дефинирајте `real f(real x)` и `graph(f, a, b)` за математички верна крива.
72. **Контрола оските со `YZero` и `XZero`:** `axis=YZero` за $x$-оската да поминува низ (0,0).
73. **Прилагодени поделеци за тригонометрија:** `real[] T = {0, pi/2, pi, 3*pi/2, 2*pi}` со LaTeX ознаки.
74. **Справување прекини со `bool3 cond`:** За асимптоти, користете `cond(real x)` да „подигнете пенкало".
75. **Мајсторство со `subpath` за акцентирање:** `subpath(g, t1, t2)` за истакнување дел од функција.
76. **Интерполација со `Hermite`:** За податоци со нагли промени, избегнува осцилации без надминување.
77. **Пресеци на прави и криви со `times`:** `times(g, c)` наоѓа точно време каде функција се сече со $x=c$.
78. **Автоматизација легенди со `legend()`:** `draw(g, "ознака")` и `add(legend(), ...)` за автоматско објаснување.
79. **Користете `UnFill` за читливост текст врз мрежа:** `filltype=UnFill` создава бел простор околу бројки.
80. **Напредно 3D означување во рамнини:** `XY * "текст"` за `Embedded` објект кој ротира со геометријата.

**Code Snippets for Educational Textbook:**

#### 1. Analytical graph with asymptote and shaded area
```asy
import graph;
size(8cm, 6cm, IgnoreAspect);

// Function f(x) = 1/(x-1) + x
real f(real x) { return 1/(x-1) + x; }

// Continuity condition
bool3 cond(real x) { return abs(x-1) > 0.05; }

path g = graph(f, -2, 4, cond, n=400);
draw(g, linewidth(1pt) + blue);

// Vertical asymptote
draw((1,-5)--(1,10), dashed + gray);

// Axes through zero
xaxis("$x$", YZero, Ticks(Step=1, Size=2pt));
yaxis("$y$", XZero, Ticks(Step=5, Size=2pt));
```

#### 2. Intersection of two paths (e.g., tangent to curve)
Finding intersection point without manual calculation.

```asy
import graph;
unitsize(2cm);

path curve = graph(exp, -1, 1.5);
path line = (-1, 1) -- (1.5, 3);

draw(curve, blue);
draw(line, dashed + gray);

// Finding intersections
real[][] t = intersections(curve, line);
if (t.length > 0) {
    dot(point(curve, t), red); // Intersection point
    label("Intersection", point(curve, t), SE);
}
```

#### 3. 3D text "glued" to plane (for stereometry)
Perfect for labeling angles between planes.

```asy
import three;
size(6cm);
currentprojection = perspective(5,2,3);

// Drawing the XY plane
draw(unitplane, surfacepen=emissive(lightgray + opacity(0.5)));

// Label embedded in plane (Embedded)
label(XY() * "$\Sigma$", (0.8, 0.8, 0), blue, Embedded);

// Label that always faces us (Billboard)
label("$z$", (0,0,1.2), red);
draw(O--1.2Z, red, Arrow3);
```

#### 4. Highlighting part of path (Subpath)
Useful for explaining arc of circle or part of parabola.

```asy
import graph;
unitsize(1cm);

path p = (0,0){up} .. (2,3) .. (4,0);
draw(p, gray + linewidth(0.5pt)); // Full path

// Highlight segment from time 0.5 to 1.5
path highlight = subpath(p, 0.5, 1.5);
draw(highlight, linewidth(1.5pt) + orange);
dot(point(p, 0.5), orange);
dot(point(p, 1.5), orange);
```

### ГРУПА 9: Еуклидски конструкции, складност и дидактичка јасност

81. **Користете го типот `triangle` за апстрактна геометрија:** Дефинирајте `triangle t = triangle(A, B, C);` за пристап до својства како `t.AB` (страна) или `t.VA` (теме).
82. **Означување складност со `StickIntervalMarker`:** `marker(stickframe(n=2))` за две цртички (ticks) на средина - меѓународен стандард за еднакви страни.
83. **Автоматизирајте ортогонални пресеци:** `foot(t.VC)` автоматски наоѓа точка каде паѓа нормала од темето $C$.
84. **Прецизни агли со `markangle`:** `markangle` овозможува еден, два или три лаци за означување еднакви агли со стрелки.
85. **Користете `perpendicularmark` за прав агол:** Автоматски црта симбол за прав агол на пресек без рачно квадрати.
86. **Контрола дебелина пенкало според хиерархија:** Главни објекти `linewidth(1.2pt)`, помошни `dashed + gray`.
87. **Маскирање ознаки со `UnFill`:** `filltype=UnFill` создава бел круг околу букви за читливост врз линии.
88. **Динамичко пресметување тежиште:** `centroid(t)` или `incenter(t)` за математичка точност без рачни пресметки.
89. **Справување бесконечни прави преку `drawline`:** `drawline(A, B)` црта права до работ на слика без менување платно.
90. **Користете `arcsubtended` за геометриски локус:** Црта кружни лак под кој се гледа отсечка $AB$ под одреден агол.

**PROBLEM ID: Triangle Construction with Properties (Group 9 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// 1. Define triangle
triangle t = triangleabc(5, 6, 7);
draw(t, linewidth(1.2pt));

// 2. Label vertices
label(t, alignFactor=3);

// 3. Construct altitude and right angle
point H = foot(t.VC);
draw(t.C--H, dashed + blue);
perpendicularmark(line(t.AB), line(t.C, H), size=0.2cm, p=blue);

// 4. Mark equal parts on base
// Assuming we want to mark congruence of two segments
marker m = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.A, H), m);
draw(segment(H, t.B), m);

// 5. Mark angle
markangle("$\alpha$", n=1, t.B, t.A, t.C, radius=0.6cm, p=red);
```

**NANO BANANA PROMPT:**
`Detailed pencil sketch on parchment paper of a classic Euclidean geometry construction, showing a triangle with compass markings and circular arcs, vintage scientific illustration style, warm sepia lighting, 3:2, No Text.`

---

**PROBLEM ID: Circumscribed Circle and Peripheral Angles (Group 9 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

// 1. Create circle and triangle
point A = (0,0), B = (4,0), C = (1,3);
triangle t = triangle(A, B, C);
circle c = circumcircle(t);

draw(c, lightgray);
draw(t);

// 2. Label center
point O = c.C;
dot("$O$", O, S, p=red);

// 3. Use UnFill for readability
label("$R$", (O+C)/2, UnFill(1mm));

// 4. Mark angles on same arc
markangle("$\beta$", B, C, A, radius=0.4cm, p=blue);
```

**NANO BANANA PROMPT:**
`A glowing neon geometric constellation in deep space, forming perfect triangular and circular patterns, cinematic starfield background, vibrant blue and magenta lighting, 16:9, No Text.`

### ГРУПА 10: Професионален работен процес, дебагирање и автоматизација

91. **Интегрирајте код директно во LaTeX со `asymptote.sty`:** Пишувајте Asymptote во `.tex` со `\begin{asy}...\end{asy}` за илустрации и текст на едно место.
92. **Автоматизирајте со `latexmk` и `latexmkrc`:** `latexmk` препознава промени и рекомпајлира само изменети дијаграми.
93. **Користете `asypictureB` за полесно дебагирање:** Репакува Asymptote грешки како LaTeX грешки за брзо наоѓање проблеми.
94. **Експлицитно решавање равенки со `extension`:** `extension(P, Q, p, q)` за експлицитни пресеци без автоматско решавање.
95. **Прецизна контрола ознаки преку bidirectional pipe:** Asymptote комуницира со TeX во два премина за точна големина.
96. **Прилагодете дебелина точки со `dotfactor`:** Стандард 6; за средно образование намалете на 4 за помалку масивни точки.
97. **Глобална стандардизација со `asydef`:** Дефинирајте заеднички стилови во LaTeX за конзистентност низ учебник.
98. **Постигнете максимална острина со `shipout(scale)`:** `shipout(scale(4.0)*currentpicture.fit())` за висококвалитетни растерски слики.
99. **Маскирање позадина со `UnFill`:** `filltype=UnFill` создава дупка во објекти под ознака.
100. **Изберете правилен излезен формат:** `pdf` за чиста 2D геометрија, `png` со висок `render` за сложени 3D површини.

**PROBLEM ID: Professional Textbook Template (Group 10 Example)**

**ASYMPTOTE CODE:**
```asy
// Settings for professional printing
settings.outformat = "pdf";
settings.prc = false;
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Global definitions (imitating asydef)
pen helper_line = dashed + gray(0.4);
pen main_line = black + linewidth(1.2pt);
real unit_size = 1.5cm;
unitsize(unit_size);

// Construction: Triangle and incircle
point A=(0,0), B=(4,0), C=(1,3);
triangle t = triangle(A, B, C);
circle ic = incircle(t);

// Drawing with line hierarchy
draw(t, main_line);
draw(ic, blue);

// Using UnFill for label readability on lines
label("$A$", A, SW, UnFill(1mm));
label("$B$", B, SE, UnFill(1mm));
label("$C$", C, N, UnFill(1mm));

// Labeling radius with Bars
point O = ic.C;
point T = intouch(t.AB);
draw(O--T, helper_line);
label("$r$", (O+T)/2, E, UnFill);
dot(O, red);

// Increasing resolution at output
shipout(scale(4.0)*currentpicture.fit());
```

**NANO BANANA PROMPT:**
`High-end macro photography of a mathematical textbook page, showing a sharp geometric diagram of a triangle and circle, soft sunlight hitting the paper texture, clean bokeh background, minimalist scholarly aesthetic, 16:9, No Text.`

---

**PROBLEM ID: 3D Layer Simulation (Group 10 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
settings.render = 16;
import three;
import solids;

// Projection adjustment for technical display
currentprojection = orthographic(5,2,3, up=Y);
currentlight = Headlamp;

// Drawing 3D sphere and axes
draw(unitsphere, white + opacity(0.6));
draw(O--1.5X, black, L=Label("$x$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Y, black, L=Label("$y$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Z, black, L=Label("$z$", position=EndPoint), arrow=Arrow3(TeXHead2));

// Moving label toward camera to avoid intersection
triple towardcamera(triple pt, real dist=0.1) {
  return pt + dist*unit(currentprojection.camera - pt);
}

dot(towardcamera(Z), red);
label("$P(x,y,z)$", towardcamera(Z), N, blue);
```

**NANO BANANA PROMPT:**
`3D wireframe glass sphere floating in a dark laboratory, laser beams as coordinate axes, cinematic blue lighting, holographic aesthetic, high-tech educational visualization, 3:2, No Text.`

### ГРУПА 11: Педагошка визуелизација, виткави загради и напредна типографија

101. **Креирајте виткави загради за интервали:** `brace(pair a, pair b)` за математички прецизни виткави загради над сегменти.
102. **Користете `minipage` за комплексни описи:** `minipage(text, width)` за форматирање блокови текст со фиксна ширина во ознаки.
103. **Обезбедете конзистентност фонтот со `defaultpen`:** `defaultpen(fontsize(10pt))` за ознаки со иста големина како текст во учебник.
104. **Применете `basealign` за порамнување математички изрази:** `basealign` за совршени базни линии на формули една до друга.
105. **Управувајте слоевите преку `layer()`:** `layer()` за PostScript објекти да се појават над ознаки или TeX команди.
106. **Искористете `unfill` за читливост легендите:** Клипинг за маскирање позадина на легенди врз густ графикон.
107. **Динамично проширување границите со `addBox`:** `pic.addBox` за ажурирање граници на слика со unscalable елементи.
108. **Интегрирајте TeX макроа преку `@` префиксот:** `@the@linewidth` со `asypictureB` за автоматско прилагодување на страница.
109. **Означување агли со стрелки:** `markangle` со `Arrow` за насока ротација или позитивна насока аголот.
110. **Контрола дебелина „мрежните" линии:** `thin()` за линии видливи како еден пиксел независно од зум.

**PROBLEM ID: Segment Visualization with Curly Brace (Group 11 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Function for curly brace
path brace(pair a, pair b, real amplitude = 0.14) {
    real d = length(b-a);
    transform t = shift(a) * rotate(degrees(atan2((b-a).y, (b-a).x)));
    path br = (0,0){expi(radians(70))} :: {expi(0)}(d/4, amplitude*d/2)
               :: {expi(radians(60))} (d/2, amplitude*d) {expi(radians(-60))}
               :: {expi(0)}(3*d/4, amplitude*d/2) :: {expi(radians(-70))} (d,0);
    return t * br;
}

// Segment construction and labeling
pair A = (0,0), B = (5,0);
draw(A--B, linewidth(1.2pt));
dot(A); dot(B);

// Adding curly brace below segment
path b = brace(B, A, 0.1); // Swap A and B for downward direction
draw(b, blue);
label("$d = 5.0 cm$", MidPoint, align=S, p=blue);

// Using minipage for definition
label(minipage("\raggedright \textbf{Definition:}\\A line segment is part of a line bounded by two points.", 4cm), (2.5, 1.5), UnFill);
```

**NANO BANANA PROMPT:**
`A macro photograph of an architect's drafting table, focus on a metallic compass tracing a perfect arc on a blueprint, blueprint lines glowing faintly in cyan, soft morning sunlight, cinematic perspective, 16:9, No Text.`

---

**PROBLEM ID: Aligning Mathematical Formulas in Diagram (Group 11 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import graph;

// Baseline alignment
pair O = (0,0);
dot(O);

// Drawing with basealign for perfect symbol alignment
label("$\alpha = 30^\circ$", O, align=N, basealign);
label("$\gamma = 90^\circ$", O, align=S, basealign);
label("$f(x) = \sqrt{x}$", O, align=E, basealign);

// Using layer() for drawing over text if needed
layer();
draw(circle(O, 0.5cm), red+dashed);
```

**NANO BANANA PROMPT:**
`A clean blackboard with complex mathematical geometry formulas written in crisp white chalk, high contrast, studio lighting, academic and scholarly aesthetic, minimalist composition, 3:2, No Text.`

### ГРУПА 12: Напредна координатна логика, оптимизација и конзистентност

111. **Разликувајте `size()` и `unitsize()` за фиксни размери:** `unitsize(1cm)` за една единица = точно 1cm на хартија; `size()` само вклопува во рамка.
112. **Користете `coordsys` за природни координати:** `cartesiansystem` за работа во ротиран систем со релативни точки.
113. **Оптимизирајте перформанси со `guide` во циклуси:** `guide` за линеарно време наместо квадратно кај `path` додавање.
114. **Мајсторство `subpath` и пресеци за дидактички приказ:** `intersections()` за точки допир, `subpath()` за исечување сегменти.
115. **Контрола дебелина ознаки со `dotfactor`:** Намалете од 6 на 4 за естетски подобри точки во средно образование.
116. **Автоматизирајте цртање агли со `markangle`:** `markangle` со stick marks за еднаквост на агли.
117. **Користете `emissive` материјали за чисти 3D илустрации:** `emissivepen` за постојана боја без сенки.
118. **Порамнување математички изрази со `basealign`:** `basealign` за совршени базни линии на формули.
119. **Користете `asypictureB` за веднаш гледате грешки:** Репакува Asymptote грешки во LaTeX лог за брзо дебагирање.
120. **Максимална резолуција со `shipout(scale)`:** `shipout(scale(4.0)*currentpicture.fit())` за остри растерски слики.

**Code Snippets for Advanced Coordination:**

#### 1. Using custom coordinate systems (coordsys)
```asy
import geometry;
unitsize(1cm);

// Define rotated coordinate system
coordsys R = cartesiansystem((2,1), i=rotate(30)*E, j=rotate(30)*N);
show(R, ipen=blue); // Visualize axes

// Points defined relative to new system
point A = point(R, (0,0));
point B = point(R, (3,0));
point C = point(R, (1,2));

draw(A--B--C--cycle, linewidth(1.2pt));
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, N);
```

#### 2. Precise angle and congruence marking
```asy
import geometry;
unitsize(1.5cm);

triangle t = triangleabc(4, 4, 5);
draw(t);

// Congruence marking on two sides
marker m = marker(stickframe(n=2, size=3));
draw(segment(t.AC), m);
draw(segment(t.BC), m);

// Marking equal angles
markangle("$\alpha$", n=1, t.B, t.A, t.C, radius=0.5cm, p=red);
markangle("$\alpha$", n=1, t.A, t.B, t.C, radius=0.5cm, p=red);
```

#### 3. 3D sphere with "clean" (emissive) lighting
```asy
import three;
settings.render = 16; // High resolution
settings.prc = false;
size(5cm, 0);

currentprojection = orthographic(5,2,3); // Technical projection

// Sphere with emissive color independent of light angle
material m = material(diffusepen=white+opacity(0.6), emissivepen=gray(0.3));
draw(unitsphere, surfacepen=m);

// Axes with 3D arrows
draw(O--1.5X, arrow=Arrow3(TeXHead2), L=Label("$x$", position=EndPoint));
draw(O--1.5Y, arrow=Arrow3(TeXHead2), L=Label("$y$", position=EndPoint));
draw(O--1.5Z, arrow=Arrow3(TeXHead2), L=Label("$z$", position=EndPoint));
```

### ГРУПА 13: Типографска конзистентност и „Светата врска" со LaTeX

121. **Никогаш не скалирајте слика во LaTeX:** Дефинирајте финална големина во Asymptote со `size()` или `unitsize()` - скалирање во LaTeX деформира фонт на ознаки.
122. **Користете `asymptote` пакет со `inline` опција:** 2D LaTeX симболи надвор од Asymptote код видливи, но додајте рачна проценка за големина во `Label`.
123. **Централизирајте стил преку `asydef`:** `\begin{asydef}...\end{asydef}` во LaTeX за заеднички `import geometry;`, фонтови, бои - конзистентност низ сите дијаграми.
124. **Принудете порамнување со `basealign`:** Естетски совршени формули со совршени базни линии на TeX карактери.
125. **Користете `texpreamble` за специјални пакети:** `\usepackage{bm}` во `texpreamble` за болд математички фонтови достапни во ознаки.
126. **Двонасочната комуникација (Bidirectional Pipe):** Asymptote комуницира со TeX во два премини - прво дознава големина на ознаки, потоа ги поставува.
127. **Управување дебелина точки (`dotfactor`):** Намалете од стандардни 6 на 4 за елегантни точки кои не доминираат.
128. **Автоматизирајте цртање висини со `foot`:** `pair H = foot(A, B, C);` за математички перфектен симбол за прав агол.
129. **Користете `minipage` за долги дефиниции:** `minipage(text, width)` форматира блок текст со правилна ширина во сликата.
130. **Стандардизирајте стрелки на оски:** `Arrow(TeXHead)` или `Arrow(TeXHead2)` одговараат на LaTeX математички стрелки.

**PROBLEM ID: Triangle Illustration with Angle and Congruence (Group 13 Example)**

**ASYMPTOTE CODE:**
```asy
// Professional printing settings for textbook
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Global adjustment
dotfactor = 4; // Elegant vertex points

// Construction: Triangle with congruence marking
point A=(0,0), B=(4,0), C=(1,3);
triangle t = triangle(A, B, C);

draw(t, linewidth(1.2pt));

// Congruence marking on equal sides
marker m = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.AC), m);
draw(segment(t.BC), m);

// Angle marking
markangle("$\alpha$", t.B, t.A, t.C, radius=0.6cm, p=red);

// UnFill for vertex labels
label("$A$", t.A, SW, UnFill(1mm));
label("$B$", t.B, SE, UnFill(1mm));
label("$C$", t.C, N, UnFill(1mm));

// Textual description in minipage
label(minipage("\raggedright Given triangle $ABC$ which is isosceles, i.e., $AC = BC$.", 3cm), (4.5, 2.5), UnFill);
```

**NANO BANANA PROMPT:**
`A hyper-realistic studio shot of an open geometry textbook on a wooden desk, focus on a sharp black and white diagram of a triangle, high-quality printing texture on paper, soft morning window light, scholarly aesthetic, 16:9, No Text.`

---

**PROBLEM ID: Stereometry and 3D Projection (Group 13 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
settings.render = 16; // High resolution for printing
settings.prc = false; // Static vector image

import three;
import solids;

// Orthographic projection for parallelism
currentprojection = orthographic(5,2,3, up=Z);

// Drawing sphere and axes
draw(unitsphere, white + opacity(0.5));
draw(O--1.5X, L=Label("$x$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Y, L=Label("$y$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Z, L=Label("$z$", position=EndPoint), arrow=Arrow3(TeXHead2));

// Moving point toward camera for better visibility
triple towardcamera(triple pt, real dist=0.15) {
  return pt + dist*unit(currentprojection.camera - pt);
}

dot(towardcamera(Z), red);
label("$P(0,0,1)$", towardcamera(Z), N, blue);
```

**NANO BANANA PROMPT:**
`A complex mathematical 3D wireframe hologram of a sphere and coordinate system, floating in a futuristic dark classroom, cinematic lighting, blue neon glows, high-tech educational concept, 3:2, No Text.`

---

## Збирка на Кодни Фрагменти (Code Snippet Collection)

Како технички илустратор за едукативна геометрија, подготвив архива со кодни фрагменти (snippets) базирани на претходно утврдените експертски групи. Овие фрагменти се оптимизирани за директно вметнување во вашиот работен процес, користејќи ги најдобрите практики од документацијата за Asymptote и LaTeX интеграцијата.

### ГРУПА 1: Темели на прецизноста и робусно скалирање

**Snippet 1.1: Дефинирање на „true" димензии (Unscalable Offset)**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));

real unit = 1.5cm; // 1 единица = 1.5cm
unitsize(unit);
real truecm = cm/unit; // Конвертор за фиксни димензии

pair A = (0,0), B = (3,0);
draw(A--B);

// Ознаката ќе биде секогаш точно 0.5cm под линијата
label("$d = 3$", (A+B)/2, align=0.5*truecm*S);
```

**Snippet 1.2: Автоматско наоѓање точки преку „times"**
```asy
import graph;
path s = (0,0){up} .. (1,1.5) .. (2,1); // Некоја крива
real x_pos = 1.2;
real t = times(s, x_pos); // Го наоѓа „времето" на патот за x=1.2
pair P = point(s, t);

draw(s, blue);
dot(P, red); // Точката е математички прецизна
```

### ГРУПА 2: Напредна 3D Визуелизација и Осветлување

**Snippet 2.1: TowardCamera Label Hack**
```asy
import three;
// Функција за поместување на ознаката малку кон камерата
triple towardcamera(triple pt, real dist=0.1) {
  return pt + dist*unit(currentprojection.camera - pt);
}

currentprojection = orthographic(5,2,3);
draw(unitsphere, white+opacity(0.6));
// Ознаката нема да се сече со сферата
dot(towardcamera(Z), red);
label("$P$", towardcamera(Z), N);
```

**Snippet 2.2: Емисивни материјали за технички нацрт**
```asy
import three;
material m = material(diffusepen=white, emissivepen=gray(0.2));
draw(unitcube, surfacepen=m); // Чист приказ без црни сенки
```

### ГРУПА 5: Моќта на `geometry.asy` (High School Geometry)

**Snippet 5.1: Автоматска висина и прав агол**
```asy
import geometry;
unitsize(1cm);
triangle t = triangleabc(4, 5, 6);
draw(t);

point H = foot(t.VC); // Подножје на висината од темето C
draw(t.C--H, blue+dashed);
// Автоматски симбол за прав агол
perpendicularmark(line(t.AB), line(t.C, H), size=0.2cm, p=blue);
```

**Snippet 5.2: Означување на еднакви страни (Congruence)**
```asy
import geometry;
point A=(0,0), B=(3,0), C=(1.5, 2.5);
// Ознака со две цртички (StickIntervalMarker)
marker складна = marker(stickframe(n=2, size=3, space=2));
draw(A--C, складна);
draw(B--C, складна); // Означува дека триаголникот е рамнокрак
```

### ГРУПА 6: Дидактичка јасност (Masking & Dimensions)

**Snippet 6.1: Маскирање на линии зад ознаки (UnFill)**
```asy
unitsize(2cm);
path s = (0,0) .. (2,1);
draw(s, linewidth(1pt));

// Текстот „сече" дупка во линијата под него
label("$x + y = 10$", relpoint(s, 0.5), filltype=UnFill(1mm));
```

**Snippet 6.2: Димензионални линии со Bars**
```asy
unitsize(1cm);
pair p1=(0,0), p2=(4,0);
// drawline со стрелки и вертикални бариери (Bars)
draw(p1-(0,0.5)--p2-(0,0.5), L=Label("$a=4$", MidPoint, align=S),
     arrow=Arrows(TeXHead), bar=Bars);
```

### ГРУПА 10: Автоматизација и Работен Процес (Workflow)

**Snippet 10.1: Глобален asydef за учебник**
```latex
\begin{asydef}
// Глобални нагодувања за целиот учебник
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt)); // Фонт од LaTeX
pen help_lines = dashed + gray(0.5);
\end{asydef}
```

**Snippet 10.2: Максимална острина (Resolution Hack)**
```asy
// Зголеми ја резолуцијата за 4 пати пред генерирање PDF
shipout(scale(4.0)*currentpicture.fit());
```

### ГРУПА 7: Стереометрија и прецизни 3D тела

**Snippet 7.1: Ротационо тело со скелет (Конус/Цилиндар)**
```asy
import solids;
size(5cm,0);
currentprojection=orthographic(5,2,3);

// Дефинирање на оска и профилна патека
path3 профил = (0,0,0)--(1,0,0)--(1,0,2);
revolution тело = revolution(профил, Z);

// Цртање со нагласување на скелетот за техничка јасност
draw(тело, lightgray+opacity(0.4));
draw(тело.silhouette(), linewidth(1pt));
draw(тело.transverse.back, dashed); // Скриени линии
```

### ГРУПА 8: Аналитичка прецизност и функции

**Snippet 8.1: Справување со дисконтинуитети (`bool3 cond`)**
```asy
import graph;
size(6cm, 4cm, IgnoreAspect);

real f(real x) { return 1/x; }
// Услов: не цртај ако x е премногу блиску до 0
bool3 cond(real x) { return abs(x) > 0.1; }

path g = graph(f, -2, 2, cond, n=400);
draw(g, blue+linewidth(1pt));
xaxis("$x$", Arrow); yaxis("$y$", Arrow);
```

### ГРУПА 9: Еуклидски структури (Апстрактна геометрија)

**Snippet 9.1: Автоматски карактеристични точки на триаголник**
```asy
import geometry;
unitsize(1cm);

triangle t = triangleabc(5, 6, 7);
draw(t);

// Наоѓање на тежиште и Gergonne точка
point G = centroid(t);
point Ge = gergonne(t);

dot("$G$", G, NE, red);
dot("$G_e$", Ge, SW, blue);
label(t); // Автоматско A, B, C
```

### ГРУПА 11: Педагошки контекст и типографија

**Snippet 11.1: Виткава заграда (Brace) за означување интервали**
```asy
// Рачно дефинирана функција за brace
path brace(pair a, pair b, real amplitude = 0.14*length(b-a)) {
    real d = length(b-a);
    transform t = shift(a)*rotate(degrees(atan2((b-a).y,(b-a).x)));
    return t * ((0,0){expi(radians(70))} :: {expi(0)}(d/4, amplitude/2)
               :: {expi(radians(60))}(d/2, amplitude) :: {expi(0)}(3*d/4, amplitude/2)
               :: {expi(radians(-70))}(d,0));
}

draw((0,0)--(5,0));
draw(brace((5,-0.2), (0,-0.2)), blue); // Заграда под линијата
label("$d=5$", (2.5, -0.5), blue);
```

### ГРУПА 12: Напредна координатна логика

**Snippet 12.1: Локален координатен систем (`coordsys`)**
```asy
import geometry;
unitsize(1cm);

// Креирање ротиран систем
coordsys R = cartesiansystem((2,2), i=rotate(30)*E, j=rotate(30)*N);
show(R, ipen=blue); // Оските на локалниот систем

// Точката е дефинирана како (1,1) во локалниот систем R
point P = point(R, (1,1));
dot("$P_R(1,1)$", P, NE);
```

### ГРУПА 13: LaTeX конзистентност и порамнување

**Snippet 13.1: Порамнување на математички формули (`basealign`)**
```asy
defaultpen(fontsize(12pt));
pair P = (0,0), Q = (2,0);

// basealign гарантира типографско порамнување
label("$\alpha = \pi$", P, N, basealign);
label("$a = 3,5$", Q, N, basealign);

draw(P--Q, dashed);
```

**NANO BANANA PROMPT ЗА ЦЕЛОСНАТА АРХИВА:**
`A professional architectural library bookshelf filled with clean white binders labeled with geometric icons, 3D holographic wireframe of a dodecahedron floating in the center, modern studio lighting with cyan accents, cinematic wide shot, 16:9, No Text.`

---

## Едукативни Реконструкции на Дијаграми

Како технички илустратор фокусиран на прецизна геометриска реконструкција за образовни цели, ги анализирав дијаграмите од **страна 15** на материјалот **Karekök Sıfır Geometri 2023**.

Во продолжение се Asymptote кодовите за рекреирање на трите клучни илустрации од оваа страница, следејќи ги специфичните избори за стил и професионален изглед.

### PROBLEM ID: Köşetaşı 1.3 (Концепт на Симетрала и Прав Агол)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

// Димензии на платното
size(200, 100);

// Дефинирање на точките на главната права
point O = (0,0);
point A = (-100, 0);
point F = (100, 0);

// Поставување на зраците според аглите од задачата
// OC и OD се под прав агол (90 степени)
point C = 80*dir(135);
point D = 80*dir(45);
point B = 80*dir(157.5); // Симетрала на AOC
point E = 80*dir(22.5);  // Симетрала на DOF

// Цртање на главната права и зраците
draw(A--F, black);
draw(O--B, black);
draw(O--C, black);
draw(O--D, black);
draw(O--E, black);

// Додавање ознаки за темињата
label("$A$", A, W);
label("$O$", O, S);
label("$F$", F, E);
label("$B$", B, NW);
label("$C$", C, N);
label("$D$", D, N);
label("$E$", E, NE);

// Означување на прав агол
perpendicularmark(line(O,C), line(O,D), size=0.2cm);

// Означување на еднакви агли (Симетрали)
// Агли означени со точки
markangle(n=1, C, O, B, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, B, O, A, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));

// Агли означени со цртички
markangle(n=1, F, O, E, radius=15, p=blue, StickIntervalMarker(1,1,size=3));
markangle(n=1, E, O, D, radius=15, p=blue, StickIntervalMarker(1,1,size=3));

dot(O);
```

**NANO BANANA PROMPT:**
`Technical blueprint of a complex sunburst geometric pattern, mathematical symmetry lines, architectural drafting style, clean white background, soft studio lighting, 16:9, No Text.`

### PROBLEM ID: Задача 3 (Геометрија на закачалка за облека)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 200);

// Главни точки на конструкцијата
point O = (0,0);
point C = (-80, 0); // Паралелно со земјата
point A = 80*dir(230);
point B = 80*dir(50); // A, O, B се колинеарни
point D = 80*dir(310); // m(AOC) = m(AOD)

// Цртање на линиите
draw(C--O, black+linewidth(1.5pt));
draw(A--B, black+linewidth(1.5pt));
draw(O--D, black+linewidth(1.5pt));

// Помошна линија за земја (паралелна)
draw(shift(0,-20)*(-100,0--100,0), gray+dashed);

// Лабели
label("$C$", C, W);
label("$O$", O, NE);
label("$A$", A, SW);
label("$B$", B, NE);
label("$D$", D, SE);

// Означување на еднакви агли m(AOC) = m(AOD)
markangle(n=1, C, O, A, radius=15, p=red, StickIntervalMarker(1,1));
markangle(n=1, A, O, D, radius=15, p=red, StickIntervalMarker(1,1));

// Означување на BOC = 130 степени
markangle("$130^\circ$", B, O, C, radius=25, p=blue);

dot(O);
```

**NANO BANANA PROMPT:**
`Minimalist industrial design of a metallic clothes drying rack, sharp geometric shadows on a concrete floor, artistic photography, high contrast lighting, 3:2, No Text.`

### PROBLEM ID: Концепт за Агол со испрекината линија (B, C, D, A)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 150);

// Точки според Source
point B = (0,0);
point C = (100, 0);
point A = 100*dir(-60);
point D = 80*dir(-25);

// Цртање зраци со стрелки
draw(B--C, Arrow(TeXHead));
draw(B--A, Arrow(TeXHead));
draw(B--D, dashed+blue, Arrow(TeXHead)); // Испрекината линија (симетрала)

// Лабели
label("$B$", B, NW);
label("$C$", C, E);
label("$A$", A, S);
label("$D$", D, E);

// Означување агли со точки
markangle(n=1, C, O=B, D, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, D, O=B, A, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));

dot(B);
```

**NANO BANANA PROMPT:**
`An open ancient scroll with hand-drawn geometric calculations, ink quill strokes, warm candle lighting, cinematic depth of field, macro photography, 16:9, No Text.`

---

## Препорака за работен процес (Workflow)
1.  **Скриптирање:** Користете `config.asy` за глобални нагодувања (како `outformat="pdf"`) за да не ги пишувате во секој фајл.
2.  **LaTeX интеграција:** Користете го пакетот `asymptote.sty` за да го пишувате кодот директно во вашите научни трудови.
3.  **Прецизност:** Секогаш претпочитајте `unitsize()` пред `size()` кога димензиите на објектите мора да бидат апсолутни и непроменливи при скалирање.
4.  **Дебагирање:** Користи го интерактивниот мод (`asy -V`) за брза проверка на визуелниот резултат без постојано компајлирање на целиот документ.
5.  **Ефикасност:** За големи проекти, користете `guide` наместо `--` во циклуси и `static` за мемориска оптимизација.
6.  **Квалитет:** За финални излези, применувајте `scale()` пред `shipout()` за максимална острина.
7.  **Професионалност:** Следете ги експертските совети за робусност, 3D визуелизација и геометриска анализа.
# Професионален водич за Asymptote - Технички дијаграми

Ова е детален водич и збирка на кодови (snippets) наменети за професионални илустратори и инженери кои го користат **Asymptote** за креирање технички дијаграми со висок квалитет. Како технички геометриски илустратор, овие алатки се основа за прецизност, конзистентност и професионален изглед.

---

## 1. Основни конфигурации (The Preamble)
Секој професионален проект започнува со дефинирање на форматот и основните стилови за да се обезбеди униформност.

```asy
// Поставување на излезниот формат во PDF за векторски квалитет
settings.outformat = "pdf";

// Оневозможување на интерактивното 3D за статични документи (постабилно за LaTeX)
settings.prc = false;

// Вклучување на основните математички и графички модули
import graph;
import geometry;
import three; // За 3D работа

// Дефинирање на фонт и големина според стандардите на документот
defaultpen(fontsize(10pt));
```

---

## 2. Манипулација со патеки (Path Mastery)
Патеките се јадрото на секој дијаграм. Разликата меѓу `--` и `..` е клучна за визуелниот впечаток.

*   **Прецизно поврзување:** Користете `cycle` за затворени форми и `^^` за неповрзани патеки кои се цртаат со еден „пен".
*   **Тензија на криви:** Операторот `::` овозможува помазна крива со помалку осцилации (`..tension atleast 1..`).

```asy
// Креирање на сложена крива со специфични насоки (tangents)
path s = (0,0){up} .. (1,1) .. {right}(2,0);

// Илустрација на "Law of Janet": Користете променливи за патеки за лесно менување
path boundary = (0,0) -- (100,0) -- (100,50) -- (0,50) -- cycle;
draw(boundary, linewidth(1pt) + blue);
```

---

## 3. Професионално означување (Labels & Arrows)
Во професионалните дијаграми, стрелките и ознаките мора да бидат јасни и естетски усогласени со LaTeX.

*   **Стил на стрелки:** Се препорачува `TeXHead` за совпаѓање со математичките симболи во текстот.
*   **Позиционирање:** Користете `Relative()` за ознаки кои следат одреден процент од должината на патеката.

```asy
// Стрелка со LaTeX стил и ознака на крајот
draw((0,0)--(2,0), L=Label("$x$", position=EndPoint, align=E), arrow=Arrow(TeXHead));

// Ознака со позадина (Fill) за да не се преклопува со линиите
label("$f(x)$", (1,1), filltype=Fill(white));

// Димензионални линии со бариери (Bars)
draw((0,1)--(2,1), L=Label("$d$", MidPoint, align=N), bar=Bars);
```

---

## 4. Геометриска прецизност (Intersections & Analysis)
Наместо рачно пресметување на точки, користете го вградениот систем за анализа.

```asy
// Наоѓање на пресек меѓу две криви
real[][] t = intersections(path1, path2);
if(t.length > 0) {
    dot(point(path1, t)); // Точка на првиот пресек
}

// Извлекување на дел од патека меѓу две точки (Subpath)
path segment = subpath(s, t, t);
draw(segment, red + linewidth(1.5pt));
```

---

## 5. Напредно 3D моделирање
За 3D дијаграми, клучот е во проекцијата и осветлувањето.

*   **Проекција:** `orthographic` е често подобра за технички цртежи бидејќи ги зачувува паралелните линии.
*   **Осветлување:** Користете `nolight` за графикони каде боите треба да бидат идентични како во 2D.

```asy
// Поставување на поглед (Camera) и "Up" вектор
currentprojection = orthographic(5, 2, 3, up=Y);

// Површина на ротација - исклучително моќна алатка за пресметковна геометрија
surface rev = surface(path3_curve, c=O, axis=X);
draw(rev, white + opacity(0.8), meshpen=gray(0.2));
```

---

## 6. Математичка контрола на пресеци и патеки
Наместо рачно одредување на координати, професионалната работа се потпира на вградените функции за анализа на патеки.

*   **Наоѓање на сите пресеци:** Функцијата `intersections(path, path)` е клучна за сложени дијаграми каде треба да најдете точки на допир помеѓу криви. Таа враќа низа од вредности за „времето" на патеката, кои потоа се користат за цртање под-патеки.
*   **Законот на Жанет (Law of Janet):** Ова е професионално правило кое вели дека откако ќе се креира една патека, таа не треба да се користи на начин кој зависи од тоа како била дефинирана (на пр. рачно внесени точки), туку преку функции како `times()` за вертикални пресеци или `intersect()` за пресеци со други фигури.
*   **Под-патеки (subpath):** Користете `subpath(path, real, real)` за да извлечете специфичен дел од крива, што е неопходно при означување на агли или делови од функции кои се преклопуваат.

---

## 7. Софистицирано 3D моделирање и материјали
Професионалните 3D дијаграми бараат фина контрола на светлината и перспективата за да се постигне јасност.

*   **Физички базирано рендерирање (PBR):** Користете ја структурата `material` за да дефинирате како површините реагираат на светлина преку `diffusepen` (дифузно одбивање), `emissivepen` (внатрешен сјај) и `specularpen` (одрази).
*   **Техничко осветлување:** Честопати за технички цртежи е подобро да се користи `light=nolight` во комбинација со `emissivepen`, за да се избегнат несакани сенки кои можат да ги сокријат важните детали или ознаки.
*   **Ориентација на камерата:** Користете `currentprojection = orthographic(...)` за технички цртежи каде паралелните линии мора да останат паралелни, или `perspective(...)` за реалистични прикази. Поставувањето на векторот `up=Y` (или друг специфичен вектор) е клучно за правилно позиционирање на оските.

---

## 8. Напредни техники за сенчење (Shading)
Сенчењето е најмоќниот начин за визуелизација на податоци во 2D и 3D.

*   **Gouraud и Tensor сенчење:** За мазни премини на бои во триаголни или четириаголни мрежи, користете `gouraudshade()` и `tensorshade()`. Овие функции овозможуваат дефинирање на бои во темињата, што е стандард за научна визуелизација.
*   **Lattice Shading:** Овозможува креирање на градиентна мрежа преку дводимензионална низа од бои (`pen[][]`), што е идеално за комплексни позадини.

---

## 9. Позиционирање на ознаки во 3D простор
Еден од најголемите предизвици е ознаките (Labels) да не бидат „потопени" во 3D објектите.

*   **Функција „кон камерата":** Професионалците користат сопствени функции како `towardcamera(triple, real)` за да ги поместат ознаките малку поблиску до камерата, со што се обезбедува тие секогаш да бидат видливи над површините.
*   **Billboard ефект:** Стандардно, ознаките во 3D користат `Billboard`, што значи дека секогаш се вртат кон гледачот. Доколку сакате ознаката да лежи во одредена рамнина, треба да ја промените во `Embedded`.

---

## 10. Оптимизација на кодот и меморијата
Кога работите на големи проекти, ефикасноста е критична.

*   **Низи vs. Патеки (Efficiency):** Градењето на патека со операторот `--` во циклус е квадратно по време (бавно), додека користењето на `guide` и негово подоцнежно разрешување во `path` е линеарно и многу поефикасно.
*   **Статични променливи:** Користете го модификаторот `static` во внатрешни функции или циклуси за да ја алоцирате меморијата само еднаш, што е корисно кај рекурзивни алгоритми.
*   **Autounravel:** Овој модификатор овозможува автоматско отпакување на полињата на структурата, што го прави кодот многу почист кога работите со библиотеки за специфични геометриски објекти.

---

## 11. Висока резолуција и излезни формати
*   **Квалитет на рендерирање:** За врвен квалитет на растерските слики (PNG/TIFF), секогаш поставувајте `settings.render = 16` или повеќе пред импортирање на `three`.
*   **Скалирање при излез:** Професионален трик за максимална острина кај PDF е да го скалирате целиот цртеж пред испраќање: `shipout(scale(4.0)*currentpicture.fit());` и потоа да го намалите при вметнување во документот.
*   **Конзистентност со LaTeX:** Секогаш користете `defaultpen(fontsize(10pt))` или соодветната големина на вашиот документ за ознаките да изгледаат како природен дел од текстот.

---

## Професионален "Cheat Sheet" за секојдневна работа

| Задача | Код / Функција | Извор |
| :--- | :--- | :--- |
| **Единица мерка** | `unitsize(1cm);` | |
| **Дебелина на линија** | `linewidth(0.8pt);` | |
| **Трансформации** | `shift(v) * rotate(45) * scale(2) * path;` | |
| **Бои** | `mediumgray`, `rgb(r,g,b)`, `cmyk(c,m,y,k)` | |
| **Специјални патеки** | `unitsquare`, `unitcircle`, `unitbox` | |
| **Тангента во точка** | `dir(path, time);` | |
| **Транспарентност** | `opacity(0.5)` (само за PDF/PNG) | |
| **3D проекција** | `currentprojection = orthographic(5,2,3,up=Y);` | |
| **Материјал** | `material(diffusepen=white, emissivepen=gray(0.2));` | |
| **Сенчење** | `gouraudshade(triangle, pens);` | |
| **Под-патека** | `subpath(path, start_time, end_time);` | |
| **Висока резолуција** | `settings.render = 16;` | |

---

## 12. Златни совети за професионално ниво
За да го доведете вашето креирање на математички дијаграми до професионално, „инженерско" ниво, постојат неколку суптилни, но моќни техники кои често се занемаруваат. Овие „златно вредни" совети се извлечени од длабоката логика на Asymptote и искуствата на експертите во областа.

### Применувајте го „Законот на Жанет" за робусност
Најважниот совет за професионален илустратор е никогаш да не се потпира на тоа како патот (path) е внатрешно дефиниран преку неговите јазли (nodes).
*   **Зошто?** Ако додадете точка во дефиницијата на патот за да го промените неговиот облик, сите претходни координати базирани на „path time" ќе се изместат.
*   **Решение:** Секогаш користете функции како `times(path, x)` за да најдете пресеци со вертикални линии или `intersections(path1, path2)` за да одредите точки базирани на геометриски односи, а не на редоследот на цртање.

### Мајсторство со апсолутни и релативни големини
Професионалните дијаграми бараат фиксни димензии за ознаки (како стрелки или ознаки за агли), без разлика на скалирањето на целата слика.
*   **Користете `unitsize()` наместо `size()`:** Додека `size()` ја присилува сликата во одредена рамка, `unitsize(1cm)` му кажува на Asymptote дека една математичка единица е точно 1 сантиметар на хартијата.
*   **Трик за нескалабилни поместувања:** Ако сакате ознаката да биде секогаш 4 милиметри десно од некоја точка, дефинирајте променлива `real truecm = cm / unit;`. Ова ви овозможува да комбинирате математички координати со прецизни офсети за печатење.

### „Маскирање" на ознаки за подобра читливост
Кога линија минува директно низ текст, дијаграмот изгледа аматерски и е тежок за читање.
*   **Златно правило:** Користете го својството `filltype=Fill(white)` при креирање на `Label`. Ова ќе создаде невидлива бела кутија околу текстот која ќе ја „пресече" линијата што поминува под него, правејќи го текстот јасен и истакнат.

### Решавање на 3D преклопувања (The Layering Hack)
Во 3D просторот, честопати ознаките (Labels) делумно „затонуваат" во површините бидејќи се на иста оддалеченост од камерата.
*   **Професионален трик:** Користете сопствена функција `towardcamera(triple point, real distance)` која математички ја поместува точката малку поблиску до окото на гledaчот пред да ја постави ознаката. Ова гарантира дека текстот секогаш ќе биде „над" објектот, без да го изобличи неговото геометриско значење.

### Напредна манипулација со патеки
Професионалците користат `subpath` за да истакнат делови од веќе постоечки функции.
*   **Тангенти:** Користете `dir(path, time)` за да го добиете векторот на тангентата во која било точка. Ова е клучно за цртање на вектори на брзина или сили во физички дијаграми без рачно пресметување изводи.
*   **Специјални конектори:** Операторот `---` е одличен за поврзување на прави сегменти кои треба да останат мазни (smooth) и во три димензии, додека `^^` е есенцијален за групирање на неповрзани патеки во еден објект за побрзо рендерирање.

### Контрола на излезот за научни трудови
Ако дијаграмите се за печатење или за PDF кој нема да се ротира интерактивно:
*   **Исклучете го PRC:** Поставете `settings.prc = false;` за да избегнете проблеми со фонтовите и за да осигурате дека сликата ќе изгледа идентично во сите PDF прегледувачи.
*   **Зголемете ја резолуцијата:** За исклучително остри растерски слики, користете `settings.render = 16;` и трикот со скалирање на сликата при самиот излез: `shipout(scale(4.0)*currentpicture.fit());`.

### Ресурси кои мора да ги консултирате
*   **Asymptote Gallery:** Официјалната галерија содржи примери за речиси секој можен математички концепт, од дијаграми на Фајнман до комплексни аналитички површини.
*   **Philippe Ivaldi's Geometry Module:** Овој модул (кој доаѓа со Asymptote) содржи готови функции за симетрали, впишани кружници и специфични ознаки за прав агол кои штедат часови работа.

---

## 13. Експертски совети (30 совети за врвна прецизност)

Како професионален илустратор на техничка геометрија, мојата работа со Asymptote се заснова на прецизност, математичка логика и способност за комбинирање на скалабилни елементи со фиксни димензии за печатење. Врз основа на детална анализа на официјалната документација и туторијалите на Staats, подготвив збирка на експертски совети и кодови организирани во групи.

### ГРУПА 1: Темели на прецизноста и робусно скалирање

1.  **Користете `unitsize` наместо `size` за апсолутна геометрија:** `unitsize(1cm)` дефинира точно колку изнесува една математичка единица на хартија.
2.  **Дефинирајте `truecm` за фиксни офсети:** `truecm = cm / unit;` за комбинирање на скалабилни координати со нескалабилни маргини.
3.  **Почитувајте го „Законот на Жанет":** Никогаш не ја користите внатрешната структура на патеките - користете пресеци наместо рачни координати.
4.  **Користете `---` за автоматска мазност:** За поврзување на точки со задржување на мазност дури и низ прави сегменти.
5.  **Групирајте со `^^` за ефикасност:** Оператор за „подигнување на пенкалото" за групирање на дисконтинуирани патеки.
6.  **Автоматско центрирање во 3D:** `size3` со `keepAspect=true` за да не се деформираат 3D модели.
7.  **Релативни позиции за ознаки:** `Relative(0.5)` или `MidPoint` наместо рачно пресметани средни точки.
8.  **LaTeX конзистентност:** `defaultpen(fontsize(10pt))` за фонтот да одговара на текстот во документот.
9.  **Конфигурација на излез:** `settings.outformat = "pdf";` на почеток за избегнување проблеми со фонтови.
10. **Затворени патеки со `cycle`:** Клучен збор за правилно спојување на аглите (line join).

**Code Snippet (Robust Scaling):**
```asy
real unit = 1.2cm;
real truecm = cm / unit; // Офсет што не се менува со скалирање
unitsize(unit);
path s = (0,0)..tension 2 ..(2,1);
draw(s, L=Label("$y=f(x)$", EndPoint, align=4*truecm*E)); // Фиксна маргина
```

### ГРУПА 2: Напредна 3D Визуелизација и Осветлување

11. **Статични PDF документи со `prc = false`:** Оневозможете PRC за подобар векторски квалитет во печатени документи.
12. **Векторска 3D графика со `render = 0`:** За едноставни објекти каде острината е поважна од сенчењето.
13. **Контрола на растерска острина:** `settings.render = 16` пред вклучување на модулот `three`.
14. **Користете PBR материјали:** `material` со `diffusepen` за боја и `specularpen` за метален одсјај.
15. **Функцијата `towardcamera`:** Поместување на ознаки кон камерата за да не бидат „потопени".
16. **Ориентација со `up=Y`:** За математички графикони каде $y$ е вертикална оска.
17. **Емисивно осветлување за „рамни" бои:** `emissive(color)` за постојана боја без сенки.
18. **Апсолутни димензии за WebGL:** `settings.absolute = true` за спречување растегнување на HTML излез.
19. **Позиционирање на камерата со `dir()`:** `orthographic(dir(theta, phi))` за прецизен агол на гледање.
20. **Претворање 2D во 3D рамнина:** `path3(path, plane)` за лесно префрлање на 2D конструкции во 3D рамнини.

**Code Snippet (3D Label Hack):**
```asy
import three;
// Поместување на ознаката кон камерата
triple towardcamera(triple pt, real dist=1) {
  return pt + dist*unit(currentprojection.camera - (currentprojection.infinity ? O : pt));
}
label("$z$", towardcamera(2Z), align=N);
```

### ГРУПА 3: Геометриска анализа и математички патеки

21. **Пресеци со вертикални линии:** `times(path, x)` за прецизни точки каде функцијата поминува низ одредена $x$.
22. **Сите пресеци одеднаш:** `intersections(path, path)` враќа низа од времиња за сите допирни точки.
23. **Под-патеки за означување:** `subpath(path, t1, t2)` за исечување дел од патека со друга боја.
24. **Автоматски тангенти:** `dir(path, time)` за вектор на тангентата - есенцијално за нормали и сили.
25. **Градење циклуси со `buildcycle`:** Автоматско наоѓање затворен простор помеѓу патеки.
26. **Делонеова триангулација:** `triangulate(pair[])` за мрежа од неправилно распоредени точки.
27. **Мазни имплицитни површини:** `smoothcontour3` за поголем квалитет од стандардниот `contour3`.
28. **Екструзија на патеки:** `extrude(path, axis)` претвора 2D облик во 3D цилиндар или призма.
29. **Мазни површини со `Spline`:** Додајте `Spline` за избегнување „набрчкани" површини.
30. **Релативно време на патека:** `reltime(path, fraction)` за време базирано на вкупната должина.

**Code Snippet (Intersection Logic):**
```asy
import graph;
path s = graph(sqrt, 0, 2);
real t = times(s, 1.4); // Најди време за x=1.4
pair P = point(s, t);
draw(P -- P + 0.5*dir(s, t), blue, Arrow); // Тангента
```

### ГРУПА 4: Напредна манипулација, структури и стилска конзистентност

31. **Користете го операторот „перо-нагоре" (`^^`) за неповрзани региони:** Есенцијален за групирање на повеќе патеки во еден објект за пополнување на региони со дупки.
32. **Мајсторство со правилата за пополнување (`fillrule`):** Разлика помеѓу `zerowinding` и `evenodd` - `evenodd` е клуч за Венови дијаграми со пресеци.
33. **Хермитова (`Hermite`) интерполација за технички графици:** Избегнува осцилации кај нагли промени на функциите.
34. **Креирање на сопствени шаблони за засенчување (`hatch`):** Користете `patterns` модул за шрафура во научна визуелизација.
35. **Третирање на функциите како променливи:** Asymptote дозволува first-class functions за генератори на криви.
36. **Автоматизација на легендите со `UnFill`:** Креира бела маска околу легендата за читливост.
37. **Контрола на ознаките (`Billboard` vs `Embedded`):** `Billboard` ротира со камерата, `Embedded` лежи на површина.
38. **Напредно мешање на бои со транспарентност:** `opacity(real, string)` со blend режими ("Multiply", "Screen").
39. **Цртање на патеки со физички волумен (`tube`):** Претвора патеки во 3D цилиндри со сенки и перспектива.
40. **Организација на комплексни дијаграми преку структури (`struct`):** Групирање на елементи со методи за цртање.

**Code Snippets for Group 4:**

#### 1. Complex region with hole (evenodd rule)
```asy
import geometry;
unitsize(1cm);

path outer = circle((0,0), 2);
path inner = circle((0,0), 1);

// ^^ connects into one path, evenodd defines the hole
fill(outer ^^ inner, evenodd + lightgray);
draw(outer ^^ inner, linewidth(1pt));

label("$A = \pi(R^2 - r^2)$", (0,0));
```

#### 2. Dynamic function generation (Higher-order functions)
```asy
import graph;
size(8cm, 6cm, IgnoreAspect);

typedef real function(real);

// Function that returns another function
function generate_sin(real n) {
    return new real(real x) { return sin(n * x); };
}

for(int n=1; n <= 3; ++n) {
    draw(graph(generate_sin(n), 0, pi), Pen(n), "$\sin(" + (string)n + "x)$");
}

xaxis("$x$", BottomTop, LeftTicks);
yaxis("$y$", LeftRight, RightTicks);
attach(legend(), (point(S).x, truepoint(S).y), 10S, UnFill); // Legend with UnFill
```

#### 3. 3D labels (Embedded vs Billboard)
```asy
import three;
size(5cm);
currentprojection = orthographic(5,2,3);

// Draw plane
draw(unitplane, surfacepen=lightgray+opacity(0.5));

// Billboard label (always faces us)
label("$B$", (0.5, 0.5, 0.5), red);

// Embedded label (lies in the plane, rotates with object)
label(XY() * "$\text{Plane } XY$", (0.5, 0.1, 0), blue, Embedded);
```

#### 4. 3D "tube" along complex path
```asy
import three;
import tube;

size(5cm);
path3 path = (0,0,0) .. (1,1,1) .. (2,0,1) .. cycle;

// Create tube with radius 0.1
surface tube = tube(path, 0.1).s;
draw(tube, material(gray, emissivepen=0.2*white));

// Add arrow on path (direction indicator)
draw(path, blue+linewidth(0.5pt), Arrow3);
```

### ГРУПА 5: Моќта на `geometry.asy` за училишна геометрија

41. **Автоматски центар на триаголник:** `incenter(t)`, `orthocenter(t)`, `circumcenter(t)` за апсолутна точност на симетрали.
42. **Означување на еднакви страни:** `StickIntervalMarker` за визуелен стандард на складност во учебници.
43. **Ознака за прав агол:** `perpendicularmark` автоматски го црта симболот со правилна ротација.
44. **Тангенти на кружница:** `tangents(circle, point)` за автоматско наоѓање допирни точки.
45. **Симетрала на агол како објект:** `bisector(line, line)` креира права за понатамошни пресеци.
46. **Масовни точки:** `mass` за Чевината теорема или центар на маса.
47. **Наоѓање подножје на висина:** `foot(vertex)` за моментално наоѓање точка на спротивната страна.
48. **Радикална оска:** `radicalline(c1, c2)` за радикалната оска на две кружници.
49. **Автоматско именување темиња:** `label(triangle)` поставува $A, B, C$ со бисекторна ориентација.
50. **Конверзија помеѓу објекти:** Кружницата автоматски станува патека при цртање.

**Code Snippet (Congruence and vertices):**
```asy
import geometry;
unitsize(1cm);
triangle t = triangleabc(4, 5, 6); // Triangle with sides 4, 5, 6
draw(t, linewidth(1pt));

// Congruence marking on two sides (e.g., AC and BC)
marker congruent = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.AC), congruent);
draw(segment(t.BC), congruent);

// Altitude mark and right angle symbol
point H = foot(t.VA);
draw(t.A--H, dashed);
perpendicularmark(line(t.BC), line(t.A,H), size=0.2cm);

label(t, alignFactor=3); // Automatic A, B, C
```

### ГРУПА 6: Дидактичка јасност и технички стандарди

51. **Маскирање линии зад ознаки:** `UnFill(1mm)` создава бел простор околу текстот.
52. **Скалабилни координати, фиксни фонтови:** `unitsize()` за цртеж, апсолутни поени (bp) за текст.
53. **Конзистентни стрелки:** `Arrow(TeXHead)` имитира LaTeX математички симболи.
54. **Координатен систем за ротирана фигура:** `coordsys` за „природни" координати (0,0), (1,0).
55. **Форматирање броеви:** `format("$%.2f$", x)` за ознаки со правилни децимали.
56. **Димензионирање со `Bars`:** `bar=Bars` за должина надвор од фигурата.
57. **Релативно позиционирање:** `Relative(0.5)` за точен центар на хипотенуза.
58. **Преклопување бои:** `opacity(0.3)` за внатрешност без сокривање елементи.
59. **Глобален хедер:** `asydef` блок во LaTeX за заеднички стилови.
60. **Автоматизација со `latexmk`:** Сам препознава промени и рекомпајлира.

**Code Snippet (Text masks and dimensions):**
```asy
import graph;
unitsize(2cm);
path s = (0,0)..(1,1.5)..(2,0);
draw(s, linewidth(1pt));

// Dimension line with masked text
pair p1 = (0, -0.2), p2 = (2, -0.2);
draw(p1--p2, L=Label("$d=10\,cm$", MidPoint, filltype=UnFill(1mm)), bar=Bars);

// Point label that doesn't overlap line
dot((1,1.5));
label("$M_{max}$", (1,1.5), N, filltype=UnFill);
```

### ГРУПА 7: Стереометрија и 3D визуелизација

61. **Triple Aliases:** Вградените `O, X, Y, Z` за брзо дефинирање точки во простор.
62. **Ортографска проекција:** `orthographic` за технички цртежи каде паралелни линии остануваат паралелни.
63. **3D површини од 2D патеки:** `surface(path3)` претвора 2D нацрт во 3D рамнина.
64. **Ротациони тела:** `solids.asy` за конуси и цилиндри: `cylinder(O, r, h, axis)`.
65. **Транспарентност тела:** `material(white+opacity(0.5))` за видливи „скриени" рабови.
66. **Означување во 3D:** `towardcamera` за ознаки да не бидат пресечени од објекти.
67. **BillboardLabels:** Ознаките секогаш го гледаат ученикот, без разлика на аголот.
68. **3D агли и лакови:** `arc(triple c, triple v1, triple v2)` за агли меѓу рамнини.
69. **Слоеви во 3D:** `shift(dist*unit(camera-pt))` за „извлекување" точки напред.
70. **Висока резолуција за принт:** `settings.render=16` за мазни слики во печат.

**Code Snippet (Cylinder with transparency):**
```asy
import solids;
settings.render=16;
settings.prc=false;
size(5cm,0);
currentprojection=orthographic(5,2,3,up=Z);

// Create and draw cylinder
revolution r = cylinder(O, 1, 2, Z);
draw(r, white+opacity(0.5)); // Transparent body
draw(r.silhouette(), linewidth(1pt)); // Emphasized outer edges

// Cylinder axis
draw(O--2.5Z, blue+dashed, L=Label("$h$", EndPoint, align=N));
dot(O);
```

### ГРУПА 8: Дизајн на функции, дисконтинуитети и аналитичка прецизност

71. **Користете го `graph` модулот за аналитичка точност:** Дефинирајте `real f(real x)` и `graph(f, a, b)` за математички верна крива.
72. **Контрола оските со `YZero` и `XZero`:** `axis=YZero` за $x$-оската да поминува низ (0,0).
73. **Прилагодени поделеци за тригонометрија:** `real[] T = {0, pi/2, pi, 3*pi/2, 2*pi}` со LaTeX ознаки.
74. **Справување прекини со `bool3 cond`:** За асимптоти, користете `cond(real x)` да „подигнете пенкало".
75. **Мајсторство со `subpath` за акцентирање:** `subpath(g, t1, t2)` за истакнување дел од функција.
76. **Интерполација со `Hermite`:** За податоци со нагли промени, избегнува осцилации без надминување.
77. **Пресеци на прави и криви со `times`:** `times(g, c)` наоѓа точно време каде функција се сече со $x=c$.
78. **Автоматизација легенди со `legend()`:** `draw(g, "ознака")` и `add(legend(), ...)` за автоматско објаснување.
79. **Користете `UnFill` за читливост текст врз мрежа:** `filltype=UnFill` создава бел простор околу бројки.
80. **Напредно 3D означување во рамнини:** `XY * "текст"` за `Embedded` објект кој ротира со геометријата.

**Code Snippets for Educational Textbook:**

#### 1. Analytical graph with asymptote and shaded area
```asy
import graph;
size(8cm, 6cm, IgnoreAspect);

// Function f(x) = 1/(x-1) + x
real f(real x) { return 1/(x-1) + x; }

// Continuity condition
bool3 cond(real x) { return abs(x-1) > 0.05; }

path g = graph(f, -2, 4, cond, n=400);
draw(g, linewidth(1pt) + blue);

// Vertical asymptote
draw((1,-5)--(1,10), dashed + gray);

// Axes through zero
xaxis("$x$", YZero, Ticks(Step=1, Size=2pt));
yaxis("$y$", XZero, Ticks(Step=5, Size=2pt));
```

#### 2. Intersection of two paths (e.g., tangent to curve)
Finding intersection point without manual calculation.

```asy
import graph;
unitsize(2cm);

path curve = graph(exp, -1, 1.5);
path line = (-1, 1) -- (1.5, 3);

draw(curve, blue);
draw(line, dashed + gray);

// Finding intersections
real[][] t = intersections(curve, line);
if (t.length > 0) {
    dot(point(curve, t), red); // Intersection point
    label("Intersection", point(curve, t), SE);
}
```

#### 3. 3D text "glued" to plane (for stereometry)
Perfect for labeling angles between planes.

```asy
import three;
size(6cm);
currentprojection = perspective(5,2,3);

// Drawing the XY plane
draw(unitplane, surfacepen=emissive(lightgray + opacity(0.5)));

// Label embedded in plane (Embedded)
label(XY() * "$\Sigma$", (0.8, 0.8, 0), blue, Embedded);

// Label that always faces us (Billboard)
label("$z$", (0,0,1.2), red);
draw(O--1.2Z, red, Arrow3);
```

#### 4. Highlighting part of path (Subpath)
Useful for explaining arc of circle or part of parabola.

```asy
import graph;
unitsize(1cm);

path p = (0,0){up} .. (2,3) .. (4,0);
draw(p, gray + linewidth(0.5pt)); // Full path

// Highlight segment from time 0.5 to 1.5
path highlight = subpath(p, 0.5, 1.5);
draw(highlight, linewidth(1.5pt) + orange);
dot(point(p, 0.5), orange);
dot(point(p, 1.5), orange);
```

### ГРУПА 9: Еуклидски конструкции, складност и дидактичка јасност

81. **Користете го типот `triangle` за апстрактна геометрија:** Дефинирајте `triangle t = triangle(A, B, C);` за пристап до својства како `t.AB` (страна) или `t.VA` (теме).
82. **Означување складност со `StickIntervalMarker`:** `marker(stickframe(n=2))` за две цртички (ticks) на средина - меѓународен стандард за еднакви страни.
83. **Автоматизирајте ортогонални пресеци:** `foot(t.VC)` автоматски наоѓа точка каде паѓа нормала од темето $C$.
84. **Прецизни агли со `markangle`:** `markangle` овозможува еден, два или три лаци за означување еднакви агли со стрелки.
85. **Користете `perpendicularmark` за прав агол:** Автоматски црта симбол за прав агол на пресек без рачно квадрати.
86. **Контрола дебелина пенкало според хиерархија:** Главни објекти `linewidth(1.2pt)`, помошни `dashed + gray`.
87. **Маскирање ознаки со `UnFill`:** `filltype=UnFill` создава бел круг околу букви за читливост врз линии.
88. **Динамичко пресметување тежиште:** `centroid(t)` или `incenter(t)` за математичка точност без рачни пресметки.
89. **Справување бесконечни прави преку `drawline`:** `drawline(A, B)` црта права до работ на слика без менување платно.
90. **Користете `arcsubtended` за геометриски локус:** Црта кружни лак под кој се гледа отсечка $AB$ под одреден агол.

**PROBLEM ID: Triangle Construction with Properties (Group 9 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// 1. Define triangle
triangle t = triangleabc(5, 6, 7);
draw(t, linewidth(1.2pt));

// 2. Label vertices
label(t, alignFactor=3);

// 3. Construct altitude and right angle
point H = foot(t.VC);
draw(t.C--H, dashed + blue);
perpendicularmark(line(t.AB), line(t.C, H), size=0.2cm, p=blue);

// 4. Mark equal parts on base
// Assuming we want to mark congruence of two segments
marker m = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.A, H), m);
draw(segment(H, t.B), m);

// 5. Mark angle
markangle("$\alpha$", n=1, t.B, t.A, t.C, radius=0.6cm, p=red);
```

**NANO BANANA PROMPT:**
`Detailed pencil sketch on parchment paper of a classic Euclidean geometry construction, showing a triangle with compass markings and circular arcs, vintage scientific illustration style, warm sepia lighting, 3:2, No Text.`

---

**PROBLEM ID: Circumscribed Circle and Peripheral Angles (Group 9 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

// 1. Create circle and triangle
point A = (0,0), B = (4,0), C = (1,3);
triangle t = triangle(A, B, C);
circle c = circumcircle(t);

draw(c, lightgray);
draw(t);

// 2. Label center
point O = c.C;
dot("$O$", O, S, p=red);

// 3. Use UnFill for readability
label("$R$", (O+C)/2, UnFill(1mm));

// 4. Mark angles on same arc
markangle("$\beta$", B, C, A, radius=0.4cm, p=blue);
```

**NANO BANANA PROMPT:**
`A glowing neon geometric constellation in deep space, forming perfect triangular and circular patterns, cinematic starfield background, vibrant blue and magenta lighting, 16:9, No Text.`

### ГРУПА 10: Професионален работен процес, дебагирање и автоматизација

91. **Интегрирајте код директно во LaTeX со `asymptote.sty`:** Пишувајте Asymptote во `.tex` со `\begin{asy}...\end{asy}` за илустрации и текст на едно место.
92. **Автоматизирајте со `latexmk` и `latexmkrc`:** `latexmk` препознава промени и рекомпајлира само изменети дијаграми.
93. **Користете `asypictureB` за полесно дебагирање:** Репакува Asymptote грешки како LaTeX грешки за брзо наоѓање проблеми.
94. **Експлицитно решавање равенки со `extension`:** `extension(P, Q, p, q)` за експлицитни пресеци без автоматско решавање.
95. **Прецизна контрола ознаки преку bidirectional pipe:** Asymptote комуницира со TeX во два премина за точна големина.
96. **Прилагодете дебелина точки со `dotfactor`:** Стандард 6; за средно образование намалете на 4 за помалку масивни точки.
97. **Глобална стандардизација со `asydef`:** Дефинирајте заеднички стилови во LaTeX за конзистентност низ учебник.
98. **Постигнете максимална острина со `shipout(scale)`:** `shipout(scale(4.0)*currentpicture.fit())` за висококвалитетни растерски слики.
99. **Маскирање позадина со `UnFill`:** `filltype=UnFill` создава дупка во објекти под ознака.
100. **Изберете правилен излезен формат:** `pdf` за чиста 2D геометрија, `png` со висок `render` за сложени 3D површини.

**PROBLEM ID: Professional Textbook Template (Group 10 Example)**

**ASYMPTOTE CODE:**
```asy
// Settings for professional printing
settings.outformat = "pdf";
settings.prc = false;
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Global definitions (imitating asydef)
pen helper_line = dashed + gray(0.4);
pen main_line = black + linewidth(1.2pt);
real unit_size = 1.5cm;
unitsize(unit_size);

// Construction: Triangle and incircle
point A=(0,0), B=(4,0), C=(1,3);
triangle t = triangle(A, B, C);
circle ic = incircle(t);

// Drawing with line hierarchy
draw(t, main_line);
draw(ic, blue);

// Using UnFill for label readability on lines
label("$A$", A, SW, UnFill(1mm));
label("$B$", B, SE, UnFill(1mm));
label("$C$", C, N, UnFill(1mm));

// Labeling radius with Bars
point O = ic.C;
point T = intouch(t.AB);
draw(O--T, helper_line);
label("$r$", (O+T)/2, E, UnFill);
dot(O, red);

// Increasing resolution at output
shipout(scale(4.0)*currentpicture.fit());
```

**NANO BANANA PROMPT:**
`High-end macro photography of a mathematical textbook page, showing a sharp geometric diagram of a triangle and circle, soft sunlight hitting the paper texture, clean bokeh background, minimalist scholarly aesthetic, 16:9, No Text.`

---

**PROBLEM ID: 3D Layer Simulation (Group 10 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
settings.render = 16;
import three;
import solids;

// Projection adjustment for technical display
currentprojection = orthographic(5,2,3, up=Y);
currentlight = Headlamp;

// Drawing 3D sphere and axes
draw(unitsphere, white + opacity(0.6));
draw(O--1.5X, black, L=Label("$x$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Y, black, L=Label("$y$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Z, black, L=Label("$z$", position=EndPoint), arrow=Arrow3(TeXHead2));

// Moving label toward camera to avoid intersection
triple towardcamera(triple pt, real dist=0.1) {
  return pt + dist*unit(currentprojection.camera - pt);
}

dot(towardcamera(Z), red);
label("$P(x,y,z)$", towardcamera(Z), N, blue);
```

**NANO BANANA PROMPT:**
`3D wireframe glass sphere floating in a dark laboratory, laser beams as coordinate axes, cinematic blue lighting, holographic aesthetic, high-tech educational visualization, 3:2, No Text.`

### ГРУПА 11: Педагошка визуелизација, виткави загради и напредна типографија

101. **Креирајте виткави загради за интервали:** `brace(pair a, pair b)` за математички прецизни виткави загради над сегменти.
102. **Користете `minipage` за комплексни описи:** `minipage(text, width)` за форматирање блокови текст со фиксна ширина во ознаки.
103. **Обезбедете конзистентност фонтот со `defaultpen`:** `defaultpen(fontsize(10pt))` за ознаки со иста големина како текст во учебник.
104. **Применете `basealign` за порамнување математички изрази:** `basealign` за совршени базни линии на формули една до друга.
105. **Управувајте слоевите преку `layer()`:** `layer()` за PostScript објекти да се појават над ознаки или TeX команди.
106. **Искористете `unfill` за читливост легендите:** Клипинг за маскирање позадина на легенди врз густ графикон.
107. **Динамично проширување границите со `addBox`:** `pic.addBox` за ажурирање граници на слика со unscalable елементи.
108. **Интегрирајте TeX макроа преку `@` префиксот:** `@the@linewidth` со `asypictureB` за автоматско прилагодување на страница.
109. **Означување агли со стрелки:** `markangle` со `Arrow` за насока ротација или позитивна насока аголот.
110. **Контрола дебелина „мрежните" линии:** `thin()` за линии видливи како еден пиксел независно од зум.

**PROBLEM ID: Segment Visualization with Curly Brace (Group 11 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Function for curly brace
path brace(pair a, pair b, real amplitude = 0.14) {
    real d = length(b-a);
    transform t = shift(a) * rotate(degrees(atan2((b-a).y, (b-a).x)));
    path br = (0,0){expi(radians(70))} :: {expi(0)}(d/4, amplitude*d/2)
               :: {expi(radians(60))} (d/2, amplitude*d) {expi(radians(-60))}
               :: {expi(0)}(3*d/4, amplitude*d/2) :: {expi(radians(-70))} (d,0);
    return t * br;
}

// Segment construction and labeling
pair A = (0,0), B = (5,0);
draw(A--B, linewidth(1.2pt));
dot(A); dot(B);

// Adding curly brace below segment
path b = brace(B, A, 0.1); // Swap A and B for downward direction
draw(b, blue);
label("$d = 5.0 cm$", MidPoint, align=S, p=blue);

// Using minipage for definition
label(minipage("\raggedright \textbf{Definition:}\\A line segment is part of a line bounded by two points.", 4cm), (2.5, 1.5), UnFill);
```

**NANO BANANA PROMPT:**
`A macro photograph of an architect's drafting table, focus on a metallic compass tracing a perfect arc on a blueprint, blueprint lines glowing faintly in cyan, soft morning sunlight, cinematic perspective, 16:9, No Text.`

---

**PROBLEM ID: Aligning Mathematical Formulas in Diagram (Group 11 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import graph;

// Baseline alignment
pair O = (0,0);
dot(O);

// Drawing with basealign for perfect symbol alignment
label("$\alpha = 30^\circ$", O, align=N, basealign);
label("$\gamma = 90^\circ$", O, align=S, basealign);
label("$f(x) = \sqrt{x}$", O, align=E, basealign);

// Using layer() for drawing over text if needed
layer();
draw(circle(O, 0.5cm), red+dashed);
```

**NANO BANANA PROMPT:**
`A clean blackboard with complex mathematical geometry formulas written in crisp white chalk, high contrast, studio lighting, academic and scholarly aesthetic, minimalist composition, 3:2, No Text.`

### ГРУПА 12: Напредна координатна логика, оптимизација и конзистентност

111. **Разликувајте `size()` и `unitsize()` за фиксни размери:** `unitsize(1cm)` за една единица = точно 1cm на хартија; `size()` само вклопува во рамка.
112. **Користете `coordsys` за природни координати:** `cartesiansystem` за работа во ротиран систем со релативни точки.
113. **Оптимизирајте перформанси со `guide` во циклуси:** `guide` за линеарно време наместо квадратно кај `path` додавање.
114. **Мајсторство `subpath` и пресеци за дидактички приказ:** `intersections()` за точки допир, `subpath()` за исечување сегменти.
115. **Контрола дебелина ознаки со `dotfactor`:** Намалете од 6 на 4 за естетски подобри точки во средно образование.
116. **Автоматизирајте цртање агли со `markangle`:** `markangle` со stick marks за еднаквост на агли.
117. **Користете `emissive` материјали за чисти 3D илустрации:** `emissivepen` за постојана боја без сенки.
118. **Порамнување математички изрази со `basealign`:** `basealign` за совршени базни линии на формули.
119. **Користете `asypictureB` за веднаш гледате грешки:** Репакува Asymptote грешки во LaTeX лог за брзо дебагирање.
120. **Максимална резолуција со `shipout(scale)`:** `shipout(scale(4.0)*currentpicture.fit())` за остри растерски слики.

**Code Snippets for Advanced Coordination:**

#### 1. Using custom coordinate systems (coordsys)
```asy
import geometry;
unitsize(1cm);

// Define rotated coordinate system
coordsys R = cartesiansystem((2,1), i=rotate(30)*E, j=rotate(30)*N);
show(R, ipen=blue); // Visualize axes

// Points defined relative to new system
point A = point(R, (0,0));
point B = point(R, (3,0));
point C = point(R, (1,2));

draw(A--B--C--cycle, linewidth(1.2pt));
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, N);
```

#### 2. Precise angle and congruence marking
```asy
import geometry;
unitsize(1.5cm);

triangle t = triangleabc(4, 4, 5);
draw(t);

// Congruence marking on two sides
marker m = marker(stickframe(n=2, size=3));
draw(segment(t.AC), m);
draw(segment(t.BC), m);

// Marking equal angles
markangle("$\alpha$", n=1, t.B, t.A, t.C, radius=0.5cm, p=red);
markangle("$\alpha$", n=1, t.A, t.B, t.C, radius=0.5cm, p=red);
```

#### 3. 3D sphere with "clean" (emissive) lighting
```asy
import three;
settings.render = 16; // High resolution
settings.prc = false;
size(5cm, 0);

currentprojection = orthographic(5,2,3); // Technical projection

// Sphere with emissive color independent of light angle
material m = material(diffusepen=white+opacity(0.6), emissivepen=gray(0.3));
draw(unitsphere, surfacepen=m);

// Axes with 3D arrows
draw(O--1.5X, arrow=Arrow3(TeXHead2), L=Label("$x$", position=EndPoint));
draw(O--1.5Y, arrow=Arrow3(TeXHead2), L=Label("$y$", position=EndPoint));
draw(O--1.5Z, arrow=Arrow3(TeXHead2), L=Label("$z$", position=EndPoint));
```

### ГРУПА 13: Типографска конзистентност и „Светата врска" со LaTeX

121. **Никогаш не скалирајте слика во LaTeX:** Дефинирајте финална големина во Asymptote со `size()` или `unitsize()` - скалирање во LaTeX деформира фонт на ознаки.
122. **Користете `asymptote` пакет со `inline` опција:** 2D LaTeX симболи надвор од Asymptote код видливи, но додајте рачна проценка за големина во `Label`.
123. **Централизирајте стил преку `asydef`:** `\begin{asydef}...\end{asydef}` во LaTeX за заеднички `import geometry;`, фонтови, бои - конзистентност низ сите дијаграми.
124. **Принудете порамнување со `basealign`:** Естетски совршени формули со совршени базни линии на TeX карактери.
125. **Користете `texpreamble` за специјални пакети:** `\usepackage{bm}` во `texpreamble` за болд математички фонтови достапни во ознаки.
126. **Двонасочната комуникација (Bidirectional Pipe):** Asymptote комуницира со TeX во два премини - прво дознава големина на ознаки, потоа ги поставува.
127. **Управување дебелина точки (`dotfactor`):** Намалете од стандардни 6 на 4 за елегантни точки кои не доминираат.
128. **Автоматизирајте цртање висини со `foot`:** `pair H = foot(A, B, C);` за математички перфектен симбол за прав агол.
129. **Користете `minipage` за долги дефиниции:** `minipage(text, width)` форматира блок текст со правилна ширина во сликата.
130. **Стандардизирајте стрелки на оски:** `Arrow(TeXHead)` или `Arrow(TeXHead2)` одговараат на LaTeX математички стрелки.

**PROBLEM ID: Triangle Illustration with Angle and Congruence (Group 13 Example)**

**ASYMPTOTE CODE:**
```asy
// Professional printing settings for textbook
settings.outformat = "pdf";
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

// Global adjustment
dotfactor = 4; // Elegant vertex points

// Construction: Triangle with congruence marking
point A=(0,0), B=(4,0), C=(1,3);
triangle t = triangle(A, B, C);

draw(t, linewidth(1.2pt));

// Congruence marking on equal sides
marker m = marker(stickframe(n=2, size=3, space=2));
draw(segment(t.AC), m);
draw(segment(t.BC), m);

// Angle marking
markangle("$\alpha$", t.B, t.A, t.C, radius=0.6cm, p=red);

// UnFill for vertex labels
label("$A$", t.A, SW, UnFill(1mm));
label("$B$", t.B, SE, UnFill(1mm));
label("$C$", t.C, N, UnFill(1mm));

// Textual description in minipage
label(minipage("\raggedright Given triangle $ABC$ which is isosceles, i.e., $AC = BC$.", 3cm), (4.5, 2.5), UnFill);
```

**NANO BANANA PROMPT:**
`A hyper-realistic studio shot of an open geometry textbook on a wooden desk, focus on a sharp black and white diagram of a triangle, high-quality printing texture on paper, soft morning window light, scholarly aesthetic, 16:9, No Text.`

---

**PROBLEM ID: Stereometry and 3D Projection (Group 13 Example)**

**ASYMPTOTE CODE:**
```asy
settings.outformat = "pdf";
settings.render = 16; // High resolution for printing
settings.prc = false; // Static vector image

import three;
import solids;

// Orthographic projection for parallelism
currentprojection = orthographic(5,2,3, up=Z);

// Drawing sphere and axes
draw(unitsphere, white + opacity(0.5));
draw(O--1.5X, L=Label("$x$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Y, L=Label("$y$", position=EndPoint), arrow=Arrow3(TeXHead2));
draw(O--1.5Z, L=Label("$z$", position=EndPoint), arrow=Arrow3(TeXHead2));

// Moving point toward camera for better visibility
triple towardcamera(triple pt, real dist=0.15) {
  return pt + dist*unit(currentprojection.camera - pt);
}

dot(towardcamera(Z), red);
label("$P(0,0,1)$", towardcamera(Z), N, blue);
```

**NANO BANANA PROMPT:**
`A complex mathematical 3D wireframe hologram of a sphere and coordinate system, floating in a futuristic dark classroom, cinematic lighting, blue neon glows, high-tech educational concept, 3:2, No Text.`

---

## Збирка на Кодни Фрагменти (Code Snippet Collection)

Како технички илустратор за едукативна геометрија, подготвив архива со кодни фрагменти (snippets) базирани на претходно утврдените експертски групи. Овие фрагменти се оптимизирани за директно вметнување во вашиот работен процес, користејќи ги најдобрите практики од документацијата за Asymptote и LaTeX интеграцијата.

### ГРУПА 1: Темели на прецизноста и робусно скалирање

**Snippet 1.1: Дефинирање на „true" димензии (Unscalable Offset)**
```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));

real unit = 1.5cm; // 1 единица = 1.5cm
unitsize(unit);
real truecm = cm/unit; // Конвертор за фиксни димензии

pair A = (0,0), B = (3,0);
draw(A--B);

// Ознаката ќе биде секогаш точно 0.5cm под линијата
label("$d = 3$", (A+B)/2, align=0.5*truecm*S);
```

**Snippet 1.2: Автоматско наоѓање точки преку „times"**
```asy
import graph;
path s = (0,0){up} .. (1,1.5) .. (2,1); // Некоја крива
real x_pos = 1.2;
real t = times(s, x_pos); // Го наоѓа „времето" на патот за x=1.2
pair P = point(s, t);

draw(s, blue);
dot(P, red); // Точката е математички прецизна
```

### ГРУПА 2: Напредна 3D Визуелизација и Осветлување

**Snippet 2.1: TowardCamera Label Hack**
```asy
import three;
// Функција за поместување на ознаката малку кон камерата
triple towardcamera(triple pt, real dist=0.1) {
  return pt + dist*unit(currentprojection.camera - pt);
}

currentprojection = orthographic(5,2,3);
draw(unitsphere, white+opacity(0.6));
// Ознаката нема да се сече со сферата
dot(towardcamera(Z), red);
label("$P$", towardcamera(Z), N);
```

**Snippet 2.2: Емисивни материјали за технички нацрт**
```asy
import three;
material m = material(diffusepen=white, emissivepen=gray(0.2));
draw(unitcube, surfacepen=m); // Чист приказ без црни сенки
```

### ГРУПА 5: Моќта на `geometry.asy` (High School Geometry)

**Snippet 5.1: Автоматска висина и прав агол**
```asy
import geometry;
unitsize(1cm);
triangle t = triangleabc(4, 5, 6);
draw(t);

point H = foot(t.VC); // Подножје на висината од темето C
draw(t.C--H, blue+dashed);
// Автоматски симбол за прав агол
perpendicularmark(line(t.AB), line(t.C, H), size=0.2cm, p=blue);
```

**Snippet 5.2: Означување на еднакви страни (Congruence)**
```asy
import geometry;
point A=(0,0), B=(3,0), C=(1.5, 2.5);
// Ознака со две цртички (StickIntervalMarker)
marker складна = marker(stickframe(n=2, size=3, space=2));
draw(A--C, складна);
draw(B--C, складна); // Означува дека триаголникот е рамнокрак
```

### ГРУПА 6: Дидактичка јасност (Masking & Dimensions)

**Snippet 6.1: Маскирање на линии зад ознаки (UnFill)**
```asy
unitsize(2cm);
path s = (0,0) .. (2,1);
draw(s, linewidth(1pt));

// Текстот „сече" дупка во линијата под него
label("$x + y = 10$", relpoint(s, 0.5), filltype=UnFill(1mm));
```

**Snippet 6.2: Димензионални линии со Bars**
```asy
unitsize(1cm);
pair p1=(0,0), p2=(4,0);
// drawline со стрелки и вертикални бариери (Bars)
draw(p1-(0,0.5)--p2-(0,0.5), L=Label("$a=4$", MidPoint, align=S),
     arrow=Arrows(TeXHead), bar=Bars);
```

### ГРУПА 10: Автоматизација и Работен Процес (Workflow)

**Snippet 10.1: Глобален asydef за учебник**
```latex
\begin{asydef}
// Глобални нагодувања за целиот учебник
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt)); // Фонт од LaTeX
pen help_lines = dashed + gray(0.5);
\end{asydef}
```

**Snippet 10.2: Максимална острина (Resolution Hack)**
```asy
// Зголеми ја резолуцијата за 4 пати пред генерирање PDF
shipout(scale(4.0)*currentpicture.fit());
```

### ГРУПА 7: Стереометрија и прецизни 3D тела

**Snippet 7.1: Ротационо тело со скелет (Конус/Цилиндар)**
```asy
import solids;
size(5cm,0);
currentprojection=orthographic(5,2,3);

// Дефинирање на оска и профилна патека
path3 профил = (0,0,0)--(1,0,0)--(1,0,2);
revolution тело = revolution(профил, Z);

// Цртање со нагласување на скелетот за техничка јасност
draw(тело, lightgray+opacity(0.4));
draw(тело.silhouette(), linewidth(1pt));
draw(тело.transverse.back, dashed); // Скриени линии
```

### ГРУПА 8: Аналитичка прецизност и функции

**Snippet 8.1: Справување со дисконтинуитети (`bool3 cond`)**
```asy
import graph;
size(6cm, 4cm, IgnoreAspect);

real f(real x) { return 1/x; }
// Услов: не цртај ако x е премногу блиску до 0
bool3 cond(real x) { return abs(x) > 0.1; }

path g = graph(f, -2, 2, cond, n=400);
draw(g, blue+linewidth(1pt));
xaxis("$x$", Arrow); yaxis("$y$", Arrow);
```

### ГРУПА 9: Еуклидски структури (Апстрактна геометрија)

**Snippet 9.1: Автоматски карактеристични точки на триаголник**
```asy
import geometry;
unitsize(1cm);

triangle t = triangleabc(5, 6, 7);
draw(t);

// Наоѓање на тежиште и Gergonne точка
point G = centroid(t);
point Ge = gergonne(t);

dot("$G$", G, NE, red);
dot("$G_e$", Ge, SW, blue);
label(t); // Автоматско A, B, C
```

### ГРУПА 11: Педагошки контекст и типографија

**Snippet 11.1: Виткава заграда (Brace) за означување интервали**
```asy
// Рачно дефинирана функција за brace
path brace(pair a, pair b, real amplitude = 0.14*length(b-a)) {
    real d = length(b-a);
    transform t = shift(a)*rotate(degrees(atan2((b-a).y,(b-a).x)));
    return t * ((0,0){expi(radians(70))} :: {expi(0)}(d/4, amplitude/2)
               :: {expi(radians(60))}(d/2, amplitude) :: {expi(0)}(3*d/4, amplitude/2)
               :: {expi(radians(-70))}(d,0));
}

draw((0,0)--(5,0));
draw(brace((5,-0.2), (0,-0.2)), blue); // Заграда под линијата
label("$d=5$", (2.5, -0.5), blue);
```

### ГРУПА 12: Напредна координатна логика

**Snippet 12.1: Локален координатен систем (`coordsys`)**
```asy
import geometry;
unitsize(1cm);

// Креирање ротиран систем
coordsys R = cartesiansystem((2,2), i=rotate(30)*E, j=rotate(30)*N);
show(R, ipen=blue); // Оските на локалниот систем

// Точката е дефинирана како (1,1) во локалниот систем R
point P = point(R, (1,1));
dot("$P_R(1,1)$", P, NE);
```

### ГРУПА 13: LaTeX конзистентност и порамнување

**Snippet 13.1: Порамнување на математички формули (`basealign`)**
```asy
defaultpen(fontsize(12pt));
pair P = (0,0), Q = (2,0);

// basealign гарантира типографско порамнување
label("$\alpha = \pi$", P, N, basealign);
label("$a = 3,5$", Q, N, basealign);

draw(P--Q, dashed);
```

**NANO BANANA PROMPT ЗА ЦЕЛОСНАТА АРХИВА:**
`A professional architectural library bookshelf filled with clean white binders labeled with geometric icons, 3D holographic wireframe of a dodecahedron floating in the center, modern studio lighting with cyan accents, cinematic wide shot, 16:9, No Text.`

---

## Едукативни Реконструкции на Дијаграми

Како технички илустратор фокусиран на прецизна геометриска реконструкција за образовни цели, ги анализирав дијаграмите од **страна 15** на материјалот **Karekök Sıfır Geometri 2023**.

Во продолжение се Asymptote кодовите за рекреирање на трите клучни илустрации од оваа страница, следејќи ги специфичните избори за стил и професионален изглед.

### PROBLEM ID: Köşetaşı 1.3 (Концепт на Симетрала и Прав Агол)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

// Димензии на платното
size(200, 100);

// Дефинирање на точките на главната права
point O = (0,0);
point A = (-100, 0);
point F = (100, 0);

// Поставување на зраците според аглите од задачата
// OC и OD се под прав агол (90 степени)
point C = 80*dir(135);
point D = 80*dir(45);
point B = 80*dir(157.5); // Симетрала на AOC
point E = 80*dir(22.5);  // Симетрала на DOF

// Цртање на главната права и зраците
draw(A--F, black);
draw(O--B, black);
draw(O--C, black);
draw(O--D, black);
draw(O--E, black);

// Додавање ознаки за темињата
label("$A$", A, W);
label("$O$", O, S);
label("$F$", F, E);
label("$B$", B, NW);
label("$C$", C, N);
label("$D$", D, N);
label("$E$", E, NE);

// Означување на прав агол
perpendicularmark(line(O,C), line(O,D), size=0.2cm);

// Означување на еднакви агли (Симетрали)
// Агли означени со точки
markangle(n=1, C, O, B, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, B, O, A, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));

// Агли означени со цртички
markangle(n=1, F, O, E, radius=15, p=blue, StickIntervalMarker(1,1,size=3));
markangle(n=1, E, O, D, radius=15, p=blue, StickIntervalMarker(1,1,size=3));

dot(O);
```

**NANO BANANA PROMPT:**
`Technical blueprint of a complex sunburst geometric pattern, mathematical symmetry lines, architectural drafting style, clean white background, soft studio lighting, 16:9, No Text.`

### PROBLEM ID: Задача 3 (Геометрија на закачалка за облека)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 200);

// Главни точки на конструкцијата
point O = (0,0);
point C = (-80, 0); // Паралелно со земјата
point A = 80*dir(230);
point B = 80*dir(50); // A, O, B се колинеарни
point D = 80*dir(310); // m(AOC) = m(AOD)

// Цртање на линиите
draw(C--O, black+linewidth(1.5pt));
draw(A--B, black+linewidth(1.5pt));
draw(O--D, black+linewidth(1.5pt));

// Помошна линија за земја (паралелна)
draw(shift(0,-20)*(-100,0--100,0), gray+dashed);

// Лабели
label("$C$", C, W);
label("$O$", O, NE);
label("$A$", A, SW);
label("$B$", B, NE);
label("$D$", D, SE);

// Означување на еднакви агли m(AOC) = m(AOD)
markangle(n=1, C, O, A, radius=15, p=red, StickIntervalMarker(1,1));
markangle(n=1, A, O, D, radius=15, p=red, StickIntervalMarker(1,1));

// Означување на BOC = 130 степени
markangle("$130^\circ$", B, O, C, radius=25, p=blue);

dot(O);
```

**NANO BANANA PROMPT:**
`Minimalist industrial design of a metallic clothes drying rack, sharp geometric shadows on a concrete floor, artistic photography, high contrast lighting, 3:2, No Text.`

### PROBLEM ID: Концепт за Агол со испрекината линија (B, C, D, A)

```asy
settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 150);

// Точки според Source
point B = (0,0);
point C = (100, 0);
point A = 100*dir(-60);
point D = 80*dir(-25);

// Цртање зраци со стрелки
draw(B--C, Arrow(TeXHead));
draw(B--A, Arrow(TeXHead));
draw(B--D, dashed+blue, Arrow(TeXHead)); // Испрекината линија (симетрала)

// Лабели
label("$B$", B, NW);
label("$C$", C, E);
label("$A$", A, S);
label("$D$", D, E);

// Означување агли со точки
markangle(n=1, C, O=B, D, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, D, O=B, A, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));

dot(B);
```

**NANO BANANA PROMPT:**
`An open ancient scroll with hand-drawn geometric calculations, ink quill strokes, warm candle lighting, cinematic depth of field, macro photography, 16:9, No Text.`

---

## Препорака за работен процес (Workflow)
1.  **Скриптирање:** Користете `config.asy` за глобални нагодувања (како `outformat="pdf"`) за да не ги пишувате во секој фајл.
2.  **LaTeX интеграција:** Користете го пакетот `asymptote.sty` за да го пишувате кодот директно во вашите научни трудови.
3.  **Прецизност:** Секогаш претпочитајте `unitsize()` пред `size()` кога димензиите на објектите мора да бидат апсолутни и непроменливи при скалирање.
4.  **Дебагирање:** Користи го интерактивниот мод (`asy -V`) за брза проверка на визуелниот резултат без постојано компајлирање на целиот документ.
5.  **Ефикасност:** За големи проекти, користете `guide` наместо `--` во циклуси и `static` за мемориска оптимизација.
6.  **Квалитет:** За финални излези, применувајте `scale()` пред `shipout()` за максимална острина.
7.  **Професионалност:** Следете ги експертските совети за робусност, 3D визуелизација и геометриска анализа.