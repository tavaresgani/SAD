import pandas as pd
import sqlite3

conn = sqlite3.connect("semana0302_flights.db")
routes = pd.read_sql_query("select cast(sa.longitude as float) as source_lon, cast(sa.latitude as float) as source_lat, cast(da.longitude as float) as dest_lon, cast(da.latitude as float) as dest_lat from routes inner join airports sa on sa.id = routes.source_id inner join airports da on da.id = routes.dest_id;", conn)


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
    
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')

m.drawcoastlines()
m.drawmapboundary()


conn.close()

