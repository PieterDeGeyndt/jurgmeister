class ObjectBase(dict):
    def __init__(self, data, client=None):
        """
        Create a new object from API result data.
        """
        super().__init__(data)
        self.client = client

    def _get_property(self, name):
        """Return the named property from dictionary values."""
        if name not in self:
            return None
        return self[name]

    def _get_link(self, name):
        """Return a link by its name."""
        try:
            return self["_links"][name]["href"]
        except (KeyError, TypeError):
            return None

    @classmethod
    def get_object_name(cls):
        name = cls.__name__.lower()
        return f"{name}s"

    @classmethod
    def get_resource_class(cls, client):
        raise NotImplementedError  # pragma: no cover
