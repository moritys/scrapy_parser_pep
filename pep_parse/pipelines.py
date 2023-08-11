from collections import defaultdict

from pep_parse.outputs import file_output


class SummaryPipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        count_statuses_dict = defaultdict(int)
        page_status = item['status']
        count_statuses_dict[page_status] += 1
        summary_table = (
            ('Статус', 'Количество'),
            *count_statuses_dict.items(),
            ('Total', sum(count_statuses_dict.values()))
        )
        print(summary_table)
        return item

    def close_spider(self, spider):
        pass
