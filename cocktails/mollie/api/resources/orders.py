from ..error import IdentifierError
from ..objects.order import Order
from .base import ResourceBase


class Orders(ResourceBase):
    RESOURCE_ID_PREFIX = "ord_"

    def get_resource_object(self, result):
        return Order(result, self.client)

    def get(self, order_id, **params):
        if not order_id or not order_id.startswith(self.RESOURCE_ID_PREFIX):
            raise IdentifierError(
                f"Invalid order ID: '{order_id}'. An order ID should start with '{self.RESOURCE_ID_PREFIX}'."
            )

        result_order = super().get(order_id, **params)

        requested_embeds = self.extract_embed(params)
        if requested_embeds:
            result_order.requested_embeds = requested_embeds

        return result_order

    def delete(self, order_id, data=None):
        """Cancel order and return the order object.

        Deleting an order causes the order status to change to canceled.
        The updated order object is returned.
        """
        if not order_id or not order_id.startswith(self.RESOURCE_ID_PREFIX):
            raise IdentifierError(
                f"Invalid order ID: '{order_id}'. An order ID should start with '{self.RESOURCE_ID_PREFIX}'."
            )
        result = super().delete(order_id, data)
        return self.get_resource_object(result)
