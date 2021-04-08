from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('skowhegan.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" DROP TABLE IF EXISTS articles """)

        self.c.execute(""" CREATE TABLE articles (
        title text,
        date text,
        link text, 
        content text
        ) """)

    def process_item(self, item, spider):
        # Insert values
        self.c.execute("INSERT INTO articles ("
                       "title, "
                       "date, "
                       "link, "
                       "content)"
                       " VALUES (?,?,?,?)",
                       (item.get('title'),
                        item.get('date'),
                        item.get('link'),
                        item.get('content')
                        ))

        if 'link' in item.keys():
            print(f"New Article: {item['link']}")
        else:
            print(f"New Article: {item['title']}")

        self.conn.commit()  # commit after every entry

        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()