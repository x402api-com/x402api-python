# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from x402api.api.assets_and_payment_controls_api import AssetsAndPaymentControlsApi
    from x402api.api.facilitator_discovery_api import FacilitatorDiscoveryApi
    from x402api.api.idempotency_api import IdempotencyApi
    from x402api.api.orders_and_payments_api import OrdersAndPaymentsApi
    from x402api.api.programmatic_charges_api import ProgrammaticChargesApi
    from x402api.api.receiving_addresses_api import ReceivingAddressesApi
    from x402api.api.resources_and_pricing_api import ResourcesAndPricingApi
    from x402api.api.wallets_and_transfers_api import WalletsAndTransfersApi

else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from x402api.api.assets_and_payment_controls_api import AssetsAndPaymentControlsApi
from x402api.api.facilitator_discovery_api import FacilitatorDiscoveryApi
from x402api.api.idempotency_api import IdempotencyApi
from x402api.api.orders_and_payments_api import OrdersAndPaymentsApi
from x402api.api.programmatic_charges_api import ProgrammaticChargesApi
from x402api.api.receiving_addresses_api import ReceivingAddressesApi
from x402api.api.resources_and_pricing_api import ResourcesAndPricingApi
from x402api.api.wallets_and_transfers_api import WalletsAndTransfersApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
