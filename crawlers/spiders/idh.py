
# coding: utf-8

# In[2]:



import scrapy, json, pdb
from scrapy.exporters import CsvItemExporter
from scrapy import signals

field_list=[
    u'name',
    u'Population in severe multidimensional poverty (%)',
    u'Life Expectancy Index',
    u'Population, total (millions)',
    u'Expected years of schooling (years)',
    u'Human Development Index (HDI), male',
    u'Population, ages 65 and older (millions)',
    u'Population, urban (%)',
    u'Inequality-adjusted education index',
    u'Overall loss in HDI due to inequality (%)',
    u'Employment to population ratio (% ages 15 and older)',
    u'Population with at least some secondary education, male (% ages 25 and older)',
    u'Gross national income (GNI) per capita (2011 PPP$)',
    u'Gross domestic product (GDP), total (2011 PPP $ billions)',
    u'Multidimensional poverty index (MPI)',
    u'Estimated gross national income per capita, male (2011 PPP$)',
    u'Gross fixed capital formation (% of GDP)',
    u'Labour force participation rate, male (% ages 15 and older)',
    u'Gender Development Index (GDI)',
    u'Under-five mortality rate (per 1,000 live births)',
    u'Inequality in life expectancy (%)',
    u'Female share of paid employment in non-agriculture',
    u'Domestic credit provided by financial sector (% of GDP)',
    u'Adult literacy rate (% ages 15 and older)',
    u'Population, under age 5 (millions)',
    u'HDI rank',
    u'Total unemployment rate (% of labour force)',
    u'Old age dependency ratio (old age (65 and older) per 100 people (ages 15-64))',
    u'Mean years of schooling, male (years)',
    u'Life expectancy at birth (years)',
    u'Inequality-adjusted income index',
    u'Labour force participation rate, female (% ages 15 and older)',
    u'Population in multidimensional poverty, headcount (thousands)',
    u'Population in multidimensional poverty, headcount (%)',
    u'Dependency ratio, young age (0-14) (per 100 people ages 15-64)',
    u'Human Development Index (HDI), female',
    u'Net migration rate (per 1,000 people)',
    u'Gross enrolment ratio, secondary (% of secondary school-age population)',
    u'Youth unemployment rate (% of labour force ages 15-24)',
    u'Remittances, inflows (% of GDP)',
    u'Estimated gross national income per capita, female (2011 PPP$)',
    u'Primary school teachers trained to teach (%)',
    u'Infant mortality rate (per 1,000 live births)',
    u'Mean years of schooling (years)',
    u'Coefficient of human inequality',
    u'Gross domestic product (GDP) per capita (2011 PPP $)',
    u'Exports and Imports (% of GDP)',
    u'Sex ratio at birth (male to female births)',
    u'Internet users (% of population)',
    u'Education index',
    u'Population with at least some secondary education, female (% ages 25 and older)',
    u'Population near multidimensional poverty (%)',
    u'Youth unemployment rate, female to male ratio',
    u'Gross enrolment ratio, tertiary (% of tertiary school-age population)',
    u'Gross enrolment ratio, pre-primary (% of preschool-age children)',
    u'Mean years of schooling, female (years)',
    u'Inequality in education (%)',
    u'Share of seats in parliament (% held by women)',
    u'Population, ages 15\u201364 (millions)',
    u'Expected years of schooling, male (years)',
    u'Inequality-adjusted life expectancy index',
    u'Forest area (% of total land area)',
    u'Population with at least some secondary education (% ages 25 and older)',
    u'Adolescent birth rate (births per 1,000 women ages 15-19)',
    u'Human Development Index (HDI)',
    u'Labour force participation rate (% ages 15 and older)',
    u'Median age (years)',
    u'Gross enrolment ratio, primary (% of primary school-age population)',
    u'Mobile phone subscriptions (per 100 people)',
    u'Life expectancy at birth, female (years)',
    u'Maternal mortality ratio (deaths per 100,000 live births)',
    u'Gender Inequality Index (GII)',
    u'Expected years of schooling, female (years)',
    u'Inequality-adjusted HDI (IHDI)',
    u'Population in multidimensional poverty, intensity of deprivation (%)',
    u'HIV prevalence, adult (% ages 15-49)',
    u'Private capital flows (% of GDP)',
    u'Income index',
    u'Inequality in income (%)',
    u'Life expectancy at birth, male (years)',
    u'Pupil-teacher ratio, primary school (number of pupils per teacher)',
    u'Foreign direct investment, net inflows (% of GDP)',
    u'Total unemployment rate, female to male ratio',
]


# In[ ]:


class IdhSpiderItem(scrapy.Item):
    fields = {f:scrapy.Field() for f in field_list}


# In[5]:


class IdhSpider(scrapy.Spider):
    name = 'idh'
    allowed_domains = []
    start_urls = ['http://hdr.undp.org/sites/all/themes/hdr_theme/js/bars.json']

    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI': 'output/idh.csv',
    }

    def parse(self, response):
        items = {}
        _list = [x for x in json.loads(response.body) if x['year'] == "2015"]
        for point in _list:
            name = point['country']
            if not name in items.keys():
                items[name] = IdhSpiderItem(name=point['country'])
            items[name][point['indicator']] = point['value']
        #print items
        for item in items.values():
            yield item