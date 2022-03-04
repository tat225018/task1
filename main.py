name = 'Татьяна'
age = 18

print('\nАвтора зовут - ' + name + '. ' + 'Возраст - ' + str(age) + ' лет.')
print((name + " ") * 5)

user_name = input("\nКак вас зовут? ")
user_age = input("Сколько вам лет? ")
print('Здравствуйте, ' + user_name + '!')
print('(ПРОБНАЯ ШУТКА) А почему Вы такой(ая) маленький(ая)? ' + '(Ведь Вам всего лишь ' + user_age + ' годиков:) )')

user_age = int(user_age)
if user_age <= 0:
    print('\nВсе ясно, автору (не Татьяне) 0 лет -_- ')
elif 0 < user_age < 18:
    print('\nВ детстве мама боялась, что я попаду в плохую компанию, а я вообще ни в какую не попал(а). класс..')
elif user_age == 18:
    print("\nДа Вам столько же сколько и мне!! :) ")
elif 18 < user_age < 25:
    print('\nДа у вас, как я погляжу, появились седые волосы!!')
elif 25 <= user_age < 50:
    print('\nДа у вас определенно уже хрустят кости!! Вот у автора уже:) ')
elif 50 <= user_age <= 100:
    print('\nЧто вы делаете за моей программой?! Вы что.. ')
elif user_age > 100:
    print('\nВы вообще кто?? Призрак, домовой или вампир?!.. ')

print("\nВаше имя со 2-й до предпоследней буквы: " + user_name[1:-1] + ".")
print("Ваше имя наоборот))) : " + user_name[::-1] + ".")
print("Ваше имя с последними 3-мя буквами: " + user_name[-3:] + ".")
print("Ваше имя с первыми 5-ю буквами: " + user_name[:5] + ".")

print("\nДлина имени составляет", len(user_name), "букв(ы).")
sum = 0
mult = 1
user_age_ex = user_age
while user_age_ex > 0:
    temp = user_age_ex % 10
    sum = sum + temp
    mult = mult * temp
    user_age_ex = user_age_ex // 10
print("Сумма чисел возраста:", str(sum) + ". А произведение:", str(mult) + ".")

print("\nИмя заглавными буквами: " + user_name.upper() + ".")
print("Имя маленькими буквами: " + user_name.lower() + ".")
user_name = str.capitalize(user_name)
print("Имя с заглавной буквы: " + user_name)
print("Имя с маленькой буквы: " + user_name.swapcase())
user_name = user_name.title()                                    # вернем/сделаем имя красивым

if " " in user_name:
    raise Exception("В Вашем имени присутствует пробел")
    
if user_age < 0 or user_age > 150:
    raise Exception("\nВы ввели запредельный возраст")           # ошибку выдает в начале


task = int(input("\nРешите задачу: 199-11**2*15 ... "))          #  1616
if task == 1616:
    print("Верно! Ответ 1616.")
else:
    print("Неверный ответ! (Ваш ответ - " + str(task) + ")")
