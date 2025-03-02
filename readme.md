Homework 6
Курс алгоритмів GoIT
Татач Юрій

Для коректної роботи програми виконайте наступні дії:
1. У терміналі перейдіть до кореневого каталогу програми;
2. Створіть віртуальне середовище для програми; Ви можете використати наступну команду:
 python3 -m venv .venv
3. Запустіть своє віртуальне середовище. Очікувана команда залежить від вашої ОС;
4. Встановіть очікувані пакети. Ви можете використати наступну команду:
 pip install -r requirements.txt
5. Щоб запустити програму до відповідного завдання, виконайте наступну команду в терміналі:
 python main.py /path/to/target/directory
6. Насолоджуйтесь результатом.

Після завершення не забудьте вимкнути віртуальне середовище.

Висновки до завдання 2:
Алгоритм DFS (пошук в глибину): Використовує стек для зберігання шляхів. Перевіряє можливість проходу вглиб, доки не знайде шлях до мети. DFS знаходить шлях, який перший з'являється в процесі глибокого пошуку, що може бути довшим і не оптимальним.
Алгоритм BFS (пошук в ширину): Використовує чергу для зберігання шляхів. Перевіряє можливість проходу по ширині, додаючи нові шляхи до черги. BFS знаходить найкоротший шлях, оскільки обхід відбувається по всіх сусідніх вузлах, поступово розширюючись до мети.
У наданому прикладі при порівнянні алгоритмів DFS та BFS для Київського метрополітену результати є ідентичними. Це зумовлено особливістю будови Київського метрополітену, що передбачає єдиний можливий шлях з однієї станції метро до іншої.
