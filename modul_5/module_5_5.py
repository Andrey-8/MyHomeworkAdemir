import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname  # атрибут имя пользователя (строка)

    def __eq__(self, other):
        return other.nickname == self.nickname  # при сравнении имени, возвращаем никнейм

    def get_info(self):  # база логинов и паролей пользователей
        return self.nickname, self.password


class Video:
    """
    title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):  # названия видео, строка.
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    """
    users(список объектов класс User), videos(список объектов класса Video), current_user(текущий пользователь, User)
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None  # изначально нет пользователя, потому None

    def log_in(self, login, password):
        for user in self.users:  # проверка наличия пользователя в списке зарегестрированных пользователей
            if (login, hash(password)) == user.get_info():  # получаем инфу из базы о пользователе (логин и пароль)
                self.current_user = user  # если пользователь найден в базе, возвращаем его ник
                return user

    def register(self, nickname, password, age):  # регистрация нового пользователя
        new_user = User(nickname, password, age)
        if new_user not in self.users:  # если нового пользователя еще нет в базе
            self.users.append(new_user)  # то добавляем в базу нового пользователя
            self.current_user = new_user  # после успешной регистрации, новый пользователь стал текущим пользователем
        else:
            print(f'Пользователь {nickname} уже существует.')

    def log_out(self):  # для сброса текущего пользователя
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:  # проверяем новое видео на наличие в базе
            if video.title not in self.videos:  # если его еще нет в базе, то добавляем его.
                self.videos.append(video)

    def get_videos(self, search):  # принимает поисковое слово и возвращает список названий всех видео,
        titles = []     # где в названии поисковое слово. Следует учесть, что слово 'UrbaN' присутствует
        for video in self.videos:  # в строке 'Urban the best' (не учитывать регистр)
            if search.lower() in str(video).lower():  # если нашли видео по слову поиска (search),
                titles.append(video)  # то добавляем его в список найденного
        return titles

    def watch_video(self, title):  # перед просмотром найденного видео, проверяем пользователя
        if self.current_user is None:  # если такого пользователя нет
            print('Войдите в аккаунт, чтобы смотреть видео')  # то просим  войти в аккаунт
            return
        for video in self.videos:  # после входа в акк, сравниваем поисковый запрос с базой видео
            if title == video.title:  # если совпадает, то проверяем возраст пользователя
                if video.adult_mode and self.current_user.age >= 18:  # и наличие возрастного ограничения самого видео
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
