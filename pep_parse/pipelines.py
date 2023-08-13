import csv
import datetime as dt

from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_summary[status] += 1
        return item

    def close_spider(self, spider):
        summary_table = (
            ('Статус', 'Количество'),
            *self.status_summary.items(),
            ('Total', sum(self.status_summary.values()))
        )
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(summary_table)
