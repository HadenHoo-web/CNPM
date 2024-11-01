from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(name ='Mobile')
        # c2 = Category(name ='Tablet')
        # c3 = Category(name ='Desktop')
        #
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()

        products = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        },
            {
                "id": 4,
                "name": "iPhone 7 Plus",
                "description": "Apple, 32GB, RAM: 3GB, iOS13",
                "price": 17000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
                "category_id": 1
            }, {
                "id": 5,
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "id": 6,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }, {
                "id": 7,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }, {
                "id": 8,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }
        ]

        for p in products:
            p = Product(**p)
            db.session.add(p)
        db.session.commit()