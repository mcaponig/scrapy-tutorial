# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

##from scrapy import signals
##from scrapy.exporters import CsvItemExporter
##
##class TutorialPipeline(object):
##    def process_item(self, item, spider):
##        return item
    
##class CSVPipeline(object):
##
##  def __init__(self):g
##    self.files = {}
##
##  @classmethod
##  def from_crawler(cls, crawler):
##    pipeline = cls()
##    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
##    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
##    return pipeline
##
##  def spider_opened(self, spider):
##    file = open('%s_items.csv' % spider.name, 'w+b')
##    self.files[spider] = file
##    self.exporter = CsvItemExporter(file)
##    self.exporter.fields_to_export = [list with Names of fields to export - order is important]
##    self.exporter.start_exporting()
##
##  def spider_closed(self, spider):
##    self.exporter.finish_exporting()
##    file = self.files.pop(spider)
##    file.close()
##
##  def process_item(self, item, spider):
##    self.exporter.export_item(item)
##    return item

# pipeline.py adapted from
# https://trorb.wordpress.com/2014/05/15/basic-scrapy-example-with-csvitemexporter-pipeline/

import csv
import settings


class WriteToCsv(object):

    def __init__(self):
        self.csvwriter = csv.writer(open('pipe_out.csv', 'wb'))
        
    def process_item(self, item, dmoz):
        altdesc = str(item['desc'])
        short = altdesc[99:-115]
        self.csvwriter.writerow([item['title'][0], item['link'][0], short])
        return item
 
##class CsvWriterPipeline(object):
## 
##    def __init__(self):
##        self.csvwriter = csv.writer(open('output.csv', 'wb'))
## 
##        # build your row to export, then export the row
##        row = [items['title'],items['link'],items['desc']]
##        self.csvwriter.writerow(row)
##        return item
