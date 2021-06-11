import requests
import pandas as pd
import pycountry
import pycountry_convert as pc

URL = "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19"

def main():
    total = get_entry_count(URL)
    responses = fetch_seq_data(URL, limit=total)
    entries = [parse_response(response) for response in responses]
    flatten = lambda t: [item for sublist in t for item in sublist]
    df = parse_entries(flatten(entries))
    print(df.describe())
    print(f"Regions: {df.region.unique()}")
    df.to_csv('metadata.tsv', sep='\t')


def get_entry_count(url):
    p = { 'query': 'id:[* TO *]', 'size': 1, 'format': 'JSON' }
    return requests.get(url, params=p).json().get("hitCount")


def fetch_seq_data(url, limit):
    batch_size = 1000
    param_list = [{
        'query': 'id:[* TO *]',
        'size': str(batch_size),
        'format': 'JSON',
        'fields': 'collection_date,country',
        'start': i} for i in range(0, limit, batch_size)]
    return [requests.get(url, p).json() for p in param_list]


def parse_response(res):
    entries = res.get('entries')
    unlist = lambda x: x[0] if x else None
    flatten = lambda x: {
        'name': x.get('acc'),
        'date': unlist(x.get('fields', {}).get('collection_date')),
        'country': unlist(x.get('fields', {}).get('country')),
    }
    return [flatten(entry) for entry in entries]


def parse_entries(entries):

    def format_date(date):
        if date is None: return "?"
        year = date[:4]
        month = date[4:6].replace("00", "XX")
        day = date[6:].replace("00", "XX")
        return f"{year}-{month}-{day}"

    def country_to_region(x):
        try:
            # 'West Bank',
            country_code = pc.country_name_to_country_alpha2(x)
            continent_code = pc.country_alpha2_to_continent_code(country_code)
            # 'TL' > 'Asia'
            region = pc.convert_continent_code_to_continent_name(continent_code)
        except KeyError:
            return '?'
        return region

    df = pd.DataFrame.from_records(entries)
    return (
        df.assign(
            virus='ncov',
            date=df.date.map(format_date),
            region=df.country.map(country_to_region),
        )
    )


if __name__ == "__main__":
    main()

