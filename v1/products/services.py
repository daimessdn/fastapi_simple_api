from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc

from .schemas import ProductCreateModel, ProductUpdateModel
from .models import Product


class ProductService:
    async def get_all_products(self, session: AsyncSession):
        statement = select(Product).order_by(desc(Product.created_at))

        result = await session.exec(statement)

        return result.all()

    async def get_product_by_id(self, product_id: str, session: AsyncSession):
        statement = select(Product).where(Product.id == product_id)

        result = await session.exec(statement)

        product = result.first()

        return product if product is not None else None

    async def create_product(self, product: ProductCreateModel, session: AsyncSession):
        product_body = product.model_dump()

        new_product = Product(**product_body)

        session.add(new_product)
        await session.commit()

        return new_product

    async def update_product(self, product_id: str, product: ProductUpdateModel, session: AsyncSession):
        product_to_update = await self.get_product_by_id(product_id, session)

        product_body = product.model_dump()

        if product_to_update is not None:
            for k, v in product_body.items():
                setattr(product_to_update, k, v)

            await session.commit()

            return product_to_update

        else:
            return None

    async def delete_product(self, product_id: str, session: AsyncSession):
        product_to_delete = await self.get_product_by_id(product_id, session)

        if product_to_delete is not None:
            await session.delete(product_to_delete)
            await session.commit()

            return True

        else:
            return None
