import re


class RecoveryAgent:

    def recover(self, data, ocr_text):

        if not isinstance(data, dict):
            return data

        # Recover Seller
        if "seller" not in data:

            seller = self.extract_seller(ocr_text)

            if seller:
                data["seller"] = seller

        # Recover Buyer
        if "buyer" not in data:

            buyer = self.extract_buyer(ocr_text)

            if buyer:
                data["buyer"] = buyer

        # Recover Currency
        if "currency" not in data:

            currency = self.extract_currency(ocr_text)

            if currency:
                data["currency"] = currency

        return data

    # ---------------------------------------

    def extract_seller(self, text):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        for i, line in enumerate(lines):

            if "bill to" in line.lower():

                if i > 0:

                    return {
                        "name": lines[i - 1]
                    }

        return None

    # ---------------------------------------

    def extract_buyer(self, text):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        for i, line in enumerate(lines):

            if "bill to" in line.lower():

                if i + 1 < len(lines):

                    return {
                        "name": lines[i + 1]
                    }

        return None

    # ---------------------------------------

    def extract_currency(self, text):

        if "$" in text:
            return "$"

        if "₹" in text:
            return "₹"

        if "€" in text:
            return "€"

        if "£" in text:
            return "£"

        return None