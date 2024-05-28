import mechanicalsoup
import os
import wget

def download_music(search_term):
    # Initialize a browser object
    music_browser = mechanicalsoup.StatefulBrowser()

    # URL for Google Music search
    music_url = f"https://www.google.com/search?q={search_term}+music+mp3"

    # Open the music search URL
    music_browser.open(music_url)

    # Get the current page HTML
    music_page = music_browser.get_current_page()

    # Find all links
    links = music_page.find_all('a')

    # Filter out links with href attribute starting with "/url?q=" which are search result links
    mp3_links = [link['href'][7:].split('&')[0] for link in links if link.get('href') and link['href'].startswith('/url?q=')]

    # Filter out links that do not end with ".mp3"
    mp3_links = [link for link in mp3_links if link.endswith('.mp3')]

    # Download MP3 files
    music_path = os.path.join(os.getcwd(), f"{search_term}_music")
    os.makedirs(music_path, exist_ok=True)
    print('Your music files are stored here:', music_path)

    # Download and save MP3 files
    for index, mp3_link in enumerate(mp3_links):
        try:
            music_save_as = os.path.join(music_path, f"{search_term}_music_{index}.mp3")
            wget.download(mp3_link, music_save_as)
        except Exception as e:
            print(f"Failed to download {mp3_link}: {e}")

# Main function
def main():
    # Input search term from the user
    search_term = input("Enter a search term: ")

    # Download music based on the search term
    download_music(search_term)

# Entry point of the script
if __name__ == "__main__":
    main()
