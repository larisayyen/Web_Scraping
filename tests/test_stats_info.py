
from Web_Scraping.stock_information import stats_info

def test_stats_info():
    assert stats_info('fb') > 0
