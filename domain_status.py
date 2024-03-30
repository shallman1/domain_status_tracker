import csv
import requests

API_USERNAME = 'api_user'
API_KEY = 'api_key'
API_ENDPOINT = 'https://api.domaintools.com/v1/iris-enrich/'
CSV_FILE_PATH = 'domains.csv'
BATCH_SIZE = 100

def read_domains_from_csv(file_path):
    with open(file_path, 'r') as file:
        return [domain for row in csv.reader(file) for domain in row]

def process_domains(domains):
    all_missing_domains = []
    for i in range(0, len(domains), BATCH_SIZE):
        batch = domains[i:i+BATCH_SIZE]
        query_url = f"{API_ENDPOINT}?domain={','.join(batch)}&api_username={API_USERNAME}&api_key={API_KEY}"
        try:
            response = requests.get(query_url)
            if response.status_code == 200:
                data = response.json()
                results = data['response']['results']
                for domain_data in results:
                    domain = domain_data['domain']
                    active_status = 'active' if domain_data['active'] else 'inactive'
                    print(f"{domain} : {active_status}")
                all_missing_domains.extend(data['response'].get('missing_domains', []))
            else:
                print(f"Request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    return all_missing_domains

def main():
    domains = read_domains_from_csv(CSV_FILE_PATH)
    missing_domains = process_domains(domains)
    if missing_domains:
        print("\nTotal Missing Domains:")
        for missing_domain in missing_domains:
            print(missing_domain)

if __name__ == '__main__':
    main()
