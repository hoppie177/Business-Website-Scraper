import requests
import csv
import time

API_KEY = "AIzaSyDqTOmB1_F_93FFxbS4ub5pj2CyzrDHlLc"
TYPE = "plumber"  # Change to 'restaurant', 'store', etc.
RADIUS = 2500  # Smaller radius for ZIP-level targeting

# Map of NYC ZIP codes to lat/lng
nyc_zip_codes = {
    "10001": (40.7506, -73.9972),  # Manhattan
    "11201": (40.6943, -73.9918),  # Brooklyn
    "10451": (40.8198, -73.9227),  # Bronx
    "11373": (40.7368, -73.8786),  # Queens
    "10301": (40.6318, -74.0944),  # Staten Island
}

def get_places_without_websites(api_key, lat, lng, radius, type, pages=2):
    places = []
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": f"{lat},{lng}",
        "radius": radius,
        "type": type
    }

    for _ in range(pages):
        res = requests.get(url, params=params)
        data = res.json()

        for result in data.get("results", []):
            place_id = result.get("place_id")
            details = get_place_details(api_key, place_id)

            if details:
                name = details.get("name")
                website = details.get("website")
                print(f"{name} | Website: {'Yes' if website else 'No'}")

                if "website" not in details:
                    places.append({
                        "Name": name,
                        "Address": details.get("formatted_address", ""),
                        "Phone": details.get("formatted_phone_number", ""),
                        "Website": "Not listed"
                    })

            time.sleep(1)  # Delay to avoid rate-limiting

        # Check for next page
        if "next_page_token" in data:
            time.sleep(2)
            params["pagetoken"] = data["next_page_token"]
        else:
            break

    return places

def get_place_details(api_key, place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "key": api_key,
        "place_id": place_id,
        "fields": "name,formatted_address,formatted_phone_number,website"
    }
    res = requests.get(url, params=params)
    return res.json().get("result", {})

# Run for all zip codes
all_results = []

for zip_code, (lat, lng) in nyc_zip_codes.items():
    print(f"\n🔍 Searching ZIP: {zip_code}")
    results = get_places_without_websites(API_KEY, lat, lng, RADIUS, TYPE, pages=2)
    all_results.extend(results)

# Save results to CSV
with open("nyc_zip_businesses_no_websites.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Address", "Phone", "Website"])
    writer.writeheader()
    writer.writerows(all_results)

print(f"\n✅ Saved {len(all_results)} businesses missing websites.")
