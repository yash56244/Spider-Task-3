"""empty message

Revision ID: 4f8c5cc13b29
Revises: 94ca9cb5a388
Create Date: 2020-09-08 00:31:12.388497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8c5cc13b29'
down_revision = '94ca9cb5a388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'product', 'sellerorder', ['seller_order_id'], ['id'])
    op.create_foreign_key(None, 'product', 'cart', ['cart_id'], ['id'])
    op.create_foreign_key(None, 'product', 'order', ['order_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_constraint(None, 'product', type_='foreignkey')
    # ### end Alembic commands ###
