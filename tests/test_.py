
from Web_Scraping.Stock_Market_Challenge.stock_information import stats_info
from Web_Scraping.Book_Scraping_Challenge.scrap_all_page import scrap_all

def test_stats_info():
    assert stats_info('fb') > 0

def test_scrap_all():
    assert len(scrap_all(10)) > 0
