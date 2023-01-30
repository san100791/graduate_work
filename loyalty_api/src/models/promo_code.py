import datetime
import uuid

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.models.mixin import JsonMixin


PromoCode = sqlalchemy.Table(
    "promocode",
    sqlalchemy.MetaData(),
    sqlalchemy.Column("id", UUID(), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
    sqlalchemy.Column("user_id", UUID(), nullable=True),
    sqlalchemy.Column("value", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("code", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("expiration_date", sqlalchemy.Date(), default='2050-01-01', nullable=False),
    sqlalchemy.Column("measure", sqlalchemy.String, default='%', nullable=False),
    sqlalchemy.Column("is_multiple", sqlalchemy.Boolean, default=False, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime(timezone=True), server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime(timezone=True), onupdate=func.now()),
)


PromoUsage = sqlalchemy.Table(
    "promo_usage",
    sqlalchemy.MetaData(),
    sqlalchemy.Column("id", UUID(), default=uuid.uuid4(), nullable=False, unique=True, primary_key=True),
    sqlalchemy.Column("promo_id", UUID(), nullable=False),
    sqlalchemy.Column("user_id", UUID(), nullable=False),
    sqlalchemy.Column("used_at", sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime(timezone=True), server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime(timezone=True), onupdate=func.now()),
)


class BasePromoApi(JsonMixin):
    """
    """
    id: uuid.UUID
    user_id: uuid.UUID
    code: str
    measure: str
    value: float
    is_multiple: bool
    expiration_date: datetime.date
    created_at: datetime.date
    updated_at: datetime.date


class PromoPriceApi(JsonMixin):
    price_before: float
    price_after: float
    promo_code: str
    user_id: uuid.UUID


class DelPromoBody(JsonMixin):
    user_id: uuid.UUID
