from .payments import Payments


class SubscriptionPayments(Payments):
    customer_id = None
    subscription_id = None

    def get_resource_name(self):
        return f"customers/{self.customer_id}/subscriptions/{self.subscription_id}/payments"

    def with_parent_id(self, customer_id, subscription_id):
        self.customer_id = customer_id
        self.subscription_id = subscription_id
        return self

    def on(self, subscription):
        # TODO: A request has been filed to mollie to add the customer id to the subscription response.
        return self.with_parent_id(subscription.customer.id, subscription.id)
