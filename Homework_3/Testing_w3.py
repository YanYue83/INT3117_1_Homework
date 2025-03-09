import unittest
def delivery_bill(weight: float, delivery_type: str, distance: float):
    price_ranges = [
        (5.0, {"thường": 10000, "hỏa tốc": 35000}),
        (20.0, {"thường": 8000, "hỏa tốc": 26000}),
        (200, {"thường": 6000, "hỏa tốc": 15000})
    ]
    
    if delivery_type not in ["thường", "hỏa tốc"]:
        raise ValueError("Loại dịch vụ không hợp lệ!")

    rate = 0
    for limit, rates in price_ranges:
        if weight <= limit:
            rate = rates[delivery_type]
            break

    # Tính tổng phí dịch vụ theo trọng lượng
    total_cost = weight * rate

    # Tính phụ phí khoảng cách
    if distance < 10:
        total_cost *= 1.05
    elif distance > 50:
        total_cost *= 1.1
    
    return round(total_cost)

# testing

class TestDeliveryBill(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (10, "nhanh", 10, ValueError, "Loại dịch vụ không hợp lệ!"),
            (3, "thường", 5, 31500, None),
            (3, "hỏa tốc", 60, 115500, None),
            (201, "hỏa tốc", 20, ValueError, "Trọng lượng không hợp lệ!")
        ]

    def test_cases(self):
        for weight, delivery_type, distance, expected, error_msg in self.test_cases:
            with self.subTest(weight=weight, delivery_type=delivery_type, distance=distance):
                try:
                    result = delivery_bill(weight, delivery_type, distance)
                    outcome = "PASS" if result == expected else "FAIL"
                    print(f"Test case ({weight}, {delivery_type}, {distance}): {result} (Expected: {expected}) -> {outcome}")
                    self.assertEqual(result, expected)
                except ValueError as e:
                    actual_error_msg = str(e)
                    outcome = "PASS" if actual_error_msg == error_msg else "FAIL"
                    print(f"Test case ({weight}, {delivery_type}, {distance}): ERROR - {actual_error_msg} (Expected: {error_msg}) -> {outcome}")
                    self.assertEqual(actual_error_msg, error_msg)
                except Exception as e:
                    print(f"Test case ({weight}, {delivery_type}, {distance}): UNEXPECTED ERROR - {e}")
                    self.fail(f"Unexpected error: {e}")

if __name__ == "__main__":
        unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestDeliveryBill))
