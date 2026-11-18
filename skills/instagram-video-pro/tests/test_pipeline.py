import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from render import valid_project
from validate_video import check

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.project=json.loads((ROOT/"templates/project.example.json").read_text(encoding="utf-8"))

    def test_example_duration(self):
        self.assertEqual(valid_project(self.project),26)

    def test_wrong_resolution_rejected(self):
        self.project["canvas"]["height"]=1350
        with self.assertRaises(ValueError): valid_project(self.project)

    def test_negative_duration_rejected(self):
        self.project["slides"][0]["seconds"]=-1
        with self.assertRaises(ValueError): valid_project(self.project)

    def test_missing_file_rejected(self):
        self.assertFalse(check("/path/that/does/not/exist.mp4")["ok"])

if __name__=="__main__":
    unittest.main()
