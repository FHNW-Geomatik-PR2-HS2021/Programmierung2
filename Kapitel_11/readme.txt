# Installation Virtual Environment:

conda create --name geopython37 python=3.7 jupyterlab -y
conda activate geopython37
conda install gdal rasterio matplotlib geopandas -y
conda install geoplot folium osmnx folium -c conda-forge -y 