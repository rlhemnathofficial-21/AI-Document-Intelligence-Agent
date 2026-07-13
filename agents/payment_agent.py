class PaymentAgent:

    def get_schema(self):

        return {

            "payment_terms": {

                "terms": None,
                "due_date": None,
                "balance_due": None,
                "payment_method": None,
                "bank_name": None,
                "account_number": None,
                "ifsc_code": None,
                "swift_code": None

            }

        }

    def merge(self, extracted_json):

        schema = self.get_schema()

        if not isinstance(extracted_json, dict):
            return schema

        payment = extracted_json.get(
            "payment_terms",
            {}
        )

        if isinstance(payment, dict):

            for key in schema["payment_terms"]:

                if key in payment:

                    schema["payment_terms"][key] = payment[key]

        return schema

    def validate(self, payment):

        if not isinstance(payment, dict):

            return self.get_schema()

        if "payment_terms" not in payment:

            payment["payment_terms"] = self.get_schema()["payment_terms"]

        terms = payment["payment_terms"]

        # Clean strings
        for key, value in terms.items():

            if isinstance(value, str):

                terms[key] = " ".join(
                    value.split()
                )

        # Convert balance due
        if terms.get("balance_due") is not None:

            terms["balance_due"] = self.to_number(
                terms["balance_due"]
            )

        return payment

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

            return value