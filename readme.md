
# DomainTools Enrich API Domain Status Tracking Script 

This Python script is designed to process a list of domains using the DomainTools Enrich API. It reads the domains from a CSV file, sends API requests to the DomainTools Enrich API in batches, and prints the domain and its active status for each processed domain. Additionally, it provides a summary of the total missing domains at the end of the output.

## Features :sparkles:

- :file_folder: Reads domains from a CSV file specified by the `CSV_FILE_PATH` constant.
- :arrows_counterclockwise: Processes domains in batches of size specified by the `BATCH_SIZE` constant to optimize API requests.
- :link: Sends API requests to the DomainTools Enrich API using the provided `API_USERNAME` and `API_KEY`.
- :page_facing_up: Prints the domain and its active status for each processed domain.
- :mag_right: Collects and displays the total missing domains at the end of the output.

## Requirements :clipboard:

- :snake: Python 3.x
- :wrench: requests library (can be installed via `pip install requests`)

## Usage :computer:

1. Set the following constants in the script:
    - `API_USERNAME`: Your DomainTools API username.
    - `API_KEY`: Your DomainTools API key.
    - `CSV_FILE_PATH`: The path to the CSV file containing the domains to be processed.
    - `BATCH_SIZE`: The number of domains to be processed in each API request batch (default is 100).
2. Prepare a CSV file with the domains to be processed. Each domain should be on a separate line or comma-separated within a single line.
3. Run the script using a Python interpreter:
   ```
   python script.py
   ```

The script will process the domains and display the output in the following format:

```
domain1.com : active
domain2.com : inactive
...

Total Missing Domains:
missing_domain1.com
missing_domain2.com
...
```

### Functions :gear:

- `read_domains_from_csv(file_path)`: Reads the domains from the specified CSV file and returns them as a list.
- `process_domains(domains)`: Processes the given list of domains in batches, sends API requests to the DomainTools Enrich API, and returns the list of missing domains.
- `main()`: The main function that orchestrates the script execution. It reads the domains from the CSV file, processes them, and displays the output.

### Error Handling :warning:

- If an API request fails, the script will print an error message with the corresponding status code.
- If an exception occurs during the API request, the script will print an error message with the exception details.

### Note :memo:

- Make sure to replace the `API_USERNAME` and `API_KEY` constants with your actual DomainTools API credentials.
- Ensure that the `CSV_FILE_PATH` constant points to the correct path of your CSV file containing the domains to be processed.
- The script requires an active internet connection to send API requests to the DomainTools Enrich API.

For any further assistance or questions, please contact the script developer.
