import pandas as pd
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

all_flights_df = pd.read_csv("airports.dat", delimiter=",")
flights_df2 = pd.read_csv("otselennud.csv", delimiter=";")
flights_df3 = pd.read_csv("flights21.csv", delimiter=";")

def merge_and_make_pre_corona_csv():
    """
    Make a new csv file
    :return:
    """
    merged_data = pd.merge(all_flights_df, flights_df2, on='IATA')
    merged_data.to_csv('pre_corona.csv')
    
    
def merge_and_make_after_corona_csv():
    """
    Make a new csv file
    :return:
    """
    merged_data = pd.merge(all_flights_df, flights_df3, on='IATA')
    merged_data.to_csv('after_corona.csv')


merge_and_make_pre_corona_csv()
merge_and_make_after_corona_csv()


lennud_df = pd.read_csv("pre_corona.csv", delimiter=",")
lennud_df2 = pd.read_csv("after_corona.csv", delimiter=",")

for index, row in lennud_df.iterrows():
    print(row['Name'], row['Latitude'], row['Longitude'])


def make_pre_corona_flights_picture():
    """
    Make a picture with flight routes from Tallinn to other airports
    :return:
    """

    plt.figure(figsize=(9, 9))
    ax = plt.axes(projection=cartopy.crs.TransverseMercator(32))
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=1)
    ax.coastlines(resolution='110m')
    ax.add_feature(cartopy.feature.OCEAN, facecolor=(0.5,0.5,0.5))
    ax.gridlines()
    ax.set_extent ((-7.5, 50, 34, 69), cartopy.crs.PlateCarree())
    
    
    tal_lat, tal_lon = 58.9907989501953, 22.8306999206542

    for index, row in lennud_df.iterrows():
        print(row['Name'], row['Latitude'], row['Longitude'])

        plt.plot([tal_lon, row['Longitude']], [tal_lat, row['Latitude']],
                 color='blue', linewidth=0.5, marker='o',
                 transform=ccrs.Geodetic(),
                 )

        plt.plot([tal_lon, row['Longitude']], [tal_lat, row['Latitude']],
                 color='gray', linestyle='--',
                 transform=ccrs.PlateCarree(),
                 )

        plt.text(tal_lon + 2, tal_lat, 'Tallinn',
                 horizontalalignment='center',
                 color='green',
                 transform=ccrs.Geodetic())
        
        
        plt.text(row['Longitude'], row['Latitude'] , row['IATA'],
        horizontalalignment='left',
        transform=ccrs.Geodetic())
        
    plt.savefig('flights_from_tallinn_pre_corona.png')

    plt.show()
    
    
    
def make_after_corona_flights_picture():
    """
    Make a picture with flight routes from Tallinn to other airports after corona
    :return:
    """

    plt.figure(figsize=(9, 9))
    ax = plt.axes(projection=cartopy.crs.TransverseMercator(32))
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=1)
    ax.coastlines(resolution='110m')
    ax.add_feature(cartopy.feature.OCEAN, facecolor=(0.5,0.5,0.5))
    ax.gridlines()
    ax.set_extent ((-7.5, 50, 34, 69), cartopy.crs.PlateCarree())
    
    
    tal_lat, tal_lon = 58.9907989501953, 22.8306999206542

    for index, row in lennud_df2.iterrows():
        print(row['Name'], row['Latitude'], row['Longitude'])

        plt.plot([tal_lon, row['Longitude']], [tal_lat, row['Latitude']],
                 color='blue', linewidth=0.5, marker='o',
                 transform=ccrs.Geodetic(),
                 )

        plt.plot([tal_lon, row['Longitude']], [tal_lat, row['Latitude']],
                 color='gray', linestyle='--',
                 transform=ccrs.PlateCarree(),
                 )

        plt.text(tal_lon + 2, tal_lat, 'Tallinn',
                 horizontalalignment='center',
                 color='green',
                 transform=ccrs.Geodetic())
        
        
        plt.text(row['Longitude'], row['Latitude'] , row['IATA'],
        horizontalalignment='left',
        transform=ccrs.Geodetic())
        
    plt.savefig('flights_from_tallinn_after_corona.png')

    plt.show()
    
make_pre_corona_flights_picture()
make_after_corona_flights_picture()


