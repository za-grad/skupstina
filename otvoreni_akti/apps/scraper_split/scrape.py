from .scrape_utils import scrape_new_periods, scrape_new_acts


def start(*args, **kwargs):
    """
    This function first checks if there are any new periods that have been added to the Grad Split website
    since the last performed scrape. It only scrapes new periods that are not inside the ScraperPeriod model
    and does not check for new acts added to a previously scraped period in the ScraperPeriod model.

    Example:
    1. The last full scrape was done on 29.Feb.2020.
    2. The database has all acts from 28.Feb.2020 to 03.June.2009
    3. This function is run on 08.Mar.2020.
    4. If it finds that a new period has been added (03.Mar.2020 to 03.Mar.2020), it will scrape all the acts from
       this new period.
    5. If it finds that no new periods have been added since 28.Feb.2020, it will exit.

    :param kwargs:
        int max_periods:
            Scrapes the latest acts within the last 'max_periods' periods.
            If max_periods is not defined it scrapes everything.
    """
    scrape_new_periods()

    if 'max_periods' in kwargs:
        max_periods = kwargs['max_periods']
        scrape_new_acts(max_periods=max_periods)
    else:
        scrape_new_acts()