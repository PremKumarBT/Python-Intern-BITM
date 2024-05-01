class clinic:
    def __init__(self,athlete_id,name,progress_data):
        self.athlete_id=athlete_id
        self.name = name
        self.progress_data = progress_data

class clinicdata:
    def __init__(self):
        self.athlete = {}

    def create(self, athlete_id, name, progress_data):
        if athlete_id in self.athlete:
            raise ValueError("Athlete ID already exists")
        self.athlete[athlete_id] = clinic(athlete_id,name,progress_data)

    def read(self, athlete_id):
        if athlete_id not in self.athlete:
            raise ValueError("Athlete ID does not exist")
        return self.athlete[athlete_id]

    def update(self, athlete_id, name=None, progress_data=None):
        if athlete_id not in self.athlete:
            raise ValueError("athlete ID does not exist")
        athlete = self.athlete[athlete_id]
        if name:
            athlete.name = name
        if progress_data:
            athlete.progress_data = progress_data

    def delete(self, athlete_id):
        if athlete_id not in self.athlete:
            raise ValueError("athlete ID does not exist")
        del self.athlete[athlete_id]
        
    def manage_medical_appointment(self,athlete_id,name = None , progress_data=None):
        if athlete_id not in self.athlete:
            raise ValueError("athlete ID does not exist")
        athlete=self.athlete[athlete_id]
        if name:
            athlete.name = name
        if progress_data:
            athlete.progress_data = progress_data
            
    def track_health_progress(self,athlete_id):
        if athlete_id not in self.athlete:
            raise ValueError("athlete ID does not exist")
        return self.athlete[athlete_id]
    
# Unit tests
import unittest

class TestClinicDatabase(unittest.TestCase):
    def setUp(self):
        self.db = clinicdata()
        self.db.create(1000, "Prem", "Improved")
        self.db.create(1001, "Prerana", "Improving")

    def test_create(self):
        self.db.create(1002, "Rishika", "Constant")
        self.assertIn(1002, self.db.athlete)
        
    def test_read(self):
        athlete = self.db.read(1000)
        self.assertEqual(athlete.name, "Prem")

    def test_update(self):
        self.db.update(1000, name="Prem Prerana")
        athlete = self.db.read(1000)
        self.assertEqual(athlete.name, "Prem Prerana")

    def test_delete(self):
        self.db.delete(1000)
        self.assertNotIn(1000, self.db.athlete)
    
    def test_manage_medical_appointment(self):
        self.db.manage_medical_appointment(1001, name="Priketh")
        athlete=self.db.read(1001)
        self.assertEqual(athlete.name, "Priketh")
        
    def test_track_health_progress(self):
        athlete=self.db.track_health_progress(1001)
        self.assertEqual(athlete.name, "Prerana")
        
if __name__ == '__main__':
    unittest.main(verbosity=7)