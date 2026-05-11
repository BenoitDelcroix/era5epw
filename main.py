from era5epw.main import download_and_make_epw
import dotenv

dotenv.load_dotenv()

download_and_make_epw(
    year=2025,
    latitude=48.8,
    longitude=2.4,
    city_name="Paris",
    time_zone=1,
    elevation=0,
    output_file="era5epw_paris_2025.epw",
    apply_time_zone_to_data=True,
)