import requests
import faker
import random
from django.core.files import File


def generate_genre(n: int) -> None:
    for _ in range(n):
        Genre.objects.create(name=fake.text().split()[2])


def generate_artist(n: int) -> None:
    for _ in range(n):
        Artist.objects.create(first_name=fake.first_name(), last_name=fake.last_name())


def generate_album(n: int) -> None:
    for _ in range(n):
        Album.objects.create(
            title=" ".join(fake.text().split()[1:4]),
            author=random.choice(Artist.objects.all()),
        )


def generate_song(n: int, cover_path: str, file_path: str) -> None:
    covers = os.listdir(cover_path)
    files = os.listdir(file_path)

    covers_count = len(covers) - 1
    files_count = len(files) - 1

    for _ in range(n):
        random_cover = cover_path + "/" + covers[random.randint(0, covers_count)]
        random_file = file_path + "/" + files[random.randint(0, files_count)]

        if os.path.exists(random_cover):
            if os.path.exists(random_file):
                song = Song(
                    title=" ".join(fake.text().split()[0:5]),
                    cover=open(random_cover, "rb"),
                    file=open(random_file, "rb"),
                    genres=[random.choice([int(i.id) for i in Genre.objects.all()])],
                    # genres=[3],
                    album=random.choice(Album.objects.all()),
                    listened=0,
                )
                # song.save()
                print(song.title, "\n", song.cover)
            else:
                print(f"{file_path}: are not valid file path")
        else:
            print(f"{cover_path}: are not valid cover path")


def main():
    generate_song(1, "D:/Pictures/Saved Pictures/pictures", "D:/musika")
    # generate_album(3)
    # generate_artist(3)
    # generate_genre(6)
    # print(fake.image())
    # generate_artist(3)
    # x=  fake.image()
    # print(x)


if __name__ == "__main__":

    import os
    from django.core.asgi import get_asgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_asgi_application()
    from apps.users.models import User, PlayList, UserProfile
    from apps.spotify.models import Genre, Artist, Album, Song

    fake = faker.Faker()

    # main()
    # user = User(
    #     username = "Saydula",
    #     first_name = "Sayd",
    #     last_name = "Botirov",
    #     email = "saydula34@gmail.com",
    #     avatar = File(open("media/avatar.png", "rb"), name="avatar.png")
    # )
    # user.set_password("2007")
    # user.save()
