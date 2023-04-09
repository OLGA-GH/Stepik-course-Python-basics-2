# Stepik-course-Python-basics-2
Institute of Bioinformatics: second part of learning Python course - solutions

## Решение задач.

### 1.1 Введение

Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.

ex_1_1.py

### 1.2 Модель данных: объекты

Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

Примечание:

Количеством различных объектов называется максимальный размер множества объектов, в котором любые два объекта являются различными.

ex_1_2.py

### 1.3 Функции и стек вызовов - 1

Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5

ex_1_3_1.py

### 1.3 Функции и стек вызовов - 2

Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Пример:

Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3.

Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.

Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).

ex_1_3_2.py

### 1.4 Пространства имён и области видимости

Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует

Рассмотрим набор запросов

add global a

create foo global

add foo b

create bar foo

add bar a

Формат входных данных

В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.

Формат выходных данных

Для каждого запроса get выведите в отдельной строке его результат.

ex_1_4.py

### 1.5 Введение в классы - 1

Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

При создании копилки, число монет в ней равно 0.

ex_1_5_1.py

### 1.5 Введение в классы - 2

Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.

Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько раз до тех пор, пока в буфере не останется менее пяти элементов.

ex_1_5_2.py

### 1.6 Наследование классов - 1

Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

ex_1_6_1.py

### 1.6 Наследование классов - 2

Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.

ex_1_6_2.py

### 1.6 Наследование классов - 3

Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.

Рассмотрим класс Loggable:

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение, добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

Примечание
Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он будет содержать метод log, описанный выше.

ex_1_6_3.py

### 2.1 Ошибки и исключения - 1

Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

ex_2_1_1.py

### 2.1 Ошибки и исключения - 2

Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:

В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных

Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

ex_2_2_1.py

### 2.1 Ошибки и исключения - 3

Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.

ex_2_2_3.py


### 2.2 Работа с кодом: модули и импорт

В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Sample Input 1:

2016 4 20
14

Sample Output 1:

2016 5 4

ex_2_2.py


### 2.3 Итераторы и генераторы - 1

Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x, а элемент x является допущенным.

В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный класс filter, но будет использовать не одну функцию, а несколько.

Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не допускают. Обозначим эти количества за pos и neg.

Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает True, если элемент допущен, и False иначе.

Рассмотрим процесс допуска подробнее на следующем примере.
a = [1, 2, 3]
f2(x) = x % 2 == 0 # возвращает True, если x делится на 2
f3(x) = x % 3 == 0
judge_any(pos, neg) = pos >= 1 # возвращает True, если хотя бы одна функция допускает элемент

В этом примере мы хотим отфильтровать последовательность a и оставить только те элементы, которые делятся на два или на три.

Функция f2 допускает только элементы, делящиеся на два, а функция f3 допускает только элементы, делящиеся на три. Решающая функция допускает элемент в случае, если он был допущен хотя бы одной из функций f2 или f3, то есть элементы, которые делятся на два или на три.

Возьмем первый элемент x = 1.
f2(x) равно False, т. е. функция f2 не допускает элемент x.
f3(x) также равно False, т. е. функция f3 также не допускает элемент x.
В этом случае pos = 0, так как ни одна функция не допускает x, и соответственно neg = 2.
judge_any(0, 2) равно False, значит мы не допускаем элемент x = 1.

Возьмем второй элемент x = 2.
f2(x) равно True
f3(x) равно False
pos = 1, neg = 1
judge_any(1, 1) равно True, значит мы допускаем элемент x = 2.

Аналогично для третьего элемента x = 3.

Таким образом, получили последовательность допущенных элементов [2, 3].

ex_2_3_1.py

### 2.3 Итераторы и генераторы - 2

Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя. Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел. Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

Пример использования:

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
\# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

ex_2_3_2.py


### 2.5 Работа с функциями: functool и лямбда функции

Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

ex_2_5.py


### 3.1 Стандартные методы и функции для строк - 1

Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

ex_3_1_1.py

### 3.1 Стандартные методы и функции для строк - 2

Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

ex_3_1_2.py


### 3.3 Обзорно об интернете: http-запросы, html-страницы и requests - 1

Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег \<a href="B"\>, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

ex_3_3_1.py

### 3.3 Обзорно об интернете: http-запросы, html-страницы и requests - 2

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида \<a ... href="..." ... \> и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
\<a href="../some_path/index.html"\>.

Сайты следует выводить в алфавитном порядке.

ex_3_3_2.py


### 3.4 Распространённые форматы текстовых файлов: CSV, JSON - 1

ам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv

ex_3_4_1.py