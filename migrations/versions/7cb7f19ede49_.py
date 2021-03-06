"""empty message

Revision ID: 7cb7f19ede49
Revises: 
Create Date: 2020-09-05 21:48:53.413956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cb7f19ede49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=20), nullable=False),
    sa.Column('description', sa.Text(length=50), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('photo', sa.LargeBinary(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
