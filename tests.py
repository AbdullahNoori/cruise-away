# from unittest import TestCase, main as unittest_main, mock
# from app import app
# from bson.objectid import ObjectId

# sample_vacation_id = ObjectId('5d55cffc4a3d4031f42827a3')
# sample_vacation = {
#     'title': 'Vacation Videos',
#     'description': 'Vacation is so fun! ',
#     'videos': [
#         'https://youtube.com/embed/hY7m5jjJ9mM',
#         'https://www.youtube.com/embed/CQ85sUNBK7w'
#     ]
# }
# sample_form_data = {
#     'title': sample_vacation['title'],
#     'description': sample_vacation['description'],
#     'videos': '\n'.join(sample_vacation['videos'])
# }

# class VacationsTests(TestCase):
#     """Flask tests."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         # Get the Flask test client
#         self.client = app.test_client()

#         # Show Flask errors that happen during tests
#         app.config['TESTING'] = True

#     def test_index(self):
#         """Test the vacations homepage."""
#         result = self.client.get('/')
#         self.assertEqual(result.status, '200 OK')
#         self.assertIn(b'Vacation', result.data)

#     def test_new(self):
#         """Test the new vacation creation page."""
#         result = self.client.get('/vacations/new')
#         self.assertEqual(result.status, '200 OK')
#         self.assertIn(b'New Vacation', result.data)
    
#     @mock.patch('pymongo.collection.Collection.find_one')
#     def test_show_vacation(self, mock_find):
#         """Test showing a single vacation."""
#         mock_find.return_value = sample_vacation

#         result = self.client.get(f'/vacations/{sample_vacation_id}')
#         self.assertEqual(result.status, '200 OK')
#         self.assertIn(b'Vacation Videos', result.data)

#     @mock.patch('pymongo.collection.Collection.find_one')
#     def test_edit_vacation(self, mock_find):
#         """Test editing a single vacation."""
#         mock_find.return_value = sample_vacation

#         result = self.client.get(f'/vacations/{sample_vacation_id}/edit')
#         self.assertEqual(result.status, '200 OK')
#         self.assertIn(b'Vacation Videos', result.data)
    
#     @mock.patch('pymongo.collection.Collection.insert_one')
#     def test_submit_vacation(self, mock_insert):
#         """Test submitting a new vacation."""
#         result = self.client.post('/vacations', data=sample_form_data)

#         # After submitting, should redirect to that vacation's page
#         self.assertEqual(result.status, '302 FOUND')
#         mock_insert.assert_called_with(sample_vacation)

#     @mock.patch('pymongo.collection.Collection.update_one')
#     def test_update_vacation(self, mock_update):
#         result = self.client.post(f'/vacations/{sample_vacation_id}/update', data=sample_form_data)

#         self.assertEqual(result.status, '302 FOUND')
#         mock_update.assert_called_with({'_id': sample_vacation_id}, {'$set': sample_vacation})

#     @mock.patch('pymongo.collection.Collection.delete_one')
#     def test_delete_vacation(self, mock_delete):
#         form_data = {'_method': 'DELETE'}
#         result = self.client.post(f'/vacations/{sample_vacation_id}/delete', data=form_data)
#         self.assertEqual(result.status, '302 FOUND')
#         mock_delete.assert_called_with({'_id': sample_vacation_id})

# if __name__ == '__main__':
#     unittest_main()
