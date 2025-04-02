import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json

st.set_page_config(layout="wide", page_title="California Map")

# Streamlit app title
st.title("Eligible Muslim Voters by County in California.")

# Load processed data
data_path = "arab_voters_by_countyWithNames.csv"  # Your pre-aggregated data: County, Count
data = pd.read_csv(data_path)

# Clean county names
data["county"] = data["County_Name"].str.strip().str.title()
# Create a column for custom hover text
data["hover_text"] = data["county"] + ": " + data["arab_voter_count"].apply(lambda x: f"{x:,}")
# Load California GeoJSON
geojson_path = "California_County_Boundaries.geojson"
with open(geojson_path, "r") as file:
    geojson_data = json.load(file)

# Extract county centroids
county_centroids = []
for feature in geojson_data["features"]:
    county_name = feature["properties"]["CountyName"]  # Check your geojson property key
    coordinates = feature["geometry"]["coordinates"]

    if feature["geometry"]["type"] == "MultiPolygon":
        coordinates = coordinates[0]

    lon = sum([point[0] for point in coordinates[0]]) / len(coordinates[0])
    lat = sum([point[1] for point in coordinates[0]]) / len(coordinates[0])

    county_centroids.append({"county": county_name, "lon": lon, "lat": lat})

centroid_df = pd.DataFrame(county_centroids)

# Build Choropleth
fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson_data,
    locations=data["County_Name"],
    z=data["arab_voter_count"],
    text=data["hover_text"],
    hoverinfo="text",
    featureidkey="properties.CountyName",  # Check your geojson key
    colorscale=[
        [0, "white"],
        [0.01, "yellow"],
        [0.1, "lightgreen"],
        [1, "darkgreen"]
    ],
    marker_opacity=0.8,
    marker_line_width=1.2
))

# Add county labels


# Set map focus to California
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5.5,
    mapbox_center={"lat": 37.5, "lon": -119.5},
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600,
    width=500,
    coloraxis_colorbar=dict(
        title="Arab Voter Count"
    )
)

st.plotly_chart(fig, use_container_width=True)
