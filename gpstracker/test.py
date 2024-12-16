from django.test import TestCase
from django.contrib.gis.geos import Point
from .models import Perangkat, RiwayatPerangkat

class PerangkatModelTest(TestCase):

    def setUp(self):
        # Data setup untuk model Perangkat
        self.perangkat = Perangkat.objects.create(
            name="Sensor A",
            description="Sensor untuk monitoring suhu",
            coordinates=Point(106.84513, -6.20876),  # Lokasi Jakarta
        )

    def test_perangkat_creation(self):
        # Test jika perangkat berhasil dibuat
        self.assertEqual(self.perangkat.name, "Sensor A")
        self.assertEqual(self.perangkat.description, "Sensor untuk monitoring suhu")
        self.assertAlmostEqual(self.perangkat.coordinates.x, 106.84513)
        self.assertAlmostEqual(self.perangkat.coordinates.y, -6.20876)
        self.assertIsNotNone(self.perangkat.last_updated)

    def test_perangkat_string_representation(self):
        # Test string representation
        self.assertEqual(str(self.perangkat), "Sensor A")


class RiwayatPerangkatModelTest(TestCase):

    def setUp(self):
        # Data setup untuk model RiwayatPerangkat
        self.perangkat = Perangkat.objects.create(
            name="Sensor B",
            description="Sensor untuk monitoring kelembapan",
            coordinates=Point(107.60981, -6.91746),  # Lokasi Bandung
        )
        self.riwayat = RiwayatPerangkat.objects.create(
            perangkat=self.perangkat,
            coordinates=Point(107.61000, -6.91700),  # Lokasi terbaru
        )

    def test_riwayat_perangkat_creation(self):
        # Test jika riwayat perangkat berhasil dibuat
        self.assertEqual(self.riwayat.perangkat, self.perangkat)
        self.assertAlmostEqual(self.riwayat.coordinates.x, 107.61000)
        self.assertAlmostEqual(self.riwayat.coordinates.y, -6.91700)
        self.assertIsNotNone(self.riwayat.last_updated)

    def test_riwayat_perangkat_string_representation(self):
        # Test string representation
        expected_str = "{} {}".format(self.perangkat.name, self.riwayat.last_updated)
        self.assertEqual(str(self.riwayat), expected_str)
