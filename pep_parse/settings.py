from pep_parse.constants import BASE_DIR


DOWNLOAD_DIR = BASE_DIR / 'results'
DOWNLOAD_DIR.mkdir(exist_ok=True)

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True

PEP_FILE = './results/pep_%(time)s.csv'
FEEDS = {
    PEP_FILE: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.SummaryPipeline': 300,
}
