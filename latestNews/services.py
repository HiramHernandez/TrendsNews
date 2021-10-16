from GoogleNews import GoogleNews

class TrendsNews():

    def get_news(self):
        googlenews = GoogleNews()
        googlenews.set_lang('es')
        googlenews.set_period('1')
        googlenews.set_encode('utf-8')
        googlenews.search('MX')
        result=googlenews.result()
        results = list()
        for x in result:
            results.append({'title': x['title'], 'when': x['date'], 'description': x['desc'], 'link': x['link'], 'img': x['img']})
        return results
