#!/usr/bin/env python
import os
import datetime
import urllib.request
import pandas as pd

# Define links to the locally saved EIA data
DATA_DIR = 'data'
ARCHIVE_DIR = f'{DATA_DIR}/archive'
# Define links to the EIA Monthly Energy Review tables
BASE_URL = 'https://www.eia.gov/totalenergy/data/browser'
MER_TABLES = {'overview': 'T01.01',
              'production': 'T01.02',
              'consumption': 'T01.03',
              'imports': 'T01.04A',
              'exports': 'T01.04B'}
OVERVIEW_TABLE = f'{DATA_DIR}/EIA_MER_overview'
TABLE_FORMATS = {'csv': 'csv',
                 'xls': 'xlsx'}

def generate_filename(table_title, table_format):
    """Generate the table's filename given its title and file format."""
    ext = TABLE_FORMATS[table_format]
    return f'EIA_MER_{table_title}.{ext}'

def get_current_data_publication_date():
    """Get the date of the current EIA MER."""
    current_data = pd.read_excel(f'{OVERVIEW_TABLE}.xlsx')
    column = current_data['U.S. Energy Information Administration'].dropna()
    date_cell = column[column.astype(str).str.contains('Release Date')].iloc[0]
    date_string = date_cell.split(':')[1].strip()
    date = datetime.datetime.strptime(date_string, '%B %d, %Y').date()
    return date

def move_current_data_to_archive():
    """
    Move the currently downloaded EIA data to the archive.

    If it exists, move the current EIA dataset to an archive (files are all
    less than one megabyte, so storing them for the conceivable future is not
    problematic.)
    """
    if os.path.isfile(f'{OVERVIEW_TABLE}.xlsx'):
        # The file exists, get the date and format it properly
        date = str(get_current_data_publication_date()).replace('-', '')
    else:
        return
    new_archive_dir = f'{ARCHIVE_DIR}/EIA_MER_{date}'
    try:
       os.makedirs(new_archive_dir)
    except OSError:
        # Give the user a chance to avoid files being overwritten
        answer = input(f"The directory '{new_archive_dir}' already exists."
                        "Should it be overwritten? [y/n]")
        if answer[0].lower() != 'y':
            return
    # Move the files to the archive
    for table_title in MER_TABLES:
        for table_format in TABLE_FORMATS:
            filename = generate_filename(table_title, table_format)
            current_path = f'{DATA_DIR}/{filename}'
            if os.path.isfile(current_path):
                new_path = f'{new_archive_dir}/{filename}'
                os.rename(current_path, new_path)
    print(f'Created the archive directory:\n\t{new_archive_dir}\n')


def download_eia_data_table(table_title):
    """
    Downloads an table type from the EIA website.

    Accesses the EIA website and downloads the given table. Tables are
    downloaded as both CSV files and Excel spreadsheets, and saved to the
    `data` directory.

    Parameters
    ––––––––––
    table : str
        The name of the table to be downloaded (e.g. production, consumption,
        imports, exports).
    """
    for table_format in TABLE_FORMATS:
        # URL from https://www.eia.gov/totalenergy/data/browser/ download link
        url = f'{BASE_URL}/{table_format}.php?tbl={MER_TABLES[table_title]}'
        filename = generate_filename(table_title, table_format)
        print(filename)
        urllib.request.urlretrieve(url, f'{DATA_DIR}/{filename}')

if __name__ == '__main__':
    print()
    # Move the current data to the archive
    move_current_data_to_archive()
    # Download the files, with printed status updates
    print('Downloading the most recent EIA monthly energy review data:')
    for table_title in MER_TABLES:
        print(f'\t-Energy {table_title} table')
        download_eia_data_table(table_title)
    print('Download complete.\n')
