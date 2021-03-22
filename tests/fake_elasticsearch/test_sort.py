from tests import TestElasticmock, INDEX_NAME, DOC_TYPE


class TestSearch(TestElasticmock):

    def test_sort_by_field_asc(self):
        index_quantity = 10
        result = []
        for i in range(0, index_quantity):
            body = {'data': 'test_{0}'.format(i), 'sort_param':'{0}'.format(i)}
            result.append(body)
            self.es.index(index=INDEX_NAME, doc_type=DOC_TYPE, body=body)

        search = self.es.search(body={'query': {'match_all': {}},
                                      'sort': [{ "sort_param" : {"order" : "asc"}}]
                                      })
        search_result = [hit.get('_source') for hit in search.get('hits').get('hits')]
        self.assertListEqual(result, search_result)

    def test_sort_by_field_desc(self):
        index_quantity = 10
        result = []
        for i in range(0, index_quantity):
            body = {'data': 'test_{0}'.format(i), 'sort_param':'{0}'.format(i)}
            result.append(body)
            self.es.index(index=INDEX_NAME, doc_type=DOC_TYPE, body=body)

        search = self.es.search(body={'query': {'match_all': {}},
                                      'sort': [{ "sort_param" : {"order" : "desc"}}]
                                      })
        search_result = [hit.get('_source') for hit in search.get('hits').get('hits')]
        result.reverse()
        self.assertListEqual(result, search_result)
