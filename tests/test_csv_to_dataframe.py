from unittest import TestCase
import pandas as pd


filepath = "./data/conversion_data.csv"

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import dtype_category, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = dtype_category(res, ["country", "new_user", "source", "converted"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_centre_and_scale(self):
        from build import centre_and_scale, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = centre_and_scale(res, ["age", "total_pages_visited"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_label_encoder(self):
        from build import label_encoder, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = label_encoder(res, ["new_user", "converted", "country"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_one_hot_encoder(self):
        from build import one_hot_encoder, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = one_hot_encoder(res, ["source"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_skewness(self):
        from build import skewness, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = skewness(res, ["age", "total_pages_visited"])
        self.assertTrue(isinstance(new_res, list))

    def test_sqrt_transform(self):
        from build import sqrt_transform, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = sqrt_transform(res, ["age", "total_pages_visited"])
        self.assertTrue(isinstance(new_res, list))