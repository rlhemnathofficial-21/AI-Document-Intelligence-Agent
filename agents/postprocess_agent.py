from datetime import datetime


class PostProcessAgent:

    def clean(self, data):

        if not isinstance(data, dict):
            return data

        # ---------------------------------
        # Clean top-level strings
        # ---------------------------------

        for key, value in data.items():

            if isinstance(value, str):
                data[key] = " ".join(value.split())

        # ---------------------------------
        # Normalize Dates
        # ---------------------------------

        if "invoice_date" in data:
            data["invoice_date"] = self.normalize_date(
                data.get("invoice_date")
            )

        if "due_date" in data:
            data["due_date"] = self.normalize_date(
                data.get("due_date")
            )

        # ---------------------------------
        # Seller Cleanup
        # ---------------------------------

        if isinstance(data.get("seller"), dict):

            for key, value in data["seller"].items():

                if isinstance(value, str):
                    data["seller"][key] = " ".join(value.split())

        # ---------------------------------
        # Buyer Cleanup
        # ---------------------------------

        if isinstance(data.get("buyer"), dict):

            for key, value in data["buyer"].items():

                if isinstance(value, str):
                    data["buyer"][key] = " ".join(value.split())

        # ---------------------------------
        # Payment Terms
        # ---------------------------------

        if isinstance(data.get("payment_terms"), dict):

            payment = data["payment_terms"]

            if "due_date" in payment:
                payment["due_date"] = self.normalize_date(
                    payment.get("due_date")
                )

            for key, value in payment.items():

                if isinstance(value, str):
                    payment[key] = " ".join(value.split())

        # ---------------------------------
        # Money Fields
        # ---------------------------------

        money_fields = [

            "subtotal",
            "discount",
            "shipping",
            "other_charges",
            "tax_rate",
            "tax_amount",
            "total",
            "amount_paid",
            "balance_due"

        ]

        for field in money_fields:

            if field in data:

                data[field] = self.to_number(
                    data[field]
                )

        # payment balance

        if isinstance(data.get("payment_terms"), dict):

            if "balance_due" in data["payment_terms"]:

                data["payment_terms"]["balance_due"] = self.to_number(
                    data["payment_terms"]["balance_due"]
                )

        # ---------------------------------
        # Items
        # ---------------------------------

        if isinstance(data.get("items"), list):

            for item in data["items"]:

                for key, value in item.items():

                    if isinstance(value, str):
                        item[key] = " ".join(value.split())

                for field in [

                    "quantity",
                    "unit_price",
                    "amount"

                ]:

                    if field in item:

                        item[field] = self.to_number(
                            item[field]
                        )

        # ---------------------------------
        # Tax Validation
        # ---------------------------------

        subtotal = data.get("subtotal")
        total = data.get("total")

        if isinstance(subtotal, (int, float)) and isinstance(total, (int, float)):

            calculated_tax = round(total - subtotal, 2)

            data["tax_amount"] = calculated_tax

        # ---------------------------------
        # Remove Duplicate Fields
        # ---------------------------------

        duplicate_fields = [

            "seller_name",
            "seller_address",
            "seller_phone",
            "seller_email",
            "seller_gstin",

            "buyer_name",
            "buyer_address",
            "buyer_phone",
            "buyer_email",
            "buyer_gstin"

        ]

        for field in duplicate_fields:
            data.pop(field, None)

        return data

    # =====================================================
    # Helpers
    # =====================================================

    def to_number(self, value):

        if value is None:
            return None

        if isinstance(value, (int, float)):
            return value

        value = str(value)

        value = value.replace("$", "")
        value = value.replace(",", "")
        value = value.replace("%", "")
        value = value.strip()

        try:

            if "." in value:
                return float(value)

            return int(value)

        except:
            return value

    def normalize_date(self, date_string):

        if not date_string:
            return date_string

        formats = [

            "%d %b %Y",
            "%d-%b-%Y",
            "%d/%m/%Y",
            "%d-%m-%Y",
            "%Y-%m-%d",
            "%d%b%Y"

        ]

        for fmt in formats:

            try:

                return datetime.strptime(
                    date_string,
                    fmt
                ).strftime("%Y-%m-%d")

            except:
                pass

        return date_string