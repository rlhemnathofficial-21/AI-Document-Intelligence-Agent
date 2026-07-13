class ValidationAgent:

    def validate(self, data):

        report = {
            "is_valid": True,
            "warnings": [],
            "confidence_score": 100
        }

        if not isinstance(data, dict):

            report["is_valid"] = False
            report["confidence_score"] = 0
            report["warnings"].append(
                "Invalid JSON returned."
            )

            return report

        # ==========================================
        # Invoice Number
        # ==========================================

        if "invoice_number" not in data:

            report["warnings"].append(
                "Invoice number not found."
            )

            report["confidence_score"] -= 5

        # ==========================================
        # Invoice Date
        # ==========================================

        if "invoice_date" not in data:

            report["warnings"].append(
                "Invoice date not found."
            )

            report["confidence_score"] -= 5

        # ==========================================
        # Items
        # ==========================================

        items = data.get("items")

        if items is not None:

            if not isinstance(items, list):

                report["warnings"].append(
                    "Items should be a list."
                )

                report["confidence_score"] -= 10

            else:

                for i, item in enumerate(items):

                    if not isinstance(item, dict):

                        continue

                    if "item_name" not in item:

                        report["warnings"].append(
                            f"Item {i+1}: Missing item_name"
                        )

                        report["confidence_score"] -= 2

                    if "amount" not in item:

                        report["warnings"].append(
                            f"Item {i+1}: Missing amount"
                        )

                        report["confidence_score"] -= 2

        # ==========================================
        # Totals
        # ==========================================

        subtotal = data.get("subtotal")
        tax = data.get("tax_amount")
        total = data.get("total")

        if (
            isinstance(subtotal, (int, float))
            and isinstance(tax, (int, float))
            and isinstance(total, (int, float))
        ):

            expected = round(subtotal + tax, 2)

            if abs(expected - total) > 1:

                report["warnings"].append(
                    "Subtotal + Tax != Total"
                )

                report["confidence_score"] -= 5

        # ==========================================
        # Seller
        # ==========================================

        if "seller" in data:

            seller = data["seller"]

            if (
                isinstance(seller, dict)
                and "name" not in seller
            ):

                report["warnings"].append(
                    "Seller name missing."
                )

                report["confidence_score"] -= 3

        # ==========================================
        # Buyer
        # ==========================================

        if "buyer" in data:

            buyer = data["buyer"]

            if (
                isinstance(buyer, dict)
                and "name" not in buyer
            ):

                report["warnings"].append(
                    "Buyer name missing."
                )

                report["confidence_score"] -= 3

        report["confidence_score"] = max(
            report["confidence_score"],
            0
        )

        return report