from observer_pattern import Observable, Observer


class YouTuber(Observable):

    def __init__(self, name: str):
        super().__init__()
        self._name = name
        self._newest_video: str = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def newest_video(self) -> str:
        return self._newest_video

    def release_video(self, video: str):
        self._newest_video = video
        self.notify()


class Audience(Observer):

    def subscribe(self, youtuber: YouTuber):
        youtuber.attach(self)

    def update(self, youtuber: YouTuber):
        print(f"{youtuber.name} updates a video: \"{youtuber.newest_video}\".")


def main():
    howfun = YouTuber("HowFun")
    leville = Audience()
    leville.subscribe(howfun)
    howfun.release_video("第一次求婚，好緊張")


if __name__ == "__main__":
    main()
