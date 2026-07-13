class HeaderAgent:

    def get_schema(self):
        return {

            "invoice_number": None,
            "invoice_date": None,
            "due_date": None,
            "purchase_order": None,
            "reference_number": None,
            "currency": None,

            "seller": {
                "name": None,
                "address": None,
                "phone": None,
                "email": None,
                "gst_number": None
            },

            "buyer": {
                "name": None,
                "address": None,
                "phone": None,
                "email": None,
                "gst_number": None
            }
        }

    def merge(self, data):

        schema = self.get_schema()

        if not isinstance(data, dict):
            return schema

        # -----------------------------
        # Basic Fields
        # -----------------------------

        for field in [
            "invoice_number",
            "invoice_date",
            "due_date",
            "purchase_order",
            "reference_number",
            "currency"
        ]:

            if field in data:
                schema[field] = data[field]

        # -----------------------------
        # Seller
        # -----------------------------

        seller = data.get("seller", {})

        if isinstance(seller, dict):

            schema["seller"]["name"] = seller.get(
                "name",
                data.get("seller_name")
            )

            schema["seller"]["address"] = seller.get(
                "address",
                data.get("seller_address")
            )

            schema["seller"]["phone"] = seller.get(
                "phone",
                data.get("seller_phone")
            )

            schema["seller"]["email"] = seller.get(
                "email",
                data.get("seller_email")
            )

            schema["seller"]["gst_number"] = seller.get(
                "gst_number",
                data.get("seller_gstin")
            )

        # -----------------------------
        # Buyer
        # -----------------------------

        buyer = data.get("buyer", {})

        if isinstance(buyer, dict):

            schema["buyer"]["name"] = buyer.get(
                "name",
                data.get("buyer_name")
            )

            schema["buyer"]["address"] = buyer.get(
                "address",
                data.get("buyer_address")
            )

            schema["buyer"]["phone"] = buyer.get(
                "phone",
                data.get("buyer_phone")
            )

            schema["buyer"]["email"] = buyer.get(
                "email",
                data.get("buyer_email")
            )

            schema["buyer"]["gst_number"] = buyer.get(
                "gst_number",
                data.get("buyer_gstin")
            )

        return schema