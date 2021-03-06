from ..error import IdentifierError
from ..objects.payment import Payment
from .base import ResourceBase


class Payments(ResourceBase):
    RESOURCE_ID_PREFIX = "tr_"

    def get_resource_object(self, result):
        return Payment(result, self.client)

    def get(self, payment_id, **params):
        if not payment_id or not payment_id.startswith(self.RESOURCE_ID_PREFIX):
            raise IdentifierError(
                f"Invalid payment ID: '{payment_id}'. A payment ID should start with '{self.RESOURCE_ID_PREFIX}'."
            )
        return super().get(payment_id, **params)

    def delete(self, payment_id, data=None):
        """Cancel payment and return the payment object.

        Deleting a payment causes the payment status to change to canceled.
        The updated payment object is returned.
        """
        if not payment_id or not payment_id.startswith(self.RESOURCE_ID_PREFIX):
            raise IdentifierError(
                f"Invalid payment ID: '{payment_id}'. A payment ID should start with '{self.RESOURCE_ID_PREFIX}'."
            )
        result = super().delete(payment_id, data)
        return self.get_resource_object(result)
