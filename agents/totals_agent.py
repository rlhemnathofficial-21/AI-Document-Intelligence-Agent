class TotalsAgent:

    def get_schema(self):

        return {

            "subtotal": None,
            "discount": None,
            "shipping": None,
            "other_charges": None,
            "tax_rate": None,
            "tax_amount": None,
            "total": None,
            "amount_paid": None,
            "balance_due": None

        }

    def merge(self, extracted_json):

        schema = self.get_schema()

        if not isinstance(extracted_json, dict):
            return schema

        for key in schema:

            if key in extracted_json:
                schema[key] = extracted_json[key]

        return schema

    def validate(self, totals):

        subtotal = self.to_number(
            totals.get("subtotal")
        )

        total = self.to_number(
            totals.get("total")
        )

        tax_amount = self.to_number(
            totals.get("tax_amount")
        )

        amount_paid = self.to_number(
            totals.get("amount_paid")
        )

        # Calculate tax only if missing
        if (
            subtotal is not None
            and total is not None
            and tax_amount is None
        ):

            totals["tax_amount"] = round(
                total - subtotal,
                2
            )

        # Calculate balance due if missing
        if (
            total is not None
            and amount_paid is not None
            and totals.get("balance_due") is None
        ):

            totals["balance_due"] = round(
                total - amount_paid,
                2
            )

        return totals

    def to_number(self, value):

        if value is None:
            return None

        if isinstance(value, (int, float)):
            return value

        value = str(value)

        value = value.replace("$", "")
        value = value.replace("₹", "")
        value = value.replace(",", "")
        value = value.replace("%", "")
        value = value.strip()

        try:

            if "." in value:
                return float(value)

            return int(value)

        except:
            return None