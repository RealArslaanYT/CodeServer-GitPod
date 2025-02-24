import vlc
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import time


def search_song(query):
    try:
        results = VideosSearch(query, limit=1)
        return results.result()['result'][0]
    except Exception as e:
        print(f"Error in search_song: {e}")
        return None


def play_song(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            song_title = info_dict['title']
            print(f"Now playing: {song_title}")

            Instance = vlc.Instance('--no-xlib -q > /dev/null 2>&1')
            Instance.log_unset()
            player = Instance.media_player_new()

            media = Instance.media_new(audio_url)
            player.set_media(media)
            player.play()

            print("Press 'q' to quit.")
            while True:
                if player.get_state() == vlc.State.Ended:
                    print("Song ended.")
                    break
                time.sleep(0.5)
                if input() == 'q':
                    print("Stopping playback.")
                    player.stop()
                    break

    except Exception as e:
        print(f"Error in play_song: {e}")


def main():
    print("Welcome to the CLI Music Player!")
    query = input("Enter song query to search: ")
    song_info = search_song(query)

    if song_info:
        print(f"Found: {song_info['title']}")
        play_song(song_info['link'])
    else:
        print("No song found.")


if __name__ == "__main__":
    main()
