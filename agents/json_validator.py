class JSONValidator:

    def merge(self, header, items):

        header["items"] = items.get("items", [])

        return header