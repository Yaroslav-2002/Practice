# Task 0

**Creating SSH key**

![photo_2021-07-04_20-04-24](https://user-images.githubusercontent.com/81532518/124393412-14e31980-dd03-11eb-85c2-7d0472ee3340.jpg)

**Adding new ssh on account**


![image](https://user-images.githubusercontent.com/81532518/124393597-d732c080-dd03-11eb-8d2c-2e6c93732046.png)

**git clone**

![photo_2021-07-04_20-04-32](https://user-images.githubusercontent.com/81532518/124393426-26c4bc80-dd03-11eb-9d04-e9a9f0398c6b.jpg)

**init commit та git push task 0**

![photo_2021-07-04_20-04-35](https://user-images.githubusercontent.com/81532518/124393428-27f5e980-dd03-11eb-933f-7032de0394ab.jpg)

**programme in VScode**

![image](https://user-images.githubusercontent.com/81532518/124393445-3512d880-dd03-11eb-8707-95d8ef2651fb.png)

**project file**

![photo_2021-07-04_20-06-15](https://user-images.githubusercontent.com/81532518/124519177-37536080-ddf1-11eb-8223-f8e3c7cc1327.jpg)

# Task 1

![photo_2021-07-06_00-25-40](https://user-images.githubusercontent.com/81532518/124519008-bd22dc00-ddf0-11eb-9177-cd9c75ec7c25.jpg)

![photo_2021-07-06_00-25-44](https://user-images.githubusercontent.com/81532518/124519011-c0b66300-ddf0-11eb-8929-dfeaeaa13a4b.jpg)


**Входимо в репозиторій та завантажуємо файл із завданням за допомогою git push**

**Пояснення до коду**

![photo_2021-07-06_00-32-37](https://user-images.githubusercontent.com/81532518/124519344-b2b51200-ddf1-11eb-9f29-f2fe97bdcac3.jpg)

**Строка 1 - імпортуємо модуль regex**

**Строка 2 - input**

**Строка 3 - findall витягує всі входження 1 або більше номерів з тексту і повертає їх у список**

**Строка 4 - re.sub видаляемо всі цифри зі строки**

**Строка 5 - замінюємо першу і останню літери за допомогою slice (-1 елемент по факту  буде завжди останнім, 0 - першим). Та склеюємо елементи с пробілом за допомгою join**

**Строка 6 - перетворюємо всі значенння массиву nums на int**

**Строка 7 - взводимо у степінь кожне число за його індексом в массиві int_nums якщо значення не дорівнює максимальному**

**Строка 8-12 - print всіх елеменнтів**

# Task 2
**Створюємо поле для вводу (одразу задаємо розтягування на 6 колонок та введення зліва):**

```python
calc = Entry(root, font=('Arial',15), justify=RIGHT)
calc.grid(row=0, column=0, columnspan=6, stick='we')
```
Для того, щоб числа вводилися нормально, то використамо конкатенацію -
```python value = calc.get()+str(digit)```
тепер кожен коли число вводиться, воно склюється з тим, що було в полі вводу.

**Задля того, щоб не можна блуо виконати декілька операцій одночасно задаємо умову, яка видалить останнє значення:**
```python
if value[-1] in '+-/*':
        value = value[:-1]
```        
**Є два основних види функцій, перші ті що створють кнопки, аби зменшити код.
Вони вертають:**

```python
return Button(text=operation, bd=5, font=('Arial', 13),  command=lambda :"функція куди направляє кнопка(дані що характеризують кнопку)")
```
*Інший вид функцій здійснює читання (calc.get()), видалення calc.delete(0, END), вставлення (calc.insert(0, дані (число), які потріібно вивести)*

**Створюємо конфігурацю (ознаки, характеристики) для колонок та рядків:**

```python
for i in range(4):
    root.grid_columnconfigure(i, minsize=60)

for i in range(1,5):
    root.grid_rowconfigure(i, minsize=60)
```


