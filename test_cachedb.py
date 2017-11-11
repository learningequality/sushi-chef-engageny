import unittest

from cache import Db
from tempfile import mkdtemp


class TestCacheDbMethods(unittest.TestCase):
    def setUp(self):
        dirname = mkdtemp(suffix='translation', prefix='teststorage')
        print(dirname)
        self.db = Db(dirname, 'es')

    def tearDown(self):
        self.db.close()

    def test_add_found(self):
        self.db.add(key='hola', data=u'mundo!')
        found, data = self.db.get('hola')
        assert found
        assert data == 'mundo!'

    def test_add_not_found(self):
        found, data = self.db.get('hola')
        assert not found
        assert not data

    def test_remove(self):
        self.db.add(key='hola', data=u'mundo!')
        self.db.remove('hola')
        found, data = self.db.get('hola')
        assert not found
        assert not data

    def test_change(self):
        self.db.add(key='hola', data=u'mundo!')
        found, data = self.db.get('hola')
        assert found
        assert data == 'mundo!'
        self.db.add(key='hola', data=u'world!')
        found, data = self.db.get('hola')
        assert found
        assert data == 'world!'

if __name__ == '__main__':
    unittest.main()