# Job Listings Scraper

A small Python script that scrapes job postings from the [Real Python fake jobs board](https://realpython.github.io/fake-jobs/) and saves them to a CSV file.

Built as a solution to the [Job Listings Scraper](https://roadmap.sh/projects/job-listings-scraper) project on roadmap.sh.

## What it does

1. Downloads the job board page with `requests`.
2. Parses each job card with BeautifulSoup.
3. Writes every job to `jobs.csv`.

For each job it collects:

| Column      | Example                                                                  |
| ----------- | ------------------------------------------------------------------------ |
| Title       | Senior Python Developer                                                  |
| Company     | Payne, Roberts and Davis                                                 |
| Location    | Stewartbury, AA                                                          |
| Date Posted | 2021-04-08                                                               |
| Link        | https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html |

## Requirements

- Python 3.10 or newer
- `requests`, `beautifulsoup4` and `truststore`

Install the dependencies:

```bash
pip install requests beautifulsoup4 truststore
```

## Usage

```bash
python req.py
```

The script prints the HTTP status code (`200` on success) and creates `jobs.csv` in the current directory, overwriting any existing file. The board currently lists 100 jobs.

Sample output:

```csv
Title,Company,Location,Date Posted,Link
Senior Python Developer,"Payne, Roberts and Davis","Stewartbury, AA",2021-04-08,https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
Energy engineer,Vasquez-Davidson,"Christopherville, AA",2021-04-08,https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html
```

## Why `truststore`?

By default `requests` checks HTTPS certificates against the `certifi` bundle of public certificate authorities. On networks where a corporate proxy inspects HTTPS traffic, sites are re-signed with a company certificate that `certifi` doesn't know, and requests fail with:

```
SSLCertVerificationError: certificate verify failed: unable to get local issuer certificate
```

Calling `truststore.inject_into_ssl()` makes Python verify certificates against the operating system's certificate store instead, where the company certificate is already trusted. Verification stays enabled, and the script works the same on networks without such a proxy.

## Project structure

```
job-listings-scraper/
├── req.py      # the scraper
├── jobs.csv    # generated output
└── README.md
```
