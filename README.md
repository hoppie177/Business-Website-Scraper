# Business-Website-Scraper
A small Python tool that allows you to find businesses without websites.

# 🧰 Business Finder — No Websites

This is a Python tool I made to scrape local (NYC) businesses that **don’t have websites** using the Google Places API. You can change the Zip codes withtin the code in order to scrape other cities. I chose New York at this time because they have a lot of millionaires. I’m mostly using it to find small businesses I can help get online — plumbers, contractors, shops, etc. In order to try and sell them my Website design services. A great tool for generating leads and finding potential long term clients. 

If you’re trying to find leads, test out outreach, or just want to experiment with Google APIs, this is a good place to start.

---

## 🔍 What It Does

- Takes a bunch of NYC ZIP codes (Zip codes can be changed, and second version will be an exe. that has an interface for all of this and more.)
- Converts them to lat/lng coordinates
- Searches for businesses (you can set type like `plumber`, `electrician`, etc.)
- Checks if they **have a website**
- Saves any business **missing a website** into a CSV file

---

## 📦 Example Output

After running it, you’ll get something like:

Name: Titan Mechanical
Website: No

Once finished scraping you'll get something like "Saved to `nyc_zip_businesses_no_websites.csv`." Will all the the business info in that file. 

(I understand from here you will have to fetch the business info yourself but this is just V1.)

Grab a Google Places API key from here:
https://console.cloud.google.com/google/maps-apis/overview

Put your API key at the top of the file:
API_KEY = "your_google_places_api_key"

Then run the script:
python business_finder.py

----------------------------------------------------
🧠 Customizing It
Change the ZIP codes or add more in the nyc_zip_codes dictionary

Adjust the business type with:

python
Copy
Edit
TYPE = "plumber"
(You can also bump up pages=3 to search deeper)


