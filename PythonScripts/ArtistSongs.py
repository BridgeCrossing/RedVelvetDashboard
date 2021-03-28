def ArtistSongsDF(DF):

    # import dependencies
    import pandas as pd

    RV_list = ['Irene', 'Wendy', 'Joy', 'Seulgi', 'Yeri']
        
    Wendy_list = []
    Irene_list = []
    Joy_list = []
    Seulgi_list = []
    Yeri_list = []

    for i, row in DF.iterrows():
        for RV in RV_list:
            artist = row[2]

            if RV == 'Wendy' and RV in artist:
                Wendy_list.append(1)
            elif RV == 'Irene' and RV in artist:
                Irene_list.append(1)
            elif RV == 'Joy' and RV in artist:
                Joy_list.append(1)
            elif RV == 'Seulgi' and RV in artist:
                Seulgi_list.append(1)
            elif RV == 'Yeri' and RV in artist:
                Yeri_list.append(1)
            else:
                pass

    Artist_SongCounter_DF = pd.DataFrame({'Artist': RV_list, 'Songs': [sum(Irene_list), sum(Wendy_list),
                                                                        sum(Joy_list), sum(Seulgi_list),
                                                                        sum(Yeri_list)], 
                                            'Color': ['rgb(255,192,203)', 'rgb(187,234,255)', 'rgb(152, 255, 152)', 'rgb(253, 221, 92)', 'rgb(238,130,238)']})
    
    return Artist_SongCounter_DF