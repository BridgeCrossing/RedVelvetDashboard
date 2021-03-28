############### Web Scrape Red Velvet Youtube Playlists ################

def SongViewsDF(Playlist_URL):

    # import dependencies
    from selenium import webdriver 
    import pandas as pd 
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import time

    # get URLS of first song in the playlists
    driver = webdriver.Chrome()
    driver.get(Playlist_URL)
    RV_Playlist_Data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    Playlist_FirstSong_URL_List = []
    for RV_Playlist in RV_Playlist_Data:
        Playlist_FirstSong_URL_List.append(RV_Playlist.get_attribute('href'))

    playlist_songs_list = []

    for FirstSong_URL in Playlist_FirstSong_URL_List:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.get(FirstSong_URL)
        time.sleep(2)
        
        
        soup = BeautifulSoup(driver.page_source,'html.parser')
        results = soup.find_all('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail")
        
        for result in results:
            result_str = str(result)
            
            if 'href' in result_str:
                result_str_split = result_str.split('href="')
                
                href_unclean = result_str_split[1]
                href_unclean_split = href_unclean.split('"')
                href_clean = href_unclean_split[0]
                
                if 'index' in href_clean:
                    playlist_song_url = "https://www.youtube.com" + href_clean
                    playlist_songs_list.append(playlist_song_url)
                else:
                    pass
            else:
                pass

    # clean song list
    playlist_songs_list.remove('https://www.youtube.com/watch?v=KZhsWw3soRE&amp;list=OLAK5uy_k-ICG9x9veLXf0SGK9N3sODx0fhI9ysvw&amp;index=2')
    other_RV_songs_list = ['https://www.youtube.com/watch?v=Ujb-gvqsoi0&list=PLQCakH1gpYY_3axEIKBLNc8v0SC2cdp_s',
                            'https://www.youtube.com/watch?v=cg-R48QN0Cg',
                            'https://www.youtube.com/watch?v=0Pokw-ouRqI',
                            'https://www.youtube.com/watch?v=Ct0i0lDrfDM',
                            'https://www.youtube.com/watch?v=GZeILCFk9w0',
                            'https://www.youtube.com/watch?v=wCWoUUWwdqg',
                            'https://www.youtube.com/watch?v=GTcM3qCeup0']

    for song in other_RV_songs_list:
        playlist_songs_list.append(song)


    # Scrape Views for each song
    views_list = []
    for song in playlist_songs_list:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.get(song)
        time.sleep(2)
        
        soup = BeautifulSoup(driver.page_source,'html.parser')
        result = soup.find_all('span', class_="view-count style-scope ytd-video-view-count-renderer")
        
        result_str = str(result)
        result_str_split = result_str.split('<span class="view-count style-scope ytd-video-view-count-renderer">')
        views = result_str_split[1].split(' view')[0]
        views_list.append(views)

    # Convert YouTube video views into numeric
    views_num_list = []
    for views in views_list:
        views_num = int(views.replace(',', ''))
        views_num_list.append(views_num)

    # Scrape YouTube video titles
    song_title_list = []
    for song in playlist_songs_list:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.get(song)
        time.sleep(2)
        
        soup = BeautifulSoup(driver.page_source,'html.parser')
        result = soup.find_all('h1', class_="title style-scope ytd-video-primary-info-renderer")
        
        result_str = str(result)
        result_str_split = result_str.split('<h1 class="title style-scope ytd-video-primary-info-renderer"><yt-formatted-string class="style-scope ytd-video-primary-info-renderer" force-default-style="">')
        song_title = result_str_split[1].split('</yt-formatted-string></h1>')[0]
        song_title_list.append(song_title)

    # create song and views dataframe 
    Song_Views_DF = pd.DataFrame({'Song': song_title_list, 'Views': views_num_list, 'Song_URL': playlist_songs_list})

    # get unique songs and view count
    Song_Views_Final = Song_Views_DF.groupby(['Song'])['Views'].sum().reset_index()

    return Song_Views_Final