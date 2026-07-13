import re


class ItemAgent:

    def extract_items(self, text):

        items = []

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        for i in range(len(lines)):

            line = lines[i]

            # Match lines like:
            # Camera 1 899.00 899.00
            # Laptop 2 1200 2400

            match = re.search(
                r"^(.*?)\s+(\d+(?:\.\d+)?)\s+\$?([\d,]+(?:\.\d+)?)\s+\$?([\d,]+(?:\.\d+)?)$",
                line
            )

            if match:

                item_name = match.group(1).strip()

                quantity = float(match.group(2))

                unit_price = float(match.group(3).replace(",", ""))

                amount = float(match.group(4).replace(",", ""))

                description = None

                # Usually description is on next line
                if i + 1 < len(lines):

                    next_line = lines[i + 1]

                    if not re.search(
                        r"\$?[\d,]+(?:\.\d+)?",
                        next_line
                    ):
                        description = next_line

                items.append(
                    {
                        "item_name": item_name,
                        "description": description,
                        "quantity": quantity,
                        "unit_price": unit_price,
                        "amount": amount,
                    }
                )

        return items