from app import app, db
from models import Pet

with app.app_context():
    print("=== Creating pets ===")
    # Create pet1
    pet1 = Pet(name="Fido", species="Dog")
    db.session.add(pet1)
    db.session.commit()
    print("Created pet1:", pet1)

    # Create pet2
    pet2 = Pet(name="Whiskers", species="Cat")
    db.session.add(pet2)
    db.session.commit()
    print("Created pet2:", pet2)

    print("\n=== Querying all pets ===")
    pets = Pet.query.all()
    print("All pets:", pets)

    print("\n=== Querying first pet ===")
    first_pet = Pet.query.first()
    print("First pet:", first_pet)

    print("\n=== Filtering by species Cat ===")
    cats = Pet.query.filter(Pet.species == 'Cat').all()
    print("Cats:", cats)

    print("\n=== Filtering by name starting with F ===")
    f_pets = Pet.query.filter(Pet.name.startswith('F')).all()
    print("Pets starting with F:", f_pets)

    print("\n=== Filtering by species using filter_by ===")
    dogs = Pet.query.filter_by(species="Dog").all()
    print("Dogs:", dogs)

    print("\n=== Getting pet by id 1 ===")
    pet_by_id = Pet.query.filter_by(id=1).first()
    print("Pet by id 1:", pet_by_id)

    print("\n=== Using db.session.get ===")
    pet_session_get = db.session.get(Pet, 1)
    print("Pet using session.get:", pet_session_get)

    print("\n=== Ordering by species ===")
    ordered_pets = Pet.query.order_by(Pet.species).all()
    print("Ordered by species:", ordered_pets)

    print("\n=== Using func.count ===")
    from sqlalchemy import func
    count = db.session.query(func.count(Pet.id)).scalar()
    print("Count of pets:", count)

    print("\n=== Updating pet1 name ===")
    pet1.name = "Buddy"
    db.session.commit()
    print("Updated pet1:", pet1)

    print("\n=== Deleting pet1 ===")
    db.session.delete(pet1)
    db.session.commit()
    print("Deleted pet1")

    print("\n=== Deleting all pets ===")
    deleted_count = Pet.query.delete()
    db.session.commit()
    print(f"Deleted {deleted_count} pets")

    print("\n=== Final query all pets ===")
    final_pets = Pet.query.all()
    print("All pets:", final_pets)
