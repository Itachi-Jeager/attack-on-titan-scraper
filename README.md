# Attack on Titan Scraper
This project scrapes Organization, Location and Titan Data from the Attack on Titan Fandom Page using Scrapy.

## Requirements
Python 3.10

black == 22.8.0

Scrapy == 2.11.1

scrapy-deltafetch==2.0.1

scrapy-magicfields==1.1.0


## Quick Start

**From the terminal**
```bash
python main.py
```
This scrapes data about titans and stores them in the scrapes file. This process also creates a file which stores the activities of the scraper in the .scrapy directory.


## Usage

`pip install -r requirements.txt`
1. Create a directory for cloning the scraper into
2. Make a virtual environment in the directory
3. Clone this Repo into the directory
4. Install the requirements for the program
5. Change directory into the repo directory
6. Change directory into the aot_scraper directory
7. Run the program by:
Either:
```python
if __name__ == "__main__":

    runner(['valid_scrpaer_name'], state=1)

```
OR:
```python

pool = Pool()
args = [(['valid_scrpaer_name'])]
pool.starmap(scrape, args)

```
8. The first implementation takes a list of valid scrapers and a deltafetch state, state=`, means the state should be reset (scrapers don't remember what they have scraped), while a state=0, means the state should not be reset (scrapers should remember URLS that have been visited before).

Using the runner function, you can quickly run the scraper to verify it's behavior, however, if the scraper is to be used a one of many services, then it might be better to use the multiprocessing function instead, as Scrapy is a multi-threaded and may conflict with other services.

## Quirks
- As with Scrapy projects the location of the scrapy config and the script executing the scrapers is very important to the functionality of the Scrapy program.
As a general rule, the scrapy config should be in the root directory of the Scrapy project and the module executing the scrapers should also be in the same directory *usually*
- Whenever the location of the scrapy config is changed the paths in the settings file and config should be updated accordingly.


## Contribute
If this project has been useful to you, leave a star.
If you would like to request a feature, open a new discussion or issue.

For major changes,
please open an issue first to discuss what you would like to change.
Make sure you assign the appropriate changelogs.

Fork this repository.

1. Create a branch: `git checkout -b <branch_name>`.
2. Make your changes and commit them: `git commit -m '<commit_message>`
3. Push to the original branch: `git push origin <project_name>/<location>`
4. Create the pull request
## License
