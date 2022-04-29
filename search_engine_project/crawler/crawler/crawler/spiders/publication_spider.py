import scrapy


class crawler(scrapy.Spider):
    name = "publications"

    start_urls = [
        "https://pureportal.coventry.ac.uk/en/organisations/school-of-computing-electronics-and-maths/publications/"]

    def parse(self, response):
        for publication in response.css('h3.title a.link::attr(href)'):
            yield response.follow(publication.get(), callback=self.parse_abstract)
        next_page = response.css('a.nextLink::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_abstract(self, response):
        abstract_text = response.css('div.textblock::text').get()
        yield {
            "title": response.css('div.rendering h1 span::text').get(),
            "link": response.selector.xpath('/html/head/meta[6]').get().replace('<meta property=\"og:url\" content=\"', '').replace('\">', ''),
            "publication date": response.css('tr.status span.date::text').get(),
            "authors": response.css('p.relations.persons::text').get(),
            "author link": response.css('a.link.person::attr(href)').get(),
            "abstract": abstract_text
        }
